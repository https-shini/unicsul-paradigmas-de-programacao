#!/usr/bin/env python3
"""Compila e executa os blocos de código dos arquivos Markdown e confere a saída.

Uso:
    python3 ferramentas/testar_codigo.py                 # todos os arquivos
    python3 ferramentas/testar_codigo.py "Aula 14"       # filtra pelo caminho
    python3 ferramentas/testar_codigo.py --exigir-todos  # falha se faltar o motor de alguma linguagem (usado no CI)

Veja em ferramentas/blocos.py o formato do comentário <!-- teste: ... -->.
"""
import sys
from blocos import todos_os_blocos
from motores import executar, compilar, motor


def conferir(bloco, res, mot):
    p = bloco.params
    if p.get("compilacao-falha") == "sim":
        return (not res.ok and res.etapa == "compilação" and p.get("erro-contem", "") in res.erro), "falha de compilação esperada"
    if res.etapa == "compilação" and not res.ok:
        return False, "não compilou"
    esperado = p.get("saida-contem", "")
    if bloco.linguagem == "clojure" and mot == "nbb" and "saida-contem-cljs" in p:
        esperado = p["saida-contem-cljs"]
    faltando = [t for t in esperado.split("|") if t and t not in res.saida]
    if faltando:
        return False, "saída sem: " + " | ".join(repr(t) for t in faltando)
    if p.get("erro-esperado") == "sim":
        return res.codigo != 0, "erro de execução esperado"
    if res.codigo != 0 and bloco.linguagem != "prolog":
        return False, f"terminou com código {res.codigo}"
    return True, ""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    exigir = "--exigir-todos" in sys.argv
    blocos = [b for b in todos_os_blocos(filtros=args) if b.testavel or b.completo]
    linhas, falhas, pulados = [], [], []
    for b in blocos:
        mot = motor(b.linguagem)
        onde = f"{b.arquivo}:{b.linha}"
        if mot is None:
            pulados.append((b, onde)); linhas.append(("PULADO", b.linguagem, onde)); continue
        if b.params.get("compilacao-falha") == "sim":
            res = compilar(b.linguagem, b.codigo, b.params)
        elif b.testavel:
            res = executar(b.linguagem, b.codigo, b.params)
        else:
            res = compilar(b.linguagem, b.codigo, b.params)
            st = "COMPILADO" if res.ok else "FALHA"
            linhas.append((st, b.linguagem, onde))
            if not res.ok:
                falhas.append((b, onde, "não compilou", res))
            continue
        ok, motivo = conferir(b, res, mot)
        linhas.append(("OK" if ok else "FALHA", f"{b.linguagem}/{mot}" if mot not in (b.linguagem,) else b.linguagem, onde))
        if not ok:
            falhas.append((b, onde, motivo, res))
    for st, lg, onde in linhas:
        print(f"{st:10} {lg:16} {onde}")
    for b, onde, motivo, res in falhas:
        print(f"\n### FALHA {onde} ({b.linguagem}) — {motivo}\n--- saída ---\n{res.saida[-800:]}\n--- erro ---\n{res.erro[-800:]}")
    n = lambda s: sum(1 for l in linhas if l[0] == s)
    print(f"\nTOTAL {len(linhas)} · OK {n('OK')} · COMPILADO {n('COMPILADO')} · PULADO {n('PULADO')} · FALHA {len(falhas)}")
    motores = {lg: motor(lg) for lg in ("c", "cpp", "java", "csharp", "python", "php", "perl", "clojure", "prolog")}
    print("Motores:", ", ".join(f"{k}={v or 'ausente'}" for k, v in motores.items()))
    if falhas or (exigir and pulados):
        if exigir and pulados:
            print("Linguagens sem motor:", sorted({b.linguagem for b, _ in pulados}))
        sys.exit(1)


if __name__ == "__main__":
    main()
