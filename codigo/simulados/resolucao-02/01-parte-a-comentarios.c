// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-02.md (linha 28).
// Seção: Parte A — comentários
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-02/01-parte-a-comentarios.c
// A saída deve conter: 1 ⏎ 2 ⏎ 3

#include <stdio.h>
void conta(void) {
    static int contador = 0;   /* inicializada uma única vez */
    contador++;
    printf("%d\n", contador);
}
int main(void) { conta(); conta(); conta(); return 0; }
