// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/02 - Resumo Teórico/resumo-aula-12.md (linha 417).
// Seção: 7. Criação e destruição de objetos (p.28–30)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resumo/07-7-criacao-e-destruicao-de-objetos-p-28-30.cpp
// Entrada de exemplo: 5 10 15
// A saída deve conter: 15 ⏎ 10 ⏎ 5

#include <iostream>
using namespace std;

class Nodo {                                   // nodo.h + nodo.cpp, reunidos para compilar
    int valor;
    Nodo* proximo;
public:
    Nodo(int x, Nodo* prox) { this->valor = x; this->proximo = prox; }
    ~Nodo() { }
    int getValor()      { return this->valor; }
    Nodo* getProximo()  { return this->proximo; }
};

class Pilha {                                  // pilha.h + pilha.cpp
    Nodo* topo;
public:
    Pilha() { this->topo = NULL; }
    ~Pilha() {                                 // DESTRUTOR: libera todos os nós restantes
        while (topo != NULL) {
            Nodo* temp = topo->getProximo();
            delete topo;
            topo = temp;
        }
    }
    void push(int n) {
        Nodo* x = new Nodo(n, this->topo);     // novo nó no heap, apontando para o antigo topo
        topo = x;
    }
    int pop() {
        if (topo == NULL) {                    // [Complemento] trecho cortado no slide
            cerr << "Erro - Pilha vazia" << endl;
            return -1;
        }
        int x = topo->getValor();
        Nodo* temp = topo->getProximo();
        delete topo;                           // libera o nó removido
        topo = temp;
        return x;
    }
};

int main() {
    Pilha *p1;
    int x;
    p1 = new Pilha();                          // objeto no heap
    for (int i = 0; i < 3; i++) {
        std::cout << "Digite um numero: ";
        std::cin >> x;
        p1->push(x);
    }
    std::cout << "\n";
    for (int i = 0; i < 3; i++) {
        x = p1->pop();
        if (x != -1) {
            std::cout << x << std::endl;
        }
    }
    delete p1;                                 // chama ~Pilha() automaticamente
    return 0;
}
