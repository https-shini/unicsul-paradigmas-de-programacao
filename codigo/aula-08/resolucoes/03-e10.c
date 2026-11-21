// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/04 - Resoluções/resolucoes-aula-08.md (linha 111).
// Seção: E10
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resolucoes/03-e10.c
// Entrada de exemplo: 4 10 20 30 40 50 60
// A saída deve conter: v[0] = 10 | v[3] = 40 | v[5] = 60 | novo tamanho: 6

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int *v = malloc(n * sizeof(int));           /* heap, tamanho decidido em execução */
    if (v == NULL) return 1;
    for (int i = 0; i < n; i++) scanf("%d", &v[i]);

    int novo = n + n / 2;                       /* +50% */
    int *tmp = realloc(v, novo * sizeof(int));  /* aumenta o bloco (pode mudar de endereço) */
    if (tmp == NULL) { free(v); return 1; }
    v = tmp;
    for (int i = n; i < novo; i++) scanf("%d", &v[i]);

    printf("novo tamanho: %d\n", novo);
    for (int i = 0; i < novo; i++) printf("v[%d] = %d\n", i, v[i]);
    free(v);                                    /* devolve a memória */
    return 0;
}
