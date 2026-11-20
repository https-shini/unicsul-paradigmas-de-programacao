# Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01–08)

> **[Explicação elaborada]** Agrupamento organizacional deste repositório, **não** uma divisão oficial do professor. Legenda: [Convenções](../../README.md#convenções-de-marcação).

| Aula | Tema | Resumo | Exercícios |
| --- | --- | --- | --- |
| 01 | Plano de ensino | [resumo](../../01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/02%20-%20Resumo%20Teórico/resumo-aula-01.md) | [exercícios](../../01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/03%20-%20Exercícios/exercicios-aula-01.md) |
| 02 | Evolução e paradigmas | [resumo](../../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md) | [exercícios](../../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/03%20-%20Exercícios/exercicios-aula-02.md) |
| 03 | Implementação | [resumo](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) | [exercícios](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/03%20-%20Exercícios/exercicios-aula-03.md) |
| 04 | Sintaxe | [resumo](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) | [exercícios](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/03%20-%20Exercícios/exercicios-aula-04.md) |
| 05 | Semântica | [resumo](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) | [exercícios](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/03%20-%20Exercícios/exercicios-aula-05.md) |
| 06 | Sistema de tipos | [resumo](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) | [exercícios](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/03%20-%20Exercícios/exercicios-aula-06.md) |
| 07 | Tipos compostos | [resumo](../../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md) | [exercícios](../../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/03%20-%20Exercícios/exercicios-aula-07.md) |
| 08 | Ponteiros | [resumo](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) | [exercícios](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/03%20-%20Exercícios/exercicios-aula-08.md) |

## Conceitos que você precisa dominar

- [ ] Definição de **paradigma** e os quatro paradigmas, com uma linguagem de cada (02)
- [ ] **Critérios de avaliação**: legibilidade, facilidade de escrita, confiabilidade, custo (02)
- [ ] **Compilação × interpretação × híbrida**: vantagens, desvantagens, exemplos; papel do bytecode e da VM (03)
- [ ] **Sintaxe × semântica**; três níveis de sintaxe; **lexema, token, padrão**; os seis grupos de token de C (04)
- [ ] Regras de **nomes**: tamanho, caracteres, *case sensitivity*, palavras reservadas × palavras-chave (04)
- [ ] Os **seis atributos** da variável (05)
- [ ] **Escopo estático × dinâmico**, com exemplo de saída diferente (05)
- [ ] **Escopo × tempo de vida**; a variável local `static` (05)
- [ ] **Semântica estática × dinâmica** (05)
- [ ] **Tipagem estática × dinâmica** e **forte × fraca**, com uma linguagem em cada quadrante (06)
- [ ] **Coerção** e por que enfraquece a tipagem; **overflow** (06)
- [ ] **Enumeração, registro, matriz**: declaração e uso; fórmula de endereço *row-major* (07)
- [ ] **Ponteiro**: declaração, `&`, `*`; regiões de memória (08)
- [ ] **Alocação estática × dinâmica**; `new`/`delete` e `new[]`/`delete[]` (08)

## Confusões frequentes

| Confusão | Esclarecimento |
| --- | --- |
| "Estática" = "forte" | São eixos **independentes**: C é estática e fraca; Python é dinâmica e forte. |
| Escopo = tempo de vida | Escopo é **onde** o nome é visível; tempo de vida é **quando** a variável existe. |
| Erro léxico × erro sintático | `x = (y + 10 * z;` tem tokens válidos: o erro é **sintático**. |
| Java é interpretado | Java é **híbrido**: compilado para bytecode e executado pela JVM. |
| `new int(4)` cria um vetor | Cria **um** inteiro com valor 4. Vetor: `new int[4]`. |
| Palavra reservada = palavra-chave | Palavra reservada **não pode** ser usada como identificador; palavra-chave só tem significado especial em certos contextos. |

## Autoteste

Responda sem consultar; depois confira na seção indicada.

1. Explique por que um programa C compilado no Windows não roda no Linux, mas um `.class` roda em ambos. → [Aula 03, §3–5](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md#3-compilação-p89)
2. Liste os tokens de `soma = x + 10;` e classifique cada um. → [Aula 04, §5](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md#5-lexema-token-e-padrão-p89)
3. Dê um exemplo em que escopo estático e dinâmico produzem saídas diferentes. → [Aula 05, §4](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md#4-variável-e-seus-seis-atributos-p513)
4. Por que `10 + "20"` dá 30 em PHP e erro em Python? Classifique as duas linguagens. → [Aula 06, §6](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#6-força-de-tipagem-p1521)
5. Calcule o endereço de `m[1][3]` numa matriz `int m[4][5]` com base 2000 e `int` de 4 bytes. → [Aula 07, §6](../../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md#6-matrizes-p1012)
6. No Exemplo 4 da Aula 08, em que região fica cada variável? → [Aula 08, §5](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#5-alocação-estática--dinâmica-p1213)

**Questões do professor sobre esta unidade:** [Lista 02, Q2–Q6](../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md).

**Próxima unidade:** [Unidade 2 — Imperativo](unidade-2-imperativo.md).
