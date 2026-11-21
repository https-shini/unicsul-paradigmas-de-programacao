// Gerado automaticamente a partir de 01 - Aulas/Aula 09 - Paradigma Imperativo I/04 - Resoluções/resolucoes-aula-09.md (linha 90).
// Seção: E8 — Atividade 2 (original, p.24)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-09/resolucoes/02-e8-atividade-2-original-p-24.c
// Entrada de exemplo: 5 -3 8 -1 2 7 -6 4 9 -2
// A saída deve conter: Positivos: 6 | Negativos: 4

#include <stdio.h>

int main(void) {
    int n, cont = 0, pos = 0, neg = 0;

le:                                  /* "início do laço" sem usar for/while */
    if (cont == 10) goto fim;        /* já leu 10 números */
    scanf("%d", &n);
    if (n == 0) goto sair;           /* 0 interrompe sem mensagem */
    if (n > 0) pos++;
    else neg++;
    cont++;
    goto le;                         /* volta para ler o próximo */

fim:
    printf("Positivos: %d\nNegativos: %d\n", pos, neg);
sair:
    return 0;
}
