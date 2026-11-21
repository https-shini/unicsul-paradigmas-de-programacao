// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/04 - Resoluções/resolucoes-aula-13.md (linha 185).
// Seção: E9
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resolucoes/05-e9.cpp
// A saída deve conter: Impressora ligada ⏎ Scanner ligado

#include <iostream>
class Impressora { public: void ligar() { std::cout << "Impressora ligada\n"; } };
class Scanner    { public: void ligar() { std::cout << "Scanner ligado\n"; } };

class Multifuncional : public Impressora, public Scanner {
public:
    void ligar() {               // resolve o conflito explicitamente
        Impressora::ligar();
        Scanner::ligar();
    }
};

int main() {
    Multifuncional m;
    m.ligar();                   // agora não é ambíguo
    return 0;
}
