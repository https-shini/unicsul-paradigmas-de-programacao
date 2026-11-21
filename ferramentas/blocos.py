"""Leitura dos blocos de código dos arquivos Markdown do repositório.

Um bloco é testável quando é precedido (imediatamente, só com espaços entre eles) por um
comentário HTML do tipo:

    <!-- teste: entrada="2 3" saida-contem="5|6" -->

Parâmetros aceitos no comentário:
    entrada="..."            texto enviado à entrada padrão (\\n vira quebra de linha)
    saida-contem="a|b"       cada trecho separado por | deve aparecer na saída
    saida-contem-cljs="..."  substitui saida-contem quando o Clojure roda como ClojureScript (nbb)
    consulta="pai(X, ana)."  consulta Prolog a executar
    compilacao-falha="sim"   o código deve NÃO compilar; erro-contem="..." confere a mensagem
    erro-esperado="sim"      o programa deve terminar com erro
    classe="Nome"            classe Java principal (quando não for detectável)
    pular="sim"              ignora o bloco

Este módulo é usado por testar_codigo.py, gerar_codigo.py e verificar.py.
"""
import os
import re
from dataclasses import dataclass, field

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERCA = re.compile(r'^([ \t]*)```([\w#+-]+)[ \t]*\n(.*?)^\1```[ \t]*$', re.S | re.M)
MARCADOR = re.compile(r'<!--\s*teste:\s*(.*?)-->', re.S)
TITULO = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$', re.M)
LINGUAGENS = {"c": "c", "cpp": "cpp", "java": "java", "python": "python", "php": "php",
              "perl": "perl", "clojure": "clojure", "prolog": "prolog", "csharp": "csharp"}
# Modelos e o caderno pessoal não são testados: o código ali é ilustrativo ou rascunho do estudante
IGNORAR_DIRS = {".git", "node_modules", "codigo", "09 - Projetos Práticos", ".devcontainer", ".github",
                "Modelos", "10 - Caderno de Anotações"}


@dataclass
class Bloco:
    arquivo: str              # caminho relativo à raiz
    linguagem: str
    codigo: str
    linha: int                # linha do Markdown onde o bloco começa
    titulo: str               # título Markdown mais próximo acima do bloco
    ordem: int                # posição do bloco no arquivo (1, 2, ...)
    params: dict = field(default_factory=dict)

    @property
    def testavel(self):
        return bool(self.params) and self.params.get("pular") != "sim"

    @property
    def completo(self):
        """Programa completo (compilável/executável) mesmo sem marcador."""
        c, lg = self.codigo, self.linguagem
        if lg in ("c", "cpp"):
            return "main(" in c or "compilacao-falha" in self.params
        if lg == "java":
            return "static void main" in c or "compilacao-falha" in self.params
        if lg == "csharp":
            return "static void Main" in c or "static int Main" in c
        return self.testavel


def ler_params(spec):
    return {k: v.replace("\\n", "\n") for k, v in re.findall(r'([\w-]+)="(.*?)"', spec, re.S)}


def blocos_do_arquivo(caminho, raiz=RAIZ):
    texto = open(caminho, encoding="utf-8").read()
    rel = os.path.relpath(caminho, raiz)
    titulos = [(m.start(), m.group(2)) for m in TITULO.finditer(texto)]
    saida, ordem = [], 0
    for m in CERCA.finditer(texto):
        lg = LINGUAGENS.get(m.group(2).lower())
        if not lg:
            continue
        ordem += 1
        antes = texto[max(0, m.start() - 600):m.start()]
        marcas = list(MARCADOR.finditer(antes))
        params = {}
        if marcas and antes[marcas[-1].end():].strip() == "":
            params = ler_params(marcas[-1].group(1))
        titulo = ""
        for pos, t in titulos:
            if pos < m.start():
                titulo = t
            else:
                break
        recuo = m.group(1)
        codigo = "".join(l[len(recuo):] if l.startswith(recuo) else l for l in m.group(3).splitlines(True))
        saida.append(Bloco(rel, lg, codigo, texto.count("\n", 0, m.start()) + 1, titulo, ordem, params))
    return saida


def todos_os_blocos(raiz=RAIZ, filtros=()):
    arquivos = []
    for dp, dn, fn in os.walk(raiz):
        dn[:] = sorted(d for d in dn if d not in IGNORAR_DIRS)
        arquivos += [os.path.join(dp, f) for f in sorted(fn) if f.endswith(".md")]
    if filtros:
        arquivos = [a for a in arquivos if any(f in os.path.relpath(a, raiz) for f in filtros)]
    blocos = []
    for a in arquivos:
        blocos += blocos_do_arquivo(a, raiz)
    return blocos
