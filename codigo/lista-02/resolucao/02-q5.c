// Gerado automaticamente a partir de 02 - Listas de Exercícios/Lista 02 - Revisão II/02 - Resolução/resolucao-lista-02.md (linha 84).
// Seção: Q5
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/lista-02/resolucao/02-q5.c
// A saída deve conter: res = 5

#include <stdio.h>
int main(void) {
    double x = 2.5; int y = 3;
    int res = x + y;              /* coerção implícita: 5.5 -> 5 (em Java: erro de compilação) */
    printf("res = %d\n", res);
    return 0;
}
