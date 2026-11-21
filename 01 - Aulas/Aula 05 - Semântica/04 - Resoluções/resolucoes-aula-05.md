# Aula 05 — Semântica · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-05.md`](../03%20-%20Exercícios/exercicios-aula-05.md). Os códigos do E7 e do E10 foram executados (gcc e perl).

## E1

Nome, endereço (l-value), valor (r-value), tipo, escopo e tempo de vida (p.6).

## E2

A sintaxe é descrita com **BNF**, notação adotada desde o Algol. A semântica envolve **significado**, que é muito mais difícil de formalizar. Existem várias abordagens — informal, semiformal (tradução dirigida pela sintaxe) e formal (operacional, denotacional, axiomática) —, e nenhuma se tornou padrão. Cada linguagem explica a sua de um jeito (p.3–4).

## E3

**Resposta: d.** O valor do índice só é conhecido durante a execução. Já um índice constante, como `v[100]` com `v` de tamanho conhecido, poderia em tese ser detectado em compilação.

## E4

`total = total + parcela;`

- **À esquerda do `=`:** `total` é **l-value** — interessa seu endereço, onde o resultado será gravado.
- **À direita:** `total` é **r-value** — interessa seu valor atual, que entra na soma. `parcela` também é r-value.

## E5

- **Mesmo identificador, posições diferentes:** uma variável local `i` declarada em uma função recursiva. Cada chamada cria um novo `i` na pilha, em endereço diferente. Ou: a mesma função chamada duas vezes em momentos diferentes pode ter suas locais em posições distintas.
- **Variáveis diferentes, mesmo endereço (aliasing):** em C++, `int x = 5; int &r = x;` — `r` e `x` são dois nomes para a mesma célula. Em Java, `p2 = p1` entre objetos faz `p1` e `p2` apontarem para o mesmo objeto (Aula 08).

## E6

**Escopo** é *onde* (em que comandos) a variável pode ser acessada; **tempo de vida** é *quando* (por quanto tempo) ela existe na memória.

Situações em que não coincidem:

1. **Chamada de função:** durante `main → f()`, as locais de `main` estão vivas, mas fora do escopo de `f`.
2. **`static` local em C:** escopo restrito à função, mas tempo de vida igual ao do programa.
3. **[Complemento]** Objetos alocados com `new`: continuam vivos depois que a variável que os referenciava sai de escopo — até `delete` (C++) ou a coleta de lixo (Java).

## E7

<!-- teste: saida-contem="10\n20\n10" -->
```c
#include <stdio.h>
int n = 10;

void f(void) {
    printf("%d\n", n);
}

void g(void) {
    int n = 20;
    f();
    printf("%d\n", n);
}

int main(void) {
    g();
    printf("%d\n", n);
    return 0;
}
```

**Saída:**

```text
10
20
10
```

1. `main` chama `g`.
2. `g` declara uma local `n = 20` e chama `f`.
3. Em `f`, `n` não é local. Pela regra do **escopo estático**, procura-se no ancestral **textual** de `f`, que é o nível global → `n = 10`. Imprime **10**.
4. De volta a `g`, `n` é a local → imprime **20**.
5. Em `main`, `n` é a global → imprime **10**.

**Erro comum:** responder 20 na primeira linha, pensando que `f` "herda" o `n` de quem a chamou. Isso só acontece com escopo dinâmico.

## E8

Com **escopo dinâmico**, a busca do `n` não local de `f` segue a **ordem de chamada**: `f` foi chamada por `g`, que tem um `n = 20`. A saída seria:

```text
20
20
10
```

Só a primeira linha muda. Isso ilustra por que o escopo dinâmico prejudica a legibilidade: lendo apenas `f`, não dá para saber qual `n` será usado (p.12).

## E9

| Item | Classificação | Justificativa |
| --- | --- | --- |
| a) Método inexistente | Estática | O compilador consulta a classe e recusa |
| b) Divisão por variável zero | Dinâmica | Só se sabe em execução: com inteiros, `ArithmeticException`; com `double`, o resultado é `Infinity` ou `NaN`, sem exceção |
| c) `int x = 3.5;` | Estática | Erro de compilação: perda de precisão |
| d) `s.length()` com `s` valendo `null` | Dinâmica | `NullPointerException` em execução. O literal `null.length()` nem compila (`<null> cannot be dereferenced`) |
| e) Local não inicializada | Estática | Java exige atribuição definida antes do uso |

## E10

<!-- teste: saida-contem="dinamico (local): do chamador|estatico (my): global" -->
```perl
use strict;
use warnings;

our $x = "global";            # variável de pacote (global)

sub mostra { print "$x\n"; }  # $x não é local de mostra

sub com_local {
    local $x = "do chamador"; # escopo DINÂMICO: vale para quem for chamado daqui
    print "dinamico (local): ";
    mostra();
}

sub com_my {
    my $x = "do chamador";    # escopo ESTÁTICO (léxico): só existe neste bloco
    print "estatico (my): ";
    mostra();
}

com_local();   # imprime: do chamador
com_my();      # imprime: global
```

**Explicação:**

- `local` salva o valor da variável global e o substitui **durante a execução** de `com_local` e de **tudo o que ela chamar**; ao sair, o valor antigo volta. É escopo dinâmico: `mostra` enxerga `"do chamador"`.
- `my` cria uma variável **nova**, visível só no texto do bloco. `mostra` foi escrita fora dele, então continua vendo a global. É escopo estático.
- Confirma o slide: "Perl permite a declaração de variáveis com escopo dinâmico, embora o padrão seja estático" (p.12).

## E11

**Resposta-modelo:** a afirmação vale no sentido estrito: um **interpretador puro** não tem fase de compilação, então nada é verificado antes de executar. Três nuances, **[Complemento]**:

1. Linguagens **híbridas** (Java, C#) têm uma etapa de compilação para o código intermediário, e nela ocorre verificação estática.
2. Nem Python nem Perl são executados por interpretadores puros. O CPython compila o módulo inteiro para bytecode antes de rodar, e um `SyntaxError` na última linha impede a execução da primeira. O Perl compila o programa todo antes de executá-lo: com `use strict`, uma variável não declarada é recusada nessa fase ("Execution … aborted due to compilation errors"). Sebesta classifica a implementação do Perl como híbrida.
3. Mesmo em linguagens interpretadas existem **ferramentas externas** de análise estática — para Python, por exemplo, verificadores de tipo como o `mypy` e analisadores de estilo. Elas verificam o código sem executá-lo, mas não fazem parte da implementação da linguagem.

A afirmação vale para interpretadores puros; para as implementações reais de Python, Perl e PHP, ela é uma simplificação. Em prova, use a forma do professor (interpretada pura → verificação **dinâmica**) e, se houver espaço, acrescente a ressalva.
