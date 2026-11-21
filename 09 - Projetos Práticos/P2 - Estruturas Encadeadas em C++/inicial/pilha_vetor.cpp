#include "pilha_vetor.hpp"
#include <stdexcept>

PilhaVetor::PilhaVetor(int capacidade_inicial)
    : dados_(nullptr), capacidade_(capacidade_inicial < 1 ? 1 : capacidade_inicial), tamanho_(0) {
    // TODO (R4): alocar o vetor no heap com new int[capacidade_]  (atenção: colchetes, não parênteses)
}

PilhaVetor::~PilhaVetor() {
    // TODO (R4): liberar o vetor (new[] combina com delete[])
}

void PilhaVetor::push(int valor) {
    // TODO (R5): se estiver cheia, alocar um vetor com o DOBRO da capacidade, copiar, liberar o antigo.
    (void) valor;
    throw std::logic_error("TODO: PilhaVetor::push");
}

int PilhaVetor::pop() {
    throw std::logic_error("TODO: PilhaVetor::pop");
}

int PilhaVetor::topo() const {
    throw std::logic_error("TODO: PilhaVetor::topo");
}

bool PilhaVetor::vazia() const { return tamanho_ == 0; }
int PilhaVetor::tamanho() const { return tamanho_; }
int PilhaVetor::capacidade() const { return capacidade_; }
