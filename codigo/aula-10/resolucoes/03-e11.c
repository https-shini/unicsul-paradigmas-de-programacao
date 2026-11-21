// Gerado automaticamente a partir de 01 - Aulas/Aula 10 - Paradigma Imperativo II/04 - Resoluções/resolucoes-aula-10.md (linha 170).
// Seção: E11
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-10/resolucoes/03-e11.c
// Entrada de exemplo: 30 15
// A saída deve conter: C(30,15) = 155117520

#include <stdio.h>

long long combinacao(int n, int p) {
    if (p > n - p) p = n - p;               /* C(n,p) = C(n,n-p): usa o menor */
    long long c = 1;
    for (int i = 1; i <= p; i++) {
        c = c * (n - p + i) / i;            /* a cada passo, c = C(n-p+i, i), sempre inteiro */
    }
    return c;
}

int main(void) {
    int n, p;
    scanf("%d %d", &n, &p);
    printf("C(%d,%d) = %lld\n", n, p, combinacao(n, p));   /* 30! não caberia em long long */
    return 0;
}
