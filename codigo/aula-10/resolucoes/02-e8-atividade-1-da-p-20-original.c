// Gerado automaticamente a partir de 01 - Aulas/Aula 10 - Paradigma Imperativo II/04 - Resoluções/resolucoes-aula-10.md (linha 100).
// Seção: E8 — Atividade 1 da p.20 (original)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-10/resolucoes/02-e8-atividade-1-da-p-20-original.c
// Entrada de exemplo: 5 2
// A saída deve conter: Arranjos A(5,2) = 20 | Combinacoes C(5,2) = 10

#include <stdio.h>

/* Nível 3: fatorial (long long suporta até 20!) */
long long fatorial(int k) {
    long long f = 1;
    for (int i = 2; i <= k; i++) f *= i;
    return f;
}

/* Nível 2: as duas fórmulas */
long long arranjo(int n, int p) {
    return fatorial(n) / fatorial(n - p);
}

long long combinacao(int n, int p) {
    return fatorial(n) / (fatorial(p) * fatorial(n - p));
}

/* Nível 2: entrada validada */
void lerDados(int *n, int *p) {
    do {
        scanf("%d %d", n, p);
    } while (*n < 0 || *p < 0 || *p > *n);
}

/* Nível 1 */
int main(void) {
    int n, p;
    lerDados(&n, &p);
    printf("Arranjos A(%d,%d) = %lld\n", n, p, arranjo(n, p));
    printf("Combinacoes C(%d,%d) = %lld\n", n, p, combinacao(n, p));
    return 0;
}
