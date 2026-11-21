#include "situacao.h"

static double maior(double a, double b) { return a > b ? a : b; }

double nota_minima_af(double a1, double a2) {
    return 6.0 - maior(a1, a2);
}

/* Sequência de testes com retorno antecipado: a ORDEM das condições é parte da regra. */
const char *situacao(double a1, double a2, double af, double freq) {
    if (freq < 75.0)
        return "REPROVADO POR FALTA";
    if (a1 + a2 >= 6.0)
        return "APROVADO";
    if (a1 < 1.0 || a2 < 1.0)               /* sem 1 ponto na A1 ou na A2: não pode fazer AF */
        return "REPROVADO";
    if (af < 0.0)                           /* ainda não fez a AF */
        return "AF";
    if (af + maior(a1, a2) >= 6.0)          /* a AF substitui a menor nota */
        return "APROVADO NA AF";
    return "REPROVADO NA AF";
}
