// Testes do projeto P2. Rode com:  python3 ferramentas/testar_projetos.py P2
// A ferramenta compila com -fsanitize=address,undefined quando disponível: vazamentos de memória,
// delete duplo e acesso fora do vetor também reprovam.
#include <cstdio>
#include <exception>
#include <functional>
#include <stdexcept>
#include "pilha.hpp"
#include "pilha_vetor.hpp"
#include "fila.hpp"

static int total = 0, falhas = 0;

#define CHECA(cond) do { total++; if (!(cond)) { falhas++; \
    std::printf("  FALHOU (linha %d): %s\n", __LINE__, #cond); } } while (0)

static bool lanca_underflow(const std::function<void()>& f) {
    try { f(); } catch (const std::underflow_error&) { return true; } catch (...) { return false; }
    return false;
}

static void teste(const char* nome, const std::function<void()>& corpo) {
    std::printf("%s\n", nome);
    try {
        corpo();
    } catch (const std::exception& e) {
        total++; falhas++;
        std::printf("  FALHOU: exceção inesperada: %s\n", e.what());
    }
}

// As duas pilhas têm a mesma interface: os mesmos testes valem para as duas representações.
template <class P>
static void testes_de_pilha(const char* nome) {
    std::printf("== %s ==\n", nome);
    teste("nova pilha está vazia", [] {
        P p;
        CHECA(p.vazia());
        CHECA(p.tamanho() == 0);
    });
    teste("LIFO: o último a entrar é o primeiro a sair", [] {
        P p;
        p.push(5); p.push(10); p.push(15);
        CHECA(!p.vazia());
        CHECA(p.tamanho() == 3);
        CHECA(p.topo() == 15);
        CHECA(p.pop() == 15);
        CHECA(p.pop() == 10);
        CHECA(p.pop() == 5);
        CHECA(p.vazia());
    });
    teste("topo não remove", [] {
        P p;
        p.push(7);
        CHECA(p.topo() == 7);
        CHECA(p.tamanho() == 1);
    });
    teste("pop e topo em pilha vazia lançam underflow_error", [] {
        P p;
        CHECA(lanca_underflow([&] { p.pop(); }));
        CHECA(lanca_underflow([&] { p.topo(); }));
        p.push(1);
        p.pop();
        CHECA(lanca_underflow([&] { p.pop(); }));
    });
    teste("muitos elementos (o vetor precisa crescer)", [] {
        P p;
        for (int i = 0; i < 1000; i++) p.push(i);
        CHECA(p.tamanho() == 1000);
        bool ordem = true;
        for (int i = 999; i >= 0; i--) ordem = ordem && p.pop() == i;
        CHECA(ordem);
        CHECA(p.vazia());
    });
    teste("destrutor libera o que sobrou (ver o AddressSanitizer)", [] {
        P p;
        for (int i = 0; i < 50; i++) p.push(i);
    });
}

int main() {
    testes_de_pilha<Pilha>("Pilha encadeada");
    testes_de_pilha<PilhaVetor>("PilhaVetor");

    std::printf("== PilhaVetor: capacidade ==\n");
    teste("dobra quando enche", [] {
        PilhaVetor p(2);
        CHECA(p.capacidade() == 2);
        p.push(1); p.push(2);
        CHECA(p.capacidade() == 2);
        p.push(3);
        CHECA(p.capacidade() == 4);
        CHECA(p.pop() == 3 && p.pop() == 2 && p.pop() == 1);
    });

    std::printf("== Pilha: cópia profunda ==\n");
    teste("a cópia tem os mesmos valores, na mesma ordem", [] {
        Pilha a;
        a.push(1); a.push(2); a.push(3);
        Pilha b(a);
        CHECA(b.tamanho() == 3);
        CHECA(b.pop() == 3 && b.pop() == 2 && b.pop() == 1);
        CHECA(a.tamanho() == 3);                       // a original não mudou
    });
    teste("cópia e original são independentes", [] {
        Pilha a;
        a.push(1);
        Pilha b = a;
        b.push(99);
        a.pop();
        CHECA(a.vazia());
        CHECA(b.tamanho() == 2 && b.topo() == 99);
    });
    teste("atribuição substitui o conteúdo e tolera p = p", [] {
        Pilha a, b;
        a.push(1); a.push(2);
        b.push(7);
        b = a;
        CHECA(b.tamanho() == 2 && b.topo() == 2);
        Pilha& ref = b;
        b = ref;                                       // autoatribuição
        CHECA(b.tamanho() == 2 && b.pop() == 2 && b.pop() == 1);
        CHECA(a.tamanho() == 2);
    });

    std::printf("== Fila ==\n");
    teste("nova fila está vazia", [] {
        Fila f;
        CHECA(f.vazia() && f.tamanho() == 0);
    });
    teste("FIFO: o primeiro a entrar é o primeiro a sair", [] {
        Fila f;
        f.enfileirar(10); f.enfileirar(20); f.enfileirar(30);
        CHECA(f.tamanho() == 3);
        CHECA(f.frente() == 10);
        CHECA(f.desenfileirar() == 10);
        f.enfileirar(40);
        CHECA(f.desenfileirar() == 20);
        CHECA(f.desenfileirar() == 30);
        CHECA(f.desenfileirar() == 40);
        CHECA(f.vazia());
    });
    teste("esvaziar e voltar a usar", [] {
        Fila f;
        f.enfileirar(1);
        f.desenfileirar();
        f.enfileirar(2);                               // fim_ precisa ter sido zerado
        CHECA(f.frente() == 2 && f.tamanho() == 1);
    });
    teste("desenfileirar e frente em fila vazia lançam underflow_error", [] {
        Fila f;
        CHECA(lanca_underflow([&] { f.desenfileirar(); }));
        CHECA(lanca_underflow([&] { f.frente(); }));
    });
    teste("destrutor da fila libera os nós", [] {
        Fila f;
        for (int i = 0; i < 50; i++) f.enfileirar(i);
    });

    std::printf("\nRESULTADO: %d testes, %d falhas\n", total, falhas);
    std::fflush(stdout);                               // o AddressSanitizer roda depois do main
    return falhas ? 1 : 0;
}
