// Gerado automaticamente a partir de 01 - Aulas/Aula 05 - Semântica/03 - Exercícios/exercicios-aula-05.md (linha 30).
// Seção: Avançado
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-05/exercicios/01-avancado.c

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
