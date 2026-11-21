// Gerado automaticamente a partir de 06 - Revisões e Sínteses/quadros-comparativos.md (linha 53).
// Seção: 2. Um mesmo problema nos quatro paradigmas
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/quadros-comparativos/01-2-um-mesmo-problema-nos-quatro-paradigmas.c
// A saída deve conter: 120

#include <stdio.h>
int main(void) {
    int f = 1;
    for (int i = 2; i <= 5; i++) f = f * i;   /* atribuição + repetição */
    printf("%d\n", f);
    return 0;
}
