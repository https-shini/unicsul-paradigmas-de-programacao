// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-01.md (linha 102).
// Seção: 13
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao/04-13.c
// A saída deve conter: valor: 1 2 | referencia: 2 1

#include <stdio.h>
void trocaValor(int a, int b)        { int t = a; a = b; b = t; (void)a; (void)b; }
void trocaReferencia(int *a, int *b) { int t = *a; *a = *b; *b = t; }
int main(void) {
    int x = 1, y = 2;
    trocaValor(x, y);       printf("valor: %d %d\n", x, y);
    trocaReferencia(&x, &y); printf("referencia: %d %d\n", x, y);
    return 0;
}
