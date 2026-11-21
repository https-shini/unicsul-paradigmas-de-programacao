// Gerado automaticamente a partir de 02 - Listas de Exercícios/Lista 02 - Revisão II/02 - Resolução/resolucao-lista-02.md (linha 59).
// Seção: Q4
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/lista-02/resolucao/01-q4.c
// A saída deve conter: 10

#include <stdio.h>
int n = 10;                         /* global */
void f(void) { printf("%d\n", n); } /* n não é local de f */
void g(void) { int n = 20; f(); }   /* g tem um n local */
int main(void) { g(); return 0; }   /* estático: imprime 10. Com escopo dinâmico, seria 20 */
