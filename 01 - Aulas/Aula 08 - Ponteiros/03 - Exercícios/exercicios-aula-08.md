# Aula 08 — Ponteiros · Exercícios

> **[Exercício autoral]**, exceto o E7, baseado no Exemplo 4 original (p.14). Base: [`Aula08_Ponteiros.pdf`](../01%20-%20Slides%20Originais/Aula08_Ponteiros.pdf). Resoluções: [`resolucoes-aula-08.md`](../04%20-%20Resoluções/resolucoes-aula-08.md)

## Básico

**E1.** O que é um ponteiro? Cite duas linguagens que permitem manipulá-los explicitamente e duas que os usam implicitamente.

**E2.** Diferencie alocação estática de dinâmica quanto ao momento em que ocorrem e à possibilidade de alterar o tamanho.

**E3.** (Objetiva) Em qual região de memória fica um objeto criado com `new` em Java ou C++?
a) Código  b) Estático  c) Pilha  d) Heap

## Intermediário

**E4.** (Interpretação de código) Qual é a saída?

```c
#include <stdio.h>
int main(void) {
    int a = 1, b = 2;
    int *p = &a;
    *p = *p + 10;
    p = &b;
    *p = *p * 3;
    printf("%d %d\n", a, b);
    return 0;
}
```

**E5.** (Interpretação de código) No Exemplo 1 (C#), o que seria impresso se `Metodo1` também fosse declarado com `ref` e chamado com `Metodo1(ref numero)`?

**E6.** No Exemplo 2 (Java), por que os elementos do vetor mudam entre a primeira e a segunda impressão, mas o tamanho percorrido não muda? O que aconteceria se `imprime` executasse `vet = new int[]{0,0,0,0,0};` antes do laço?

## Avançado

**E7.** O Exemplo 4 do slide usa `int* vetor = new int(4);`. Explique o erro, mostre a correção e indique, para cada variável (`n`, `res`, `a`, `b`, `x`, `y`, `*vetor`), em que região de memória ela fica.

**E8.** (Programação) Escreva em C uma função `void troca(int *a, int *b)` que troque os valores de duas variáveis do chamador. Explique por que `void troca(int a, int b)` não funcionaria.

**E9.** Considere a classe Java `Pessoa` do Exemplo 3. Escreva a sequência de comandos que deixa `p1.nome` igual a "Ana" e `p2.nome` igual a "Bia", usando **um único** `new`. É possível? Justifique.

## Aprofundamento

**E10.** (Programação) Em C, aloque dinamicamente um vetor cujo tamanho é lido do teclado, preencha-o, aumente seu tamanho em 50% com `realloc` e imprima tudo. Relacione com a frase do slide "alocação dinâmica: tamanho pode ser alterado".

**E11.** Por que "a utilização correta de ponteiros deixa o programa mais rápido" (p.3)? Dê um exemplo envolvendo a passagem de uma estrutura grande para uma função.
