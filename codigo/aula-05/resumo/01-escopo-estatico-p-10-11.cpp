// Gerado automaticamente a partir de 01 - Aulas/Aula 05 - Semântica/02 - Resumo Teórico/resumo-aula-05.md (linha 99).
// Seção: Escopo estático (p.10–11)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-05/resumo/01-escopo-estatico-p-10-11.cpp
// A saída deve conter: local: 2 | global: 1 | bloco interno: 3 | de volta: 2

#include <iostream>
int x = 1;                         // global

int main() {
    int x = 2;                     // local de main: esconde (sombreia) a global
    std::cout << "local: " << x << "\n";        // 2
    std::cout << "global: " << ::x << "\n";     // 1  -> operador de escopo
    {
        int x = 3;                 // bloco interno: esconde a de main
        std::cout << "bloco interno: " << x << "\n";  // 3
    }
    std::cout << "de volta: " << x << "\n";     // 2
    return 0;
}
