// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/04 - Resoluções/resolucoes-aula-06.md (linha 82).
// Seção: C — tentativa literal
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resolucoes/02-c-tentativa-literal-nao-compila.c
// ATENÇÃO: este exemplo NÃO compila de propósito (ilustra um erro).

#include <stdio.h>

int main(void) {
    int x = 10;
    char *y = "20";          /* em C, "20" é um vetor de char (ponteiro) */
    double w = 10.2;
    double z = x + y + w;    /* x + y vira aritmética de PONTEIRO; ponteiro + double = erro */
    printf("%f\n", z);
    return 0;
}
