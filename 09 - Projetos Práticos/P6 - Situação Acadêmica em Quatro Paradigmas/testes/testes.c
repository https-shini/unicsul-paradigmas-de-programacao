/* Gerado por gerar_testes.py a partir de casos.csv — não edite à mão. */
#include <math.h>
#include <stdio.h>
#include <string.h>
#include "situacao.h"

static int total = 0, falhas = 0;

static void caso(double a1, double a2, double af, double freq, const char *esperado, const char *coment) {
    const char *obtido = situacao(a1, a2, af, freq);
    total++;
    if (obtido == NULL || strcmp(obtido, esperado) != 0) {
        falhas++;
        printf("  FALHOU situacao(%.1f, %.1f, %.1f, %.1f): esperado \"%s\", obtido \"%s\"  (%s)\n",
               a1, a2, af, freq, esperado, obtido ? obtido : "NULL", coment);
    }
}

static void minima(double a1, double a2, double esperado) {
    double obtido = nota_minima_af(a1, a2);
    total++;
    if (fabs(obtido - esperado) > 1e-9) {
        falhas++;
        printf("  FALHOU nota_minima_af(%.1f, %.1f): esperado %.2f, obtido %.2f\n", a1, a2, esperado, obtido);
    }
}

int main(void) {
    caso(3.5, 4.0, SEM_AF, 80.0, "APROVADO", "soma 7,5");
    caso(3.0, 3.0, SEM_AF, 75.0, "APROVADO", "limites: soma 6,0 e frequência 75%");
    caso(2.1, 3.9, SEM_AF, 80.0, "APROVADO", "soma 6,0 com decimais");
    caso(5.0, 5.0, SEM_AF, 74.9, "REPROVADO POR FALTA", "nota máxima não salva a frequência");
    caso(0.0, 0.0, SEM_AF, 0.0, "REPROVADO POR FALTA", "a frequência é verificada primeiro");
    caso(2.0, 3.0, 5.0, 70.0, "REPROVADO POR FALTA", "AF não salva a frequência");
    caso(0.5, 5.0, SEM_AF, 100.0, "REPROVADO", "menos de 1 ponto na A1: sem direito à AF");
    caso(5.0, 0.9, SEM_AF, 100.0, "REPROVADO", "menos de 1 ponto na A2: sem direito à AF");
    caso(0.5, 5.0, 5.0, 80.0, "REPROVADO", "a nota de AF é ignorada");
    caso(2.0, 3.0, SEM_AF, 90.0, "AF", "soma 5,0: precisa de 3,0 na AF");
    caso(1.0, 1.0, SEM_AF, 80.0, "AF", "exatamente 1 ponto: tem direito à AF");
    caso(2.0, 3.0, 3.5, 90.0, "APROVADO NA AF", "3,5 substitui o 2,0: 6,5");
    caso(1.0, 1.0, 5.0, 80.0, "APROVADO NA AF", "5,0 + 1,0 = 6,0");
    caso(2.9, 3.0, 3.0, 80.0, "APROVADO NA AF", "3,0 + 3,0 = 6,0");
    caso(4.5, 1.4, 2.0, 76.0, "APROVADO NA AF", "2,0 substitui o 1,4: 6,5");
    caso(2.0, 3.0, 2.5, 90.0, "REPROVADO NA AF", "2,5 + 3,0 = 5,5");
    caso(4.0, 1.9, 1.9, 80.0, "REPROVADO NA AF", "1,9 + 4,0 = 5,9");
    caso(4.0, 4.0, 3.0, 80.0, "APROVADO", "já aprovado: a AF não muda nada");
    minima(2.0, 3.0, 3.0);
    minima(1.0, 1.0, 5.0);
    minima(4.5, 1.4, 1.5);
    minima(4.1, 1.0, 1.9);
    printf("\nRESULTADO: %d testes, %d falhas\n", total, falhas);
    return falhas ? 1 : 0;
}
