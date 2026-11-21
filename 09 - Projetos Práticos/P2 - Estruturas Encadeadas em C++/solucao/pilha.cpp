#include "pilha.hpp"
#include <stdexcept>

Pilha::Pilha() : topo_(nullptr), tamanho_(0) {}

Pilha::~Pilha() { limpar(); }

Pilha::Pilha(const Pilha& outra) : topo_(nullptr), tamanho_(0) { copiar_de(outra); }

Pilha& Pilha::operator=(const Pilha& outra) {
    if (this != &outra) {                    // p = p não pode apagar os próprios nós
        limpar();
        copiar_de(outra);
    }
    return *this;
}

void Pilha::push(int valor) {
    topo_ = new Nodo{valor, topo_};          // o novo nó aponta para o antigo topo
    tamanho_++;
}

int Pilha::pop() {
    if (vazia()) throw std::underflow_error("pilha vazia");
    Nodo* velho = topo_;
    int valor = velho->valor;
    topo_ = velho->proximo;
    delete velho;                            // sem isto, cada pop vaza um nó
    tamanho_--;
    return valor;
}

int Pilha::topo() const {
    if (vazia()) throw std::underflow_error("pilha vazia");
    return topo_->valor;
}

bool Pilha::vazia() const { return topo_ == nullptr; }

int Pilha::tamanho() const { return tamanho_; }

void Pilha::limpar() {
    while (topo_ != nullptr) {
        Nodo* proximo = topo_->proximo;
        delete topo_;
        topo_ = proximo;
    }
    tamanho_ = 0;
}

void Pilha::copiar_de(const Pilha& outra) {
    // percorre a outra pilha do topo para a base, mantendo a mesma ordem
    Nodo** fim = &topo_;
    for (Nodo* p = outra.topo_; p != nullptr; p = p->proximo) {
        *fim = new Nodo{p->valor, nullptr};
        fim = &(*fim)->proximo;
    }
    tamanho_ = outra.tamanho_;
}
