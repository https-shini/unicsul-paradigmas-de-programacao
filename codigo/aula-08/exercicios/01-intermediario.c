// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/03 - Exercícios/exercicios-aula-08.md (linha 18).
// Seção: Intermediário
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/exercicios/01-intermediario.c

#include <stdio.h>
int main(void) {
    int a = 1, b = 2;
    int *p = &a;
    *p = *p + 10;
    p = &b;
    *p = *p * 3;
    printf("%d %d\n", a, b);
    return 0;
}
