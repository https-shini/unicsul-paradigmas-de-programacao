#include "situacao.h"

/* TODO: devolva 6 menos a maior entre a1 e a2. */
double nota_minima_af(double a1, double a2) {
    (void) a1; (void) a2;
    return -1.0;
}

/* TODO: implemente a regra (veja o README). A ORDEM dos testes importa:
   1. frequência < 75             → "REPROVADO POR FALTA"
   2. a1 + a2 >= 6                → "APROVADO"
   3. a1 < 1 ou a2 < 1            → "REPROVADO"           (sem direito à AF)
   4. af < 0 (SEM_AF)             → "AF"                  (ainda vai fazer a AF)
   5. af + maior(a1, a2) >= 6     → "APROVADO NA AF"      (a AF substitui a menor nota)
   6. senão                       → "REPROVADO NA AF"                                    */
const char *situacao(double a1, double a2, double af, double freq) {
    (void) a1; (void) a2; (void) af; (void) freq;
    return "TODO";
}
