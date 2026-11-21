// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/04 - Resoluções/resolucoes-aula-08.md (linha 28).
// Seção: E4
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resolucoes/01-e4.c
// A saída deve conter: 11 6

#include <stdio.h>
int main(void) {
    int a = 1, b = 2;
    int *p = &a;        /* p -> a */
    *p = *p + 10;       /* a = 1 + 10 = 11 */
    p = &b;             /* p agora -> b */
    *p = *p * 3;        /* b = 2 * 3 = 6 */
    printf("%d %d\n", a, b);
    return 0;
}
