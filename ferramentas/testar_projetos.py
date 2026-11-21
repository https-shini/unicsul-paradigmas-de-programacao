#!/usr/bin/env python3
"""Roda os testes automáticos dos projetos de "09 - Projetos Práticos".

Cada projeto tem um projeto.json que descreve as suítes de teste. Por padrão, os testes rodam
sobre a pasta inicial/ — que é onde você trabalha. A pasta solucao/ tem a resolução de referência.

Uso:
    python3 ferramentas/testar_projetos.py --listar
    python3 ferramentas/testar_projetos.py P1                    # testa P1/inicial (o seu código)
    python3 ferramentas/testar_projetos.py P6 --linguagem prolog # só uma das suítes
    python3 ferramentas/testar_projetos.py P1 --alvo ~/meu-calc  # testa outra pasta
    python3 ferramentas/testar_projetos.py --alvo solucao        # todas as soluções de referência
    python3 ferramentas/testar_projetos.py -v P2                 # mostra a saída completa

Resultados por suíte: OK (todos os testes passaram) · FALHA (os testes rodaram e algum falhou) ·
ERRO (não compilou ou não chegou a rodar os testes) · PULADO (ferramenta não instalada).
Opções de CI: --exigir-todos (PULADO conta como erro) e --aceitar-falhas (só ERRO reprova; usado
para conferir que os esqueletos de inicial/ continuam compilando).
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motores import executar, motor, _run  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if "UTF-8" not in (os.environ.get("LC_ALL") or os.environ.get("LANG") or "").upper().replace("UTF8", "UTF-8"):
    os.environ["LC_ALL"] = "C.UTF-8"          # javac/java precisam ler caminhos com acentos
PROJETOS = os.path.join(RAIZ, "09 - Projetos Práticos")
LIMITE = 240


def projetos():
    for d in sorted(glob.glob(os.path.join(PROJETOS, "P*"))):
        arq = os.path.join(d, "projeto.json")
        if os.path.isfile(arq):
            yield os.path.basename(d).split(" ")[0], d, json.load(open(arq, encoding="utf-8"))


_san_cache = {}


def flags_sanitizer(compilador):
    """Usa AddressSanitizer/UBSan quando o sistema suporta (detecta vazamento e acesso inválido)."""
    if compilador not in _san_cache:
        d = tempfile.mkdtemp()
        src = os.path.join(d, "t.c")
        open(src, "w").write("int main(void){return 0;}\n")
        flags = ["-fsanitize=address,undefined", "-fno-omit-frame-pointer", "-g"]
        rc, *_ = _run([compilador] + flags + [src, "-o", os.path.join(d, "t")])
        ok = rc == 0 and _run([os.path.join(d, "t")])[0] == 0
        _san_cache[compilador] = flags if ok else []
        shutil.rmtree(d, ignore_errors=True)
    return _san_cache[compilador]


def arquivos(alvo, padroes, excluir=()):
    out = []
    for p in padroes:
        out += sorted(glob.glob(os.path.join(alvo, p)))
    return [f for f in out if os.path.basename(f) not in excluir]


def resumo_harness(saida):
    """(rodou, falhas) a partir da linha 'RESULTADO: N testes, M falhas' dos testes em C, C++ e Java."""
    m = re.search(r"RESULTADO: (\d+) testes?, (\d+) falhas?", saida)
    return (True, int(m.group(2))) if m else (False, None)


def suite_python(s, alvo, proj):
    testes = os.path.join(proj, s.get("testes", "testes"))
    env = dict(os.environ, PYTHONPATH=alvo, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", testes, "-t", testes],
                       capture_output=True, text=True, env=env, timeout=LIMITE, cwd=alvo)
    saida = p.stdout + p.stderr
    rodou = re.search(r"Ran \d+ tests?", saida) is not None and "ImportError" not in saida \
        and "ModuleNotFoundError" not in saida
    return ("OK" if p.returncode == 0 else ("FALHA" if rodou else "ERRO")), saida


def suite_compilada(s, alvo, proj, lingua):
    comp = "gcc" if lingua == "c" else "g++"
    if not shutil.which(comp):
        return "PULADO", f"{comp} não encontrado"
    fontes = arquivos(alvo, s.get("fontes", ["*.c" if lingua == "c" else "*.cpp"]), s.get("excluir", []))
    testes = [os.path.join(proj, t) for t in s["testes"]]
    padrao = ["-std=c11"] if lingua == "c" else ["-std=c++17"]
    d = tempfile.mkdtemp(prefix="plp-proj-")
    try:
        exe = os.path.join(d, "testes")
        cmd = [comp] + padrao + ["-Wall", "-Wextra", "-I", alvo] + flags_sanitizer(comp) + fontes + testes + ["-o", exe, "-lm"]
        rc, o, e = _run(cmd, timeout=LIMITE)
        if rc != 0:
            return "ERRO", "Falha de compilação:\n" + o + e
        rc, o, e = _run([exe], timeout=LIMITE)
        saida = o + e
        rodou, falhas = resumo_harness(saida)
        if rc == 0 and rodou and falhas == 0:
            return "OK", saida
        if rodou and falhas == 0:
            saida += ("\nOs testes passaram, mas o programa terminou com erro: o AddressSanitizer acusou "
                      "vazamento de memória, delete duplo ou acesso inválido (veja acima).")
        return ("FALHA" if rodou else "ERRO"), saida
    finally:
        shutil.rmtree(d, ignore_errors=True)


def suite_java(s, alvo, proj):
    if not shutil.which("javac"):
        return "PULADO", "javac não encontrado"
    fontes = arquivos(alvo, s.get("fontes", ["*.java"]), s.get("excluir", []))
    testes = [os.path.join(proj, t) for t in s["testes"]]
    d = tempfile.mkdtemp(prefix="plp-proj-")
    try:
        rc, o, e = _run(["javac", "-encoding", "UTF-8", "-d", d] + fontes + testes, timeout=LIMITE)
        if rc != 0:
            return "ERRO", "Falha de compilação:\n" + o + e
        rc, o, e = _run(["java", "-ea", "-Duser.language=en", "-Duser.country=US", "-cp", d, s["principal"]], timeout=LIMITE)
        saida = o + e
        rodou, falhas = resumo_harness(saida)
        if rc == 0 and rodou and falhas == 0:
            return "OK", saida
        return ("FALHA" if rodou else "ERRO"), saida
    finally:
        shutil.rmtree(d, ignore_errors=True)


def juntar(alvo, proj, s):
    partes = []
    for f in arquivos(alvo, s["fontes"]):
        partes.append(open(f, encoding="utf-8").read())
    if not partes:
        return None
    partes.append(open(os.path.join(proj, s["testes"]), encoding="utf-8").read())
    return "\n".join(partes)


def suite_clojure(s, alvo, proj):
    if not motor("clojure"):
        return "PULADO", "Clojure (ou nbb) não encontrado"
    codigo = juntar(alvo, proj, s)
    if codigo is None:
        return "ERRO", f"nenhum arquivo {s['fontes']} em {alvo}"
    r = executar("clojure", codigo, timeout=LIMITE)
    saida = r.saida + r.erro
    m = re.search(r"(\d+) failures, (\d+) errors", saida)
    if not m or "Ran " not in saida:
        return "ERRO", saida
    return ("OK" if m.group(1) == "0" and m.group(2) == "0" else "FALHA"), saida


def suite_prolog(s, alvo, proj):
    if not motor("prolog"):
        return "PULADO", "SWI-Prolog (ou Tau-Prolog) não encontrado"
    codigo = juntar(alvo, proj, s)
    if codigo is None:
        return "ERRO", f"nenhum arquivo {s['fontes']} em {alvo}"
    r = executar("prolog", codigo, {"consulta": "executar_testes(Falhas)."}, timeout=LIMITE)
    saida = r.saida + r.erro
    m = re.search(r"Falhas = \[(.*?)\]", saida)
    if not m:
        return "ERRO", saida
    return ("OK" if m.group(1).strip() == "" else "FALHA"), saida


def rodar_suite(s, alvo, proj):
    tipo = s["tipo"]
    if tipo == "python":
        return suite_python(s, alvo, proj)
    if tipo in ("c", "cpp"):
        return suite_compilada(s, alvo, proj, tipo)
    if tipo == "java":
        return suite_java(s, alvo, proj)
    if tipo == "clojure":
        return suite_clojure(s, alvo, proj)
    if tipo == "prolog":
        return suite_prolog(s, alvo, proj)
    raise ValueError(tipo)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("projetos", nargs="*", help="P1, P2… (padrão: todos)")
    ap.add_argument("--alvo", default="inicial", help="inicial (padrão), solucao ou o caminho de uma pasta")
    ap.add_argument("--linguagem", help="roda só as suítes desta linguagem (c, cpp, java, python, clojure, prolog)")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--exigir-todos", action="store_true", help="ferramenta ausente conta como erro")
    ap.add_argument("--aceitar-falhas", action="store_true", help="só ERRO reprova (conferência dos esqueletos)")
    ap.add_argument("-v", "--verboso", action="store_true")
    a = ap.parse_args()

    todos = list(projetos())
    if a.listar:
        for cod, d, cfg in todos:
            linguas = ", ".join(s["tipo"] for s in cfg["suites"])
            print(f"{cod:<4} {cfg['titulo']:<60} [{linguas}]")
        return 0
    pedidos = {p.upper() for p in a.projetos}
    sel = [t for t in todos if not pedidos or t[0].upper() in pedidos]
    if pedidos and not sel:
        print("Projeto não encontrado. Use --listar.")
        return 2
    cont = {"OK": 0, "FALHA": 0, "ERRO": 0, "PULADO": 0}
    for cod, d, cfg in sel:
        alvo = a.alvo if os.path.isabs(os.path.expanduser(a.alvo)) or a.alvo.startswith(".") else os.path.join(d, a.alvo)
        alvo = os.path.abspath(os.path.expanduser(alvo))
        for s in cfg["suites"]:
            if a.linguagem and s["tipo"] != a.linguagem:
                continue
            pasta = os.path.join(alvo, s["pasta"]) if s.get("pasta") else alvo
            try:
                estado, saida = rodar_suite(s, pasta, d)
            except subprocess.TimeoutExpired:
                estado, saida = "ERRO", f"tempo esgotado ({LIMITE}s)"
            cont[estado] += 1
            print(f"{estado:<7} {cod} · {s['nome']:<28} {os.path.relpath(pasta, RAIZ)}")
            if a.verboso or estado in ("FALHA", "ERRO"):
                linhas = saida.strip().splitlines()
                trecho = linhas if a.verboso else linhas[-40:]
                print("\n".join("        " + l for l in trecho))
    print(f"\nTOTAL {sum(cont.values())} · " + " · ".join(f"{k} {v}" for k, v in cont.items()))
    ruim = cont["ERRO"] + (0 if a.aceitar_falhas else cont["FALHA"]) + (cont["PULADO"] if a.exigir_todos else 0)
    return 1 if ruim else 0


if __name__ == "__main__":
    sys.exit(main())
