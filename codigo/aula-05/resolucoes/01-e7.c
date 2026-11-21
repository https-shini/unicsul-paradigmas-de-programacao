// Gerado automaticamente a partir de 01 - Aulas/Aula 05 - Semântica/04 - Resoluções/resolucoes-aula-05.md (linha 46).
// Seção: E7
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-05/resolucoes/01-e7.c
// A saída deve conter: 10 ⏎ 20 ⏎ 10

#include <stdio.h>
int n = 10;

void f(void) {
    printf("%d\n", n);
}

void g(void) {
    int n = 20;
    f();
    printf("%d\n", n);
}

int main(void) {
    g();
    printf("%d\n", n);
    return 0;
}
