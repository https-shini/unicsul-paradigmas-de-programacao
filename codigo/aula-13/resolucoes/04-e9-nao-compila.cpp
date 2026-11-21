// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/04 - Resoluções/resolucoes-aula-13.md (linha 173).
// Seção: E9
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resolucoes/04-e9-nao-compila.cpp
// ATENÇÃO: este exemplo NÃO compila de propósito (ilustra um erro).

#include <iostream>
class Impressora { public: void ligar() { std::cout << "Impressora ligada\n"; } };
class Scanner    { public: void ligar() { std::cout << "Scanner ligado\n"; } };
class Multifuncional : public Impressora, public Scanner { };

int main() {
    Multifuncional m;
    m.ligar();          // ERRO: request for member 'ligar' is ambiguous
    return 0;
}
