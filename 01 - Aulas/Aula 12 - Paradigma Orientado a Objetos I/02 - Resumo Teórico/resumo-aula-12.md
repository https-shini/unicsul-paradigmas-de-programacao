# Aula 12 — Paradigma Orientado a Objetos I · Resumo teórico

> **Fonte:** [`Aula12_ParadigmaOrientadoObjetos1.pdf`](../01%20-%20Slides%20Originais/Aula12_ParadigmaOrientadoObjetos1.pdf) (31 páginas). Título interno: "Aula 13 – Paradigma Orientado a Objetos – Parte 1". Apoio indicado: Tucker & Noonan, cap. 13; Sebesta (9ª ed.), caps. 11 e 12 (p.31).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF. Os códigos Java e C++ foram compilados e executados; nos testes, a pilha recebeu 5, 10 e 15 (ou 1 a 5).

---

## 1. Objetivos (p.2)

**[Material original]** Revisar a diferença entre abstração de processos e de dados; conceituar tipo de dado abstrato e encapsulamento; conceituar classes, atributos e métodos; diferenciar a definição de uma classe em C++ e em Java; conhecer a coleta manual de lixo.

## 2. Por que surgiu a OO (p.3–6)

**[Material original]**

- **Crise de Software:** crescente demanda por soluções de software e aumento da complexidade delas.
- Necessidade de aumentar a **produtividade** dos programadores por meio de **reusabilidade**, **manutenibilidade** e **extensibilidade**.
- Os recursos dos paradigmas **imperativo, funcional e lógico** dificultavam essas tarefas.

| Qualidade | Definição (p.4) |
| --- | --- |
| **Reusabilidade** | Utilizar conceitos ou soluções previamente elaborados para criar um novo software |
| **Extensibilidade** | Facilidade de **estender** o software: adicionar novas funcionalidades |
| **Manutenibilidade** | Facilidade de **alterar** o software: corrigir bugs, alterar funcionalidades |

**Histórico (p.5):**

- O modelo de abstração por **decomposição funcional** (abstração de processos) não era adequado para determinados problemas.
- Os **pacotes** — tipos de dados abstratos dos anos 1980 — tinham problemas, como a **inexistência de mecanismos automáticos de inicialização e finalização** de valores.
- As primeiras ideias surgiram no **SIMULA 67** e evoluíram até o **Smalltalk 80**, considerado uma linguagem **OO pura**.

**Os três recursos principais da POO (p.6):**

1. **Tipos de dados abstratos** (classes).
2. **Herança**.
3. **Vinculação dinâmica** de chamadas a métodos (**polimorfismo**).

**[Explicação elaborada]** Os "mecanismos automáticos de inicialização e finalização" que faltavam aos pacotes são os **construtores** e **destrutores**, que a OO introduziu (seção 7). Herança e polimorfismo são o tema da [Aula 13](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md).

## 3. O exemplo progressivo da pilha (p.7–16)

**[Material original]** Pilha é uma estrutura de dados que **só permite inserir e retirar elementos no seu topo** (LIFO). A figura da p.7 mostra: empilhar 10 (topo = 0), empilhar 5 (topo = 1), empilhar 15 (topo = 2), desempilhar (topo = 1), empilhar 25 (topo = 2), desempilhar (topo = 1).

O professor mostra **quatro versões** do mesmo programa em Java, que empilha números lidos do teclado e depois os desempilha e imprime. Cada versão acrescenta um nível de abstração.

> **[Atenção]** O enunciado (p.8) fala em "empilhar **três** números", mas os laços de todas as versões Java vão de 0 a 4 (**cinco** números). Só a versão C++ da p.30 usa 3.

### Versão 1a — tudo no `main` (p.8–9)

**Pergunta do professor:** "Há algum tipo de abstração neste programa?"

<!-- teste: entrada="1\n2\n3\n4\n5" saida-contem="5\n4\n3\n2\n1" -->
```java
import java.util.*;

public class Main {
    static int[] pilha = new int[5];
    static int topo = 0;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        for (int i = 0; i < 5; i++) {                 // empilha
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            if (topo == 5) {
                System.out.println("Erro - pilha cheia");
            } else {
                pilha[topo] = elemento;
                topo++;
            }
        }
        for (int i = 0; i < 5; i++) {                 // desempilha
            if (topo == 0) {
                System.out.println("Erro - pilha vazia");
            } else {
                topo--;
                elemento = pilha[topo];
                System.out.println(elemento);
            }
        }
    }
}
```

**Resposta:** **nenhuma abstração** — dados e lógica de empilhar e desempilhar estão misturados no `main`. Para usar uma segunda pilha, seria preciso duplicar tudo.

### Versão 1b — métodos `push` e `pop` (p.10–11)

**Perguntas:** "A única forma de incluir e retirar elementos da pilha é por meio dos métodos `push` e `pop`? O que isso significa em termos de abstração?"

<!-- teste: entrada="1\n2\n3\n4\n5" saida-contem="5\n4\n3\n2\n1" -->
```java
import java.util.*;

public class Main {
    static int[] pilha = new int[5];
    static int topo = 0;

    static void push(int n) {
        if (topo == 5) {
            System.out.println("Erro - pilha cheia");
        } else {
            pilha[topo] = n;
            topo++;
        }
    }

    static int pop() {
        if (topo == 0) {
            System.out.println("Erro - pilha vazia");
            return -1;
        } else {
            topo--;
            int n = pilha[topo];
            return n;
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            push(elemento);
        }
        for (int i = 0; i < 5; i++) {
            elemento = pop();
            if (elemento != -1) {
                System.out.println(elemento);
            }
        }
    }
}
```

**Resposta:** **não** — `pilha` e `topo` são campos `static` visíveis em toda a classe, e o `main` ainda poderia fazer `pilha[topo] = 99`. Há **abstração de processos** (as operações têm nome), mas **sem ocultação dos dados**.

### Versão 1c — classe `Pilha` com atributos privados (p.12–13)

**Perguntas:** "É possível interagir com a estrutura `vetPilha` no `main`? Se a forma de armazenar mudar de vetor para alocação encadeada, é preciso mudar algo no `main`?"

<!-- teste: entrada="1\n2\n3\n4\n5" saida-contem="5\n4\n3\n2\n1" -->
```java
import java.util.*;

class Pilha {
    private int[] vetPilha = new int[5];   // representação OCULTA
    private int topo;

    public Pilha() {                       // construtor (no slide: "public void Pilha()", ver [Atenção])
        topo = 0;
    }

    public void push(int n) {
        if (this.topo == 5) {
            System.out.println("Erro - pilha cheia");
        } else {
            this.vetPilha[this.topo] = n;
            this.topo++;
        }
    }

    public int pop() {
        if (this.topo == 0) {
            System.out.println("Erro - pilha vazia");
            return -1;
        } else {
            this.topo--;
            int n = this.vetPilha[this.topo];
            return n;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        Pilha pilha = new Pilha();
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            pilha.push(elemento);
        }
        for (int i = 0; i < 5; i++) {
            elemento = pilha.pop();
            if (elemento != -1) {
                System.out.println(elemento);
            }
        }
    }
}
```

> **[Atenção]** No slide (p.13), o "construtor" está escrito `public void Pilha() { topo = 0; }`. Com o tipo de retorno `void`, isso **não é um construtor**, e sim um método comum chamado `Pilha`, que `new Pilha()` não executa. O programa funciona mesmo assim porque o Java inicializa `topo` com 0 por padrão. O mesmo acontece na versão 1d (p.15 e p.29, `public void Pilha() { this.topo = null; }`). Construtor não tem tipo de retorno: `public Pilha() { ... }`, como no código acima.

**Resposta:** **não é possível** acessar `vetPilha`, que é `private` — `pilha.vetPilha[0] = 9` não compila. E **não** seria preciso mudar o `main` se a representação mudasse: ele só depende de `push` e `pop`. É a **abstração de dados** com **encapsulamento**, um TDA.

### Versão 1d — lista encadeada (p.14–16)

**Pergunta:** "A troca de vetor para alocação encadeada fez com que alguma mudança tivesse que ser feita no `main`?"

<!-- teste: entrada="1\n2\n3\n4\n5" saida-contem="5\n4\n3\n2\n1" -->
```java
import java.util.*;

class Nodo {
    private int valor;
    private Nodo proximo;

    public Nodo(int x, Nodo prox) {
        this.valor = x;
        this.proximo = prox;
    }
    public int getValor()     { return this.valor; }
    public Nodo getProximo()  { return this.proximo; }
}

class Pilha {
    private Nodo topo;                 // a representação mudou...

    public Pilha() {                   // no slide: "public void Pilha()" (ver [Atenção] da 1c)
        this.topo = null;
    }

    public void push(int n) {          // ...mas a interface é a mesma
        Nodo x = new Nodo(n, this.topo);
        topo = x;
    }

    public int pop() {
        if (topo != null) {
            int x = topo.getValor();
            topo = topo.getProximo();
            return x;
        } else {
            System.out.println("Erro - pilha vazia");
            return -1;
        }
    }
}

public class Main {                     // main IDÊNTICO ao da versão com vetor (p.16)
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        Pilha pilha = new Pilha();
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            pilha.push(elemento);
        }
        for (int i = 0; i < 5; i++) {
            elemento = pilha.pop();
            if (elemento != -1) {
                System.out.println(elemento);
            }
        }
    }
}
```

**Resposta:** **nenhuma mudança** no `main` — a p.16 põe os dois `main` lado a lado e eles são idênticos. A interface (`push`/`pop`) **não depende da representação** (vetor ou lista).

**[Explicação elaborada] — resumo da progressão:**

| Versão | Dados ocultos? | Operações nomeadas? | Abstração |
| --- | --- | --- | --- |
| 1a | Não | Não | Nenhuma |
| 1b | Não (`static` visível) | Sim (`push`/`pop`) | De **processos** |
| 1c | **Sim** (`private`) | Sim | De **dados** (TDA) |
| 1d | Sim | Sim, mesma interface | De dados + **independência de representação** |

> **[Complemento]** As versões usam **−1** como sinal de "pilha vazia", então empilhar o valor −1 tornaria o `main` incapaz de distinguir um elemento válido de um erro. Em Java, a solução idiomática é lançar uma exceção (`throw new RuntimeException("pilha vazia")`).

## 4. Abstração em linguagens de programação (p.17)

**[Material original]**

- **Abstração de processos:** subprogramas — característica básica da programação **imperativa**.
- **Abstração de dados:** tipos de dados abstratos, com **atributos** (dados) e **comportamentos** (subprogramas) — base da programação **orientada a objetos**.

## 5. Tipo de dado abstrato e encapsulamento (p.18–21)

**[Material original]**

- **TDA (Sebesta):** "um invólucro que inclui apenas a representação de dados de um tipo de dados específico e os subprogramas que fornecem as operações para este tipo."
- Um TDA deve fornecer: (1) uma definição de tipo que permita **declarar variáveis** do tipo, mas que **oculte a representação** dos dados (**encapsulamento**); (2) um conjunto de **métodos** para manipular os dados.
- **Encapsulamento (Tucker e Noonan):** "mecanismo que permite que constantes logicamente relacionadas, tipos, variáveis, métodos, entre outros, sejam agrupados em uma nova entidade."
  - Os dados são chamados de **atributos** ou variáveis e podem aparecer nas classes e nas instâncias.
  - As funções são chamadas de **funções membros** ou **métodos**.
  - **Todas as instâncias compartilham o mesmo conjunto de métodos, mas cada instância tem seu próprio conjunto de atributos.**

**Tipos de dados abstratos (p.20):**

- permitem declarar variáveis do tipo;
- ocultam a representação interna — as operações são a única forma de acesso;
- oferecem operações para manipular as variáveis;
- têm uma **interface que não depende** da representação nem da implementação das operações;
- permitem que outras unidades do programa, os **clientes**, usem seus serviços.

**Vantagens — confiabilidade e legibilidade (p.21):**

1. Clientes **não podem alterar os atributos diretamente**, nem de propósito nem por acidente.
2. Reduz a quantidade de código e de variáveis que o programador precisa acompanhar num trecho.
3. Reduz **conflitos de nomes**, por gerar escopos menores.

**Implementação de TDAs (p.22):**

- As primeiras linguagens usavam **pacotes**.
- **C++, C# e Object Pascal (Delphi)** permitem abstração por **classes** e por **registros** (`struct`/`record`).
- **Java e Smalltalk** não têm registros: **todas as abstrações são classes**.

## 6. Classe (p.23–27)

**[Material original]**

- **Classe** é uma declaração de tipo que encapsula constantes, variáveis e funções para manipular essas variáveis. Define o **estado** e o **comportamento** dos objetos.
- Suas variáveis — **atributos** ou **variáveis de instância** — podem ser **inicializadas por construtores** e **finalizadas por destrutores**. As demais funções são **métodos**.
- **Cliente** de uma classe X é qualquer outra classe ou método que declara e usa um objeto de X.

**Modificadores de acesso (p.25):**

| Modificador | Quem acessa |
| --- | --- |
| `public` | Qualquer classe |
| `private` | Apenas a própria classe |
| `protected` | A própria classe e suas derivadas (herança) |

Em geral, **métodos são públicos** e **atributos são privados ou protegidos**, acessados por métodos **get** e **set**.

**Classe em C++ × Java (p.26–27):** em C++, a classe pode ser criada de duas maneiras:

1. **Definição completa na própria classe** (interface e implementação no mesmo arquivo) — "ideal para a programação de sistemas de tempo real".
2. **Interface e implementação em arquivos separados** (`.h` e `.cpp`) — melhora a legibilidade e facilita a manutenção.

Em Java, a classe é sempre definida inteira num único arquivo `.java`.

**Pilha com vetor em C++, separada (p.27):**

```cpp
// Arquivo pilha.h — INTERFACE
class Pilha {
    private:
        int vetPilha[5];
        int topo;
    public:
        Pilha();
        ~Pilha();
        void push(int n);
        int pop();
};
```

```cpp
// Arquivo pilha.cpp — IMPLEMENTAÇÃO
#include <iostream>
#include "pilha.h"

Pilha::Pilha() {             // construtor
    topo = -1;
}

Pilha::~Pilha() {            // destrutor (nada a liberar aqui)
}

void Pilha::push(int n) {
    if (topo == tamanho-1) {           // [Atenção] 'tamanho' não está declarado em pilha.h
        std::cerr << "Erro - pilha cheia\n";
    }
    else {
        topo++;
        vetPilha[topo] = n;
    }
}

int Pilha::pop() {
    if (topo == -1) {
        std::cerr << "Erro - Pilha vazia" << std::endl;
        return -1;
    }
    else {
        return vetPilha[topo--];
    }
}
```

> **[Atenção]** `tamanho` não aparece em `pilha.h`; o código só compila se for definido em outro lugar (por exemplo, `const int tamanho = 5;`).
>
> **[Explicação elaborada]** Aqui `topo` começa em **−1** e aponta o **último elemento** (pré-incremento: `topo++` e depois grava; `vetPilha[topo--]` lê e depois decrementa). Na versão Java, `topo` começa em **0** e aponta a **próxima posição livre**. As duas convenções são válidas.

## 7. Criação e destruição de objetos (p.28–30)

**[Material original]**

- Objetos dinâmicos precisam ser **criados e destruídos**.
- Na criação, recursos e áreas de memória podem ser **alocados**.
- Em algumas linguagens, é **dever do programador** prever a liberação desses recursos e da memória durante a destruição do objeto.
- Algumas linguagens fazem **coleta de lixo automática** (Java).

A p.29 reúne numa só tela as três classes Java da versão 1d (`Nodo`, `Pilha`, `Main`).

**Pilha encadeada em C++ (p.30):** `main` com `Pilha *p1 = new Pilha();`, que empilha 3 números, desempilha e termina com `delete p1;`; `Pilha` com destrutor que percorre a lista e libera cada nó; `Nodo` com construtor, destrutor vazio, `getValor` e `getProximo`.

> **[Atenção]** O corpo de `Pilha::pop()` está **cortado na borda do slide** (p.30); só aparecem `int x = topo->getValor();` e `Nodo* temp = topo->getProximo();`. A versão abaixo completa o método e acrescenta uma quebra de linha entre os dois laços do `main` **[Complemento]**, de forma compatível com o restante.

<!-- teste: entrada="5 10 15" saida-contem="15\n10\n5" -->
```cpp
#include <iostream>
using namespace std;

class Nodo {                                   // nodo.h + nodo.cpp, reunidos para compilar
    int valor;
    Nodo* proximo;
public:
    Nodo(int x, Nodo* prox) { this->valor = x; this->proximo = prox; }
    ~Nodo() { }
    int getValor()      { return this->valor; }
    Nodo* getProximo()  { return this->proximo; }
};

class Pilha {                                  // pilha.h + pilha.cpp
    Nodo* topo;
public:
    Pilha() { this->topo = NULL; }
    ~Pilha() {                                 // DESTRUTOR: libera todos os nós restantes
        while (topo != NULL) {
            Nodo* temp = topo->getProximo();
            delete topo;
            topo = temp;
        }
    }
    void push(int n) {
        Nodo* x = new Nodo(n, this->topo);     // novo nó no heap, apontando para o antigo topo
        topo = x;
    }
    int pop() {
        if (topo == NULL) {                    // [Complemento] trecho cortado no slide
            cerr << "Erro - Pilha vazia" << endl;
            return -1;
        }
        int x = topo->getValor();
        Nodo* temp = topo->getProximo();
        delete topo;                           // libera o nó removido
        topo = temp;
        return x;
    }
};

int main() {
    Pilha *p1;
    int x;
    p1 = new Pilha();                          // objeto no heap
    for (int i = 0; i < 3; i++) {
        std::cout << "Digite um numero: ";
        std::cin >> x;
        p1->push(x);
    }
    std::cout << "\n";
    for (int i = 0; i < 3; i++) {
        x = p1->pop();
        if (x != -1) {
            std::cout << x << std::endl;
        }
    }
    delete p1;                                 // chama ~Pilha() automaticamente
    return 0;
}
```

**[Explicação elaborada]**

- Em C++, cada `new` precisa de um `delete` correspondente; caso contrário, há **vazamento de memória**. O **destrutor** `~Pilha()` é chamado automaticamente pelo `delete p1` e libera os nós que ainda estiverem na pilha. `pop` também precisa dar `delete` no nó que remove.
- Em Java, a versão 1d nunca libera nada explicitamente: quando um `Nodo` deixa de ser referenciado (após `topo = topo.getProximo()`), o **coletor de lixo** o recolhe.
- Esse é o "mecanismo automático de finalização" que faltava aos pacotes (p.5).

## 8. Conexões e pontos para a prova

- Abstração de processos × de dados vem da [Aula 10](../../Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md); registros → classes, da [Aula 07](../../Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md); heap e `new`/`delete`, da [Aula 08](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md).
- Cobrado na [Lista 02, Q8 e Q10](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q10).
- **Decorar:** Crise de Software e as três "-dades"; os 3 recursos da POO; definição de TDA e de encapsulamento; os modificadores de acesso; destrutor × coleta de lixo. **Saber explicar a progressão 1a → 1d.**

---

**Anterior:** [Aula 11](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md) · **Próxima:** [Aula 13 — Paradigma Orientado a Objetos II](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)
