// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/02 - Resumo Teórico/resumo-aula-13.md (linha 68).
// Seção: 3. Exemplo: impressora multifuncional (p.7–9)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resumo/01-3-exemplo-impressora-multifuncional-p-7-9.cpp
// A saída deve conter: Estou imprimindo um documento. ⏎ Estou digitalizando um documento. ⏎ Estou copiando um documento ⏎ ****** ⏎ Estou digitalizando um documento. ⏎ Estou imprimindo um documento. ⏎ ******

#include <iostream>
using namespace std;

// Classe base 1
class Impressora {
public:
    void imprimaDocumento() {
        cout << "Estou imprimindo um documento." << endl;
    }
};

// Classe base 2
class Scanner {
public:
    void digitalizeDocumento() {
        cout << "Estou digitalizando um documento." << endl;
    }
};

// Classe com herança múltipla
class Multifuncional : public Impressora, public Scanner {
public:
    void copieDocumento() {
        cout << "Estou copiando um documento" << endl;
        cout << "******" << endl;
        digitalizeDocumento();      // herdado de Scanner
        imprimaDocumento();         // herdado de Impressora
        cout << "******" << endl;
    }
};

int main() {
    Multifuncional hp3000;
    hp3000.imprimaDocumento();
    hp3000.digitalizeDocumento();
    hp3000.copieDocumento();
    return 0;
}
