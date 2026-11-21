// Gerado automaticamente a partir de 06 - Revisões e Sínteses/resolucao-questoes-integradoras.md (linha 67).
// Seção: QI3
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/resolucao-questoes-integradora/02-qi3.c
// A saída deve conter: menor = 1, maior = 10

#include <stdio.h>

/* v e n: entrada; menor e maior: saída (simulada por ponteiros) */
void minmax(const int v[], int n, int *menor, int *maior) {
    *menor = *maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < *menor) *menor = v[i];
        if (v[i] > *maior) *maior = v[i];
    }
}

int main(void) {
    int dados[] = {9, 3, 7, 1, 8, 2, 10, 5, 4, 6};
    int mn, mx;
    minmax(dados, 10, &mn, &mx);
    printf("menor = %d, maior = %d\n", mn, mx);
    return 0;
}
