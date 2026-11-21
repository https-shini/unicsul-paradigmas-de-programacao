// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-01.md (linha 22).
// Seção: Parte A — comentários
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao/01-parte-a-comentarios.c
// A saída deve conter: 10

#include <stdio.h>
int n = 10;
void f(void) { printf("%d\n", n); }
void g(void) { int n = 20; (void) n; f(); }
int main(void) { g(); return 0; }
