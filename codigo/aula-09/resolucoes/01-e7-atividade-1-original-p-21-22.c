// Gerado automaticamente a partir de 01 - Aulas/Aula 09 - Paradigma Imperativo I/04 - Resoluções/resolucoes-aula-09.md (linha 66).
// Seção: E7 — Atividade 1 (original, p.21–22)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-09/resolucoes/01-e7-atividade-1-original-p-21-22.c
// A saída deve conter: goto: 10 | do-while: 10 | while: (nada)

#include <stdio.h>
int main(void) {
    int x;

    x = 10;                                   /* versão com goto */
repete: printf("goto: %d\n", x);
    x++;
    if (x < 10) goto repete;

    x = 10;                                   /* do-while: também pós-testado */
    do { printf("do-while: %d\n", x); x++; } while (x < 10);

    x = 10;                                   /* while: pré-testado */
    int imprimiu = 0;
    while (x < 10) { printf("while: %d\n", x); x++; imprimiu = 1; }
    if (!imprimiu) printf("while: (nada)\n");
    return 0;
}
