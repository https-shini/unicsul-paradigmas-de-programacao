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
    codigo: list[tuple] = []

    def expr(no):                                   # pós-ordem: operandos antes do operador
        if isinstance(no, Num):
            codigo.append(("PUSH", no.valor))
        elif isinstance(no, Var):
            codigo.append(("LOAD", no.nome, no.linha))
        elif isinstance(no, Unario):
            expr(no.expr)
            codigo.append(("NEG",))
        elif isinstance(no, Binario):
            expr(no.esq)
            expr(no.dir)
            codigo.append((OPCODES[no.op], no.linha))

    for cmd in programa.comandos:
        expr(cmd.expr)
        codigo.append(("STORE", cmd.nome) if isinstance(cmd, Atribuicao) else ("PRINT",))
    return codigo


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
        saidas = []
        for ins in codigo:
            op = ins[0]
            if op == "PUSH":
                self.pilha.append(ins[1])
            elif op == "LOAD":
                if ins[1] not in self.memoria:
                    raise ErroExecucao(f"linha {ins[2]}: variável '{ins[1]}' não definida")
                self.pilha.append(self.memoria[ins[1]])
            elif op == "STORE":
                self.memoria[ins[1]] = self.pilha.pop()
            elif op == "NEG":
                self.pilha.append(-self.pilha.pop())
            elif op == "PRINT":
                saidas.append(self.pilha.pop())
            else:
                b, a = self.pilha.pop(), self.pilha.pop()
                self.pilha.append(aplicar(OPERADOR[op], a, b, ins[1]))
        return saidas
