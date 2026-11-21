// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/simulado-02.md (linha 92).
// Seção: Parte B — Questões discursivas e de programação (2 pontos cada)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/simulado-02/01-parte-b-questoes-discursivas-e-de-programacao-2.c

#include <stdio.h>
int x = 1;
void mostra(void) { printf("%d\n", x); }
void a(void) { int x = 2; mostra(); }
void b(void) { int x = 3; a(); }
int main(void) { b(); mostra(); return 0; }
