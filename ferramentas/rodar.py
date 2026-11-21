#!/usr/bin/env python3
"""Executa um programa de qualquer linguagem da disciplina, compilando quando necessário.

Uso:
    python3 ferramentas/rodar.py caminho/do/programa.ext [--entrada "2 3"] [--consulta "pai(X, ana)."]

- Se existir um arquivo .entrada.txt ao lado do programa, ele é usado como entrada padrão.
- Para Prolog, a consulta vem de --consulta ou da linha "Consulta: ?- ..." do cabeçalho;
  sem consulta, executa main/0.
- Sem --entrada nem .entrada.txt, a entrada é lida do terminal (digite e tecle Ctrl+D ao final).
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motores import executar, motor

LG = {".c": "c", ".cpp": "cpp", ".cc": "cpp", ".java": "java", ".cs": "csharp", ".py": "python",
      ".php": "php", ".clj": "clojure", ".cljs": "clojure", ".pro": "prolog"}


def linguagem(caminho, codigo):
    ext = os.path.splitext(caminho)[1].lower()
    if ext == ".pl":  # Perl ou Prolog
        return "prolog" if re.search(r"^\s*%|:-|^\w+\(.*\)\.\s*$", codigo, re.M) and "use strict" not in codigo and "my $" not in codigo else "perl"
    return LG.get(ext)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo")
    ap.add_argument("--entrada")
    ap.add_argument("--consulta")
    a = ap.parse_args()
    codigo = open(a.arquivo, encoding="utf-8").read()
    lg = linguagem(a.arquivo, codigo)
    if not lg:
        sys.exit(f"Extensão não reconhecida: {a.arquivo}")
    if motor(lg) is None:
        sys.exit(f"Não há ferramenta instalada para {lg}. Rode: bash ferramentas/instalar-ambiente.sh")
    params = {}
    entrada = a.entrada
    lateral = os.path.splitext(a.arquivo)[0] + ".entrada.txt"
    if entrada is None and os.path.exists(lateral):
        entrada = open(lateral, encoding="utf-8").read()
    if entrada is None and not sys.stdin.isatty():
        entrada = sys.stdin.read()
    if entrada is None and re.search(r"\(read|Scanner|scanf|input\(|ReadLine|<STDIN>|fgets|cin\s*>>|read\(", codigo):
        print("(o programa lê dados: digite a entrada e tecle Ctrl+D)", file=sys.stderr)
        entrada = sys.stdin.read()
    params["entrada"] = (entrada or "").replace("\\n", "\n")
    if lg == "prolog":
        m = re.search(r"Consulta: \?- (.+)$", codigo, re.M)
        params["consulta"] = a.consulta or (m.group(1).strip() if m else "main.")
        print(f"?- {params['consulta']}", file=sys.stderr)
    r = executar(lg, codigo, params)
    sys.stdout.write(r.saida)
    if r.erro:
        sys.stderr.write(r.erro)
    sys.exit(0 if r.ok else (r.codigo or 1))


if __name__ == "__main__":
    main()
