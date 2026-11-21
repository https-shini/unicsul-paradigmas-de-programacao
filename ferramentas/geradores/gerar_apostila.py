#!/usr/bin/env python3
"""Gera as apostilas em PDF a partir dos arquivos Markdown do repositório.

Saídas (em 06 - Revisões e Sínteses/Apostila/):
    apostila-plp.pdf                 teoria: resumo geral, resumos das 15 aulas, sínteses e glossário
    caderno-de-exercicios-plp.pdf    exercícios, listas e simulados; resoluções no fim, em parte separada

Requer: pandoc (2.19+), Google Chrome ou Chromium (modo headless) e ferramentas/node_modules
(npm ci em ferramentas/, para desenhar os diagramas Mermaid).

Uso:
    python3 ferramentas/geradores/gerar_apostila.py             # gera os dois PDFs
    python3 ferramentas/geradores/gerar_apostila.py --html      # também guarda o HTML intermediário
    python3 ferramentas/geradores/gerar_apostila.py --so teoria # só a apostila de teoria
"""
import argparse, datetime, glob, html, os, re, shutil, subprocess, sys, tempfile, urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SAIDA = os.path.join(RAIZ, "06 - Revisões e Sínteses", "Apostila")
MERMAID = os.path.join(RAIZ, "ferramentas", "node_modules", "mermaid", "dist", "mermaid.min.js")
GITHUB = "https://github.com/https-shini/unicsul-paradigmas-de-programacao/blob/main/"


def aulas(subpasta, padrao):
    out = []
    for d in sorted(glob.glob(os.path.join(RAIZ, "01 - Aulas", "Aula *"))):
        out += sorted(glob.glob(os.path.join(d, subpasta, padrao)),
                      key=lambda p: ("artigo" in p, p))      # resumo da aula antes do resumo do artigo
    return out


def r(*partes):
    return os.path.join(RAIZ, *partes)


def volumes():
    S = "06 - Revisões e Sínteses"
    teoria = [
        ("Visão geral", [r(S, "resumo-geral-da-disciplina.md")]),
        ("Resumos das aulas", aulas("02 - Resumo Teórico", "resumo-*.md")),
        ("Sínteses", [r(S, "quadros-comparativos.md"), r(S, "mapas-conceituais.md"), r(S, "erratas-e-inconsistencias.md")]),
        ("Glossário", [r("07 - Glossário", "glossario.md")]),
    ]
    L = "02 - Listas de Exercícios"
    SIM = ("04 - Provas e Avaliações", "Simulados")
    exercicios = [
        ("Exercícios das aulas", aulas("03 - Exercícios", "exercicios-*.md")),
        ("Listas do professor", [r(L, "Lista 01 - Revisão I", "README.md"), r(L, "Lista 02 - Revisão II", "README.md")]),
        ("Simulados e questões integradoras", [r(*SIM, f"simulado-0{i}.md") for i in (1, 2, 3)] + [r(S, "questoes-integradoras.md")]),
        ("Resoluções comentadas", aulas("04 - Resoluções", "resolucoes-*.md")
            + [r(L, "Lista 01 - Revisão I", "02 - Resolução", "resolucao-lista-01.md"),
               r(L, "Lista 02 - Revisão II", "02 - Resolução", "resolucao-lista-02.md")]
            + [r(*SIM, f"resolucao-simulado-0{i}.md") for i in (1, 2, 3)]
            + [r(S, "resolucao-questoes-integradoras.md")]),
    ]
    return {
        "teoria": ("apostila-plp.pdf", "Apostila de estudo",
                   "Resumo geral, resumos das 15 aulas, quadros comparativos, mapas conceituais, erratas e glossário", teoria),
        "exercicios": ("caderno-de-exercicios-plp.pdf", "Caderno de exercícios",
                       "Exercícios das aulas, listas do professor e simulados; resoluções comentadas no fim", exercicios),
    }


# ---------------------------------------------------------------- Markdown → HTML

LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(<?([^)\s>]+)>?(\s+\"[^\"]*\")?\)")


def slug_github(texto):
    t = texto.strip().lower()
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[`*_]", "", t)
    t = "".join(c for c in t if c.isalnum() or c in " -_")
    return t.replace(" ", "-")


def reescrever_links(md, arquivo, ids):
    """Links para arquivos incluídos viram âncoras internas; os demais apontam para o GitHub."""
    pasta = os.path.dirname(arquivo)

    def troca(m):
        img, texto, alvo, titulo = m.group(1), m.group(2), m.group(3), m.group(4) or ""
        if re.match(r"^[a-z]+:", alvo):
            return m.group(0)
        caminho, _, ancora = alvo.partition("#")
        if caminho:
            destino = os.path.normpath(os.path.join(pasta, urllib.parse.unquote(caminho)))
        else:
            destino = arquivo
        if destino in ids and not img:
            prefixo = ids[destino]
            novo = f"#{prefixo}-{urllib.parse.unquote(ancora)}" if ancora else f"#{prefixo}"
        else:
            rel = os.path.relpath(destino, RAIZ).replace(os.sep, "/")
            novo = GITHUB + urllib.parse.quote(rel) + (f"#{ancora}" if ancora else "")
            if img:
                return f"*[figura: {texto or os.path.basename(rel)}]({novo})*"
        return f"{img}[{texto}]({novo}{titulo})"

    return LINK.sub(troca, md)


def md_para_html(arquivo, prefixo, ids):
    md = open(arquivo, encoding="utf-8").read()
    md = re.sub(r"<!--.*?-->\n?", "", md, flags=re.S)          # marcadores de teste
    md = reescrever_links(md, arquivo, ids)
    out = subprocess.run(
        ["pandoc", "-f", "gfm+tex_math_dollars", "-t", "html5", "--shift-heading-level-by=1",
         "--highlight-style=tango", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True).stdout
    # ids únicos no volume: prefixo do capítulo (os links já reescritos começam com cNN-)
    out = re.sub(r' id="([^"]+)"', lambda m: f' id="{prefixo}-{m.group(1)}"', out)
    out = re.sub(r' href="#(?!c\d{2}|parte\d)([^"]+)"', lambda m: f' href="#{prefixo}-{m.group(1)}"', out)
    out = re.sub(r'<pre class="mermaid"><code>(.*?)</code></pre>',
                 lambda m: f'<pre class="mermaid">{m.group(1)}</pre>', out, flags=re.S)
    rel = os.path.relpath(arquivo, RAIZ)
    return f'<section class="capitulo" id="{prefixo}">\n<p class="origem">{html.escape(rel)}</p>\n{out}\n</section>'


def sumario(partes_html):
    itens = []
    for titulo_parte, pid, caps in partes_html:
        sub = "".join(f'<li><a href="#{cid}">{html.escape(ct)}</a></li>' for cid, ct in caps)
        itens.append(f'<li class="parte"><a href="#{pid}">{html.escape(titulo_parte)}</a><ol>{sub}</ol></li>')
    return f'<nav class="sumario"><h1>Sumário</h1><ol>{"".join(itens)}</ol></nav>'


CSS = r"""
@page { size: A4; margin: 20mm 18mm 20mm 18mm;
  @bottom-center { content: counter(page); font: 9pt "DejaVu Sans", sans-serif; color: #666; }
  @top-right { content: "Paradigmas de Linguagens de Programação"; font: 8pt "DejaVu Sans", sans-serif; color: #999; } }
@page :first { @bottom-center { content: none; } @top-right { content: none; } }
html { font: 10.5pt/1.45 "DejaVu Serif", Georgia, serif; color: #1a1a1a; }
h1, h2, h3, h4, h5 { font-family: "DejaVu Sans", sans-serif; line-height: 1.25; break-after: avoid; }
h1 { font-size: 22pt; color: #12355b; }
h2 { font-size: 16pt; color: #12355b; border-bottom: 2px solid #12355b; padding-bottom: 3pt; margin-top: 0; }
h3 { font-size: 12.5pt; color: #1d4e89; margin-top: 16pt; }
h4 { font-size: 11pt; } h5 { font-size: 10.5pt; }
a { color: #1d4e89; text-decoration: none; }
code { font: 9pt "DejaVu Sans Mono", monospace; background: #f3f4f6; padding: 0 2pt; border-radius: 2pt; }
pre { font: 8.6pt/1.35 "DejaVu Sans Mono", monospace; background: #f6f8fa; border: 1px solid #e1e4e8;
      border-radius: 3pt; padding: 6pt 8pt; white-space: pre-wrap; word-break: break-word; break-inside: avoid; }
pre code { background: none; padding: 0; font-size: inherit; }
pre.mermaid { background: none; border: none; text-align: center; white-space: pre; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 8pt 0; break-inside: auto; }
th, td { border: 1px solid #c8ccd1; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #e8eef5; } tr { break-inside: avoid; }
blockquote { margin: 8pt 0; padding: 4pt 10pt; border-left: 4px solid #d29922; background: #fff8e6; color: #333; }
img { max-width: 100%; }
.capa { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; break-after: page; }
.capa h1 { font-size: 30pt; margin: 0 0 8pt; } .capa .sub { font: 14pt "DejaVu Sans", sans-serif; color: #1d4e89; }
.capa .desc { margin: 24pt auto; max-width: 140mm; color: #444; } .capa .aviso { font-size: 9pt; color: #666; max-width: 140mm; margin: 0 auto; }
.sumario { break-after: page; } .sumario ol { list-style: none; padding-left: 0; } .sumario ol ol { padding-left: 14pt; columns: 1; }
.sumario li.parte { margin-top: 8pt; font-weight: bold; font-family: "DejaVu Sans", sans-serif; }
.sumario li.parte li { font-weight: normal; font-family: "DejaVu Serif", serif; font-size: 9.5pt; margin: 1pt 0; }
.parte-titulo { break-before: page; height: 200mm; display: flex; align-items: center; justify-content: center; }
.parte-titulo h1 { font-size: 28pt; text-align: center; }
.capitulo { break-before: page; }
.origem { font: 7.5pt "DejaVu Sans Mono", monospace; color: #888; margin: 0 0 4pt; }
.sourceCode .kw { color: #204a87; font-weight: bold; } .sourceCode .st { color: #4e9a06; } .sourceCode .co { color: #8f5902; font-style: italic; }
.sourceCode .dv, .sourceCode .fl { color: #0000cf; } .sourceCode .fu { color: #000; } .sourceCode .op { color: #ce5c00; }
"""


def montar(chave, nome_pdf, titulo, descricao, partes, manter_html):
    ids, n = {}, 0
    for _, arquivos in partes:
        for a in arquivos:
            n += 1
            ids[os.path.normpath(a)] = f"c{n:02d}"
    corpo, toc = [], []
    for i, (tparte, arquivos) in enumerate(partes, 1):
        pid = f"parte{i}"
        corpo.append(f'<div class="parte-titulo" id="{pid}"><h1>Parte {i}<br/>{html.escape(tparte)}</h1></div>')
        caps = []
        for a in arquivos:
            a = os.path.normpath(a)
            if not os.path.exists(a):
                sys.exit(f"arquivo ausente: {a}")
            pref = ids[a]
            primeira = next((l for l in open(a, encoding="utf-8") if l.startswith("# ")), "# " + os.path.basename(a))
            caps.append((pref, re.sub(r"[*`]", "", primeira[2:].strip())))
            corpo.append(md_para_html(a, pref, ids))
        toc.append((tparte, pid, caps))
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    capa = (f'<div class="capa"><h1>Paradigmas de Linguagens de Programação</h1>'
            f'<div class="sub">{html.escape(titulo)} · UNICSUL</div>'
            f'<p class="desc">{html.escape(descricao)}.</p>'
            f'<p class="aviso">Gerado em {hoje} a partir do repositório de estudos. Os resumos, explicações, exercícios autorais e resoluções '
            f'<b>não são material oficial do professor</b> e não substituem os slides originais. As marcações [Material original], '
            f'[Explicação elaborada], [Complemento], [Atenção], [Exercício autoral] e [Resolução elaborada] indicam a origem de cada trecho.</p></div>')
    mermaid_js = open(MERMAID, encoding="utf-8").read() if os.path.exists(MERMAID) else ""
    if not mermaid_js:
        print("aviso: mermaid.min.js não encontrado (rode npm ci em ferramentas/); diagramas sairão como texto")
    script = ("<script>" + mermaid_js.replace("</script>", "<\\/script>") + "</script>"
              "<script>mermaid.initialize({startOnLoad:false, theme:'neutral', flowchart:{htmlLabels:false}});"
              "mermaid.run({querySelector:'pre.mermaid'}).then(()=>{document.body.dataset.pronto='1'});</script>") if mermaid_js else ""
    doc = (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>PLP — {html.escape(titulo)}</title>'
           f'<style>{CSS}</style></head><body>{capa}{sumario(toc)}{"".join(corpo)}{script}</body></html>')
    tmp = tempfile.mkdtemp()
    html_path = os.path.join(tmp, chave + ".html")
    open(html_path, "w", encoding="utf-8").write(doc)
    os.makedirs(SAIDA, exist_ok=True)
    destino = os.path.join(SAIDA, nome_pdf)
    chrome = next((c for c in ("google-chrome", "chromium", "chromium-browser", "chrome") if shutil.which(c)), None)
    if not chrome:
        sys.exit("Chrome/Chromium não encontrado")
    subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=60000", "--run-all-compositor-stages-before-draw",
                    "--generate-pdf-document-outline", f"--print-to-pdf={destino}", "file://" + html_path],
                   check=True, capture_output=True)
    if manter_html:
        shutil.copy(html_path, os.path.join(SAIDA, chave + ".html"))
    shutil.rmtree(tmp)
    return destino, n


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", action="store_true", help="guarda também o HTML intermediário")
    ap.add_argument("--so", choices=["teoria", "exercicios"])
    a = ap.parse_args()
    for chave, (pdf, titulo, desc, partes) in volumes().items():
        if a.so and a.so != chave:
            continue
        destino, n = montar(chave, pdf, titulo, desc, partes, a.html)
        print(f"{os.path.relpath(destino, RAIZ)}: {n} capítulos, {os.path.getsize(destino) // 1024} KB")
