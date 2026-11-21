// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/02 - Resumo Teórico/resumo-aula-06.md (linha 151).
// Seção: 6.1 Java ou C? (p.16)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resumo/04-6-1-java-ou-c-p-16.c
// A saída deve conter: res = 5

#include <stdio.h>

int main(void) {
    double x = 2.5;
    int y = 3;
    int res = x + y;          /* 5.5 é convertido IMPLICITAMENTE para int -> 5 */
    printf("res = %d\n", res);
    return 0;
}
