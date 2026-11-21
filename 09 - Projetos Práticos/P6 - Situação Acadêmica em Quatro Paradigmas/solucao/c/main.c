/* Demonstração: lê "a1 a2 af freq" por linha (af = -1 se não fez) e mostra a situação.
   gcc -std=c11 situacao.c main.c -o situacao && echo "2 3 -1 90" | ./situacao */
#include <stdio.h>
#include "situacao.h"

int main(void) {
    double a1, a2, af, freq;
    while (scanf("%lf %lf %lf %lf", &a1, &a2, &af, &freq) == 4) {
        const char *s = situacao(a1, a2, af, freq);
        printf("A1=%.1f A2=%.1f -> %s", a1, a2, s);
        if (s[0] == 'A' && s[1] == 'F' && s[2] == '\0')
            printf(" (precisa de %.1f)", nota_minima_af(a1, a2));
        printf("\n");
    }
    return 0;
}
