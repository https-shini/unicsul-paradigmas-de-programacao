# Lista 01 — Revisão I ("Exercícios para treinar")

> **Original:** [`Aula16a_ExRevisao1.pdf`](01%20-%20Enunciado%20Original/Aula16a_ExRevisao1.pdf) (2 páginas). Lista de revisão disponibilizada pelo professor.
> **Resolução comentada:** [`resolucao-lista-01.md`](02%20-%20Resolução/resolucao-lista-01.md) — **[Resolução elaborada]**, não é gabarito oficial.

## Assuntos e aulas relacionadas

A lista é quase toda sobre os paradigmas **funcional** e **lógico**. As 11 questões são **discursivas**; uma pede código Clojure (Q7), uma pede a análise de expressões Clojure (Q6) e uma pede consultas Prolog (Q11).

| Questão | Assunto | Aulas |
| --- | --- | --- |
| Q1 | Procedural × declarativa; classificação dos paradigmas | [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#2-procedural--declarativa-p35) |
| Q2 | Imperativo × von Neumann; por que funcional e lógico se afastam | [09](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md#3-paradigma-imperativo-e-von-neumann-p7), [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#2-ponto-de-partida-o-que-já-sabemos-p36) |
| Q3 | Funcionais puras × impuras; efeitos colaterais | [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#4-puras--impuras-onde-o-funcional-aparece-p910) |
| Q4 | História do funcional; Clojure | [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#5-a-linguagem-clojure-p11) |
| Q5 | Os 4 componentes de uma funcional pura | [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#6-o-que-uma-linguagem-funcional-pura-fornece-p12-e-p22) |
| Q6 | Sintaxe prefixada; `/`, `quot`, `rem`; `not` | [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#7-sintaxe-prefixada-e-funções-primitivas-de-clojure-p1321) |
| Q7 | Programa Clojure com `def` | [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#73-leitura-de-valores-e-def-p1819) |
| Q8 | Estrutura do programa lógico; 3 necessidades da lógica formal | [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#3-fundamentos-lógica-simbólica-p67) |
| Q9 | Proposicional × 1ª ordem; quantificadores | [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#5-lógica-de-predicados-de-primeira-ordem-p1112) |
| Q10 | Termo composto; fatos × consultas | [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#7-proposições-termos-fatos-e-consultas-p1418) |
| Q11 | Consultas Prolog sobre `pai/2` | [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#8-exemplos-e-atividades-p1923) |

## Enunciados (transcrição fiel do original)

**[Material original]**

**Questão 1.** Explique a diferença fundamental entre as abordagens de programação procedural e declarativa, classificando os quatro principais paradigmas de programação (Imperativo, Orientado a Objetos, Funcional e Lógico) nessas duas categorias. Além disso, cite exemplos de linguagens declarativas que não são consideradas linguagens de programação.

**Questão 2.** Qual é a relação histórica e arquitetural entre as linguagens imperativas e a arquitetura de von Neumann? Explique por que os paradigmas Funcional e Lógico se distanciam desse modelo.

**Questão 3.** No contexto do Paradigma Funcional, diferencie linguagens funcionais "puras" de "impuras", explicando o conceito de efeitos colaterais e citando pelo menos dois exemplos de linguagens para cada classificação.

**Questão 4.** Apresente o contexto histórico do surgimento da programação funcional e descreva as principais características da linguagem Clojure, mencionando sua origem, ambiente de execução padrão e exemplos de adoção no mercado corporativo.

**Questão 5.** De acordo com a teoria do paradigma funcional, quais são os quatro componentes essenciais que uma linguagem funcional pura deve fornecer?

**Questão 6.** Analise a sintaxe prefixada e as funções primitivas da linguagem Clojure. Explique o comportamento e o resultado esperado para as seguintes expressões:
a) `(/ 10 3)` versus `(quot 10 3)` e `(rem 10 3)`\
b) `(not (= x 0))` e o motivo de sua utilização em Clojure.

**Questão 7.** Escreva um trecho de código em Clojure que leia dois valores numéricos informados pelo usuário, vincule-os aos símbolos x e y utilizando o comando `def`, e calcule e exiba na tela (em linhas separadas) o resultado das expressões matemáticas ((x + 2) \* y) / (10 \* (x + 8)) e (3 \* y)^2 - (x + y). Explique a vantagem de usar o comando `def` nesse cenário.

**Questão 8.** Explique como os programas são estruturados no Paradigma Lógico e quais são as três necessidades da lógica formal que a lógica simbólica atende.

**Questão 9.** Diferencie a Lógica Proposicional do Cálculo de Predicados de Primeira Ordem, destacando os elementos exclusivos deste último (predicados, variáveis e quantificadores) e exemplificando os quantificadores universal e existencial.

**Questão 10.** Na programação em Prolog, qual é a estrutura de um termo composto e como proposições atômicas são utilizadas para diferenciar "Fatos" de "Consultas"? Dê exemplos sintáticos de ambos.

**Questão 11.** Considere a seguinte base de fatos em Prolog:

```prolog
pai(joao, ana).
pai(joao, maria).
pai(joao, carlos).
pai(carlos, renata).
```

Escreva as consultas atômicas em Prolog necessárias para responder às seguintes perguntas e indique o retorno esperado do interpretador para cada uma:\
a) João é pai de Renata?\
b) Quem é o pai de Ana?\
c) Quem são os filhos de João?
