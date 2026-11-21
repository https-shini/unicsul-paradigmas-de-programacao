// Mesma interface da Pilha, com outra REPRESENTAÇÃO: vetor dinâmico que dobra de tamanho.
// O cliente (main, testes) não muda — é a independência de representação do TDA (Aula 12).
#ifndef PILHA_VETOR_HPP
#define PILHA_VETOR_HPP

class PilhaVetor {
public:
    explicit PilhaVetor(int capacidade_inicial = 4);
    ~PilhaVetor();
    PilhaVetor(const PilhaVetor&) = delete;              // cópia rasa causaria delete[] duplo
    PilhaVetor& operator=(const PilhaVetor&) = delete;

    void push(int valor);                               // cresce quando cheia
    int pop();                                          // lança std::underflow_error se vazia
    int topo() const;
    bool vazia() const;
    int tamanho() const;
    int capacidade() const;

private:
    int* dados_;                                        // new int[n], não new int(n) (ver errata 14)
    int capacidade_;
    int tamanho_;
};

#endif
