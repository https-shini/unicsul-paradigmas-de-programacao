// Gerado automaticamente a partir de 01 - Aulas/Aula 09 - Paradigma Imperativo I/02 - Resumo Teórico/resumo-aula-09.md (linha 171).
// Seção: 8. Programas com `goto` (p.19–22)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-09/resumo/03-8-programas-com-goto-p-19-22.c
// A saída deve conter: 0 ⏎ 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5 ⏎ 6 ⏎ 7 ⏎ 8 ⏎ 9

#include <stdio.h>   /* o slide omite os #include */
int main() {
    int x = 0;
    while (x < 10) {
        printf("%d\n", x);
        x++;
    }
    return 0;
}
