// Gerado automaticamente a partir de 01 - Aulas/Aula 09 - Paradigma Imperativo I/03 - Exercícios/exercicios-aula-09.md (linha 34).
// Seção: Avançado
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-09/exercicios/01-avancado.c

int main() {
    int x = 0;
repete: printf("%d\n", x);
    x++;
    if (x < 10)
        goto repete;
    return 0;
}
