// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/02 - Resumo Teórico/resumo-aula-08.md (linha 37).
// Seção: 2. O que é um ponteiro (p.3)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resumo/01-2-o-que-e-um-ponteiro-p-3.c
// A saída deve conter: x = 10 | x = 5 | v[1] = 20

#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;                       /* p guarda o endereço de x */
    printf("x = %d\n", *p);            /* lê x através de p: 10 */
    *p = 5;                            /* escreve em x através de p */
    printf("x = %d\n", x);             /* 5 */
    printf("endereco de x = %p\n", (void *)p);

    int v[3] = {10, 20, 30};
    int *q = v;                        /* o nome do vetor é o endereço do 1º elemento */
    printf("v[1] = %d\n", *(q + 1));   /* aritmética de ponteiros: 20 */
    return 0;
}
