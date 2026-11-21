"""Análise sintática descendente recursiva (Aula 04): um método para cada regra da gramática em BNF.

    <programa> ::= { <linha> } FIM
    <linha>    ::= [ <comando> ] ( FIM_LINHA | FIM )
    <comando>  ::= id "=" <expr> | "print" <expr>
    <expr>     ::= <termo> { ( "+" | "-" ) <termo> }
    <termo>    ::= <fator> { ( "*" | "/" ) <fator> }
    <fator>    ::= "-" <fator> | num | id | "(" <expr> ")"

A precedência vem da própria gramática: <termo> fica "mais embaixo" que <expr>, então * e / são
agrupados antes de + e -. O laço { ... } monta a árvore da esquerda para a direita, o que dá
associatividade à esquerda: 10 - 3 - 2 = (10 - 3) - 2.
"""
from __future__ import annotations
from .lexico import Token
from .arvore import Num, Var, Unario, Binario, Atribuicao, Imprime, Programa


class ErroSintatico(Exception):
    """Sequência de tokens que não respeita a gramática."""


class Analisador:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    # ---- utilitários
    def atual(self) -> Token:
        return self.tokens[self.pos]

    def ver(self, tipo, lexema=None) -> bool:
        t = self.atual()
        return t.tipo == tipo and (lexema is None or t.lexema == lexema)

    def consumir(self, tipo, lexema=None) -> Token:
        if not self.ver(tipo, lexema):
            t = self.atual()
            esperado = repr(lexema) if lexema else tipo
            achado = repr(t.lexema) if t.tipo not in ("FIM", "FIM_LINHA") else "fim da linha"
            raise ErroSintatico(f"linha {t.linha}, coluna {t.coluna}: esperava {esperado}, encontrou {achado}")
        self.pos += 1
        return self.tokens[self.pos - 1]

    # ---- regras da gramática
    def programa(self) -> Programa:
        comandos = []
        while not self.ver("FIM"):
            if not self.ver("FIM_LINHA"):
                comandos.append(self.comando())
            if not self.ver("FIM"):
                self.consumir("FIM_LINHA")
        return Programa(comandos)

    def comando(self):
        if self.ver("PRINT"):
            self.consumir("PRINT")
            return Imprime(self.expr())
        nome = self.consumir("ID")
        self.consumir("ATRIB")
        return Atribuicao(nome.lexema, self.expr())

    def expr(self):
        """<expr> ::= <termo> { ( "+" | "-" ) <termo> }   — monte Binario(op, esq, dir, linha)"""
        raise NotImplementedError("TODO: etapa 2 — <expr>")

    def termo(self):
        """<termo> ::= <fator> { ( "*" | "/" ) <fator> }"""
        raise NotImplementedError("TODO: etapa 2 — <termo>")

    def fator(self):
        """<fator> ::= "-" <fator> | num | id | "(" <expr> ")"

        num → Num(int ou float); id → Var(nome, linha); "-" → Unario("-", ...).
        Qualquer outro token: raise ErroSintatico("linha L, coluna C: esperava número, variável ou '(' ...").
        """
        raise NotImplementedError("TODO: etapa 2 — <fator>")


def analisar(tokens: list[Token]) -> Programa:
    return Analisador(tokens).programa()
