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
        no = self.termo()
        while self.ver("OP", "+") or self.ver("OP", "-"):
            op = self.consumir("OP")
            no = Binario(op.lexema, no, self.termo(), op.linha)
        return no

    def termo(self):
        no = self.fator()
        while self.ver("OP", "*") or self.ver("OP", "/"):
            op = self.consumir("OP")
            no = Binario(op.lexema, no, self.fator(), op.linha)
        return no

    def fator(self):
        t = self.atual()
        if self.ver("OP", "-"):
            self.consumir("OP")
            return Unario("-", self.fator())
        if self.ver("NUM"):
            self.consumir("NUM")
            return Num(float(t.lexema) if "." in t.lexema else int(t.lexema))
        if self.ver("ID"):
            self.consumir("ID")
            return Var(t.lexema, t.linha)
        if self.ver("ABRE"):
            self.consumir("ABRE")
            no = self.expr()
            self.consumir("FECHA")
            return no
        achado = repr(t.lexema) if t.tipo not in ("FIM", "FIM_LINHA") else "fim da linha"
        raise ErroSintatico(f"linha {t.linha}, coluna {t.coluna}: esperava número, variável ou '(', encontrou {achado}")


def analisar(tokens: list[Token]) -> Programa:
    return Analisador(tokens).programa()
