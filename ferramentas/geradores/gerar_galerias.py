#!/usr/bin/env python3
"""Gera as galerias dos PDFs originais: cada página vira uma imagem WebP, exibida numa nota Markdown.

Para cada pasta "01 - Slides Originais" (aulas) e "01 - Enunciado Original" (listas):
    paginas/<prefixo>-pNN.webp   uma imagem por página (1200 px de largura)
    README.md                    galeria do PDF principal: índice de páginas, imagens e o texto de cada página
    <outro>.md                   galeria de um PDF adicional da mesma pasta (o artigo de Dijkstra, na Aula 09)

Qualquer outro PDF do repositório (por exemplo, um que você anexe ao caderno de anotações) ganha uma
galeria <nome-do-pdf>.md ao lado dele, com as imagens em paginas/. A apostila (gerada) fica de fora.

O texto extraído de cada página vai num bloco recolhível: assim o conteúdo dos slides aparece na busca
do GitHub e do Obsidian, que não indexam o interior de PDFs e imagens.

Uso:
    python3 ferramentas/geradores/gerar_galerias.py              # gera tudo (imagens só se faltarem)
    python3 ferramentas/geradores/gerar_galerias.py --refazer    # recria também as imagens
Requer: poppler-utils (pdftoppm, pdftotext, pdfinfo) e Pillow com suporte a WebP.
"""
import argparse, glob, os, re, subprocess, sys, tempfile, urllib.parse

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LARGURA = 1200
QUALIDADE = 75
SECUNDARIOS = {"Aula09a_ArtigoDijkstra68.pdf": ("artigo-dijkstra-1968.md", "Artigo de Dijkstra (1968)")}
MARCA = "<!-- gerado por ferramentas/geradores/gerar_galerias.py: não edite à mão -->"


def q(caminho):
    return urllib.parse.quote(caminho)


def paginas(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


def prefixo(pdf):
    nome = os.path.basename(pdf)
    if re.match(r"^Aula\d", nome):
        return nome.split("_")[0].lower()                      # Aula09a_ArtigoDijkstra68.pdf → aula09a
    return slug_arquivo(os.path.splitext(nome)[0])


def slug_arquivo(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60] or "documento"


def renderizar(pdf, destino, refazer):
    os.makedirs(destino, exist_ok=True)
    n = paginas(pdf)
    pre = prefixo(pdf)
    faltam = [p for p in range(1, n + 1) if refazer or not os.path.exists(os.path.join(destino, f"{pre}-p{p:02d}.webp"))]
    if faltam:
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["pdftoppm", "-f", str(min(faltam)), "-l", str(max(faltam)), "-scale-to-x", str(LARGURA),
                            "-scale-to-y", "-1", "-png", pdf, os.path.join(tmp, "p")], check=True)
            for png in sorted(glob.glob(os.path.join(tmp, "p-*.png"))):
                p = int(re.search(r"-(\d+)\.png$", png).group(1))
                if p in faltam:
                    Image.open(png).convert("RGB").save(os.path.join(destino, f"{pre}-p{p:02d}.webp"),
                                                         "WEBP", quality=QUALIDADE, method=6)
    return n, pre


def texto_da_pagina(pdf, p):
    t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", pdf, "-"],
                       capture_output=True, text=True).stdout
    linhas = [l.rstrip() for l in t.replace("\f", "").splitlines()]
    while linhas and not linhas[0].strip():
        linhas.pop(0)
    while linhas and not linhas[-1].strip():
        linhas.pop()
    # reduz o recuo comum, para o bloco não ficar deslocado
    recuos = [len(l) - len(l.lstrip()) for l in linhas if l.strip()]
    r = min(recuos) if recuos else 0
    texto = "\n".join(l[r:] for l in linhas)
    return re.sub(r"\n{3,}", "\n\n", texto).replace("```", "'''")


def titulo_da_aula(pasta):
    if os.path.basename(pasta) in ("01 - Slides Originais", "01 - Enunciado Original"):
        return os.path.basename(os.path.dirname(pasta))          # "Aula 12 - Paradigma ..." ou "Lista 01 - Revisão I"
    return os.path.basename(pasta)


def galeria(pdf, pasta, arquivo_md, rotulo, n, pre, irmaos):
    nome_pdf = os.path.basename(pdf)
    base = titulo_da_aula(pasta)
    linhas = [MARCA, "", f"# {base} · {rotulo}", "",
              f"> **[Material original]** {rotulo} do professor, página por página, para ler aqui mesmo no GitHub. "
              f"O arquivo original é o PDF [`{nome_pdf}`]({q(nome_pdf)}) ({n} páginas): use-o para baixar ou imprimir. "
              "As imagens e o texto de cada página foram extraídos do PDF, sem alteração do conteúdo.", ""]
    for outro_md, outro_rot in irmaos:
        linhas += [f"Nesta pasta também: [{outro_rot}]({q(outro_md)}).", ""]
    linhas += ["**Ir para a página:** " + " · ".join(f"[{p}](#página-{p})" for p in range(1, n + 1)), "",
               "O texto de cada página fica em **Texto da página**, logo abaixo da imagem: é por ele que a busca encontra o conteúdo dos slides.", ""]
    for p in range(1, n + 1):
        img = f"paginas/{pre}-p{p:02d}.webp"
        linhas += ["---", "", f"### Página {p}", "", f"![{base}, {rotulo.lower()}, página {p}]({q(img)})", ""]
        texto = texto_da_pagina(pdf, p)
        if texto.strip():
            linhas += ["<details>", "<summary>Texto da página</summary>", "", "```text", texto, "```", "", "</details>", ""]
        else:
            linhas += ["*Página sem texto extraível (só imagem).*", ""]
        linhas += [f"<sub>[↑ voltar ao índice](#{slug(f'{base} · {rotulo}')})</sub>", ""]
    open(os.path.join(pasta, arquivo_md), "w", encoding="utf-8").write("\n".join(linhas).rstrip() + "\n")


def slug(titulo):
    t = titulo.strip().lower()
    t = "".join(c for c in t if c.isalnum() or c in " -_")
    return t.replace(" ", "-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refazer", action="store_true", help="recria as imagens mesmo se já existirem")
    ap.add_argument("--novos", action="store_true", help="só os PDFs que ainda não têm galeria (usado no GitHub Actions)")
    a = ap.parse_args()
    pastas = sorted(glob.glob(os.path.join(RAIZ, "01 - Aulas", "Aula *", "01 - Slides Originais"))) + \
        sorted(glob.glob(os.path.join(RAIZ, "02 - Listas de Exercícios", "Lista *", "01 - Enunciado Original")))
    total = 0
    for pasta in pastas:
        pdfs = sorted(glob.glob(os.path.join(pasta, "*.pdf")))
        principais = [p for p in pdfs if os.path.basename(p) not in SECUNDARIOS]
        secundarios = [p for p in pdfs if os.path.basename(p) in SECUNDARIOS]
        if len(principais) != 1:
            sys.exit(f"esperava um PDF principal em {pasta}: {principais}")
        rotulo = "Slides originais" if "Slides" in pasta else "Enunciado original"
        if a.novos and os.path.exists(os.path.join(pasta, "README.md")):
            continue
        info = {}
        for pdf in pdfs:
            info[pdf] = renderizar(pdf, os.path.join(pasta, "paginas"), a.refazer)
            total += info[pdf][0]
        irmaos = [SECUNDARIOS[os.path.basename(s)] for s in secundarios]
        galeria(principais[0], pasta, "README.md", rotulo, *info[principais[0]], irmaos)
        for s in secundarios:
            md, rot = SECUNDARIOS[os.path.basename(s)]
            galeria(s, pasta, md, rot, *info[s], [("README.md", rotulo)])
        print(f"{os.path.relpath(pasta, RAIZ)}: {len(pdfs)} PDF(s)")
    # demais PDFs: galeria ao lado
    for raiz, dirs, fs in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "paginas", "codigo") and not d.startswith(".")]
        if raiz in pastas or os.path.basename(raiz) == "Apostila":
            continue
        for f in sorted(fs):
            if f.lower().endswith(".pdf"):
                pdf = os.path.join(raiz, f)
                if a.novos and os.path.exists(os.path.join(raiz, slug_arquivo(os.path.splitext(f)[0]) + ".md")):
                    continue
                n, pre = renderizar(pdf, os.path.join(raiz, "paginas"), a.refazer)
                galeria(pdf, raiz, slug_arquivo(os.path.splitext(f)[0]) + ".md", f"Documento {os.path.splitext(f)[0]}", n, pre, [])
                total += n
                print(f"{os.path.relpath(pdf, RAIZ)}: galeria criada")
    print(f"{len(pastas)} pastas de slides e listas, {total} páginas")


if __name__ == "__main__":
    main()
