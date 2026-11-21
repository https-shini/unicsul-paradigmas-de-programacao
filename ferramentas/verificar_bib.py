#!/usr/bin/env python3
"""Valida o arquivo BibTeX de 08 - Referências e Fontes e confere se cada entrada aparece no catálogo.

Uso: python3 ferramentas/verificar_bib.py   (requer: pip install "bibtexparser<2")"""
import collections, os, re, sys
import bibtexparser

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, "08 - Referências e Fontes")
db = bibtexparser.load(open(os.path.join(PASTA, "referencias.bib"), encoding="utf-8"))
erros = []
chaves = collections.Counter(e["ID"] for e in db.entries)
erros += [f"chave duplicada: {k}" for k, c in chaves.items() if c > 1]
for e in db.entries:
    for campo in ("author", "title", "year"):
        if campo not in e:
            erros.append(f"{e['ID']}: falta o campo {campo}")
catalogo = open(os.path.join(PASTA, "livros.md"), encoding="utf-8").read() + open(os.path.join(PASTA, "artigos.md"), encoding="utf-8").read()
ids_catalogo = set(re.findall(r"^### ([LA]\d\d) —", catalogo, re.M))
ids_bib = {re.search(r"([la]\d\d)$", e["ID"]).group(1).upper() for e in db.entries}
erros += [f"no catálogo mas não no BibTeX: {i}" for i in sorted(ids_catalogo - ids_bib)]
erros += [f"no BibTeX mas não no catálogo: {i}" for i in sorted(ids_bib - ids_catalogo)]
for e in erros:
    print("ERRO", e)
print(f"ENTRADAS {len(db.entries)} · NO CATÁLOGO {len(ids_catalogo)} · ERROS {len(erros)}")
sys.exit(1 if erros else 0)
