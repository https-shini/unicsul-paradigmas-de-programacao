// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/04 - Resoluções/resolucoes-aula-08.md (linha 78).
// Seção: E8
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resolucoes/02-e8.c
// A saída deve conter: antes: x=1 y=2 | depois: x=2 y=1 | sem ponteiro: x=2 y=1

#include <stdio.h>

void troca(int *a, int *b) {     /* recebe ENDEREÇOS */
    int temp = *a;               /* guarda o valor apontado por a */
    *a = *b;                     /* escreve no x do chamador */
    *b = temp;                   /* escreve no y do chamador */
}

void troca_errada(int a, int b) {   /* recebe CÓPIAS */
    int temp = a; a = b; b = temp;  /* troca só as cópias locais */
}

int main(void) {
    int x = 1, y = 2;
    printf("antes: x=%d y=%d\n", x, y);
    troca(&x, &y);
    printf("depois: x=%d y=%d\n", x, y);
    troca_errada(x, y);
    printf("sem ponteiro: x=%d y=%d\n", x, y);   /* não mudou */
    return 0;
}
