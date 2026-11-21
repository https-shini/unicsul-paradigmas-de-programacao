#!/usr/bin/env python3
"""Gera os quatro arquivos de teste a partir de ../casos.csv, para que C, Java, Clojure e Prolog
sejam testados com EXATAMENTE os mesmos casos. Depois de alterar casos.csv:

    python3 "09 - Projetos Práticos/P6 - Situação Acadêmica em Quatro Paradigmas/testes/gerar_testes.py"
"""
import csv, os

AQUI = os.path.dirname(os.path.abspath(__file__))
casos = list(csv.DictReader(open(os.path.join(AQUI, "..", "casos.csv"), encoding="utf-8"), delimiter=";"))
MINIMAS = [(2.0, 3.0, 3.0), (1.0, 1.0, 5.0), (4.5, 1.4, 1.5), (4.1, 1.0, 1.9)]
AVISO = "Gerado por gerar_testes.py a partir de casos.csv — não edite à mão."


def num(x):
    return x if "." in x else x + ".0"


def chave(s, sep):
    return s.lower().replace(" ", sep)


# ---- C
L = [f"/* {AVISO} */", '#include <math.h>', '#include <stdio.h>', '#include <string.h>', '#include "situacao.h"', "",
     "static int total = 0, falhas = 0;", "",
     "static void caso(double a1, double a2, double af, double freq, const char *esperado, const char *coment) {",
     "    const char *obtido = situacao(a1, a2, af, freq);",
     "    total++;",
     "    if (obtido == NULL || strcmp(obtido, esperado) != 0) {",
     "        falhas++;",
     '        printf("  FALHOU situacao(%.1f, %.1f, %.1f, %.1f): esperado \\"%s\\", obtido \\"%s\\"  (%s)\\n",',
     '               a1, a2, af, freq, esperado, obtido ? obtido : "NULL", coment);',
     "    }", "}", "",
     "static void minima(double a1, double a2, double esperado) {",
     "    double obtido = nota_minima_af(a1, a2);",
     "    total++;",
     "    if (fabs(obtido - esperado) > 1e-9) {",
     "        falhas++;",
     '        printf("  FALHOU nota_minima_af(%.1f, %.1f): esperado %.2f, obtido %.2f\\n", a1, a2, esperado, obtido);',
     "    }", "}", "", "int main(void) {"]
for c in casos:
    af = "SEM_AF" if c["af"] == "-" else num(c["af"])
    L.append(f'    caso({num(c["a1"])}, {num(c["a2"])}, {af}, {num(c["freq"])}, "{c["esperado"]}", "{c["comentario"]}");')
for a1, a2, m in MINIMAS:
    L.append(f"    minima({a1}, {a2}, {m});")
L += ['    printf("\\nRESULTADO: %d testes, %d falhas\\n", total, falhas);', "    return falhas ? 1 : 0;", "}", ""]
open(os.path.join(AQUI, "testes.c"), "w", encoding="utf-8").write("\n".join(L))

# ---- Java
L = [f"// {AVISO}", "public class TestesSituacao {", "    static int total = 0, falhas = 0;", "",
     "    static void caso(double a1, double a2, Double af, double freq, String esperado, String coment) {",
     "        total++;",
     "        String obtido;",
     "        try { obtido = new Desempenho(a1, a2, af, freq).situacao(); }",
     "        catch (RuntimeException e) { obtido = e.toString(); }",
     "        if (!esperado.equals(obtido)) {",
     "            falhas++;",
     '            System.out.printf("  FALHOU Desempenho(%s, %s, %s, %s): esperado \\"%s\\", obtido \\"%s\\"  (%s)%n", a1, a2, af, freq, esperado, obtido, coment);',
     "        }", "    }", "",
     "    static void minima(double a1, double a2, double esperado) {",
     "        total++;",
     "        try {",
     "            double obtido = new Desempenho(a1, a2, null, 100).notaMinimaAF();",
     "            if (Math.abs(obtido - esperado) > 1e-9) {",
     '                falhas++; System.out.printf("  FALHOU notaMinimaAF(%s, %s): esperado %s, obtido %s%n", a1, a2, esperado, obtido);',
     "            }",
     '        } catch (RuntimeException e) { falhas++; System.out.println("  FALHOU notaMinimaAF: " + e); }',
     "    }", "",
     "    static void invalido(double a1, double a2, Double af, double freq) {",
     "        total++;",
     "        try {",
     "            new Desempenho(a1, a2, af, freq);",
     '            falhas++; System.out.printf("  FALHOU: Desempenho(%s, %s, %s, %s) deveria lançar IllegalArgumentException%n", a1, a2, af, freq);',
     "        } catch (IllegalArgumentException e) { /* esperado */ }",
     '        catch (RuntimeException e) { falhas++; System.out.println("  FALHOU: exceção errada: " + e); }',
     "    }", "",
     "    public static void main(String[] args) {"]
for c in casos:
    af = "null" if c["af"] == "-" else num(c["af"])
    L.append(f'        caso({num(c["a1"])}, {num(c["a2"])}, {af}, {num(c["freq"])}, "{c["esperado"]}", "{c["comentario"]}");')
for a1, a2, m in MINIMAS:
    L.append(f"        minima({a1}, {a2}, {m});")
L += ["        invalido(5.5, 3.0, null, 80);   // A1 vale no máximo 5", "        invalido(3.0, -1.0, null, 80);",
      "        invalido(3.0, 2.0, 6.0, 80);    // AF vale no máximo 5", "        invalido(3.0, 2.0, null, 101);",
      '        System.out.println("\\nRESULTADO: " + total + " testes, " + falhas + " falhas");',
      "        System.exit(falhas == 0 ? 0 : 1);", "    }", "}", ""]
open(os.path.join(AQUI, "TestesSituacao.java"), "w", encoding="utf-8").write("\n".join(L))

# ---- Clojure
L = [f";; {AVISO}", "(ns situacao-test", "  (:require [clojure.test :refer [deftest is run-tests]]))", "",
     "(deftest casos-de-casos-csv"]
for c in casos:
    af = "nil" if c["af"] == "-" else num(c["af"])
    L.append(f'  (is (= :{chave(c["esperado"], "-")} (situacao/situacao {{:a1 {num(c["a1"])} :a2 {num(c["a2"])} :af {af} :freq {num(c["freq"])}}})) "{c["comentario"]}")')
L[-1] += ")"
L += ["", "(deftest nota-minima"]
for a1, a2, m in MINIMAS:
    L.append(f"  (is (< (Math/abs (- {m} (situacao/nota-minima-af {a1} {a2}))) 1e-9))")
L[-1] += ")"
L += ["", "(run-tests 'situacao-test)", ""]
open(os.path.join(AQUI, "situacao_test.clj"), "w", encoding="utf-8").write("\n".join(L))

# ---- Prolog
L = [f"% {AVISO}", "% Cada caso exige UMA resposta só: findall(S, situacao(...), [Esperado])."]
for i, c in enumerate(casos, 1):
    af = "nenhuma" if c["af"] == "-" else num(c["af"])
    L.append(f'teste(caso_{i:02d}, findall(S, situacao({num(c["a1"])}, {num(c["a2"])}, {af}, {num(c["freq"])}, S), [{chave(c["esperado"], "_")}])).')
for i, (a1, a2, m) in enumerate(MINIMAS, 1):
    L.append(f"teste(minima_{i}, (nota_minima_af({a1}, {a2}, N), abs(N - {m}) < 1.0e-9)).")
L += ["", "executar_testes(Falhas) :-", "    findall(Nome, (teste(Nome, Objetivo), \\+ catch(Objetivo, _, fail)), Falhas).", ""]
open(os.path.join(AQUI, "testes.pl"), "w", encoding="utf-8").write("\n".join(L))
print(f"{len(casos)} casos → testes.c, TestesSituacao.java, situacao_test.clj, testes.pl")
