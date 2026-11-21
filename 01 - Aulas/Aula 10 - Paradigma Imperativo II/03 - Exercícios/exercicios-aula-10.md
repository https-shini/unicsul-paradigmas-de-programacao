<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 10](../README.md) › [03 - Exercícios](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 10 — Paradigma Imperativo II · Exercícios

> **[Exercício autoral]**, exceto o E7 e o E8 (exercício e Atividade 1 originais, [p.19](../01%20-%20Slides%20Originais/README.md#página-19) e [p.20](../01%20-%20Slides%20Originais/README.md#página-20)). Base: [`Aula10_ParadigmaImperativo2.pdf`](../01%20-%20Slides%20Originais/Aula10_ParadigmaImperativo2.pdf). Resoluções: [`resolucoes-aula-10.md`](../04%20-%20Resoluções/resolucoes-aula-10.md)

## Básico

**E1.** Defina abstração e abstração procedural.

**E2.** Quais são os três passos do processo de abstração procedural?

**E3.** (Objetiva) Segundo a aula, a abstração de dados é característica de qual paradigma?
a) Imperativo  b) Orientado a objetos  c) Funcional  d) Lógico

## Intermediário

**E4.** Defina acoplamento e coesão. Qual combinação é desejável? Por que variáveis globais são prejudiciais?

**E5.** Liste as cinco características de um tipo abstrato de dados apresentadas na [p.18](../01%20-%20Slides%20Originais/README.md#página-18).

**E6.** No exemplo de ordenação, por que `encontrarMenor` devolve a **posição** do menor elemento e não o **valor**? O que aconteceria com `trocarElementos` se ela devolvesse o valor?

## Avançado

**E7 — Exercício da [p.19](../01%20-%20Slides%20Originais/README.md#página-19) (original).** Em C, leia 10 notas inteiras (0 a 100) num vetor, exiba-as, inverta o próprio vetor (sem vetor auxiliar) e exiba de novo. O `main` deve apenas chamar `lerVetor`, `mostrarVetor` e `inverterVetor`, e `inverterVetor` deve delegar a troca a `trocarElementos`.

**E8 — Atividade 1 da [p.20](../01%20-%20Slides%20Originais/README.md#página-20) (original).** Leia `n` (total de elementos) e `p` (elementos agrupados) e calcule a quantidade de arranjos e combinações, usando abstração procedural, sem Java e sem recursos de OO.

**E9.** Aplique os três passos da abstração procedural ao problema "calcular a média das notas de uma turma e listar os alunos acima da média". Desenhe a hierarquia de funções com entradas e saídas.

## Aprofundamento

**E10.** O slide diz que a legibilidade e a manutenibilidade "foram melhoradas significativamente com a OO". Usando os conceitos de acoplamento, coesão e TDA, explique o que a OO acrescenta à abstração procedural.

**E11.** No E8, a partir de qual valor de `n` o cálculo de `n!` com `int` (32 bits) estoura? Proponha uma forma de calcular C(n, p) que evite calcular fatoriais enormes.


<!-- nav:rodape -->

---

**Aula 10:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-10.md) · **Exercícios** · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-10.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 09 · Exercícios](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/03%20-%20Exercícios/exercicios-aula-09.md) · [Aula 11 · Exercícios](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/03%20-%20Exercícios/exercicios-aula-11.md) →

**Links para esta página (4):** [Aula 10 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-10.md) · [Aula 10 · visão geral](../README.md) · [Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-2-imperativo.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
