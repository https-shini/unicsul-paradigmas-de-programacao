<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 12](../README.md) › [04 - Resoluções](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 12 — Paradigma Orientado a Objetos I · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-12.md`](../03%20-%20Exercícios/exercicios-aula-12.md). Os programas Java foram compilados e executados.

## E1

**Crise de Software:** crescimento da demanda e da complexidade dos sistemas, sem aumento proporcional da produtividade dos programadores. Os paradigmas da época dificultavam três qualidades ([p.3–4](../01%20-%20Slides%20Originais/README.md#página-3)):

- **Reusabilidade:** usar soluções já elaboradas em um novo software.
- **Extensibilidade:** facilidade de adicionar funcionalidades.
- **Manutenibilidade:** facilidade de alterar o software (corrigir bugs, mudar funcionalidades).

## E2

Tipos de dados abstratos (classes), herança e vinculação dinâmica de chamadas a métodos (polimorfismo) ([p.6](../01%20-%20Slides%20Originais/README.md#página-6)).

## E3

**Resposta: c.** `protected` permite o acesso pela própria classe e pelas derivadas. `private` permite só pela própria classe; `public`, por qualquer uma. `static` não é modificador de acesso.

## E4

- **TDA (Sebesta):** invólucro que inclui apenas a representação de dados de um tipo específico e os subprogramas que fornecem suas operações.
- **Encapsulamento (Tucker e Noonan):** mecanismo de agrupar constantes, tipos, variáveis e métodos relacionados em uma nova entidade.
- **Relação:** o encapsulamento é o **mecanismo** que constrói o TDA. Ele agrupa dados e operações, e, com controle de acesso (`private`), **oculta** a representação. O TDA é o **resultado**: um tipo usado só pela interface.

## E5

```java
Pilha a = new Pilha();
Pilha b = new Pilha();
a.push(10);
b.push(99);
```

- **Atributos próprios:** `a` e `b` têm cada um seu `vetPilha` e seu `topo`. Depois do código, `a` contém 10 e `b` contém 99, independentes.
- **Métodos compartilhados:** o código de `push` existe **uma vez** na classe. Quando se chama `a.push(10)`, `this` aponta para `a`; em `b.push(99)`, para `b`. É o mesmo código operando sobre dados diferentes.

## E6

1. **Tudo dentro da classe**, interface e implementação no mesmo arquivo: o slide diz que é "ideal para sistemas de tempo real". **[Complemento]** Métodos definidos dentro da classe são candidatos a *inline*, o que evita o custo da chamada.
2. **Interface (`.h`) e implementação (`.cpp`) separadas:** melhora a legibilidade e facilita a manutenção. O cliente lê só a interface, e a implementação pode mudar sem alterar o `.h`.

## E7 — Perguntas originais

**a) 1a:** **não há abstração.** O vetor, o topo e toda a lógica de empilhar e desempilhar estão no `main`. Não há operações com nome nem dados ocultos.

**b) 1b:** **não.** `pilha` e `topo` são atributos `static` visíveis na classe inteira, e o `main` poderia manipulá-los direto. Há **abstração de processos** — as operações têm nome e interface —, mas **não abstração de dados**, porque a representação não está oculta.

**c) 1c:** **não é possível** acessar `vetPilha`, que é `private`. E **não é preciso mudar o `main`**, que depende só da interface pública (`Pilha()`, `push`, `pop`). Isso é **abstração de dados / encapsulamento**: a representação está oculta, e o cliente só usa as operações.

**d) 1d:** **nenhuma mudança** foi necessária — os dois `main` são idênticos ([p.16](../01%20-%20Slides%20Originais/README.md#página-16)). Isso mostra que a **interface do TDA independe da representação** ([p.20](../01%20-%20Slides%20Originais/README.md#página-20)): a implementação pode mudar (vetor → lista encadeada) sem afetar os clientes. Na prática, é **baixo acoplamento** entre o `main` e a `Pilha`.

## E8

<!-- teste: entrada="1\n2\n3\n4\n5" saida-contem="1\n2\n3\n4\n5" -->
```java
import java.util.Scanner;

class Fila {
    private int[] dados = new int[5];
    private int inicio = 0;      // posição do primeiro elemento
    private int fim = 0;         // próxima posição livre
    private int quantidade = 0;

    public void enfileirar(int n) {
        if (quantidade == dados.length) {
            System.out.println("Erro - fila cheia");
            return;
        }
        dados[fim] = n;
        fim = (fim + 1) % dados.length;          // circular: volta ao 0 depois do último
        quantidade++;
    }

    public int desenfileirar() {
        if (quantidade == 0) {
            System.out.println("Erro - fila vazia");
            return -1;
        }
        int n = dados[inicio];
        inicio = (inicio + 1) % dados.length;
        quantidade--;
        return n;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Fila fila = new Fila();
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            fila.enfileirar(Integer.parseInt(input.nextLine()));
        }
        for (int i = 0; i < 5; i++) {
            int elemento = fila.desenfileirar();
            if (elemento != -1) System.out.println(elemento);
        }
    }
}
```

**Raciocínio:**

- O **vetor circular** usa o operador `%` para que `inicio` e `fim` "deem a volta", reaproveitando as posições liberadas.
- O atributo `quantidade` distingue fila cheia de fila vazia, casos em que `inicio == fim`.
- Os atributos são `private`, então o `main` só usa `enfileirar` e `desenfileirar`, como na pilha 1c.
- **Saída:** 1, 2, 3, 4, 5 — a mesma ordem de entrada (FIFO), enquanto a pilha inverte (LIFO).

## E9

- **O destrutor** só roda quando o objeto `Pilha` é destruído (`delete p1`) e libera os nós **que ainda estão** na pilha.
- **O `pop`** retira um nó da lista. Sem `delete` nesse nó, ele ficaria no heap **sem nenhum ponteiro** para ele: o destrutor não o alcançaria, porque não está mais na lista, e o programa perderia a memória para sempre. Isso é um **vazamento de memória** (*memory leak*).
- **Em Java**, o nó retirado também fica sem referência, mas o **coletor de lixo** o encontra e libera automaticamente ([p.28](../01%20-%20Slides%20Originais/README.md#página-28)).

## E10

**Problema:** o valor −1 é um elemento legítimo. Se o usuário empilhar −1, o `main` acha que a pilha está vazia e deixa de imprimi-lo. Além disso, nada obriga o cliente a verificar o −1.

<!-- teste: entrada="-1\n2\n3" saida-contem="3\n2\n-1\nPilha vazia: Pilha vazia" -->
```java
import java.util.Scanner;

class Pilha {
    private int[] vetPilha = new int[5];
    private int topo = 0;

    public void push(int n) {
        if (topo == vetPilha.length) throw new IllegalStateException("Pilha cheia");
        vetPilha[topo++] = n;
    }

    public int pop() {
        if (topo == 0) throw new IllegalStateException("Pilha vazia");
        return vetPilha[--topo];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Pilha pilha = new Pilha();
        for (int i = 0; i < 3; i++) pilha.push(Integer.parseInt(input.nextLine()));
        try {
            for (int i = 0; i < 4; i++) {          // uma vez a mais, de propósito
                System.out.println(pilha.pop());   // -1 agora é um valor como outro qualquer
            }
        } catch (IllegalStateException e) {
            System.out.println("Pilha vazia: " + e.getMessage());
        }
    }
}
```

Com exceção, o erro sai do **canal de dados** (o `return`) e passa a um **canal de erro** separado. O valor −1 volta a ser um elemento válido.

## E11

Sem inicialização automática, o programador precisava **lembrar** de chamar algo como `inicializaPilha(&p)` antes de usar o pacote. Se esquecesse, o topo começava com lixo. Sem finalização automática, precisava lembrar de chamar `liberaPilha(&p)`, ou haveria vazamento de memória.

- **Construtor:** é chamado **automaticamente** na criação (`new Pilha()`), garantindo que todo objeto nasce em estado válido (`topo = 0` ou `NULL`).
- **Destrutor (C++):** é chamado **automaticamente** quando o objeto é destruído (`delete`, ou o fim do escopo de um objeto local), liberando os recursos.
- **Coleta de lixo (Java):** cuida da memória.

Em todos os casos, a responsabilidade sai do cliente e vai para a própria classe — mais confiabilidade.


<!-- nav:rodape -->

---

**Aula 12:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-12.md) · [Exercícios](../03%20-%20Exercícios/exercicios-aula-12.md) · **Resoluções** · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 11 · Resoluções](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md) · [Aula 13 · Resoluções](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md) →

**Links para esta página (3):** [Aula 12 · Exercícios](../03%20-%20Exercícios/exercicios-aula-12.md) · [Aula 12 · visão geral](../README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
