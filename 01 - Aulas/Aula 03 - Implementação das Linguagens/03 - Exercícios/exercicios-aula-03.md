# Aula 03 — Implementação das Linguagens · Exercícios

> **[Exercício autoral]**, exceto o E9, que é a atividade original da p.17. Base: [`Aula03_Implementacao_LinguagensDeProgramacao.pdf`](../01%20-%20Slides%20Originais/Aula03_Implementacao_LinguagensDeProgramacao.pdf). Resoluções: [`resolucoes-aula-03.md`](../04%20-%20Resoluções/resolucoes-aula-03.md)

## Básico

**E1.** Quais são as três formas de implementação de uma linguagem? Dê dois exemplos de linguagem para cada uma, conforme os slides.

**E2.** (Objetiva) Em qual forma de implementação o programa é traduzido e executado **simultaneamente**, instrução por instrução?
a) Compilação  b) Interpretação pura  c) Híbrida  d) Montagem

**E3.** Diferencie **ambiente de programação** de **linguagem de programação**.

## Intermediário

**E4.** Ordene as fases de um compilador e diga o que cada uma produz: gerador de código, analisador sintático, gerador de código intermediário/analisador semântico, analisador léxico, otimização.

**E5.** Qual é o papel da **tabela de símbolos**? Por que ela é consultada por várias fases?

**E6.** Explique por que um programa Java compilado em Windows roda sem recompilação em Linux, enquanto um programa C precisa ser recompilado.

## Avançado

**E7.** Monte uma tabela comparando compilação, interpretação pura e híbrida quanto a velocidade, portabilidade, detecção antecipada de erros e facilidade de depuração. Justifique cada célula.

**E8.** Um colega afirma: "Python é interpretado, então nunca gera código intermediário". Avalie a afirmação, separando o que diz o slide do que acontece na implementação CPython.

## Prática

**E9 — Atividade da p.17 (original).** Implemente um programa que leia dez números e imprima a média, o maior e o menor. Faça em pelo menos duas linguagens de grupos diferentes, compare com Java e classifique cada linguagem quanto à forma de implementação.

## Aprofundamento

**E10.** Usando a figura de computadores virtuais em camadas (p.15), explique o que um programador Scheme "enxerga" ao programar e o que de fato acontece até chegar ao hardware.
