// Demonstração no estilo do slide (Aula 12 p.30): empilha 3 números lidos e desempilha.
// Compile: g++ -std=c++17 *.cpp -o demo && ./demo
#include <iostream>
#include <stdexcept>
#include "pilha.hpp"
#include "fila.hpp"

int main() {
    Pilha* p = new Pilha();                  // objeto no heap, como no slide
    Fila f;                                  // objeto na pilha de execução: destrutor automático
    int x;
    for (int i = 0; i < 3; i++) {
        std::cout << "Digite um numero: ";
        if (!(std::cin >> x)) break;
        p->push(x);
        f.enfileirar(x);
    }
    std::cout << "\nPilha (LIFO):";
    while (!p->vazia()) std::cout << ' ' << p->pop();
    std::cout << "\nFila  (FIFO):";
    while (!f.vazia()) std::cout << ' ' << f.desenfileirar();
    std::cout << '\n';
    try {
        p->pop();
    } catch (const std::underflow_error& e) {
        std::cout << "pop na pilha vazia: " << e.what() << '\n';   // no slide: devolve -1
    }
    delete p;                                // chama ~Pilha()
    return 0;
}
