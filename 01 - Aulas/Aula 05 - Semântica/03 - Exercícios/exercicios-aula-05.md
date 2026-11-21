<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 05](../README.md) › [03 - Exercícios](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

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
a) chamar um método inexistente; b) dividir por uma variável que vale zero; c) atribuir `3.5` a uma variável `int`; d) chamar `s.length()` quando `String s = null;`; e) usar variável local não inicializada.

## Aprofundamento

**E10.** (Programação) Escreva um programa em Perl que demonstre, com a mesma função `mostra`, a diferença entre escopo estático (`my`) e dinâmico (`local`).

**E11.** O slide afirma que "por definição, não há verificação estática em linguagens interpretadas". Discuta essa afirmação considerando linguagens híbridas (Aula 03) e ferramentas como analisadores de código para Python.


<!-- nav:rodape -->

---

**Aula 05:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-05.md) · **Exercícios** · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-05.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 04 · Exercícios](../../Aula%2004%20-%20Sintaxe/03%20-%20Exercícios/exercicios-aula-04.md) · [Aula 06 · Exercícios](../../Aula%2006%20-%20Sistema%20de%20Tipos/03%20-%20Exercícios/exercicios-aula-06.md) →

**Links para esta página (4):** [Aula 05 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-05.md) · [Aula 05 · visão geral](../README.md) · [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-1-fundamentos.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
