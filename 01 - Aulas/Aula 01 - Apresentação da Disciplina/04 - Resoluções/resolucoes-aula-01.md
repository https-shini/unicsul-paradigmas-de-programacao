# Aula 01 — Apresentação da Disciplina · Resoluções comentadas

> **[Resolução elaborada]** Soluções produzidas para estudo, não são gabarito oficial. Enunciados: [`exercicios-aula-01.md`](../03%20-%20Exercícios/exercicios-aula-01.md). Base: [`Aula01_Intro.pdf`](../01%20-%20Slides%20Originais/Aula01_Intro.pdf).

## E1

**Resposta:** imperativo, orientado a objetos, funcional e lógico (p.3 e p.5).

**Raciocínio:** a ementa os cita nominalmente ("paradigma imperativo", "orientação a objetos", "paradigma funcional", "paradigma baseado em lógica"). A Aula 02 confirma a mesma lista de quatro.

## E2

**Resposta:** A1 = Prova Regimental (5,0). A2 = Avaliação Parcial (3,0) + Exercícios (2,0) = 5,0. Nota final = A1 + A2, máximo 10,0 (p.6).

## E3

**Resposta:** 75%. Frequência inferior a 75% reprova, independentemente das notas (p.7).

## E4

**Resposta-modelo (uma de muitas possíveis):**

- **Cognitivo:** ao ver um trecho com `class`, `extends` e métodos sobrescritos, identificar que são construtos do paradigma OO (herança e polimorfismo).
- **Habilidades:** escrever o mesmo programa (ex.: "o dobro de n1 é igual a n2?") em Pascal, Java e Prolog, como na Aula 02.
- **Atitudes:** justificar a escolha de Prolog para um sistema baseado em regras ou de uma linguagem imperativa para um sistema embarcado com restrição de memória.

**Comentário:** a resposta precisa usar os verbos dos objetivos — reconhecer, construir, decidir.

## E5

Regras (p.7): A1 + A2 ≥ 6,0 aprova; menos de 1,0 em A1 **ou** A2 reprova sem AF; nos demais casos, AF.

| Aluno | A1 + A2 | Situação | Por quê |
| --- | --- | --- | --- |
| a | 6,5 | **Aprovado** | Soma ≥ 6,0 |
| b | 4,5 | **Reprovado sem AF** | A2 = 0,5 < 1,0 |
| c | 4,5 | **AF** | Soma < 6,0, ambas ≥ 1,0 |
| d | 5,7 | **Reprovado sem AF** | A1 = 0,8 < 1,0, mesmo com soma alta |

**Erro comum:** achar que o aluno d, com 5,7, "quase passou" e pode fazer AF. A regra do 1 ponto vem antes da AF.

## E6

A AF substitui a **menor** nota; a aprovação exige AF + maior nota ≥ 6,0.

- **Aluno c:** maior nota = 2,5 → AF ≥ 6,0 − 2,5 = **3,5**.

## E7

**Resposta:** sim. As duas notas são ≥ 1,0, então ele tem direito à AF. A maior nota é 1,0, logo AF ≥ 6,0 − 1,0 = **5,0** — ele precisa da nota máxima na AF.

**Generalização:** a nota mínima de AF é 6,0 − max(A1, A2). Como a AF vale no máximo 5,0, só há chance se max(A1, A2) ≥ 1,0, o que a regra do 1 ponto já garante.

## E8

**Resposta-modelo:** os verbos indicam profundidade decrescente, e o cronograma confirma: imperativo tem 3 aulas (09, 10, 11) mais o artigo de Dijkstra; OO tem 2 (12, 13); funcional e lógico têm 1 cada (14, 15). Além disso, as Aulas 04–08 (sintaxe, semântica, tipos, ponteiros) usam quase só exemplos imperativos.

**O que sugere sobre a prova:** o imperativo e os fundamentos devem ser cobrados com mais detalhe (passagem de parâmetros, escopo, tipagem). Funcional e lógico tendem a ser cobrados em nível conceitual e em pequenos trechos de código (Clojure e Prolog), como mostram as [listas de revisão](../../../02%20-%20Listas%20de%20Exercícios/README.md).

> **[Atenção]** Essa é uma inferência a partir do material, não uma informação do professor sobre a prova.

## E9

| Obra | Aula relacionada | Relação |
| --- | --- | --- |
| Dijkstra, *Go To Statement Considered Harmful* | 09 | Fundamento da programação estruturada; o artigo é material da aula ([`Aula09a`](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf)) |
| Eck, *Introduction to Programming Using Java* | 12–13 | Java é a linguagem principal dos exemplos de OO |
| Dybvig, *The Scheme Programming Language* | 14 | Scheme é um dialeto de LISP, como Clojure, usado na aula |
| Normark, *Functional Programming in Scheme* | 14 | Programação funcional |
| Endriss, *An Introduction to Prolog Programming* | 15 | Prolog é a linguagem do paradigma lógico |
