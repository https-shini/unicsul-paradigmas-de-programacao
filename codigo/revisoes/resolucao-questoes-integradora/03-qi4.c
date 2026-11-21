// Gerado automaticamente a partir de 06 - Revisões e Sínteses/resolucao-questoes-integradoras.md (linha 97).
// Seção: QI4
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/resolucao-questoes-integradora/03-qi4.c
// A saída deve conter: 30

#include <stdio.h>
int main(void) {
    int s = 0;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) s = s + i;
    }
    printf("%d\n", s);
    return 0;
}
