<!-- nav:topo -->
[Início](../../README.md) › [06 - Revisões e Sínteses](../README.md) › [Revisões por Unidade](README.md) · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)

> **[Explicação elaborada]** Agrupamento organizacional deste repositório, **não** uma divisão oficial do professor. Legenda: [Convenções](../../README.md#convenções-de-marcação).

| Aula | Tema | Resumo | Exercícios |
| --- | --- | --- | --- |
| 09 | Von Neumann, Turing-completude, `goto`, estruturada | [resumo](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [artigo de Dijkstra](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) | [exercícios](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/03%20-%20Exercícios/exercicios-aula-09.md) |
| 10 | Abstração procedural e de dados | [resumo](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) | [exercícios](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/03%20-%20Exercícios/exercicios-aula-10.md) |
| 11 | Subprogramas e passagem de parâmetros | [resumo](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md) | [exercícios](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/03%20-%20Exercícios/exercicios-aula-11.md) |

## Conceitos que você precisa dominar

- [ ] Arquitetura de **von Neumann** e por que o imperativo é sua abstração (09)
- [ ] Requisitos de **Turing-completude** de uma linguagem imperativa (09)
- [ ] **Variável, expressão, atribuição** e a forma `destino = expressão` (09)
- [ ] Programação **não estruturada** (`goto`) × **estruturada** (09)
- [ ] Argumento de **Dijkstra**: índices textuais e dinâmicos; papel de **Böhm e Jacopini** (09)
- [ ] **Abstração procedural**: refinamento sucessivo, vantagens e limitações (10)
- [ ] **Acoplamento** e **coesão**; por que a meta é baixo acoplamento e alta coesão (10)
- [ ] **Tipo abstrato de dados** e **encapsulamento** (10)
- [ ] **Subprograma**: cabeçalho, parâmetros formais × reais, procedimento × função (11)
- [ ] Os **quatro modelos de passagem** e sua semântica (entrada, saída, entrada e saída) (11)
- [ ] Modificadores de C#: `ref`, `out`, `in`, `ref readonly` (11)

## Confusões frequentes

| Confusão | Esclarecimento |
| --- | --- |
| "Dijkstra provou que o `goto` é dispensável" | A prova é de **Böhm e Jacopini (1966)**. Dijkstra argumentou que o `goto` prejudica a compreensão e deveria ser **abolido**. |
| "O slide diz que a abstração procedural não favorece a baixa coesão" | O correto é **alta** coesão (ver [erratas](../erratas-e-inconsistencias.md)). |
| Valor-resultado = referência | Ambos são entrada e saída, mas valor-resultado **copia** (o argumento só muda no retorno); referência usa o **endereço** (muda na hora). |
| `out` é "passagem por resultado" pura | Em C#, `out` tem a **semântica** de saída, mas é **implementado** por referência. |
| Abstração procedural = TDA | A procedural esconde **como se calcula**; o TDA esconde **como o dado é representado**. |

## Autoteste

1. Por que variáveis e atribuição são "abstrações de von Neumann"? → [Aula 09, §3](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md#3-paradigma-imperativo-e-von-neumann-p7)
2. Explique, com suas palavras, os índices textuais e dinâmicos do artigo de Dijkstra. → [resumo do artigo](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)
3. Decomponha "calcular a média das notas acima de 7" em três níveis de abstração procedural. → [Aula 10, §4](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md#4-exemplo-guiado-ordenar-dez-números-p814)
4. Por que variáveis globais aumentam o acoplamento? → [Aula 10, §6](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md#6-limitações-acoplamento-e-coesão-p16)
5. Que modelo de passagem é mais adequado para um vetor grande que a função só lê? Por quê? → [Aula 11, §5](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md#5-modelos-de-passagem-de-parâmetros-semânticos-e-de-implementação-p1318)

**Questões do professor sobre esta unidade:** [Lista 01, Q2](../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/README.md) · [Lista 02, Q7–Q9](../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md).

**Anterior:** [Unidade 1](unidade-1-fundamentos.md) · **Próxima:** [Unidade 3 — Orientação a objetos](unidade-3-orientacao-a-objetos.md).


<!-- nav:rodape -->

---

← [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](unidade-1-fundamentos.md) · [Revisão da Unidade 3 — Paradigma orientado a objetos (Aulas…](unidade-3-orientacao-a-objetos.md) →

**Links para esta página (5):** [Cronograma](../../00%20-%20Planejamento%20e%20Organização/cronograma.md) · [06 — Revisões e Sínteses](../README.md) · [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](unidade-1-fundamentos.md) · [Revisão da Unidade 3 — Paradigma orientado a objetos (Aulas…](unidade-3-orientacao-a-objetos.md) · [Guia de estudo para as avaliações](../guia-de-estudo-para-provas.md)

<!-- /nav:rodape -->
