// Gerado automaticamente a partir de 06 - Revisões e Sínteses/resolucao-questoes-integradoras.md (linha 41).
// Seção: QI2
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/resolucao-questoes-integradora/01-qi2.c
// A saída deve conter: total = 7, chamadas = 2

#include <stdio.h>
#include <stdlib.h>
int total = 0;
int soma(int x) {
    static int chamadas = 0;
    int *p = malloc(sizeof(int));
    *p = x;
    total += *p;
    chamadas++;
    free(p);
    return chamadas;
}
int main(void) {
    soma(3);
    int c = soma(4);
    printf("total = %d, chamadas = %d\n", total, c);
    return 0;
}
