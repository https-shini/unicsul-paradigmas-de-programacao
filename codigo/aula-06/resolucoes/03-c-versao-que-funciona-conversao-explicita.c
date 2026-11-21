// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/04 - Resoluções/resolucoes-aula-06.md (linha 104).
// Seção: C — versão que funciona (conversão explícita)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resolucoes/03-c-versao-que-funciona-conversao-explicita.c
// A saída deve conter: x eh int | y eh char* (string) | w eh double | Resultado(x+y+w): 40.2

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 10;
    char *y = "20";
    double w = 10.2;
    printf("x eh int\ny eh char* (string)\nw eh double\n");  /* C não tem gettype: o tipo é fixo e conhecido */
    double z = x + atoi(y) + w;          /* conversão string -> int feita pelo programador */
    printf("Resultado(x+y+w): %.1f\n", z);
    return 0;
}
