#include "fila.hpp"
#include <stdexcept>

Fila::Fila() : inicio_(nullptr), fim_(nullptr), tamanho_(0) {}

Fila::~Fila() {
    // TODO (R6): liberar todos os nós
}

void Fila::enfileirar(int valor) {
    // TODO (R6): o novo nó entra depois de fim_. Fila vazia: ele também vira o início.
    (void) valor;
    throw std::logic_error("TODO: Fila::enfileirar");
}

int Fila::desenfileirar() {
    // TODO (R6): remove do início. Se a fila esvaziar, fim_ também precisa voltar a nullptr.
    throw std::logic_error("TODO: Fila::desenfileirar");
}

int Fila::frente() const {
    throw std::logic_error("TODO: Fila::frente");
}

bool Fila::vazia() const { return inicio_ == nullptr; }
int Fila::tamanho() const { return tamanho_; }
