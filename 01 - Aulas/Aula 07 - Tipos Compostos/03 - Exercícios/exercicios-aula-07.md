<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 07](../README.md) › [03 - Exercícios](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 07 — Tipos Compostos · Exercícios

> **[Exercício autoral]**, exceto o E8 e o E9, que são o exercício e o desafio originais ([p.14](../01%20-%20Slides%20Originais/README.md#página-14) e [p.16](../01%20-%20Slides%20Originais/README.md#página-16)). Base: [`Aula07_Tipos Compostos.pdf`](../01%20-%20Slides%20Originais/Aula07_Tipos%20Compostos.pdf). Resoluções: [`resolucoes-aula-07.md`](../04%20-%20Resoluções/resolucoes-aula-07.md)

## Básico

**E1.** Liste os quatro tipos compostos apresentados na aula e diga, para cada um, se os elementos são homogêneos ou heterogêneos e como são acessados.

**E2.** Quais são as duas vantagens das enumerações citadas no slide?

**E3.** (Objetiva) Em qual linguagem os índices de um vetor vão, por padrão, de 1 a N?
a) C  b) Java  c) Fortran  d) C++

## Intermediário

**E4.** Diferencie registro (estrutura) de classe. Por que o slide diz que Java "não suporta estruturas diretamente"?

**E5.** Para cada declaração, diga a linguagem, o número de dimensões e o número total de elementos:
a) `int m[2][2][2][2];`  b) `float x[10][20];`  c) `x : array[1..100] of integer;`  d) `char nome[30];`

**E6.** (Interpretação de código) Em C++, depois de `struct Pessoa p1, p2; ... p2 = p1; p1.idade = 99;`, quanto vale `p2.idade` se `p1.idade` valia 20 antes da atribuição? Justifique.

## Avançado

**E7.** Uma matriz C `float x[10][20]` começa no endereço 1000. Sabendo que cada `float` ocupa 4 bytes e que C armazena por linhas, em que endereço está `x[3][5]`? Mostre o cálculo.

**E8 — Exercício da [p.14](../01%20-%20Slides%20Originais/README.md#página-14) (original).** Elabore em Java um programa que leia as 3 notas dos 4 alunos em cada uma das 2 disciplinas do semestre, armazene-as em uma única matriz de `float` e apresente: (a) a média final de cada aluno em cada disciplina; (b) a média na primeira avaliação de cada aluno em todas as disciplinas.

**E9 — Desafio da [p.16](../01%20-%20Slides%20Originais/README.md#página-16) (original).** Altere o programa anterior para armazenar os dados de dois semestres (cada um com 2 disciplinas, 4 alunos e 3 avaliações) em uma única matriz.

## Aprofundamento

**E10.** Por que, em C, `char nome[10]` armazena no máximo 9 caracteres úteis? O que acontece se você copiar 10 letras para ele?

**E11.** Compare `enum` em C e em Java quanto à verificação de tipos. Qual das duas implementações torna a linguagem mais fortemente tipada, no sentido da Aula 06?


<!-- nav:rodape -->

---

**Aula 07:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-07.md) · **Exercícios** · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-07.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 06 · Exercícios](../../Aula%2006%20-%20Sistema%20de%20Tipos/03%20-%20Exercícios/exercicios-aula-06.md) · [Aula 08 · Exercícios](../../Aula%2008%20-%20Ponteiros/03%20-%20Exercícios/exercicios-aula-08.md) →

**Links para esta página (4):** [Aula 07 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-07.md) · [Aula 07 · visão geral](../README.md) · [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-1-fundamentos.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
