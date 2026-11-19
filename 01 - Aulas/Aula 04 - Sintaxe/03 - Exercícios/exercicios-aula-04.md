# Aula 04 — Sintaxe · Exercícios

> **[Exercício autoral]**, exceto o E8, que é o Exemplo 1 original (p.20). Base: [`Aula04_Sintaxe.pdf`](../01%20-%20Slides%20Originais/Aula04_Sintaxe.pdf). Resoluções: [`resolucoes-aula-04.md`](../04%20-%20Resoluções/resolucoes-aula-04.md)

## Básico

**E1.** Diferencie sintaxe de semântica, citando a definição de Sebesta usada na aula.

**E2.** Defina lexema, token e padrão.

**E3.** (Objetiva) Qual destes **não** é um método formal citado para definir a sintaxe de uma linguagem?
a) Expressões regulares  b) Autômatos finitos  c) Gramáticas livres de contexto  d) Fluxogramas

## Intermediário

**E4.** Classifique cada lexema do trecho abaixo em um dos seis grupos de tokens de C (p.9):

```c
for (i = 0; i < 10; i++) printf("%d", vet[i]);
```

**E5.** Para cada linha, diga se há erro **léxico**, **sintático** ou nenhum erro (considere C):

1. `total = preco * 1.5;`
2. `total = (preco * 1.5;`
3. `total = preco @ 2;`
4. `if x > 0 { y = 1; }`

**E6.** Explique a diferença entre palavra reservada e palavra-chave e dê um exemplo de por que palavras-chave podem prejudicar a legibilidade.

## Avançado

**E7.** Para a expressão `r = (a + b) * (c - d);`:
a) liste os tokens;
b) desenhe a árvore sintática abstrata;
c) explique por que os parênteses aparecem na sintaxe concreta e não na abstrata.

**E8 — Exemplo 1 (original, p.20).** Execute o programa três vezes e compare os resultados. O que cada linha imprime e por que uma delas muda?

**E9.** Em Perl, por que se escreve `$cidades[0]` e não `@cidades[0]` para obter um elemento do vetor `@cidades`? O que isso revela sobre o uso de símbolos nos nomes dessa linguagem?

## Aprofundamento

**E10.** (Programação) Escreva, em Python, um analisador léxico simples que receba uma linha de código C e imprima cada lexema com seu grupo de token (identificador, palavra reservada, constante, string, símbolo especial, operador). Teste com `soma = x + 10;`.

**E11.** Escreva uma gramática em BNF que gere comandos de atribuição da forma `id = expressão;`, em que a expressão pode ter `+`, `*` e parênteses, com `*` tendo precedência sobre `+`.
