#include "fila.hpp"
#include <stdexcept>

Fila::Fila() : inicio_(nullptr), fim_(nullptr), tamanho_(0) {}

Fila::~Fila() {
    while (inicio_ != nullptr) {
        Nodo* proximo = inicio_->proximo;
        delete inicio_;
        inicio_ = proximo;
    }
}

void Fila::enfileirar(int valor) {
    Nodo* novo = new Nodo{valor, nullptr};
    if (fim_ == nullptr) inicio_ = novo;     // fila vazia: o novo é início e fim
    else fim_->proximo = novo;
    fim_ = novo;
    tamanho_++;
}

int Fila::desenfileirar() {
    if (vazia()) throw std::underflow_error("fila vazia");
    Nodo* velho = inicio_;
    int valor = velho->valor;
    inicio_ = velho->proximo;
    if (inicio_ == nullptr) fim_ = nullptr;  // esvaziou: fim também deixa de apontar para o nó apagado
    delete velho;
    tamanho_--;
    return valor;
}

int Fila::frente() const {
    if (vazia()) throw std::underflow_error("fila vazia");
    return inicio_->valor;
}

bool Fila::vazia() const { return inicio_ == nullptr; }
int Fila::tamanho() const { return tamanho_; }
