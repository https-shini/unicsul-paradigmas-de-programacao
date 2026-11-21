#include "pilha.hpp"
#include <stdexcept>

Pilha::Pilha() : topo_(nullptr), tamanho_(0) {}

Pilha::~Pilha() {
    // TODO (R3): liberar todos os nós. Dica: reaproveite limpar().
}

Pilha::Pilha(const Pilha& outra) : topo_(nullptr), tamanho_(0) {
    // TODO (R7): cópia profunda — criar NOVOS nós com os mesmos valores, na mesma ordem.
    (void) outra;
}

Pilha& Pilha::operator=(const Pilha& outra) {
    // TODO (R7): se não for autoatribuição (this != &outra), liberar os nós atuais e copiar os da outra.
    (void) outra;
    return *this;
}

void Pilha::push(int valor) {
    // TODO (R1): criar um nó no heap apontando para o topo atual; ele vira o novo topo.
    (void) valor;
    throw std::logic_error("TODO: Pilha::push");
}

int Pilha::pop() {
    // TODO (R2): pilha vazia → throw std::underflow_error("pilha vazia").
    // Guardar o valor, avançar o topo e dar delete no nó antigo (senão vaza memória).
    throw std::logic_error("TODO: Pilha::pop");
}

int Pilha::topo() const {
    throw std::logic_error("TODO: Pilha::topo");
}

bool Pilha::vazia() const { return topo_ == nullptr; }

int Pilha::tamanho() const { return tamanho_; }

void Pilha::limpar() {
    // TODO (R3): percorrer a lista dando delete em cada nó; no fim, topo_ = nullptr e tamanho_ = 0.
}

void Pilha::copiar_de(const Pilha& outra) {
    // TODO (R7): auxiliar opcional para o construtor de cópia e o operator=.
    (void) outra;
}
