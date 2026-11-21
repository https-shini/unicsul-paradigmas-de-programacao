// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-02.md (linha 95).
// Seção: 13
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-02/03-13.c
// Entrada de exemplo: 5
// A saída deve conter: 0 1 4 9 16

#include <stdio.h>
#include <stdlib.h>

int *quadrados(int n) {
    int *v = malloc(n * sizeof(int));   /* vetor no HEAP */
    if (v == NULL) return NULL;
    for (int i = 0; i < n; i++)
        v[i] = i * i;
    return v;                           /* o vetor sobrevive ao fim da função */
}

int main(void) {
    int n;
    scanf("%d", &n);
    int *q = quadrados(n);              /* q: variável local, na PILHA */
    if (q == NULL) return 1;
    for (int i = 0; i < n; i++)
        printf("%d%s", q[i], i < n - 1 ? " " : "\n");
    free(q);                            /* libera a área do heap */
    return 0;
}
