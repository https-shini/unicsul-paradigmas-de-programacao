#!/usr/bin/env python3
"""Autocorreção: executa a SUA solução de um exercício contra os casos de teste da resolução comentada.

Uso:
    python3 ferramentas/verificar.py --listar               # exercícios com correção automática
    python3 ferramentas/verificar.py 14 E8 minha.clj        # Aula 14, exercício E8
    python3 ferramentas/verificar.py lista-01 Q7 q7.clj     # Lista 01, questão 7
    python3 ferramentas/verificar.py 15 E9 base.pl          # Prolog: roda as mesmas consultas
    python3 ferramentas/verificar.py 11 E8 Atividade.cs --estrito
    python3 ferramentas/verificar.py projeto P1             # projetos práticos (09): o mesmo que testar_projetos.py P1

Os casos de teste são os mesmos usados para validar a resolução comentada (entrada + o que a
saída deve conter). A comparação padrão é TOLERANTE: ignora maiúsculas, acentos, pontuação e
textos extras, e confere se os valores esperados aparecem na ordem certa (12 = 12.0; 3/25 = 0.12).
Use --estrito para exigir o texto exato. Você pode resolver em outra linguagem: o que importa é a saída.
"""
import argparse, os, re, sys, unicodedata
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blocos import RAIZ, blocos_do_arquivo
from motores import executar, motor
from rodar import linguagem


def arquivo_resolucao(alvo):
    m = re.fullmatch(r"(?:aula-?)?(\d{1,2})", alvo)
    if m:
        n = int(m.group(1))
        base = os.path.join(RAIZ, "01 - Aulas")
        d = next((x for x in os.listdir(base) if x.startswith(f"Aula {n:02d}")), None)
        return d and os.path.join(base, d, "04 - Resoluções", f"resolucoes-aula-{n:02d}.md")
    m = re.fullmatch(r"lista-?(\d{1,2})", alvo)
    if m:
        base = os.path.join(RAIZ, "02 - Listas de Exercícios")
        d = next((x for x in os.listdir(base) if x.startswith(f"Lista {int(m.group(1)):02d}")), None)
        return d and os.path.join(base, d, "02 - Resolução", f"resolucao-lista-{int(m.group(1)):02d}.md")
    m = re.fullmatch(r"simulado-?(\d{1,2})", alvo)
    if m:
        return os.path.join(RAIZ, "04 - Provas e Avaliações", "Simulados", f"resolucao-simulado-{int(m.group(1)):02d}.md")
    return None


def exercicio_do_titulo(titulo):
    m = re.match(r"(E\d+|Q\d+|QI\d+|\d+)\b", titulo.strip())
    return m.group(1).upper() if m else None


def casos(arquivo, exercicio):
    return [b for b in blocos_do_arquivo(arquivo) if b.testavel and exercicio_do_titulo(b.titulo) == exercicio.upper()
            and (b.params.get("saida-contem") or b.params.get("consulta"))]


def normalizar(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def tokens(t):
    return re.findall(r"-?\d+/\d+|-?\d+(?:\.\d+)?|[a-z_]+", normalizar(t))


def valor(tok):
    try:
        return float(Fraction(tok)) if "/" in tok else float(tok)
    except (ValueError, ZeroDivisionError):
        return None


def contem_em_ordem(esperado, obtido):
    exp, obt = tokens(esperado), tokens(obtido)
    i = 0
    for e in exp:
        ve = valor(e)
        while i < len(obt):
            vo = valor(obt[i])
            i += 1
            if (ve is not None and vo is not None and abs(ve - vo) < 1e-6) or e == obt[i - 1]:
                break
        else:
            return False
    return True


def listar():
    print("Exercícios com correção automática:\n")
    alvos = [f"{n:02d}" for n in range(1, 16)] + ["lista-01", "lista-02", "simulado-01", "simulado-02", "simulado-03"]
    for alvo in alvos:
        arq = arquivo_resolucao(alvo)
        if not arq or not os.path.exists(arq):
            continue
        ex = {}
        for b in blocos_do_arquivo(arq):
            e = exercicio_do_titulo(b.titulo)
            if e and b.testavel and (b.params.get("saida-contem") or b.params.get("consulta")):
                ex.setdefault(e, set()).add(b.linguagem)
        if ex:
            nome = f"Aula {alvo}" if alvo.isdigit() else alvo
            print(f"  {nome:12} " + "  ".join(f"{k} ({'/'.join(sorted(v))})" for k, v in ex.items()))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "projeto":          # atalho para os projetos práticos
        import subprocess
        return subprocess.call([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "testar_projetos.py")]
                               + sys.argv[2:])
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("alvo", nargs="?", help="número da aula (14), lista-01 ou simulado-02")
    ap.add_argument("exercicio", nargs="?", help="E8, Q7, QI3...")
    ap.add_argument("arquivo", nargs="?", help="sua solução")
    ap.add_argument("--estrito", action="store_true")
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()
    if a.listar or not a.arquivo:
        listar(); return
    arq = arquivo_resolucao(a.alvo)
    if not arq or not os.path.exists(arq):
        sys.exit(f"Não encontrei a resolução de '{a.alvo}'.")
    cs = casos(arq, a.exercicio)
    rel = os.path.relpath(arq, RAIZ)
    if not cs:
        sys.exit(f"{a.exercicio} não tem casos de teste automáticos (é discursivo ou de leitura). Compare com a resolução comentada: {rel}")
    codigo = open(a.arquivo, encoding="utf-8").read()
    lg = linguagem(a.arquivo, codigo)
    if not lg or motor(lg) is None:
        sys.exit(f"Linguagem não reconhecida ou não instalada para {a.arquivo}. Rode: bash ferramentas/instalar-ambiente.sh")
    aprovados = 0
    for i, c in enumerate(cs, 1):
        params = {k: v for k, v in c.params.items() if k in ("entrada", "consulta")}
        if lg == "prolog" and "consulta" not in params:
            params["consulta"] = "main."
        r = executar(lg, codigo, params)
        esperado = c.params.get("saida-contem", "")
        if lg == "clojure" and motor("clojure") == "nbb" and "saida-contem-cljs" in c.params:
            esperado = c.params["saida-contem-cljs"]
        if not r.ok and r.etapa == "compilação":
            print(f"❌ Caso {i}: não compilou\n{r.erro[-1500:]}"); continue
        partes = [p for p in esperado.split("|") if p]
        if a.estrito:
            falta = [p for p in partes if p not in r.saida]
        else:
            falta = [p for p in partes if not contem_em_ordem(p, r.saida)]
        desc = f"entrada: {params['entrada']!r}" if params.get("entrada") else (f"consulta: ?- {params['consulta']}" if params.get("consulta") else "sem entrada")
        if falta:
            print(f"❌ Caso {i} ({desc})")
            for p in falta:
                print(f"   esperado (em ordem): {p!r}")
            print("   sua saída:\n" + "\n".join("     " + l for l in r.saida.strip().splitlines()[-15:]))
            if r.erro.strip():
                print("   erros:\n" + "\n".join("     " + l for l in r.erro.strip().splitlines()[-8:]))
        else:
            aprovados += 1
            print(f"✅ Caso {i} ({desc})")
    print(f"\n{aprovados}/{len(cs)} casos aprovados. Resolução comentada: {rel} (seção {a.exercicio.upper()}).")
    sys.exit(0 if aprovados == len(cs) else 1)


if __name__ == "__main__":
    sys.exit(main())
