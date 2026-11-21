// Fila de inteiros encadeada: insere no fim, remove do início (FIFO).
#ifndef FILA_HPP
#define FILA_HPP

class Fila {
public:
    Fila();
    ~Fila();
    Fila(const Fila&) = delete;
    Fila& operator=(const Fila&) = delete;

    void enfileirar(int valor);
    int desenfileirar();                     // lança std::underflow_error se vazia
    int frente() const;                      // idem
    bool vazia() const;
    int tamanho() const;

private:
    struct Nodo {
        int valor;
        Nodo* proximo;
    };
    Nodo* inicio_;                           // de onde se remove
    Nodo* fim_;                              // onde se insere: O(1) sem percorrer a lista
    int tamanho_;
};

#endif
