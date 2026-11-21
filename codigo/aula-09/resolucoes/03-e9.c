// Gerado automaticamente a partir de 01 - Aulas/Aula 09 - Paradigma Imperativo I/04 - Resoluções/resolucoes-aula-09.md (linha 122).
// Seção: E9
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-09/resolucoes/03-e9.c
// Entrada de exemplo: 5 -3 8 -1 2 7 -6 4 9 -2
// A saída deve conter: Positivos: 6 | Negativos: 4

#include <stdio.h>

int main(void) {
    int n, pos = 0, neg = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &n);
        if (n == 0) return 0;        /* encerra sem mensagem */
        if (n > 0) pos++; else neg++;
    }
    printf("Positivos: %d\nNegativos: %d\n", pos, neg);
    return 0;
}
