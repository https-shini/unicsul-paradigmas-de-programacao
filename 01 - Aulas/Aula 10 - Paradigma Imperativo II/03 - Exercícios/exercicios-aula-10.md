# Aula 10 — Paradigma Imperativo II · Exercícios

> **[Exercício autoral]**, exceto o E7 e o E8 (exercício e Atividade 1 originais, p.19 e p.20). Base: [`Aula10_ParadigmaImperativo2.pdf`](../01%20-%20Slides%20Originais/Aula10_ParadigmaImperativo2.pdf). Resoluções: [`resolucoes-aula-10.md`](../04%20-%20Resoluções/resolucoes-aula-10.md)

## Básico

**E1.** Defina abstração e abstração procedural.

**E2.** Quais são os três passos do processo de abstração procedural?

**E3.** (Objetiva) Segundo a aula, a abstração de dados é característica de qual paradigma?
a) Imperativo  b) Orientado a objetos  c) Funcional  d) Lógico

## Intermediário

**E4.** Defina acoplamento e coesão. Qual combinação é desejável? Por que variáveis globais são prejudiciais?

**E5.** Liste as cinco características de um tipo abstrato de dados apresentadas na p.18.

**E6.** No exemplo de ordenação, por que `encontrarMenor` devolve a **posição** do menor elemento e não o **valor**? O que aconteceria com `trocarElementos` se ela devolvesse o valor?

## Avançado

**E7 — Exercício da p.19 (original).** Em C, leia 10 notas inteiras (0 a 100) num vetor, exiba-as, inverta o próprio vetor (sem vetor auxiliar) e exiba de novo. O `main` deve apenas chamar `lerVetor`, `mostrarVetor` e `inverterVetor`, e `inverterVetor` deve delegar a troca a `trocarElementos`.

**E8 — Atividade 1 da p.20 (original).** Leia `n` (total de elementos) e `p` (elementos agrupados) e calcule a quantidade de arranjos e combinações, usando abstração procedural, sem Java e sem recursos de OO.

**E9.** Aplique os três passos da abstração procedural ao problema "calcular a média das notas de uma turma e listar os alunos acima da média". Desenhe a hierarquia de funções com entradas e saídas.

## Aprofundamento

**E10.** O slide diz que a legibilidade e a manutenibilidade "foram melhoradas significativamente com a OO". Usando os conceitos de acoplamento, coesão e TDA, explique o que a OO acrescenta à abstração procedural.

**E11.** No E8, a partir de qual valor de `n` o cálculo de `n!` com `int` (32 bits) estoura? Proponha uma forma de calcular C(n, p) que evite calcular fatoriais enormes.
