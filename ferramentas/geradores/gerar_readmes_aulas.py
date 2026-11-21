#!/usr/bin/env python3
"""Gera o README.md de cada pasta de aula (índice dos arquivos e navegação)."""
import os, re, json, urllib.parse
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
root = os.path.join(RAIZ, "01 - Aulas")
inv = {os.path.basename(r[1]): r for r in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inventario.json')))}
temas = {
1:("Apresentação da disciplina (plano de ensino)","Ementa, objetivos, conteúdo, sistema de avaliação e bibliografia."),
2:("Evolução das linguagens e paradigmas de programação","O que é uma linguagem; o mesmo problema em Pascal, Java e Prolog; os quatro paradigmas; restrições de projeto; critérios de avaliação; gerações e linha do tempo."),
3:("Implementação das linguagens de programação","Compilação, interpretação pura e implementação híbrida; fases do compilador; JVM e bytecode; computadores virtuais em camadas; ambientes de programação."),
4:("Introdução à sintaxe das linguagens de programação","Sintaxe × semântica; BNF; sintaxe léxica, concreta e abstrata; lexema, token e padrão; os tokens de C; regras de nomes e palavras reservadas."),
5:("Introdução à semântica das linguagens de programação","Formas de especificar a semântica; os seis atributos da variável; escopo estático × dinâmico; tempo de vida; constantes nomeadas; semântica estática × dinâmica."),
6:("Sistema de tipos","Tipos básicos e tamanhos; overflow; tipagem estática × dinâmica; força de tipagem e coerção (C, Java, PHP, Python); representação no processador; sobrecarga de operadores."),
7:("Tipos compostos","Enumerações, registros (struct), classes, matrizes multidimensionais e strings; exercício da matriz de notas em Java."),
8:("Ponteiros","Ponteiros e endereços; organização da memória; passagem por valor × referência em C, C++ e Java; alocação estática × dinâmica; regiões de memória."),
9:("Paradigma imperativo — parte 1","Origem nos primeiros computadores; arquitetura de von Neumann; Turing-completude; variáveis e atribuição; programação não estruturada (goto) × estruturada; artigo de Dijkstra (1968)."),
10:("Paradigma imperativo — parte 2","Abstração; abstração procedural e refinamento sucessivo (ordenação de dez números); acoplamento e coesão; abstração de dados e TDA."),
11:("Paradigma imperativo — parte 3","Subprogramas; parâmetros formais e reais; os quatro modelos semânticos de passagem; modificadores ref, out, in e ref readonly do C#."),
12:("Paradigma orientado a objetos — parte 1","Motivação da OO; a pilha reescrita progressivamente em Java e C++; abstração, TDA e encapsulamento; classe, modificadores de acesso; construtor, destrutor e coleta de lixo."),
13:("Paradigma orientado a objetos — parte 2","Herança simples e múltipla (impressora multifuncional); interfaces em Java; polimorfismo estático e dinâmico; classe abstrata × interface; hierarquia de contas."),
14:("Paradigma funcional","Origem e ideia central; linguagens puras × impuras; o que uma linguagem funcional fornece; Clojure: notação prefixa, funções numéricas, Ratio, def, leitura e predicados."),
15:("Paradigma lógico","Procedural × declarativo; lógica proposicional e de predicados; Prolog: termos, fatos, regras, consultas, unificação, findall; atividades com a relação pai/2."),
}
dirs = sorted(d for d in os.listdir(root) if d.startswith("Aula "))
q = lambda p: p.replace(' ', '%20')
for i, d in enumerate(dirs):
    n = int(d[5:7]); base = os.path.join(root, d)
    titulo, desc = temas[n]
    pdfs = sorted(os.listdir(os.path.join(base, "01 - Slides Originais")))
    resumos = sorted(os.listdir(os.path.join(base, "02 - Resumo Teórico")), key=lambda r: (not r.startswith('resumo-aula'), r))
    ex = os.path.join(base, "03 - Exercícios", f"exercicios-aula-{n:02d}.md")
    nex = len(re.findall(r'(?m)^(?:\*\*|#+ )E\d+', open(ex).read()))
    res = os.path.join(base, "04 - Resoluções", f"resolucoes-aula-{n:02d}.md")
    ncode = len(re.findall(r'<!--\s*teste:', open(res).read()))
    L = [f"# {d}", "", f"**{titulo}.** {desc}", ""]
    L += ["| Pasta | Conteúdo |", "| --- | --- |"]
    pdfcell = " · ".join(f"[`{p}`]({q('01 - Slides Originais/'+p)}) ({inv[p][3]} p.)" for p in pdfs)
    L.append(f"| 01 - Slides Originais | **[Material original]** {pdfcell} |")
    rcell = " · ".join(f"[{r}]({q('02 - Resumo Teórico/'+r)})" for r in resumos)
    L.append(f"| 02 - Resumo Teórico | {rcell} |")
    L.append(f"| 03 - Exercícios | [exercicios-aula-{n:02d}.md]({q('03 - Exercícios/exercicios-aula-%02d.md' % n)}) — {nex} exercícios em quatro níveis |")
    L.append(f"| 04 - Resoluções | [resolucoes-aula-{n:02d}.md]({q('04 - Resoluções/resolucoes-aula-%02d.md' % n)}) — **[Resolução elaborada]**, não é gabarito oficial |")
    L.append(f"| 05 - Materiais Complementares | [materiais-complementares.md]({q('05 - Materiais Complementares/materiais-complementares.md')}) |")
    L.append("")
    L.append("**Ordem sugerida:** slides → resumo → exercícios → resoluções → complementares.")
    L.append("")
    nav = []
    if i > 0: nav.append(f"**Anterior:** [{dirs[i-1]}](../{q(dirs[i-1])}/README.md)")
    nav.append("[Índice das aulas](../../README.md#aulas)")
    if i < len(dirs)-1: nav.append(f"**Próxima:** [{dirs[i+1]}](../{q(dirs[i+1])}/README.md)")
    L.append(" · ".join(nav))
    open(os.path.join(base, "README.md"), "w").write("\n".join(L) + "\n")
    print(d, nex, ncode)
