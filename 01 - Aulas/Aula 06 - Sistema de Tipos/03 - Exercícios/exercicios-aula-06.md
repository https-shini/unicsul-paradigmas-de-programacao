<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 06](../README.md) › [03 - Exercícios](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 06 — Sistema de Tipos · Exercícios

> **[Exercício autoral]**, exceto o E9, que é a atividade original da [p.20](../01%20-%20Slides%20Originais/README.md#página-20). Base: [`Aula06_Tipos.pdf`](../01%20-%20Slides%20Originais/Aula06_Tipos.pdf). Resoluções: [`resolucoes-aula-06.md`](../04%20-%20Resoluções/resolucoes-aula-06.md)

## Básico

**E1.** Defina tipo de dado, sistema de tipos e erro de tipo.

**E2.** Diferencie tipos primitivos de tipos compostos e dê dois exemplos de cada.

**E3.** (Objetiva) Em qual linguagem o tamanho de cada tipo primitivo é **fixado pela própria linguagem**, segundo a aula?
a) C  b) C++  c) Pascal  d) Java

## Intermediário

**E4.** Classifique cada linguagem quanto à tipagem (estática ou dinâmica): Ada, PHP, C++, JavaScript, Java, Perl.

**E5.** Explique cada linha do quadro comparativo estática × dinâmica ([p.14](../01%20-%20Slides%20Originais/README.md#página-14)), justificando por que a estática é mais rápida e a dinâmica é mais simples de escrever.

**E6.** Quais são os dois critérios principais que tornam uma linguagem "fracamente tipada", segundo a [p.21](../01%20-%20Slides%20Originais/README.md#página-21)? Explique por que cada um enfraquece a tipagem.

## Avançado

**E7.** (Interpretação de código) Qual é a saída de cada trecho? Algum não compila?

a) C: `double y = 2.6; int x = y; printf("%d", x);`\
b) Java: `double y = 2.6; int x = y; System.out.println(x);`\
c) Java: `double y = 2.6; int x = (int) y; System.out.println(x);`\
d) C: `printf("%d %f", 7 / 2, 7.0 / 2);`

**E8.** "Python é dinamicamente tipada, logo é fracamente tipada." A afirmação está correta? Justifique com um exemplo e monte a tabela 2×2 estática/dinâmica × forte/fraca.

**E9 — Atividade da [p.20](../01%20-%20Slides%20Originais/README.md#página-20) (original).** Crie um programa em C e outro em Python que apresentem as mesmas informações do programa PHP da [p.19](../01%20-%20Slides%20Originais/README.md#página-19) (`$x = 10; $y = "20"; $w = 10.2;` e a soma). Compare os resultados das três linguagens: qual tem a tipagem mais fraca e qual tem a mais forte?

**E10.** Explique o que o compilador faz com `int a; float b, c; c = a + b;` e por que essa operação não pode ser executada diretamente pelo processador.

## Aprofundamento

**E11.** O slide classifica Perl como fortemente tipada. Usando o critério da [p.21](../01%20-%20Slides%20Originais/README.md#página-21) e um exemplo, argumente contra e a favor dessa classificação.

**E12.** (Programação) Escreva um programa em C que demonstre que `sizeof(long)` depende do compilador e da plataforma. Explique como isso se relaciona com a frase "o tamanho mínimo é definido pela linguagem e o tamanho a ser usado é definido pelo desenvolvedor do compilador".


<!-- nav:rodape -->

---

**Aula 06:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-06.md) · **Exercícios** · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-06.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 05 · Exercícios](../../Aula%2005%20-%20Semântica/03%20-%20Exercícios/exercicios-aula-05.md) · [Aula 07 · Exercícios](../../Aula%2007%20-%20Tipos%20Compostos/03%20-%20Exercícios/exercicios-aula-07.md) →

**Links para esta página (4):** [Aula 06 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-06.md) · [Aula 06 · visão geral](../README.md) · [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-1-fundamentos.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
