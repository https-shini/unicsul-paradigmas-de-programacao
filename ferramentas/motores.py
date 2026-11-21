"""Compilação e execução de programas nas linguagens da disciplina.

Cada linguagem tem um "motor". Quando a ferramenta oficial não está instalada, há alternativas:
    clojure: Clojure CLI (JVM)  →  alternativa: nbb (ClojureScript, via ferramentas/node_modules)
    prolog:  SWI-Prolog         →  alternativa: Tau-Prolog (via ferramentas/node_modules)
As alternativas têm pequenas diferenças (ex.: ClojureScript não tem o tipo Ratio).
"""
import os
import re
import shutil
import subprocess
import tempfile

FERRAMENTAS = os.path.dirname(os.path.abspath(__file__))
NODE_MODULES = os.path.join(FERRAMENTAS, "node_modules")
EXT = {"c": ".c", "cpp": ".cpp", "java": ".java", "python": ".py", "php": ".php",
       "perl": ".pl", "clojure": ".clj", "prolog": ".pl", "csharp": ".cs"}


class Resultado:
    def __init__(self, ok, saida="", erro="", codigo=0, etapa="execução"):
        self.ok, self.saida, self.erro, self.codigo, self.etapa = ok, saida, erro, codigo, etapa


def _tem(cmd):
    return shutil.which(cmd) is not None


def motor(linguagem):
    """Nome do motor disponível para a linguagem, ou None."""
    escolhas = {
        "c": ["gcc"], "cpp": ["g++"], "java": ["javac"], "python": ["python3"],
        "php": ["php"], "perl": ["perl"], "csharp": ["dotnet"],
        "clojure": ["clojure", "nbb"], "prolog": ["swipl", "tau"],
    }[linguagem]
    for e in escolhas:
        if e == "nbb" and _tem("node") and os.path.exists(os.path.join(NODE_MODULES, "nbb")):
            return "nbb"
        if e == "tau" and _tem("node") and os.path.exists(os.path.join(NODE_MODULES, "tau-prolog")):
            return "tau"
        if e not in ("nbb", "tau") and _tem(e):
            return e
    return None


def _run(cmd, entrada="", cwd=None, timeout=60):
    try:
        p = subprocess.run(cmd, input=entrada, capture_output=True, text=True, cwd=cwd, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"tempo esgotado ({timeout}s)"


def _classe_java(codigo):
    m = re.search(r'public\s+(?:final\s+)?class\s+(\w+)', codigo) or \
        re.search(r'class\s+(\w+)[^{]*\{(?:(?!\bclass\b).)*static\s+void\s+main', codigo, re.S) or \
        re.search(r'class\s+(\w+)', codigo)
    return m.group(1) if m else "Main"


def _prolog_swi(arquivo, consulta, d):
    consulta = consulta.strip().rstrip(".")
    wrapper = os.path.join(d, "_consulta.pl")
    with open(wrapper, "w", encoding="utf-8") as f:
        f.write(f""":- initialization(roda, main).
roda :-
    load_files({arquivo!r}, [silent(true)]),
    term_string(G, {consulta!r}, [variable_names(Vs)]),
    forall(call(G), mostra(Vs)),
    write('false.'), nl.
mostra([]) :- !, write(true), nl.
mostra(Vs) :- mostra_vars(Vs), nl.
mostra_vars([N=V]) :- !, format('~w = ~q', [N, V]).
mostra_vars([N=V|R]) :- format('~w = ~q, ', [N, V]), mostra_vars(R).
""")
    return ["swipl", "-q", wrapper]


def preparar(linguagem, codigo, d, params=None, nome=None):
    """Grava o código em d e devolve (comando_de_execução, Resultado_de_compilação_ou_None)."""
    params = params or {}
    if linguagem in ("c", "cpp"):
        src = os.path.join(d, "programa" + EXT[linguagem])
        open(src, "w", encoding="utf-8").write(codigo)
        comp = (["gcc", "-std=c11", "-Werror=implicit-function-declaration"] if linguagem == "c" else ["g++", "-std=c++17"])
        rc, o, e = _run(comp + ["-w", "-o", os.path.join(d, "programa"), src, "-lm"])
        return [os.path.join(d, "programa")], Resultado(rc == 0, o, e, rc, "compilação")
    if linguagem == "java":
        nome = params.get("classe") or _classe_java(codigo)
        open(os.path.join(d, nome + ".java"), "w", encoding="utf-8").write(codigo)
        rc, o, e = _run(["javac", "-nowarn", "-encoding", "UTF-8", nome + ".java"], cwd=d)
        return ["java", "-Duser.language=en", "-Duser.country=US", "-cp", d, nome], Resultado(rc == 0, o, e, rc, "compilação")
    if linguagem == "csharp":
        maior = (_run(["dotnet", "--version"])[1].strip().split(".") or ["8"])[0]
        open(os.path.join(d, "Programa.cs"), "w", encoding="utf-8").write(codigo)
        open(os.path.join(d, "Programa.csproj"), "w").write(
            '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
            f'<TargetFramework>net{maior}.0</TargetFramework><ImplicitUsings>disable</ImplicitUsings>'
            '<Nullable>disable</Nullable><InvariantGlobalization>true</InvariantGlobalization></PropertyGroup></Project>')
        rc, o, e = _run(["dotnet", "build", "-nologo", "-v", "q", "-o", os.path.join(d, "bin")], cwd=d, timeout=240)
        return ["dotnet", os.path.join(d, "bin", "Programa.dll")], Resultado(rc == 0, o, e or o, rc, "compilação")
    if linguagem == "python":
        open(os.path.join(d, "programa.py"), "w", encoding="utf-8").write(codigo)
        return ["python3", os.path.join(d, "programa.py")], None
    if linguagem == "php":
        open(os.path.join(d, "programa.php"), "w", encoding="utf-8").write(codigo)
        return ["php", os.path.join(d, "programa.php")], None
    if linguagem == "perl":
        open(os.path.join(d, "programa.pl"), "w", encoding="utf-8").write(codigo)
        return ["perl", os.path.join(d, "programa.pl")], None
    if linguagem == "clojure":
        if motor("clojure") == "clojure":
            open(os.path.join(d, "programa.clj"), "w", encoding="utf-8").write(codigo)
            return ["clojure", "-M", os.path.join(d, "programa.clj")], None
        # nbb (ClojureScript): read/read-line leem de uma fila montada com a entrada
        vals = params.get("entrada", "").split()
        prel = ("(ns user (:refer-clojure :exclude [read read-line]))\n"
                f"(def __in (atom (vector {' '.join(vals)})))\n"
                "(defn read [] (let [v (first @__in)] (swap! __in rest) v))\n"
                "(defn read-line [] (str (read)))\n")
        open(os.path.join(d, "programa.cljs"), "w", encoding="utf-8").write(prel + codigo)
        return ["node", os.path.join(NODE_MODULES, "nbb", "cli.js"), os.path.join(d, "programa.cljs")], None
    if linguagem == "prolog":
        arq = os.path.join(d, "programa.pl")
        sem_init = re.sub(r'^:-\s*initialization\((main|main,\s*main)\)\.\s*$', '', codigo, flags=re.M)
        open(arq, "w", encoding="utf-8").write(sem_init)
        consulta = params.get("consulta", "main.")
        if motor("prolog") == "swipl":
            return _prolog_swi(arq, consulta, d), None
        return ["node", os.path.join(FERRAMENTAS, "tau.js"), arq, consulta], None
    raise ValueError(linguagem)


def executar(linguagem, codigo, params=None, entrada=None, timeout=60):
    """Compila (se preciso) e executa; devolve Resultado."""
    params = params or {}
    d = tempfile.mkdtemp(prefix="plp-")
    try:
        cmd, comp = preparar(linguagem, codigo, d, params)
        if comp is not None and not comp.ok:
            return comp
        ent = params.get("entrada", "") if entrada is None else entrada
        if linguagem == "clojure" and motor("clojure") == "nbb":
            ent = ""
        rc, o, e = _run(cmd, ent, timeout=max(timeout, 120 if linguagem in ("clojure", "csharp") else timeout))
        return Resultado(rc == 0, o, e, rc)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def compilar(linguagem, codigo, params=None):
    d = tempfile.mkdtemp(prefix="plp-")
    try:
        _, comp = preparar(linguagem, codigo, d, params or {})
        return comp or Resultado(True)
    finally:
        shutil.rmtree(d, ignore_errors=True)
