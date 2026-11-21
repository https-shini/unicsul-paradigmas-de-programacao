#!/usr/bin/env python3
"""Navegação da base de conhecimento: transforma as pastas do repositório num "caderno" interligado,
no estilo do Notion e do Obsidian, usando só Markdown que o GitHub renderiza.

O que este script faz (sempre de forma idempotente — rodar duas vezes não muda nada):
  1. Índices: cria README.md nas pastas que não têm um, listando o conteúdo com títulos e descrições.
     Só reescreve READMEs que ele mesmo gerou (marcados com <!-- indice gerado -->).
  2. Trilha (breadcrumb) no topo de cada nota: Início › seção › aula › pasta.
  3. Rodapé de cada nota: atalhos "Nesta aula", anterior/próxima da mesma série e
     "Links para esta página" (backlinks, como no Obsidian).
  4. Citações de página dos slides (p.12, Aula08 p.13, Aula 04, p.11) viram links para a imagem
     daquela página na galeria dos slides.
  5. MAPA.md na raiz: todas as notas do repositório, em árvore.

Os blocos gerados ficam entre <!-- nav:topo --> … <!-- /nav:topo --> e <!-- nav:rodape --> … <!-- /nav:rodape -->.
Escreva as notas normalmente, fora desses blocos, e rode o script de novo.

Uso:
    python3 ferramentas/geradores/gerar_navegacao.py              # aplica
    python3 ferramentas/geradores/gerar_navegacao.py --verificar  # CI: falha se algo estiver desatualizado
"""
import argparse, os, re, subprocess, sys, urllib.parse
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IGNORAR_PASTAS = {".git", "node_modules", "codigo", "paginas", "__pycache__", ".pytest_cache"}
MARCA_INDICE = "<!-- indice gerado por ferramentas/geradores/gerar_navegacao.py -->"
MARCA_GALERIA = "<!-- gerado por ferramentas/geradores/gerar_galerias.py"
TOPO = re.compile(r"<!-- nav:topo -->.*?<!-- /nav:topo -->\n*", re.S)
RODAPE = re.compile(r"\n*<!-- nav:rodape -->.*?<!-- /nav:rodape -->\n*", re.S)
MAX_BACKLINKS = 40

DESCRICOES = {
    "01 - Slides Originais": "Slides do professor: o PDF original e a galeria com cada página em imagem.",
    "02 - Resumo Teórico": "Resumo teórico da aula. Clique em qualquer p.N para ver aquela página do slide.",
    "03 - Exercícios": "Exercícios da aula em quatro níveis: básico, intermediário, avançado e aprofundamento. As resoluções ficam na pasta 04.",
    "04 - Resoluções": "Resoluções comentadas dos exercícios. **[Resolução elaborada]**: não são gabarito oficial.",
    "05 - Materiais Complementares": "Leituras indicadas pelo professor e complementos para aprofundar.",
    "01 - Enunciado Original": "Enunciado original da lista: o PDF e a galeria com cada página em imagem.",
    "02 - Resolução": "Resolução comentada da lista. **[Resolução elaborada]**: não é gabarito oficial.",
    "Simulados": "Simulados autorais, cada um com a resolução em arquivo separado. Faça antes de abrir a resolução.",
    "Revisões por Unidade": "Uma revisão para cada unidade da disciplina.",
    "07 - Glossário": "Glossário alfabético dos termos da disciplina, com as aulas em que aparecem.",
    "inicial": "Esqueleto do projeto: é aqui que você programa (procure os TODO).",
    "solucao": "Resolução de referência do projeto. **[Resolução elaborada]**: consulte depois de tentar.",
    "testes": "Testes automáticos do projeto. Rode com `python3 ferramentas/testar_projetos.py`.",
    "exemplos": "Programas de exemplo para experimentar.",
    ".github": "Configuração do GitHub: o workflow de validação automática (CI).",
    "workflows": "Workflow que executa o código e valida links, diagramas e referências a cada envio.",
    ".devcontainer": "Ambiente do GitHub Codespaces, com todas as linguagens da disciplina instaladas.",
    "geradores": "Scripts que geram partes do repositório a partir dos Markdown (galerias, navegação, glossário, flashcards, referências, apostila).",
    "c": "Versão em C (imperativa).", "java": "Versão em Java (orientada a objetos).",
    "clojure": "Versão em Clojure (funcional).", "prolog": "Versão em Prolog (lógica).",
    "calc": "Pacote Python do interpretador.", "Apostila": "Apostila em PDF.", "Flashcards": "Flashcards para o Anki.",
}
LINGUAGEM = {".py": "Python", ".c": "C", ".h": "C (cabeçalho)", ".cpp": "C++", ".hpp": "C++ (cabeçalho)",
             ".java": "Java", ".clj": "Clojure", ".cljs": "ClojureScript", ".pl": "Prolog", ".cs": "C#",
             ".php": "PHP", ".js": "JavaScript", ".mjs": "JavaScript", ".sh": "Shell", ".json": "JSON",
             ".yml": "YAML", ".yaml": "YAML", ".csv": "CSV", ".tsv": "TSV", ".calc": "calc (P1)", ".bib": "BibTeX",
             ".apkg": "Baralho do Anki", ".pdf": "PDF", ".webp": "Imagem", ".png": "Imagem", ".jpg": "Imagem",
             ".jpeg": "Imagem", ".gif": "Imagem", ".svg": "Imagem"}


# ------------------------------------------------------------------ utilidades de caminho e texto

def rel(caminho):
    return os.path.relpath(caminho, RAIZ).replace(os.sep, "/")


def link(de_arquivo, para):
    r = os.path.relpath(para, os.path.dirname(de_arquivo)).replace(os.sep, "/")
    return r.replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def limpar_md(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_`]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def curto(t, n=70):
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def nome_curto_pasta(nome):
    m = re.match(r"^(Aula \d+|Lista \d+|P\d+) - ", nome)
    return m.group(1) if m else nome


def listar(pasta):
    try:
        itens = sorted(os.listdir(pasta))
    except FileNotFoundError:
        return [], []
    dirs = [i for i in itens if os.path.isdir(os.path.join(pasta, i)) and i not in IGNORAR_PASTAS
            and not (i.startswith(".") and pasta != RAIZ)]
    arqs = [i for i in itens if os.path.isfile(os.path.join(pasta, i)) and not i.startswith(".")]
    return dirs, arqs


def todas_as_pastas():
    for raiz, dirs, _ in os.walk(RAIZ):
        # .github fica de fora: um .github/README.md substituiria o README da página inicial do repositório
        dirs[:] = sorted(d for d in dirs if d not in IGNORAR_PASTAS and not (d.startswith(".") and d != ".devcontainer"))
        if raiz != RAIZ:
            yield raiz


def titulo_de(caminho, texto=None):
    if texto is None:
        try:
            texto = open(caminho, encoding="utf-8").read()
        except (FileNotFoundError, UnicodeDecodeError):
            return os.path.basename(caminho)
    texto = TOPO.sub("", texto)
    for linha in texto.splitlines():
        if linha.startswith("# "):
            return limpar_md(linha[2:])
    return os.path.splitext(os.path.basename(caminho))[0]


def primeira_linha_comentario(caminho):
    try:
        for linha in open(caminho, encoding="utf-8"):
            s = linha.strip()
            if not s or s.startswith("#!") or s.startswith("#include") or s.startswith("import ") or s.startswith("package "):
                continue
            m = re.match(r'^(?://+|/\*+|\*|;+|%+|#+|"""|--)\s*(.*?)\s*(?:\*/)?$', s)
            if m and m.group(1) and not m.group(1).startswith("ifndef"):
                return curto(m.group(1).rstrip('"'), 110)
            return ""
    except (UnicodeDecodeError, FileNotFoundError):
        return ""
    return ""


# ------------------------------------------------------------------ 1. índices de pasta

def gerar_indice(pasta):
    nome = os.path.basename(pasta)
    destino = os.path.join(pasta, "README.md")
    if os.path.exists(destino) and MARCA_INDICE not in open(destino, encoding="utf-8").read():
        return None                                     # README escrito à mão: não mexe
    if nome == "01 - Aulas":
        corpo = indice_aulas(pasta)
    else:
        corpo = indice_generico(pasta)
    if corpo is None:
        return None
    return destino, MARCA_INDICE + "\n\n" + corpo


def indice_generico(pasta):
    nome = os.path.basename(pasta)
    dirs, arqs = listar(pasta)
    arqs = [a for a in arqs if a != "README.md"]
    if not dirs and not arqs:
        return None
    acima = os.path.basename(os.path.dirname(pasta))
    titulo = nome if not re.match(r"^\d\d - ", nome) or os.path.dirname(pasta) == RAIZ else f"{nome_curto_pasta(acima)} · {nome[5:]}"
    if nome in ("inicial", "solucao", "testes", "exemplos"):
        titulo = f"{nome_curto_pasta(acima)} · {nome}"
    elif nome in ("c", "java", "clojure", "prolog", "calc"):
        titulo = f"{nome_curto_pasta(os.path.basename(os.path.dirname(os.path.dirname(pasta))))} · {acima}/{nome}"
    linhas = [f"# {titulo}", ""]
    if nome in DESCRICOES:
        linhas += [DESCRICOES[nome], ""]
    linhas += ["| Conteúdo | Tipo | Descrição |", "| --- | --- | --- |"]
    f = os.path.join(pasta, "README.md")
    for d in dirs:
        alvo = os.path.join(pasta, d, "README.md")
        desc = DESCRICOES.get(d, "")
        if os.path.exists(alvo) and MARCA_INDICE not in open(alvo, encoding="utf-8").read():
            desc = desc or titulo_de(alvo)
        linhas.append(f"| [{d}/]({link(f, alvo)}) | Pasta | {desc} |")
    for a in arqs:
        caminho = os.path.join(pasta, a)
        ext = os.path.splitext(a)[1].lower()
        if ext == ".md":
            linhas.append(f"| [{titulo_de(caminho)}]({link(f, caminho)}) | Nota | `{a}` |")
        else:
            tipo = LINGUAGEM.get(ext, ext.lstrip(".").upper() or "Arquivo")
            desc = primeira_linha_comentario(caminho) if tipo not in ("PDF", "Imagem", "Baralho do Anki") else ""
            linhas.append(f"| [`{a}`]({link(f, caminho)}) | {tipo} | {desc} |")
    return "\n".join(linhas) + "\n"


def indice_aulas(pasta):
    f = os.path.join(pasta, "README.md")
    linhas = ["# 01 - Aulas", "",
              "As 15 aulas da disciplina. Todas têm a mesma estrutura: **slides** (PDF e galeria de imagens), "
              "**resumo** teórico, **exercícios**, **resoluções** e **materiais complementares**.", "",
              "| Aula | Tema | Slides | Resumo | Exercícios | Resoluções | Complementos |",
              "| :-: | --- | :-: | :-: | :-: | :-: | :-: |"]
    for d in sorted(os.listdir(pasta)):
        m = re.match(r"^Aula (\d+) - (.+)$", d)
        if not m:
            continue
        base = os.path.join(pasta, d)

        def lk(sub, padrao, rotulo):
            alvos = sorted(x for x in os.listdir(os.path.join(base, sub)) if re.match(padrao, x)) if os.path.isdir(os.path.join(base, sub)) else []
            return f"[{rotulo}]({link(f, os.path.join(base, sub, alvos[0]))})" if alvos else "—"
        linhas.append(f"| [{m.group(1)}]({link(f, os.path.join(base, 'README.md'))}) | {m.group(2)} | "
                      f"{lk('01 - Slides Originais', r'README\.md$', 'ver')} | {lk('02 - Resumo Teórico', r'resumo-aula', 'ler')} | "
                      f"{lk('03 - Exercícios', r'exercicios-', 'fazer')} | {lk('04 - Resoluções', r'resolucoes-', 'conferir')} | "
                      f"{lk('05 - Materiais Complementares', r'materiais-', 'ler')} |")
    linhas += ["", "Unidades: 1 — Fundamentos (Aulas 01–08) · 2 — Imperativo (09–11) · 3 — Orientação a objetos (12–13) · "
               "4 — Funcional e lógico (14–15). Revisões por unidade em "
               f"[06 - Revisões e Sínteses]({link(f, os.path.join(RAIZ, '06 - Revisões e Sínteses', 'Revisões por Unidade', 'README.md'))})."]
    return "\n".join(linhas) + "\n"


# ------------------------------------------------------------------ 4. citações de página

PAGINAS = {}           # chave da galeria → (arquivo .md da galeria, nº de páginas)


def carregar_galerias():
    for pasta in sorted(os.listdir(os.path.join(RAIZ, "01 - Aulas"))):
        m = re.match(r"^Aula (\d+)", pasta)
        if not m:
            continue
        num = int(m.group(1))
        sl = os.path.join(RAIZ, "01 - Aulas", pasta, "01 - Slides Originais")
        for md, chave in (("README.md", f"{num:02d}"), ("artigo-dijkstra-1968.md", f"{num:02d}a")):
            g = os.path.join(sl, md)
            if os.path.exists(g):
                n = len(re.findall(r"^### Página \d+$", open(g, encoding="utf-8").read(), re.M))
                PAGINAS[chave] = (g, n)
    for i, letra in ((1, "a"), (2, "b")):
        for pasta in os.listdir(os.path.join(RAIZ, "02 - Listas de Exercícios")):
            if pasta.startswith(f"Lista {i:02d}"):
                g = os.path.join(RAIZ, "02 - Listas de Exercícios", pasta, "01 - Enunciado Original", "README.md")
                if os.path.exists(g):
                    n = len(re.findall(r"^### Página \d+$", open(g, encoding="utf-8").read(), re.M))
                    PAGINAS[f"16{letra}"] = (g, n)
                    PAGINAS[f"lista{i:02d}"] = (g, n)


def chave_padrao(arquivo):
    """Galeria a que um p.N sem aula se refere, pela pasta onde a nota está."""
    r = rel(arquivo)
    m = re.match(r"^01 - Aulas/Aula (\d+)", r)
    if m:
        return f"{int(m.group(1)):02d}a" if "dijkstra" in os.path.basename(arquivo) else f"{int(m.group(1)):02d}"
    m = re.match(r"^02 - Listas de Exercícios/Lista (\d+)", r)
    if m and "01 - Enunciado Original" in r:
        return f"lista{int(m.group(1)):02d}"
    return None


PROTEGIDO = re.compile(r"(```.*?```|~~~.*?~~~|`[^`\n]*`|<!--.*?-->|!?\[(?:[^\[\]]|\[[^\]]*\])*\]\([^)]*\)|<[^>\n]+>|https?://\S+)", re.S)
REF_AULA = re.compile(r"\bAula ?(\d{1,2})([ab]?)\b")
LISTA_P = r"p\.(\d+)(?:[–-]\d+)?"
PREFIXADA = re.compile(r"\bAula ?(\d{1,2})([ab]?)(,? \(?| \(| )(" + LISTA_P + r"(?:(?:, | e |; |/| a )" + LISTA_P + r")*)")
NUA = re.compile(r"(?<![\w./\[])(" + LISTA_P + r"(?:(?:, | e |; |/)" + LISTA_P + r")*)")
ITEM = re.compile(r"p\.(\d+)((?:[–-]\d+)?)")
SUFIXO = re.compile(r"\)?\s+(?:da|na|do|das|nas)\s+\[?Aula ?(\d{1,2})([ab]?)\b")
LINK_PAGINA = re.compile(r"\[(p\.\d+(?:[–-]\d+)?)\]\([^)\s]*#página-\d+\)")


def ligar_lista(texto_lista, chave, arquivo, avisos):
    if chave not in PAGINAS:
        return texto_lista
    galeria, n = PAGINAS[chave]

    def um(m):
        p = int(m.group(1))
        if p < 1 or p > n:
            avisos.append(f"{rel(arquivo)}: p.{p} além das {n} páginas de {rel(galeria)}")
            return m.group(0)
        return f"[{m.group(0)}]({link(arquivo, galeria)}#página-{p})"
    return ITEM.sub(um, texto_lista)


def ligar_paginas_no_trecho(trecho, arquivo, padrao, contexto_linha, avisos):
    """Liga as citações de página de um trecho de texto comum (sem código nem links)."""
    saida, pos = [], 0
    for m in PREFIXADA.finditer(trecho):
        saida.append(ligar_nuas(trecho[pos:m.start()], arquivo, padrao, contexto_linha, avisos))
        chave = f"{int(m.group(1)):02d}{m.group(2)}"
        if chave in PAGINAS:
            saida.append(trecho[m.start():m.end(3)])          # "Aula08 " / "Aula 04, " / "Aula 05 ("
            saida.append(ligar_lista(m.group(4), chave, arquivo, avisos))
        else:
            saida.append(m.group(0))
        contexto_linha[0] = chave
        pos = m.end()
    saida.append(ligar_nuas(trecho[pos:], arquivo, padrao, contexto_linha, avisos))
    return "".join(saida)


def ligar_nuas(trecho, arquivo, padrao, contexto_linha, avisos):
    saida, pos = [], 0
    for m in NUA.finditer(trecho):
        antes = trecho[pos:m.start()]
        mencoes = list(REF_AULA.finditer(antes))
        if mencoes:
            contexto_linha[0] = f"{int(mencoes[-1].group(1)):02d}{mencoes[-1].group(2)}"
        # "p.19–22 da Aula 02": a aula vem depois da página
        depois = SUFIXO.match(trecho, m.end())
        if depois:
            chave = f"{int(depois.group(1)):02d}{depois.group(2)}"
        # "([Aula 14](...), p.7)": a página vem logo depois de um link para outra aula
        elif contexto_linha[1] and not saida and re.fullmatch(r"[\s,;(]*", antes):
            chave = contexto_linha[1]
        # nas pastas das aulas, p.N sem aula é da própria aula; fora delas, da última aula citada na linha
        elif rel(arquivo).startswith("01 - Aulas/"):
            chave = padrao
        else:
            chave = contexto_linha[0] or padrao
        saida.append(antes)
        saida.append(ligar_lista(m.group(1), chave, arquivo, avisos) if chave else m.group(1))
        pos = m.end()
    contexto_linha[1] = None
    saida.append(trecho[pos:])
    return "".join(saida)


def ligar_paginas(texto, arquivo, avisos):
    padrao = chave_padrao(arquivo)
    saida = []
    em_codigo = False
    for linha in texto.split("\n"):
        s = linha.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            em_codigo = not em_codigo
            saida.append(linha)
            continue
        if em_codigo or s.startswith("#") or "p." not in linha:
            saida.append(linha)
            continue
        contexto = [None, None]               # [última aula citada na linha, aula do link imediatamente anterior]
        partes, pos = [], 0
        for m in PROTEGIDO.finditer(linha):
            partes.append(ligar_paginas_no_trecho(linha[pos:m.start()], arquivo, padrao, contexto, avisos))
            prot = m.group(0)
            ref = REF_AULA.findall(re.sub(r"\]\(.*", "", prot)) if prot.startswith("[") else []
            if ref:                                   # "[Aula 05](...) (p.17)": o link informa o contexto
                contexto[0] = contexto[1] = f"{int(ref[-1][0]):02d}{ref[-1][1]}"
            partes.append(prot)
            pos = m.end()
        partes.append(ligar_paginas_no_trecho(linha[pos:], arquivo, padrao, contexto, avisos))
        saida.append("".join(partes))
    return "\n".join(saida)


# ------------------------------------------------------------------ 2 e 3. trilha, rodapé, backlinks

LINK_MD = re.compile(r"(?<!!)\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^)\s]+)\)")


def links_de(texto, arquivo):
    sem_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
    alvos = set()
    for m in LINK_MD.finditer(sem_codigo):
        url = m.group(1)
        if re.match(r"^[a-z]+:", url) or url.startswith("#"):
            continue
        caminho = urllib.parse.unquote(url.split("#")[0])
        if not caminho.endswith(".md"):
            continue
        alvo = os.path.normpath(os.path.join(os.path.dirname(arquivo), caminho))
        if alvo != arquivo:
            alvos.add(alvo)
    return alvos


def trilha(arquivo, existentes):
    r = rel(arquivo)
    partes = r.split("/")
    pastas = partes[:-1]
    eh_readme = partes[-1] == "README.md"
    crumbs = [f"[Início]({link(arquivo, os.path.join(RAIZ, 'README.md'))})"]
    for i, nome in enumerate(pastas):
        alvo = os.path.join(RAIZ, *pastas[:i + 1], "README.md")
        ultimo = i == len(pastas) - 1
        rotulo = nome_curto_pasta(nome)
        if ultimo and eh_readme:
            crumbs.append(f"**{rotulo}**")
        elif alvo in existentes:
            crumbs.append(f"[{rotulo}]({link(arquivo, alvo)})")
        else:
            crumbs.append(rotulo)
    if r == "MAPA.md":
        return " › ".join(crumbs + ["**Mapa do repositório**"])
    return " › ".join(crumbs) + f" · [Mapa]({link(arquivo, os.path.join(RAIZ, 'MAPA.md'))})"


def chave_serie(r):
    k = re.sub(r"^\d\d - [^/]+/README\.md$", "#SECAO", r)
    k = re.sub(r"Aula \d+ - [^/]+", "Aula #", k)
    k = re.sub(r"Lista \d+ - [^/]+", "Lista #", k)
    k = re.sub(r"P\d+ - [^/]+", "P#", k)
    k = re.sub(r"\d+", "#", k)
    return re.sub(r"(unidade-#)-[^/]+\.md$", r"\1.md", k)


def nesta_aula(arquivo):
    r = rel(arquivo)
    m = re.match(r"^01 - Aulas/(Aula (\d+) - [^/]+)", r)
    if not m:
        return None
    base = os.path.join(RAIZ, "01 - Aulas", m.group(1))
    itens = [("Visão geral", os.path.join(base, "README.md")),
             ("Slides", os.path.join(base, "01 - Slides Originais", "README.md"))]
    for sub, pad, rot in (("02 - Resumo Teórico", r"resumo-aula-\d+\.md$", "Resumo"),
                          ("02 - Resumo Teórico", r"resumo-artigo-.*\.md$", "Artigo"),
                          ("03 - Exercícios", r"exercicios-.*\.md$", "Exercícios"),
                          ("04 - Resoluções", r"resolucoes-.*\.md$", "Resoluções"),
                          ("05 - Materiais Complementares", r"materiais-.*\.md$", "Complementos")):
        d = os.path.join(base, sub)
        if os.path.isdir(d):
            for x in sorted(os.listdir(d)):
                if re.match(pad, x):
                    itens.append((rot, os.path.join(d, x)))
    partes = []
    for rot, alvo in itens:
        if not os.path.exists(alvo):
            continue
        partes.append(f"**{rot}**" if os.path.normpath(alvo) == os.path.normpath(arquivo) else f"[{rot}]({link(arquivo, alvo)})")
    return f"**Aula {m.group(2)}:** " + " · ".join(partes)


TIPO_PASTA = {"01 - Slides Originais": "Slides", "02 - Resumo Teórico": "Resumo", "03 - Exercícios": "Exercícios",
              "04 - Resoluções": "Resoluções", "05 - Materiais Complementares": "Complementos",
              "01 - Enunciado Original": "Enunciado", "02 - Resolução": "Resolução"}


def rotulo(arquivo, titulos):
    """Nome curto de uma nota, para anterior/próxima e backlinks: "Aula 12 · Resumo", "Lista 02 · Resolução"."""
    partes = rel(arquivo).split("/")
    m = re.match(r"^(Aula|Lista) (\d+) - ", partes[1]) if len(partes) > 2 and partes[0] in ("01 - Aulas", "02 - Listas de Exercícios") else None
    if m:
        base = f"{m.group(1)} {m.group(2)}"
        if len(partes) == 3:
            return f"{base} · visão geral" if m.group(1) == "Aula" else base
        tipo = TIPO_PASTA.get(partes[2], partes[2])
        if "dijkstra" in partes[-1]:
            tipo = "Artigo de Dijkstra" + (" (resumo)" if tipo == "Resumo" else "")
        return f"{base} · {tipo}" + (" (pasta)" if partes[-1] == "README.md" and tipo not in ("Slides", "Enunciado") else "")
    return curto(titulos[arquivo], 60)


def rodape(arquivo, series, titulos, backlinks, ignorar_bl):
    linhas = []
    na = nesta_aula(arquivo)
    if na:
        linhas.append(na)
    serie = series.get(chave_serie(rel(arquivo)), [])
    if len(serie) > 1 and arquivo in serie:
        i = serie.index(arquivo)
        ant = f"← [{rotulo(serie[i - 1], titulos)}]({link(arquivo, serie[i - 1])})" if i > 0 else ""
        prox = f"[{rotulo(serie[i + 1], titulos)}]({link(arquivo, serie[i + 1])}) →" if i < len(serie) - 1 else ""
        linhas.append(" · ".join(x for x in (ant, prox) if x))
    bl = sorted(b for b in backlinks.get(arquivo, ()) if b not in ignorar_bl)
    if bl:
        itens = [f"[{rotulo(b, titulos)}]({link(arquivo, b)})" for b in bl[:MAX_BACKLINKS]]
        mais = f" · e mais {len(bl) - MAX_BACKLINKS}" if len(bl) > MAX_BACKLINKS else ""
        linhas.append(f"**Links para esta página ({len(bl)}):** " + " · ".join(itens) + mais)
    if not linhas:
        return ""
    return "\n\n<!-- nav:rodape -->\n\n---\n\n" + "\n\n".join(linhas) + "\n\n<!-- /nav:rodape -->\n"


# ------------------------------------------------------------------ 5. mapa

def gerar_mapa(arquivos, titulos):
    existentes = set(arquivos)
    destino = os.path.join(RAIZ, "MAPA.md")
    linhas = ["# Mapa do repositório", "",
              f"Todas as {len(arquivos)} notas da base, na ordem das pastas. Use **Ctrl+F** nesta página para achar uma nota pelo título, "
              "ou a busca do GitHub (tecla `/`) para procurar no texto de todas elas, inclusive no texto dos slides.", ""]
    def ordem(a):                       # dentro de cada pasta: README, depois as notas, depois as subpastas
        c = rel(a).split("/")
        return tuple("1" + x.lower() for x in c[:-1]) + (("00" if c[-1] == "README.md" else "01") + c[-1].lower(),)
    por_secao = defaultdict(list)
    for a in sorted(arquivos, key=ordem):
        r = rel(a)
        if r in ("README.md", "MAPA.md"):
            continue
        por_secao[r.split("/")[0] if "/" in r else "Raiz"].append(a)
    for secao in sorted(por_secao):
        readme = os.path.join(RAIZ, secao, "README.md")
        cab = f"[{secao}]({link(destino, readme)})" if readme in existentes else secao
        linhas += [f"## {secao}", "", f"Índice da seção: {cab}", ""]
        for a in por_secao[secao]:
            r = rel(a)
            leia_me = os.path.basename(a) == "README.md"
            if leia_me and r.count("/") == 1:
                continue
            nivel = r.count("/") - (2 if leia_me else 1)     # o índice da subpasta fica no nível das notas da pasta-mãe
            nome = titulos[a]
            linhas.append("  " * max(nivel, 0) + f"- [{curto(nome, 90)}]({link(destino, a)})")
        linhas.append("")
    return destino, MARCA_INDICE.replace("indice", "mapa") + "\n\n" + "\n".join(linhas).rstrip() + "\n"


# ------------------------------------------------------------------ principal

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true", help="não escreve; falha se algum arquivo mudaria")
    ap.add_argument("--refazer-paginas", action="store_true",
                    help="desfaz os links p.N existentes e liga de novo (depois de mudar as regras ou as galerias)")
    a = ap.parse_args()
    carregar_galerias()
    novos = {}                                            # caminho → conteúdo (antes da navegação)

    # 1. índices
    for pasta in todas_as_pastas():
        r = gerar_indice(pasta)
        if r:
            novos[r[0]] = r[1]

    # arquivos .md existentes (+ os índices novos)
    arquivos = set(novos)
    for raiz, dirs, fs in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in IGNORAR_PASTAS and not (d.startswith(".") and d != ".devcontainer")]
        for f in fs:
            if f.endswith(".md"):
                arquivos.add(os.path.join(raiz, f))
    mapa_path = os.path.join(RAIZ, "MAPA.md")
    arquivos.add(mapa_path)

    corpos, avisos = {}, []
    for f in sorted(arquivos):
        if f == mapa_path:
            continue
        texto = novos.get(f) or open(f, encoding="utf-8").read()
        texto = RODAPE.sub("\n", TOPO.sub("", texto)).rstrip() + "\n"
        if a.refazer_paginas:
            texto = LINK_PAGINA.sub(r"\1", texto)
        if MARCA_GALERIA not in texto and MARCA_INDICE not in texto:
            texto = ligar_paginas(texto, f, avisos)
        corpos[f] = texto
    titulos = {f: titulo_de(f, t) for f, t in corpos.items()}
    titulos[mapa_path] = "Mapa do repositório"
    mapa_destino, mapa_corpo = gerar_mapa(arquivos, titulos)
    corpos[mapa_path] = mapa_corpo

    # backlinks (ignora índices gerados, o mapa e a raiz como origem)
    ignorar = {f for f, t in corpos.items() if MARCA_INDICE in t or "<!-- mapa gerado" in t} | {mapa_path}
    backlinks = defaultdict(set)
    for f, t in corpos.items():
        if f in ignorar:
            continue
        for alvo in links_de(t, f):
            if alvo in corpos:
                backlinks[alvo].add(f)
    series = defaultdict(list)
    for f in sorted(corpos, key=rel):
        series[chave_serie(rel(f))].append(f)

    mudou = []
    for f, corpo in sorted(corpos.items()):
        if rel(f) == "README.md":
            final = corpo                                 # a página inicial fica limpa
        else:
            final = f"<!-- nav:topo -->\n{trilha(f, corpos)}\n<!-- /nav:topo -->\n\n" + corpo.rstrip("\n") + "\n" + \
                    rodape(f, series, titulos, backlinks, ignorar)
        atual = open(f, encoding="utf-8").read() if os.path.exists(f) else None
        if atual != final:
            mudou.append(rel(f))
            if not a.verificar:
                open(f, "w", encoding="utf-8").write(final)
    for av in avisos:
        print("aviso:", av)
    if a.verificar:
        if mudou:
            print(f"{len(mudou)} arquivo(s) com navegação desatualizada; rode ferramentas/geradores/gerar_navegacao.py:")
            print("\n".join("   " + m for m in mudou[:30]))
            return 1
        print(f"navegação em dia: {len(corpos)} notas")
        return 0
    print(f"{len(corpos)} notas; {len(mudou)} atualizadas; {len(novos)} índices de pasta gerados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
