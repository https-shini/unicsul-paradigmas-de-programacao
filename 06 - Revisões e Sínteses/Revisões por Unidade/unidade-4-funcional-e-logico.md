# Revisão da Unidade 4 — Paradigmas funcional e lógico (Aulas 14–15)

> **[Explicação elaborada]** Agrupamento organizacional deste repositório, **não** uma divisão oficial do professor. É a unidade mais cobrada nas listas: a Lista 01 é quase toda sobre ela. Legenda: [Convenções](../../README.md#convenções-de-marcação).

| Aula | Tema | Resumo | Exercícios |
| --- | --- | --- | --- |
| 14 | Paradigma funcional com Clojure | [resumo](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) | [exercícios](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/03%20-%20Exercícios/exercicios-aula-14.md) |
| 15 | Paradigma lógico com Prolog | [resumo](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) | [exercícios](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/03%20-%20Exercícios/exercicios-aula-15.md) |

## Conceitos que você precisa dominar

**Funcional (14)**
- [ ] Origem: funções matemáticas, Backus e a crítica ao estilo de von Neumann
- [ ] Características do modelo puro: sem variáveis mutáveis, atribuição ou laços; sem efeitos colaterais; recursão
- [ ] Linguagens **puras** (Haskell, Miranda) × **impuras** (LISP, Scheme, Clojure, Elixir, Erlang)
- [ ] O que uma linguagem funcional pura fornece: funções primitivas, formas funcionais, aplicação e estruturas de dados
- [ ] Clojure: notação **prefixa**, `+ - * /`, `quot`, `rem`, tipo `Ratio`, `def`, `read`, `println`, comparações e predicados (`zero?`, `even?`, `odd?`)
- [ ] Avaliar e escrever expressões aninhadas

**Lógico (15)**
- [ ] Abordagem **procedural × declarativa** e a classificação do professor
- [ ] Lógica **proposicional** (proposições, conectivos ¬ ∧ ∨ → ↔) e de **predicados** de primeira ordem (quantificadores ∀ ∃)
- [ ] Prolog: **termos**, **fatos**, **regras**, **consultas**
- [ ] **Unificação** e variáveis (maiúsculas) × constantes (minúsculas)
- [ ] `findall/3`, leitura com `read/1`, saída com `write`/`nl`, condicional `->`

## Confusões frequentes

| Confusão | Esclarecimento |
| --- | --- |
| `(/ 10 4)` dá `2` em Clojure | Na JVM, dá `5/2` (`Ratio`). Quociente inteiro: `quot`. |
| Escrever `(+ 1 2 3)` como `1 + 2 + 3` | Clojure é **prefixa**: o operador vem primeiro e aceita vários argumentos. |
| Em Prolog, `Joao` é uma constante | Iniciais **maiúsculas** são **variáveis**; constantes começam com minúscula: `joao`. |
| `X = 2 + 3` faz `X` valer 5 | `=` **unifica**: `X` fica ligado ao termo `2+3`. Para calcular: `X is 2 + 3`. |
| Prolog responde `false` = "é mentira" | `false` significa "**não foi possível provar** com a base atual" (mundo fechado). |
| Funcional é declarativo para o professor | Na Aula15 p.3–5, o professor o classifica como **procedural**; a literatura diverge (ver [erratas](../erratas-e-inconsistencias.md)). |

## Autoteste

1. Avalie de dentro para fora: `(* (+ 2 3) (- 10 (quot 9 2)))`. → [Aula 14, §7](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#7-sintaxe-prefixada-e-funções-primitivas-de-clojure-p1321)
2. Por que a ausência de efeitos colaterais facilita o paralelismo? → [Aula 14, §8](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#8-funcional--imperativo--quadro-resumo)
3. Escreva a regra `avo(X, Z)` a partir de `pai/2` e faça a consulta "quem são os netos de João?". → [Aula 15, §8](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#8-exemplos-e-atividades-p1923)
4. Traduza para lógica de predicados: "todo aluno que estuda é aprovado". → [Aula 15, §5](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#5-lógica-de-predicados-de-primeira-ordem-p1112)

**Questões do professor sobre esta unidade:** [Lista 01 inteira](../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/README.md) · [Lista 02, Q12](../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md).

**Anterior:** [Unidade 3](unidade-3-orientacao-a-objetos.md) · **Visão geral:** [Resumo geral da disciplina](../resumo-geral-da-disciplina.md).
