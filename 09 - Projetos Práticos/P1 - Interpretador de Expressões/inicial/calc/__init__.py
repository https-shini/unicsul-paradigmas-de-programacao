"""calc — interpretador e compilador de uma pequena linguagem de expressões.

Projeto P1 de "Paradigmas de Linguagens de Programação". Cada módulo é uma fase
da implementação vista nas Aulas 03–05:

    lexico.py        caracteres  → tokens            (análise léxica)
    sintatico.py     tokens      → árvore sintática  (análise sintática, BNF)
    interpretador.py árvore      → resultados        (interpretação pura)
    compilador.py    árvore      → bytecode → VM     (implementação híbrida)
"""
from .lexico import tokenizar, Token, ErroLexico
from .sintatico import analisar, ErroSintatico
from .interpretador import Interpretador, ErroExecucao, formatar
from .compilador import compilar, desmontar, MaquinaVirtual


def executar(codigo, modo="interpretador"):
    """Executa um programa e devolve a lista de linhas impressas.

    modo="interpretador" percorre a árvore; modo="vm" compila para bytecode e executa na máquina virtual.
    """
    programa = analisar(tokenizar(codigo))
    if modo == "vm":
        saidas = MaquinaVirtual().executar(compilar(programa))
    else:
        saidas = Interpretador().executar(programa)
    return [formatar(v) for v in saidas]
