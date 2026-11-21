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
    """Devolve a lista de tokens do código, terminada por um token FIM.

    Etapa 1. Percorra o código caractere a caractere, controlando linha e coluna:
      - "\n"           → Token("FIM_LINHA", "\\n", ...); avance a linha e volte a coluna para 1
      - espaço/tab     → descarte
      - "#"            → comentário: descarte até o fim da linha
      - dígito         → NUM: leia todos os dígitos e, se houver ".", a parte decimal ("2.5")
      - letra ou "_"   → ID ou palavra reservada (veja PALAVRAS_RESERVADAS)
      - + - * / = ( )  → veja SIMBOLOS
      - outro          → raise ErroLexico("linha L, coluna C: caractere inesperado ...")
    No fim, acrescente Token("FIM", "", linha, coluna).
    """
    tokens: list[Token] = []
    i, linha, coluna = 0, 1, 1
    while i < len(codigo):
        c = codigo[i]
        # TODO: reconheça cada tipo de lexema (veja a lista acima)
        raise NotImplementedError("TODO: etapa 1 — análise léxica")
    tokens.append(Token("FIM", "", linha, coluna))
    return tokens
