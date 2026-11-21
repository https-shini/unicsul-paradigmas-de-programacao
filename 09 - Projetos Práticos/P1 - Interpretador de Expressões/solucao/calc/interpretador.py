"""Interpretação pura (Aula 03 p.10–11): percorre a árvore e executa cada comando diretamente.

Os erros desta fase são semânticos e DINÂMICOS (Aula 05 p.17): só aparecem quando o comando executa.
"""
from __future__ import annotations
from .arvore import Num, Var, Unario, Binario, Atribuicao, Imprime, Programa


class ErroExecucao(Exception):
    """Erro detectado durante a execução: variável não definida, divisão por zero."""


def aplicar(op, a, b, linha=0):
    """Operação aritmética compartilhada pelo interpretador e pela máquina virtual."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ErroExecucao(f"linha {linha}: divisão por zero")
        return a / b
    raise ErroExecucao(f"operador desconhecido {op!r}")


def formatar(v) -> str:
    return str(v)


class Interpretador:
    def __init__(self):
        self.memoria: dict[str, int | float] = {}      # vinculação nome → valor (Aula 05)

    def executar(self, programa: Programa) -> list:
        saidas = []
        for cmd in programa.comandos:
            if isinstance(cmd, Atribuicao):
                self.memoria[cmd.nome] = self.avaliar(cmd.expr)
            elif isinstance(cmd, Imprime):
                saidas.append(self.avaliar(cmd.expr))
        return saidas

    def avaliar(self, no):
        if isinstance(no, Num):
            return no.valor
        if isinstance(no, Var):
            if no.nome not in self.memoria:
                raise ErroExecucao(f"linha {no.linha}: variável '{no.nome}' não definida")
            return self.memoria[no.nome]
        if isinstance(no, Unario):
            return -self.avaliar(no.expr)
        if isinstance(no, Binario):
            return aplicar(no.op, self.avaliar(no.esq), self.avaliar(no.dir), no.linha)
        raise ErroExecucao(f"nó desconhecido: {no!r}")
