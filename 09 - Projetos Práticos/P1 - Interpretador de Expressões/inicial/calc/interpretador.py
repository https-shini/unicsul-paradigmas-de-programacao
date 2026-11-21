"""Interpretação pura (Aula 03 p.10–11): percorre a árvore e executa cada comando diretamente.

Os erros desta fase são semânticos e DINÂMICOS (Aula 05 p.17): só aparecem quando o comando executa.
"""
from __future__ import annotations
from .arvore import Num, Var, Unario, Binario, Atribuicao, Imprime, Programa


class ErroExecucao(Exception):
    """Erro detectado durante a execução: variável não definida, divisão por zero."""


def aplicar(op, a, b, linha=0):
    """Operação aritmética compartilhada pelo interpretador e pela máquina virtual."""
    # TODO: etapa 3 — + - * /; divisão por zero → raise ErroExecucao(f"linha {linha}: divisão por zero")
    raise NotImplementedError("TODO: etapa 3 — aplicar")


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
        """Num → valor; Var → memória (não definida: ErroExecucao); Unario → negação; Binario → aplicar()."""
        raise NotImplementedError("TODO: etapa 3 — avaliar")
