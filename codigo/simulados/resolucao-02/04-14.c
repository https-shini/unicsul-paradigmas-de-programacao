// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-02.md (linha 129).
// Seção: 14
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-02/04-14.c
// Entrada de exemplo: 10
// A saída deve conter: 55

#include <stdio.h>
int main(void) {
    int n, s = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        s = s + i;
    printf("%d\n", s);
    return 0;
}
