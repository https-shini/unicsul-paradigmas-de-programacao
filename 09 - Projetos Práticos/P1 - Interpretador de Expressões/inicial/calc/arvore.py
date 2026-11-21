"""Nós da árvore sintática abstrata (AST). Cada classe corresponde a uma regra da gramática."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Union


@dataclass
class Num:
    valor: Union[int, float]


@dataclass
class Var:
    nome: str
    linha: int = 0


@dataclass
class Unario:
    op: str           # só "-"
    expr: "Expr"


@dataclass
class Binario:
    op: str           # "+", "-", "*" ou "/"
    esq: "Expr"
    dir: "Expr"
    linha: int = 0


Expr = Union[Num, Var, Unario, Binario]


@dataclass
class Atribuicao:
    nome: str
    expr: Expr


@dataclass
class Imprime:
    expr: Expr


@dataclass
class Programa:
    comandos: list = field(default_factory=list)


def mostrar(no, nivel=0):
    """Representação indentada da árvore, para estudo (python3 -m calc --arvore)."""
    pad = "  " * nivel
    if isinstance(no, Programa):
        return "Programa\n" + "\n".join(mostrar(c, nivel + 1) for c in no.comandos)
    if isinstance(no, Atribuicao):
        return f"{pad}Atribuicao {no.nome}\n{mostrar(no.expr, nivel + 1)}"
    if isinstance(no, Imprime):
        return f"{pad}Imprime\n{mostrar(no.expr, nivel + 1)}"
    if isinstance(no, Binario):
        return f"{pad}Binario {no.op}\n{mostrar(no.esq, nivel + 1)}\n{mostrar(no.dir, nivel + 1)}"
    if isinstance(no, Unario):
        return f"{pad}Unario {no.op}\n{mostrar(no.expr, nivel + 1)}"
    if isinstance(no, Var):
        return f"{pad}Var {no.nome}"
    return f"{pad}Num {no.valor}"
