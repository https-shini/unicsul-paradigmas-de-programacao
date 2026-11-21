// Gerado automaticamente a partir de 01 - Aulas/Aula 14 - Paradigma Funcional/04 - Resoluções/resolucoes-aula-14.md (linha 48).
// Seção: E6
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-14/resolucoes/01-e6.c
// A saída deve conter: primeira: 1 | segunda: 2

#include <stdio.h>
int contador = 0;                          /* estado global */
int proximo(void) { return ++contador; }   /* efeito colateral: altera o global */

int main(void) {
    printf("primeira: %d\n", proximo());   /* 1 */
    printf("segunda: %d\n", proximo());    /* 2: mesma chamada, resultado diferente! */
    return 0;
}
