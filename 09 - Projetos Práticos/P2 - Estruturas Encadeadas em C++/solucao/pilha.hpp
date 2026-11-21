// Pilha de inteiros com alocação ENCADEADA (Aula 12, versão 1d/C++; Aula 08, heap e ponteiros).
#ifndef PILHA_HPP
#define PILHA_HPP

class Pilha {
public:
    Pilha();
    ~Pilha();                                // libera todos os nós
    Pilha(const Pilha& outra);               // cópia PROFUNDA: novos nós, mesmos valores
    Pilha& operator=(const Pilha& outra);

    void push(int valor);
    int pop();                               // lança std::underflow_error se vazia
    int topo() const;                        // idem
    bool vazia() const;
    int tamanho() const;

private:
    struct Nodo {                            // no slide, Nodo é uma classe com getValor/getProximo
        int valor;
        Nodo* proximo;
    };
    Nodo* topo_;
    int tamanho_;

    void limpar();
    void copiar_de(const Pilha& outra);
};

#endif
