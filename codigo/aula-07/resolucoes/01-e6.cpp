// Gerado automaticamente a partir de 01 - Aulas/Aula 07 - Tipos Compostos/04 - Resoluções/resolucoes-aula-07.md (linha 42).
// Seção: E6
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-07/resolucoes/01-e6.cpp
// A saída deve conter: p2.idade = 20

#include <iostream>
struct Pessoa { char nome[30]; int idade; char sexo; };

int main() {
    Pessoa p1 = {"Ana", 20, 'F'}, p2;
    p2 = p1;            // cópia campo a campo
    p1.idade = 99;      // altera só p1
    std::cout << "p2.idade = " << p2.idade << "\n";   // 20
    return 0;
}
