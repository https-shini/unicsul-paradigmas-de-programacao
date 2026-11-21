# Aula 14 — Paradigma Funcional · Exercícios

> **[Exercício autoral]**, exceto o E7 e o E8 (Atividades 1 e 2 originais, p.17 e p.20). Base: [`Aula14_ParadigmaFuncional.pdf`](../01%20-%20Slides%20Originais/Aula14_ParadigmaFuncional.pdf). Resoluções: [`resolucoes-aula-14.md`](../04%20-%20Resoluções/resolucoes-aula-14.md)

## Básico

**E1.** Em que década e por qual motivo surgiu a programação funcional? Qual foi a primeira linguagem funcional?

**E2.** Diferencie linguagens funcionais puras de impuras e cite dois exemplos de cada.

**E3.** (Objetiva) Qual é o resultado de `(quot 17 5)` em Clojure?
a) 3.4  b) 3  c) 2  d) 17/5

## Intermediário

**E4.** Quais são os quatro componentes que uma linguagem funcional pura deve fornecer?

**E5.** Converta para a notação prefixada de Clojure: (a) 4 · (x + 1); (b) (a − b) / (a + b); (c) x² + 2x + 1; (d) |y − 10|.

**E6.** Por que a ausência de efeitos colaterais torna os programas "mais legíveis e confiáveis"? Explique com um exemplo de função imperativa que tem efeito colateral.

## Avançado

**E7 — Atividade 1 (original, p.17).** Calcule o valor de cada expressão e escreva um programa Clojure que mostre os valores, um por linha: `(+ 2 10)`, `(- 20 7 4)`, `(* 5 2 3)`, `(/ 60 6 5)`, `(- 30 (* 3 4))`, `(Math/sqrt 9)`, `(Math/pow 4 2)`.

**E8 — Atividade 2 (original, p.20).** Crie um programa Clojure que leia x e y e mostre, um por linha: x + y − 10; x + 2·y; (x + 2)·y; (x + 2)·y / [10·(x + 8)]; (3·y)² − (x + y).

**E9.** (Interpretação de código) Qual é a saída, no Clojure da JVM?

```clojure
(println (/ 10 4))
(println (/ 10 5))
(println (float (/ 1 3)))
(println (rem -7 3))
(println (not (= 3 3.0)))
```

## Aprofundamento

**E10.** (Programação) Escreva em Clojure, **sem usar `def` dentro de laços nem atribuição**, uma função recursiva `fatorial` e uma versão com `reduce`. Compare com a versão imperativa da Aula 10.

**E11.** O slide diz que a OO "não é muito diferente do imperativo", porque as diferenças estão na organização e não nos comandos. Explique por que o mesmo **não** vale para o funcional.
