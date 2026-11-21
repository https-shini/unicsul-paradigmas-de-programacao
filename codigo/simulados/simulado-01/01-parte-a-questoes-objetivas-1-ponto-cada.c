// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/simulado-01.md (linha 26).
// Seção: Parte A — Questões objetivas (1 ponto cada)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/simulado-01/01-parte-a-questoes-objetivas-1-ponto-cada.c

#include <stdio.h>
int n = 10;
void f(void) { printf("%d", n); }
void g(void) { int n = 20; f(); }
int main(void) { g(); return 0; }
