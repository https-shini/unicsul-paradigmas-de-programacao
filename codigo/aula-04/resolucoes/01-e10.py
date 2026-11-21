# Gerado automaticamente a partir de 01 - Aulas/Aula 04 - Sintaxe/04 - Resoluções/resolucoes-aula-04.md (linha 77).
# Seção: E10
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-04/resolucoes/01-e10.py
# Entrada de exemplo: soma = x + 10;
# A saída deve conter: soma -> identificador | = -> simbolo especial | 10 -> constante | ; -> simbolo especial | + -> operador

import re

RESERVADAS = {"int", "float", "char", "double", "if", "else", "for", "while", "return", "void"}

# Ordem importa: padrões mais longos primeiro (== antes de =, ++ antes de +).
PADROES = [
    ("string",            r'"[^"]*"'),
    ("constante",         r'\d+\.\d+|\d+'),
    ("nome",              r'[A-Za-z_]\w*'),
    ("operador",          r'\+\+|--|==|!=|<=|>=|[+\-*/%<>]'),
    ("simbolo especial",  r'[=&()\[\]{};,]'),
    ("espaco",            r'\s+'),
]
REGEX = re.compile("|".join(f"(?P<g{i}>{p})" for i, (_, p) in enumerate(PADROES)))

def analisar(linha):
    pos = 0
    while pos < len(linha):
        m = REGEX.match(linha, pos)
        if not m:
            raise SyntaxError(f"erro lexico: caractere invalido {linha[pos]!r} na posicao {pos}")
        grupo = PADROES[int(m.lastgroup[1:])][0]
        lexema = m.group()
        if grupo == "nome":
            grupo = "palavra reservada" if lexema in RESERVADAS else "identificador"
        if grupo != "espaco":
            print(f"{lexema} -> {grupo}")
        pos = m.end()

analisar(input())
