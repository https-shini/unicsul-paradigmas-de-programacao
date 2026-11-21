// Gerado automaticamente a partir de 01 - Aulas/Aula 09 - Paradigma Imperativo I/02 - Resumo Teórico/resumo-aula-09.md (linha 155).
// Seção: 8. Programas com `goto` (p.19–22)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-09/resumo/01-8-programas-com-goto-p-19-22.c
// A saída deve conter: Iniciando o programa ⏎ Terminando o programa

#include <stdio.h>
int main(void) {
    printf("Iniciando o programa\n");
    goto fim;
    printf("Meio do programa\n");      /* código inalcançável */
fim: printf("Terminando o programa\n");
    return 0;
}
