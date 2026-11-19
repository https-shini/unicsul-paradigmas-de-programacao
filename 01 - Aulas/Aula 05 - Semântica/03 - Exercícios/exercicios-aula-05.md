# Aula 05 — Semântica · Exercícios

> **[Exercício autoral]** Base: [`Aula05_Semantica.pdf`](../01%20-%20Slides%20Originais/Aula05_Semantica.pdf). Resoluções: [`resolucoes-aula-05.md`](../04%20-%20Resoluções/resolucoes-aula-05.md)

## Básico

**E1.** Liste os seis atributos de uma variável apresentados na aula.

**E2.** Por que se diz que a sintaxe tem uma notação universalmente aceita e a semântica não? Qual é essa notação?

**E3.** (Objetiva) A verificação de que um índice de vetor está dentro dos limites, quando o índice é lido do teclado, é:
a) léxica  b) sintática  c) semântica estática  d) semântica dinâmica

## Intermediário

**E4.** No comando `total = total + parcela;`, identifique onde `total` é usado como l-value e onde é usado como r-value.

**E5.** Explique as duas afirmações do slide sobre endereço: "um mesmo identificador pode representar diferentes posições de memória" e "diferentes variáveis podem indicar o mesmo endereço". Dê um exemplo para cada.

**E6.** Diferencie escopo de tempo de vida. Cite duas situações em que eles **não** coincidem.

## Avançado

**E7.** (Interpretação de código) Qual é a saída do programa C abaixo? Explique linha a linha.

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

**E8.** Suponha que a mesma estrutura do E7 fosse executada numa linguagem com **escopo dinâmico**. O que mudaria na saída? Justifique pela regra de busca.

**E9.** Classifique cada verificação como semântica estática ou dinâmica, considerando Java:
a) chamar um método inexistente; b) dividir por uma variável que vale zero; c) atribuir `3.5` a uma variável `int`; d) acessar `null.length()`; e) usar variável local não inicializada.

## Aprofundamento

**E10.** (Programação) Escreva um programa em Perl que demonstre, com a mesma função `mostra`, a diferença entre escopo estático (`my`) e dinâmico (`local`).

**E11.** O slide afirma que "por definição, não há verificação estática em linguagens interpretadas". Discuta essa afirmação considerando linguagens híbridas (Aula 03) e ferramentas como analisadores de código para Python.
