#include "pilha_vetor.hpp"
#include <stdexcept>

PilhaVetor::PilhaVetor(int capacidade_inicial)
    : dados_(nullptr), capacidade_(capacidade_inicial < 1 ? 1 : capacidade_inicial), tamanho_(0) {
    dados_ = new int[capacidade_];
}

PilhaVetor::~PilhaVetor() { delete[] dados_; }          // new[] combina com delete[]

void PilhaVetor::push(int valor) {
    if (tamanho_ == capacidade_) {                      // cheia: realoca com o dobro e copia
        int* maior = new int[capacidade_ * 2];
        for (int i = 0; i < tamanho_; i++) maior[i] = dados_[i];
        delete[] dados_;
        dados_ = maior;
        capacidade_ *= 2;
    }
    dados_[tamanho_++] = valor;
}

int PilhaVetor::pop() {
    if (vazia()) throw std::underflow_error("pilha vazia");
    return dados_[--tamanho_];
}

int PilhaVetor::topo() const {
    if (vazia()) throw std::underflow_error("pilha vazia");
    return dados_[tamanho_ - 1];
}

bool PilhaVetor::vazia() const { return tamanho_ == 0; }
int PilhaVetor::tamanho() const { return tamanho_; }
int PilhaVetor::capacidade() const { return capacidade_; }
