# Aula 15 — Paradigma Lógico · Exercícios

> **[Exercício autoral]**, exceto o E7 e o E8 (Atividades 1 e 2 originais, p.20 e p.23). Base: [`Aula15_Paradigma Lógico.pdf`](../01%20-%20Slides%20Originais/Aula15_Paradigma%20Lógico.pdf). Resoluções: [`resolucoes-aula-15.md`](../04%20-%20Resoluções/resolucoes-aula-15.md)

## Básico

**E1.** Diferencie a abordagem procedural da declarativa e classifique os quatro paradigmas segundo o professor.

**E2.** Quais são as três necessidades da lógica formal atendidas pela lógica simbólica?

**E3.** (Objetiva) Em Prolog, `pai(joao, ana).` escrito na base de conhecimento é:
a) uma consulta  b) um fato  c) uma regra  d) um quantificador

## Intermediário

**E4.** Complete a tabela-verdade de (P ∧ ¬Q) ⇒ P para todas as combinações de P e Q. É uma tautologia?

**E5.** Escreva em lógica de primeira ordem: (a) "Todo aluno estuda"; (b) "Existe um aluno que gosta de Prolog"; (c) "Todo pai de alguém é homem".

**E6.** Identifique o functor e os parâmetros de cada termo e diga se cada parâmetro é constante ou variável: (a) `gosta(joao, X)`; (b) `aula(plp, segunda, 19)`; (c) `pai(P, renata)`.

## Avançado

**E7 — Atividade 1 (original, p.20).** Com os fatos abaixo, escreva as consultas e as respostas esperadas: João é pai de Carlos? João é pai de Renata? Quem é o pai de Ana? Quem é o filho de Carlos?

```prolog
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).
```

**E8 — Atividade 2 (original, p.23).** Usando os mesmos fatos, crie um programa que leia dois nomes. Para o primeiro, mostre o pai (cada pessoa tem um único pai); para o segundo, mostre os filhos.

**E9.** Explique, passo a passo, como o Prolog responde à consulta `pai(X, maria).` usando unificação. E como responde a `pai(joao, X).`, pedindo todas as soluções?

## Aprofundamento

**E10.** (Programação) Usando **regras** (`:-`), defina `avo(A, N)` ("A é avô de N") e `irmao(X, Y)` ("X e Y têm o mesmo pai e são pessoas diferentes"). Teste: quem é neto de João? Quem são os irmãos de Ana?

**E11.** Por que `homem(pedro).` responde `false`, mesmo que no mundo real Pedro possa ser homem? Explique a hipótese do mundo fechado e o que significa "não há semântica intrínseca nos termos".
