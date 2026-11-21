"""Linha de comando: python3 -m calc [arquivo.calc] [--tokens | --arvore | --bytecode | --vm]

Sem arquivo, abre um modo interativo (REPL). As opções mostram cada fase da implementação.
"""
import sys
from . import tokenizar, analisar, Interpretador, MaquinaVirtual, compilar, desmontar, formatar
from .arvore import mostrar
from .lexico import ErroLexico
from .sintatico import ErroSintatico
from .interpretador import ErroExecucao


def rodar(codigo, opcoes, estado):
    tokens = tokenizar(codigo)
    if "--tokens" in opcoes:
        for t in tokens:
            print(f"{t.linha}:{t.coluna}\t{t.tipo:<10}{t.lexema!r}")
        return
    programa = analisar(tokens)
    if "--arvore" in opcoes:
        print(mostrar(programa))
        return
    if "--bytecode" in opcoes:
        print("\n".join(desmontar(compilar(programa))))
        return
    if "--vm" in opcoes:
        saidas = estado.setdefault("vm", MaquinaVirtual()).executar(compilar(programa))
    else:
        saidas = estado.setdefault("int", Interpretador()).executar(programa)
    for v in saidas:
        print(formatar(v))


def main(argv):
    opcoes = [a for a in argv if a.startswith("--")]
    arquivos = [a for a in argv if not a.startswith("--")]
    estado = {}
    try:
        if arquivos:
            rodar(open(arquivos[0], encoding="utf-8").read(), opcoes, estado)
            return 0
        print("calc — digite comandos (x = 2 * 3, print x). Linha vazia ou Ctrl+D para sair.")
        while True:
            try:
                linha = input("> ")
            except EOFError:
                break
            if not linha.strip():
                break
            try:
                rodar(linha, opcoes, estado)
            except (ErroLexico, ErroSintatico, ErroExecucao) as e:
                print(f"erro: {e}")
        return 0
    except (ErroLexico, ErroSintatico, ErroExecucao) as e:
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        return 1


sys.exit(main(sys.argv[1:]))
