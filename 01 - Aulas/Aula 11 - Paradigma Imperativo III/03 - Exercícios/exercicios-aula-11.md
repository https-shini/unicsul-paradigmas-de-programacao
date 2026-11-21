<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 11](../README.md) › [03 - Exercícios](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 11 — Paradigma Imperativo III · Exercícios

> **[Exercício autoral]**, exceto o E8 (Atividade 1 original, [p.21](../01%20-%20Slides%20Originais/README.md#página-21)). Base: [`Aula11_ParadigmaImperativo3.pdf`](../01%20-%20Slides%20Originais/Aula11_ParadigmaImperativo3.pdf). Resoluções: [`resolucoes-aula-11.md`](../04%20-%20Resoluções/resolucoes-aula-11.md)

## Básico

**E1.** Diferencie procedimento de função e dê um exemplo de cabeçalho de cada um em C++ e em Pascal.

**E2.** Liste as quatro características de um subprograma apresentadas na [p.4](../01%20-%20Slides%20Originais/README.md#página-4).

**E3.** (Objetiva) Em C#, qual modificador **obriga** o método a atribuir um valor ao parâmetro?
a) `ref`  b) `in`  c) `out`  d) `ref readonly`

## Intermediário

**E4.** Diferencie parâmetro formal de parâmetro real. Na chamada `elevado(base, expo)` e no cabeçalho `int elevado(int x, int y = 2)`, identifique cada um.

**E5.** Por que parâmetros com valor padrão devem ser os últimos da lista? Por que parâmetros nomeados resolvem o problema de funções como `MLPClassifier`?

**E6.** Monte uma tabela com os quatro modelos de passagem indicando, para cada um, a direção (entrada/saída), se há cópia e o principal risco ou custo.

## Avançado

**E7.** (Interpretação de código) Considere o procedimento abaixo, em pseudocódigo, chamado com `p(a, a)` e `a = 2`:

```text
procedimento p(x, y):
    x = x + 1
    y = y * 10
```

Qual é o valor final de `a` se a passagem for: (a) por valor; (b) por referência; (c) por valor-resultado, copiando de volta primeiro `x` e depois `y`?

**E8 — Atividade 1 (original, [p.21](../01%20-%20Slides%20Originais/README.md#página-21)).** Crie um programa em C# com três funções `void`: a primeira lê dois inteiros, a segunda inverte a ordem dos dois valores e a terceira os imprime. Todo parâmetro deve ter algum modificador. Descreva a forma de passagem usada em cada função.

**E9.** (Programação) Implemente em C++ a mesma lógica do E8 usando referências (`int&`) e referências constantes (`const int&`). Relacione cada parâmetro com um modificador C#.

## Aprofundamento

**E10.** Por que o acesso a dados por referência é "mais lento", se a passagem é mais rápida? Explique o que é indireção.

**E11.** A recapitulação ([p.20](../01%20-%20Slides%20Originais/README.md#página-20)) afirma que aspectos da programação imperativa "prevalecem na maioria das linguagens, inclusive nas OO". Mostre isso apontando, num método Java qualquer, os quatro conceitos principais do imperativo.


<!-- nav:rodape -->

---

**Aula 11:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-11.md) · **Exercícios** · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-11.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 10 · Exercícios](../../Aula%2010%20-%20Paradigma%20Imperativo%20II/03%20-%20Exercícios/exercicios-aula-10.md) · [Aula 12 · Exercícios](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/03%20-%20Exercícios/exercicios-aula-12.md) →

**Links para esta página (4):** [Aula 11 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-11.md) · [Aula 11 · visão geral](../README.md) · [Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-2-imperativo.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
