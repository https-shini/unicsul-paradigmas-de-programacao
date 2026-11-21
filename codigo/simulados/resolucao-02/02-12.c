// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-02.md (linha 70).
// Seção: 12
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-02/02-12.c
// A saída deve conter: 1 ⏎ 1

#include <stdio.h>
int x = 1;
void mostra(void) { printf("%d\n", x); }
void a(void) { int x = 2; (void) x; mostra(); }
void b(void) { int x = 3; (void) x; a(); }
int main(void) { b(); mostra(); return 0; }
