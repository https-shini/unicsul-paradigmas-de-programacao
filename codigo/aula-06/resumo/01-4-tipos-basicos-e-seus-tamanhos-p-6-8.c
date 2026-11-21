// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/02 - Resumo Teórico/resumo-aula-06.md (linha 65).
// Seção: 4. Tipos básicos e seus tamanhos (p.6–8)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resumo/01-4-tipos-basicos-e-seus-tamanhos-p-6-8.c
// A saída deve conter: max = 2147483647 | max + 1 = -2147483648

#include <stdio.h>
#include <limits.h>

int main(void) {
    int max = INT_MAX;                 /* 2147483647 */
    unsigned int u = (unsigned int)max + 1u;
    printf("max = %d\n", max);
    printf("max + 1 = %d\n", (int)u); /* "dá a volta": -2147483648 */
    return 0;
}
