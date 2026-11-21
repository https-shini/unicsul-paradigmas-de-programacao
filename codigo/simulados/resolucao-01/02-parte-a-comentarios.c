// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-01.md (linha 39).
// Seção: Parte A — comentários
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-01/02-parte-a-comentarios.c
// A saída deve conter: deslocamento = 36

#include <stdio.h>
int main(void) {
    int m[3][4];
    long desl = (char*)&m[2][1] - (char*)&m[0][0];
    printf("deslocamento = %ld bytes (sizeof(int) = %zu)\n", desl, sizeof(int));
    return 0;
}
