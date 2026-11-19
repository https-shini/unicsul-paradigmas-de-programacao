# Aula 06 — Sistema de Tipos · Exercícios

> **[Exercício autoral]**, exceto o E9, que é a atividade original da p.20. Base: [`Aula06_Tipos.pdf`](../01%20-%20Slides%20Originais/Aula06_Tipos.pdf). Resoluções: [`resolucoes-aula-06.md`](../04%20-%20Resoluções/resolucoes-aula-06.md)

## Básico

**E1.** Defina tipo de dado, sistema de tipos e erro de tipo.

**E2.** Diferencie tipos primitivos de tipos compostos e dê dois exemplos de cada.

**E3.** (Objetiva) Em qual linguagem o tamanho de cada tipo primitivo é **fixado pela própria linguagem**, segundo a aula?
a) C  b) C++  c) Pascal  d) Java

## Intermediário

**E4.** Classifique cada linguagem quanto à tipagem (estática ou dinâmica): Ada, PHP, C++, JavaScript, Java, Perl.

**E5.** Explique cada linha do quadro comparativo estática × dinâmica (p.14), justificando por que a estática é mais rápida e a dinâmica é mais simples de escrever.

**E6.** Quais são os dois critérios principais que tornam uma linguagem "fracamente tipada", segundo a p.21? Explique por que cada um enfraquece a tipagem.

## Avançado

**E7.** (Interpretação de código) Qual é a saída de cada trecho? Algum não compila?

a) C: `double y = 2.6; int x = y; printf("%d", x);`
b) Java: `double y = 2.6; int x = y; System.out.println(x);`
c) Java: `double y = 2.6; int x = (int) y; System.out.println(x);`
d) C: `printf("%d %f", 7 / 2, 7.0 / 2);`

**E8.** "Python é dinamicamente tipada, logo é fracamente tipada." A afirmação está correta? Justifique com um exemplo e monte a tabela 2×2 estática/dinâmica × forte/fraca.

**E9 — Atividade da p.20 (original).** Crie um programa em C e outro em Python que apresentem as mesmas informações do programa PHP da p.19 (`$x = 10; $y = "20"; $w = 10.2;` e a soma). Compare os resultados das três linguagens: qual tem a tipagem mais fraca e qual tem a mais forte?

**E10.** Explique o que o compilador faz com `int a; float b, c; c = a + b;` e por que essa operação não pode ser executada diretamente pelo processador.

## Aprofundamento

**E11.** O slide classifica Perl como fortemente tipada. Usando o critério da p.21 e um exemplo, argumente contra e a favor dessa classificação.

**E12.** (Programação) Escreva um programa em C que demonstre que `sizeof(long)` depende do compilador e da plataforma. Explique como isso se relaciona com a frase "o tamanho mínimo é definido pela linguagem e o tamanho a ser usado é definido pelo desenvolvedor do compilador".
