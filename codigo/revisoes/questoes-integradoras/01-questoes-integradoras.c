// Gerado automaticamente a partir de 06 - Revisões e Sínteses/questoes-integradoras.md (linha 12).
// Seção: Questões integradoras
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/questoes-integradoras/01-questoes-integradoras.c

#include <stdlib.h>
int total = 0;
void soma(int x) {
    static int chamadas = 0;
    int *p = malloc(sizeof(int));
    *p = x;
    total += *p;
    chamadas++;
    free(p);
}
int main(void) { soma(3); soma(4); return 0; }
