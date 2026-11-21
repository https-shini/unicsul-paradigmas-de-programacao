#!/usr/bin/env python3
"""Gera a pasta codigo/ com cada exemplo dos arquivos Markdown em um arquivo executável.

Os Markdown continuam sendo a fonte: edite o exemplo no resumo/resolução e rode este script.

Uso:
    python3 ferramentas/gerar_codigo.py             # (re)gera codigo/
    python3 ferramentas/gerar_codigo.py --verificar # só confere se codigo/ está atualizado (usado no CI)
"""
import filecmp, os, re, shutil, sys, tempfile, unicodedata
from blocos import RAIZ, todos_os_blocos

EXT = {"c": ".c", "cpp": ".cpp", "java": ".java", "python": ".py", "php": ".php", "perl": ".pl",
       "clojure": ".clj", "prolog": ".pl", "csharp": ".cs"}
COMENTARIO = {"c": "//", "cpp": "//", "java": "//", "csharp": "//", "python": "#", "php": "//",
              "perl": "#", "clojure": ";;", "prolog": "%"}
NOME_LG = {"c": "C", "cpp": "C++", "java": "Java", "csharp": "C#", "python": "Python", "php": "PHP",
           "perl": "Perl", "clojure": "Clojure", "prolog": "Prolog"}


def ascii_slug(t, n=48):
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:n].rstrip("-") or "exemplo"


def grupo(arquivo):
    m = re.match(r"01 - Aulas/Aula (\d+)", arquivo)
    if m: return f"aula-{m.group(1)}"
    m = re.match(r"02 - Listas de Exercícios/Lista (\d+)", arquivo)
    if m: return f"lista-{m.group(1)}"
    if arquivo.startswith("04 - Provas"): return "simulados"
    if arquivo.startswith("06 - Revis"): return "revisoes"
    return ascii_slug(arquivo.split("/")[0])


def origem(arquivo):
    base = os.path.splitext(os.path.basename(arquivo))[0]
    base = re.sub(r"-aula-\d+$", "", base)
    base = re.sub(r"-lista-\d+$", "", base)
    base = re.sub(r"-simulado-(\d+)$", r"-\1", base)   # vários simulados no mesmo grupo
    return ascii_slug(base, 30)


def cabecalho(b, como_rodar):
    c = COMENTARIO[b.linguagem]
    link = "../" * 3 + b.arquivo
    linhas = [f"Gerado automaticamente a partir de {b.arquivo} (linha {b.linha}).",
              f"Seção: {b.titulo}" if b.titulo else None,
              "Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py",
              f"Como executar:  {como_rodar}"]
    p = b.params
    if p.get("entrada"): linhas.append("Entrada de exemplo: " + p["entrada"].replace("\n", " ⏎ "))
    if p.get("consulta"): linhas.append("Consulta: ?- " + p["consulta"])
    if p.get("saida-contem"): linhas.append("A saída deve conter: " + " | ".join(p["saida-contem"].split("|")).replace("\n", " ⏎ "))
    if p.get("compilacao-falha") == "sim": linhas.append("ATENÇÃO: este exemplo NÃO compila de propósito (ilustra um erro).")
    return "\n".join(f"{c} {l}" for l in linhas if l) + "\n"


def gerar(destino):
    blocos = [b for b in todos_os_blocos() if b.testavel or b.completo]
    usados, indice = set(), []
    for b in blocos:
        g, o = grupo(b.arquivo), origem(b.arquivo)
        base = f"{b.ordem:02d}-{ascii_slug(b.titulo)}"
        if b.params.get("compilacao-falha") == "sim": base += "-nao-compila"
        pasta = os.path.join(destino, g, o)
        rel_runner = f"python3 ferramentas/rodar.py codigo/{g}/{o}/"
        if b.linguagem in ("java", "csharp"):
            from motores import _classe_java
            nome = (b.params.get("classe") or _classe_java(b.codigo)) + ".java" if b.linguagem == "java" else "Programa.cs"
            pasta = os.path.join(pasta, base)
            caminho = os.path.join(pasta, nome)
            rel = os.path.relpath(caminho, destino)
        else:
            caminho = os.path.join(pasta, base + EXT[b.linguagem])
            rel = os.path.relpath(caminho, destino)
        assert rel not in usados, rel
        usados.add(rel)
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        cab = cabecalho(b, f"python3 ferramentas/rodar.py codigo/{rel}")
        codigo = b.codigo
        if b.linguagem == "php" and codigo.lstrip().startswith("<?php"):
            primeira, _, resto = codigo.lstrip().partition("\n")
            texto = primeira + "\n" + cab + resto
        else:
            texto = cab + "\n" + codigo
        open(caminho, "w", encoding="utf-8").write(texto)
        if b.params.get("entrada"):
            open(os.path.splitext(caminho)[0] + ".entrada.txt", "w", encoding="utf-8").write(b.params["entrada"].rstrip("\n") + "\n")
        if b.linguagem == "csharp":
            open(os.path.join(pasta, "Programa.csproj"), "w").write(
                '<Project Sdk="Microsoft.NET.Sdk">\n  <PropertyGroup>\n    <OutputType>Exe</OutputType>\n'
                '    <TargetFramework>net10.0</TargetFramework>\n    <ImplicitUsings>disable</ImplicitUsings>\n'
                '    <Nullable>disable</Nullable>\n  </PropertyGroup>\n</Project>\n')
        indice.append((g, o, rel, b))
    escrever_readme(destino, indice)
    escrever_readmes_pastas(destino, indice)
    return indice


def escrever_readmes_pastas(destino, indice):
    """Um README.md em cada subpasta de codigo/, para navegar pelo GitHub como num caderno."""
    from collections import defaultdict
    progs = defaultdict(list)                      # pasta (relativa a codigo/) → [(arquivo, bloco)]
    pastas = set()
    for g, o, rel, b in indice:
        d = os.path.dirname(rel)
        progs[d].append((os.path.basename(rel), b))
        while d:
            pastas.add(d)
            d = os.path.dirname(d)
    for d in sorted(pastas):
        nivel = d.count("/") + 2                   # codigo/<d> → profundidade até a raiz do repositório
        ate_raiz = "../" * nivel
        partes = d.split("/")
        trilha = [f"[Início]({ate_raiz}README.md)", f"[codigo]({'../' * (nivel - 1)}README.md)"]
        for i, nome in enumerate(partes):
            trilha.append(f"**{nome}**" if i == len(partes) - 1 else f"[{nome}]({'../' * (len(partes) - 1 - i)}README.md)")
        L = [" › ".join(trilha), "", f"# codigo/{d}", "",
             "> **Gerado automaticamente** por `ferramentas/gerar_codigo.py`. A fonte de cada programa é o Markdown indicado em *Origem*: edite lá.", ""]
        subs = sorted(x for x in pastas if os.path.dirname(x) == d)
        if subs:
            L += ["| Pasta | Programas |", "| --- | :-: |"]
            for x in subs:
                n = sum(len(v) for k, v in progs.items() if k == x or k.startswith(x + "/"))
                L.append(f"| [{os.path.basename(x)}/]({os.path.basename(x).replace(' ', '%20')}/README.md) | {n} |")
            L.append("")
        if progs.get(d):
            L += ["| Programa | Linguagem | Origem | Executar |", "| --- | --- | --- | --- |"]
            for nome, b in sorted(progs[d], key=lambda t: t[0]):
                src = ate_raiz + b.arquivo.replace(" ", "%20") + "#" + secao_ancora(b.titulo)
                L.append(f"| [`{nome}`]({nome.replace(' ', '%20')}) | {NOME_LG[b.linguagem]} | "
                         f"[{os.path.basename(b.arquivo)} — {b.titulo or 'início'}]({src}) | `python3 ferramentas/rodar.py codigo/{d}/{nome}` |")
            L.append("")
        open(os.path.join(destino, d, "README.md"), "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")


def escrever_readme(destino, indice):
    from collections import Counter, OrderedDict
    cont = Counter(b.linguagem for *_, b in indice)
    grupos = OrderedDict()
    for g, o, rel, b in indice:
        grupos.setdefault(g, []).append((o, rel, b))
    L = ["[Início](../README.md) › **codigo** · [Mapa](../MAPA.md)", "", "# Código dos exemplos", "",
         "Todos os programas dos resumos, resoluções, listas, simulados e revisões, um por arquivo, prontos para executar.",
         "", "> **Gerado automaticamente** por `ferramentas/gerar_codigo.py` a partir dos arquivos Markdown, que são a fonte. "
         "Para alterar um exemplo, edite o Markdown e gere de novo; os testes automáticos conferem se esta pasta está atualizada.",
         "", "## Como executar", "",
         "Abra o repositório no **Codespaces** (todas as linguagens já instaladas) ou instale o ambiente com `bash ferramentas/instalar-ambiente.sh`. Depois:",
         "", "```bash", "python3 ferramentas/rodar.py codigo/aula-14/resolucoes/04-e8-atividade-2-original-p-20.clj",
         "```", "",
         "O `rodar.py` compila quando preciso, usa automaticamente o arquivo `.entrada.txt` ao lado do programa (se existir) e, para Prolog, executa a consulta indicada no cabeçalho. Opções: `--entrada \"2 3\"` e `--consulta \"pai(X, ana).\"`.",
         "", "Também é possível usar cada ferramenta diretamente:", "",
         "| Linguagem | Comando |", "| --- | --- |",
         "| C | `gcc arquivo.c -o programa -lm && ./programa` |",
         "| C++ | `g++ -std=c++17 arquivo.cpp -o programa && ./programa` |",
         "| Java | `java Classe.java` (dentro da pasta do exemplo) |",
         "| C# | `dotnet run` (dentro da pasta do exemplo) |",
         "| Python / PHP / Perl | `python3 arquivo.py` · `php arquivo.php` · `perl arquivo.pl` |",
         "| Clojure | `clojure -M arquivo.clj` |",
         "| Prolog | `swipl arquivo.pl` e, no prompt, a consulta do cabeçalho |",
         "", "## Totais", "",
         "| Linguagem | Programas |", "| --- | :-: |"]
    for lg in ("c", "cpp", "java", "csharp", "python", "php", "perl", "clojure", "prolog"):
        if cont[lg]: L.append(f"| {NOME_LG[lg]} | {cont[lg]} |")
    L += [f"| **Total** | **{sum(cont.values())}** |", "", "## Índice", ""]
    for g, itens in grupos.items():
        L += [f"### {g}", "", "| Programa | Linguagem | Origem |", "| --- | --- | --- |"]
        for o, rel, b in itens:
            link_src = "../" + b.arquivo.replace(" ", "%20") + "#" + secao_ancora(b.titulo)
            L.append(f"| [`{rel}`]({rel.replace(' ', '%20')}) | {NOME_LG[b.linguagem]} | [{os.path.basename(b.arquivo)} — {b.titulo or 'início'}]({link_src}) |")
        L.append("")
    open(os.path.join(destino, "README.md"), "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")


def secao_ancora(titulo):
    h = titulo.strip().lower()
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = "".join(c for c in h if c.isalnum() or c in " -_")
    return h.replace(" ", "-")


def dirs_iguais(a, b):
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False, cmp.left_only + cmp.right_only + cmp.diff_files
    for sub in cmp.common_dirs:
        ok, dif = dirs_iguais(os.path.join(a, sub), os.path.join(b, sub))
        if not ok: return False, [f"{sub}/{d}" for d in dif]
    return True, []


if __name__ == "__main__":
    alvo = os.path.join(RAIZ, "codigo")
    if "--verificar" in sys.argv:
        tmp = tempfile.mkdtemp()
        gerar(tmp)
        ok, dif = dirs_iguais(tmp, alvo) if os.path.isdir(alvo) else (False, ["codigo/ não existe"])
        shutil.rmtree(tmp)
        print("codigo/ atualizado" if ok else "codigo/ DESATUALIZADO — rode python3 ferramentas/gerar_codigo.py. Diferenças: " + ", ".join(dif[:10]))
        sys.exit(0 if ok else 1)
    if os.path.isdir(alvo): shutil.rmtree(alvo)
    idx = gerar(alvo)
    print(f"{len(idx)} programas gerados em codigo/")
