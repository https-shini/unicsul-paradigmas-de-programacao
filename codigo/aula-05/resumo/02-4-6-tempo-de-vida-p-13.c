// Gerado automaticamente a partir de 01 - Aulas/Aula 05 - Semântica/02 - Resumo Teórico/resumo-aula-05.md (linha 157).
// Seção: 4.6 Tempo de vida (p.13)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-05/resumo/02-4-6-tempo-de-vida-p-13.c
// A saída deve conter: chamada 1 | chamada 2 | chamada 3

#include <stdio.h>

void conta(void) {
    static int vezes = 0;   /* inicializada uma única vez; sobrevive entre chamadas */
    vezes++;
    printf("chamada %d\n", vezes);
}

int main(void) {
    conta(); conta(); conta();   /* imprime chamada 1, 2, 3 */
    return 0;
}
