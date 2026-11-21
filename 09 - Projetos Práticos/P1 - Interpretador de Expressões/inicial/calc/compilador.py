"""Implementação híbrida (Aula 03 p.12–14): a árvore é traduzida para um código intermediário
(bytecode de uma máquina de pilha), que uma máquina virtual executa — o mesmo esquema da JVM.

Instruções: PUSH v · LOAD x · STORE x · ADD · SUB · MUL · DIV · NEG · PRINT
"""
from __future__ import annotations
from .arvore import Num, Var, Unario, Binario, Atribuicao, Imprime, Programa
from .interpretador import ErroExecucao, aplicar

OPCODES = {"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}
OPERADOR = {v: k for k, v in OPCODES.items()}


def compilar(programa: Programa) -> list[tuple]:
    """Etapa 4. Gere as instruções em PÓS-ORDEM (operandos antes do operador):
        Num → ("PUSH", valor)        Var → ("LOAD", nome, linha)       Unario → expr + ("NEG",)
        Binario → esq + dir + (OPCODES[op], linha)
        Atribuicao → expr + ("STORE", nome)                        Imprime → expr + ("PRINT",)
    """
    raise NotImplementedError("TODO: etapa 4 — compilar")


def desmontar(codigo: list[tuple]) -> list[str]:
    """Texto legível do bytecode: ["PUSH 2", "PUSH 3", "ADD", "STORE x"]."""
    linhas = []
    for ins in codigo:
        if ins[0] in ("PUSH", "LOAD", "STORE"):
            linhas.append(f"{ins[0]} {ins[1]}")
        else:
            linhas.append(ins[0])
    return linhas


class MaquinaVirtual:
    def __init__(self):
        self.pilha: list = []
        self.memoria: dict = {}

    def executar(self, codigo: list[tuple]) -> list:
        """Execute cada instrução usando self.pilha e self.memoria; PRINT desempilha para a lista de saídas.
        Nas operações binárias, o operando da DIREITA está no topo da pilha. Reaproveite aplicar().
        """
        raise NotImplementedError("TODO: etapa 4 — máquina virtual")
