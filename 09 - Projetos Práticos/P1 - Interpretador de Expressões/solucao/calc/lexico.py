"""Análise léxica (Aula 03 p.9; Aula 04 p.8–9): agrupa caracteres em lexemas e classifica cada um como token."""
from __future__ import annotations
from dataclasses import dataclass


class ErroLexico(Exception):
    """Caractere que não inicia nenhum token válido."""


@dataclass(frozen=True)
class Token:
    tipo: str       # NUM, ID, PRINT, OP, ATRIB, ABRE, FECHA, FIM_LINHA, FIM
    lexema: str
    linha: int
    coluna: int


PALAVRAS_RESERVADAS = {"print": "PRINT"}
SIMBOLOS = {"+": "OP", "-": "OP", "*": "OP", "/": "OP", "=": "ATRIB", "(": "ABRE", ")": "FECHA"}


def tokenizar(codigo: str) -> list[Token]:
    """Devolve a lista de tokens do código, terminada por um token FIM."""
    tokens: list[Token] = []
    i, linha, coluna = 0, 1, 1
    n = len(codigo)
    while i < n:
        c = codigo[i]
        if c == "\n":
            tokens.append(Token("FIM_LINHA", "\\n", linha, coluna))
            i, linha, coluna = i + 1, linha + 1, 1
        elif c in " \t\r":                                   # espaços separam lexemas e são descartados
            i, coluna = i + 1, coluna + 1
        elif c == "#":                                       # comentário até o fim da linha
            while i < n and codigo[i] != "\n":
                i, coluna = i + 1, coluna + 1
        elif c.isdigit() or (c == "." and i + 1 < n and codigo[i + 1].isdigit()):
            inicio = i
            while i < n and codigo[i].isdigit():
                i += 1
            if i < n and codigo[i] == "." and i + 1 < n and codigo[i + 1].isdigit():
                i += 1
                while i < n and codigo[i].isdigit():
                    i += 1
            lexema = codigo[inicio:i]
            tokens.append(Token("NUM", lexema, linha, coluna))
            coluna += i - inicio
        elif c.isalpha() or c == "_":
            inicio = i
            while i < n and (codigo[i].isalnum() or codigo[i] == "_"):
                i += 1
            lexema = codigo[inicio:i]
            tokens.append(Token(PALAVRAS_RESERVADAS.get(lexema, "ID"), lexema, linha, coluna))
            coluna += i - inicio
        elif c in SIMBOLOS:
            tokens.append(Token(SIMBOLOS[c], c, linha, coluna))
            i, coluna = i + 1, coluna + 1
        else:
            raise ErroLexico(f"linha {linha}, coluna {coluna}: caractere inesperado {c!r}")
    tokens.append(Token("FIM", "", linha, coluna))
    return tokens
