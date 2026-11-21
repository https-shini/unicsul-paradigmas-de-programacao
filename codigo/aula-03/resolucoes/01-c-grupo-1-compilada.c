// Gerado automaticamente a partir de 01 - Aulas/Aula 03 - Implementação das Linguagens/04 - Resoluções/resolucoes-aula-03.md (linha 67).
// Seção: C (Grupo 1, compilada)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-03/resolucoes/01-c-grupo-1-compilada.c
// Entrada de exemplo: 5 3 9 1 7 2 8 6 4 10
// A saída deve conter: Media: 5.50 | Maior: 10.00 | Menor: 1.00

#include <stdio.h>

int main(void) {
    double x, soma = 0, maior = 0, menor = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%lf", &x);
        if (i == 0) { maior = menor = x; }      /* primeiro valor inicializa */
        if (x > maior) maior = x;
        if (x < menor) menor = x;
        soma += x;
    }
    printf("Media: %.2f\nMaior: %.2f\nMenor: %.2f\n", soma / 10, maior, menor);
    return 0;
}
