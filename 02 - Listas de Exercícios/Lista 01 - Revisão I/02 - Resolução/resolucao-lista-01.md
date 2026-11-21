# Lista 01 — Revisão I · Resolução comentada

> **[Resolução elaborada]** Resolução produzida para estudo. **Não é gabarito oficial do professor.** Enunciados: [README da lista](../README.md) · original: [`Aula16a_ExRevisao1.pdf`](../01%20-%20Enunciado%20Original/Aula16a_ExRevisao1.pdf).
> Cada questão traz: **assunto**, **conceitos necessários**, **resposta-modelo** com fonte (`AulaXX p.N`) e, quando pertinente, **erros comuns**. O código Clojure foi executado com nbb (ClojureScript) e o Prolog, com Tau-Prolog.

---

## Q1

**Assunto:** abordagens de programação. **Conceitos:** procedural, declarativo, os quatro paradigmas. **Fonte:** Aula15 p.3–5.

**Resposta-modelo:** a diferença fundamental está **no que o programador especifica**.

- Na abordagem **procedural**, ele descreve **os passos** — a sequência de ações — que levam à solução (o **como**).
- Na **declarativa**, descreve **o resultado desejado** ou o problema (o **o quê**), e um mecanismo da linguagem, como o algoritmo de inferência do Prolog, encontra a solução.

Pela classificação da disciplina, **imperativo, orientado a objetos e funcional são procedurais** — todos especificam os passos — e **o lógico é declarativo**. Exemplos de linguagens declarativas que **não** são linguagens de programação: **HTML, CSS e SQL**.

**[Atenção]** Muitos autores classificam o funcional como declarativo. Siga o slide; se quiser, mencione a divergência numa frase.

## Q2

**Assunto:** von Neumann e paradigmas. **Conceitos:** programa armazenado, atribuição, execução sequencial. **Fontes:** Aula02 p.10, p.15; Aula09 p.3–7; Aula11 p.20; Aula14 p.3–8.

**Resposta-modelo:**

- **Relação histórica:** o imperativo foi o **primeiro paradigma**, surgido na década de 1940 junto com os primeiros computadores, e é **baseado no modelo de von Neumann**.
- **Relação arquitetural:** na arquitetura de von Neumann, **programa e dados ficam na mesma memória**, e o processador **busca e executa uma instrução por vez**, alterando a memória **por meio de atribuições**. Os elementos do imperativo são abstrações diretas disso: **variáveis** = células de memória; **atribuição** = gravar na memória; **sequência** = execução instrução a instrução; **desvios** (`goto`, seleção, repetição) = alteração do fluxo. As linguagens imperativas foram projetadas para usar eficientemente essa arquitetura.
- **Por que funcional e lógico se afastam:** partem de **outras bases teóricas**, não do hardware.
  - O **funcional** modela a computação como **funções matemáticas** que mapeiam entradas em saídas. No modelo puro, não há variável (estado), atribuição nem laço — justamente os elementos que espelham a memória de von Neumann.
  - O **lógico** baseia-se no **cálculo de predicados**: o programa é um conjunto de proposições, e o resultado vem de **inferência lógica**, não de uma sequência de alterações de memória.

**[Material original]** Segundo a Aula02 (p.15), as linguagens são projetadas para a arquitetura de von Neumann, e as tentativas inversas (LISP e PROLOG) não deram certo. Por isso, essas linguagens rodam sobre hardware von Neumann, por meio de interpretadores ou compiladores.

## Q3

**Assunto:** funcionais puras e impuras. **Conceitos:** efeito colateral, estado. **Fonte:** Aula14 p.8–9.

**Resposta-modelo:**

- **Puras:** seguem o modelo funcional puro — **não aceitam variáveis** (controle de estado), **atribuição nem laços de repetição**. Exemplos: **Haskell** e **Miranda**.
- **Impuras:** são funcionais, mas **possuem variáveis, atribuição e laços**. Exemplos: **LISP, Scheme, Clojure, Elixir e Erlang**.
- **Efeito colateral** é qualquer alteração que uma função provoca **além de produzir seu resultado**: modificar uma variável global ou um parâmetro, escrever na tela ou num arquivo. No modelo puro **não há efeitos colaterais**, então o resultado de uma função depende só dos seus argumentos, o que torna o programa **mais legível e confiável**, como destacou John Backus no Prêmio Turing de 1977.

**Erro comum:** colocar Clojure ou LISP entre as puras.

## Q4

**Assunto:** história do funcional e Clojure. **Fonte:** Aula14 p.7, p.11.

**Resposta-modelo:**

- **Contexto histórico:** a programação funcional surgiu nos **anos 1960**, motivada pelas necessidades da **Inteligência Artificial** — computação simbólica, prova de teoremas, sistemas baseados em regras e processamento de linguagem natural. A primeira linguagem funcional foi o **LISP**.
- **Clojure:**
  - **Origem:** surgiu em **2005**, como **dialeto do LISP**, o que facilita a compreensão para quem já usou LISP ou Common Lisp.
  - **Ambiente de execução padrão:** a **JVM** (Máquina Virtual Java), com versões para outros ambientes. Por rodar na JVM, acessa bibliotecas Java, como `(Math/sqrt 16)`.
  - **Adoção corporativa:** usada por **Walmart** e **Nubank**.
  - É uma linguagem funcional **impura**, com sintaxe **prefixada**.

## Q5

**Assunto:** componentes de uma funcional pura. **Fonte:** Aula14 p.12 e p.22.

**Resposta-modelo:**

1. Um **conjunto de funções primitivas**.
2. Uma **operação de aplicação de função**.
3. Um **conjunto de formas funcionais** para criar funções complexas a partir das primitivas.
4. **Estruturas para representar os dados** usados como parâmetros e valores calculados pelas funções.

**Exemplos em Clojure:** `+` e `quot` (primitivas); `(f a b)` (aplicação); `comp`, `map` e `reduce` (formas funcionais); listas e vetores (estruturas).

## Q6

**Assunto:** sintaxe prefixada e primitivas. **Fonte:** Aula14 p.13–16, p.21, p.23.

**Sintaxe prefixada:** toda expressão tem a forma `(operador arg1 arg2 ...)` — o operador vem antes dos operandos, e os parênteses delimitam a aplicação. As expressões aninhadas são avaliadas de dentro para fora, e os operadores aceitam vários argumentos: `(* 5 2 3)` = 30.

**a)** Valores no Clojure da JVM:

| Expressão | Resultado | Comportamento |
| --- | --- | --- |
| `(/ 10 3)` | `10/3` | Divisão **exata**: como 10 não é divisível por 3, o resultado é um **número racional** (tipo `Ratio`), sem perder precisão. Para ver o decimal: `(float (/ 10 3))` → 3.3333333 |
| `(quot 10 3)` | `3` | **Quociente inteiro** da divisão |
| `(rem 10 3)` | `1` | **Resto** da divisão (10 = 3·3 + 1) |

**b)** `(not (= x 0))` testa se **x é diferente de zero**: `(= x 0)` produz `true` ou `false`, e `not` inverte o resultado. **Motivo, segundo o slide (p.21):** "não existe o comparador diferente; deve-se usar o `=` negado (`not`)".

> **[Atenção]** Clojure tem a função `not=`, então `(not= x 0)` é equivalente. Na prova, apresente a justificativa do slide; citar `not=` é um acréscimo.

## Q7

**Assunto:** programa Clojure com `def`. **Fonte:** Aula14 p.16, p.18–20.

<!-- teste: entrada="2 3" saida-contem="3/25\n76.0" saida-contem-cljs="0.12\n76" -->
```clojure
(println "Digite os valores de x e y:")
(def x (read))                                 ; vincula o 1º valor lido ao símbolo x
(def y (read))                                 ; vincula o 2º valor lido ao símbolo y
(println (/ (* (+ x 2) y) (* 10 (+ x 8))))     ; ((x + 2) * y) / (10 * (x + 8))
(println (- (Math/pow (* 3 y) 2) (+ x y)))     ; (3 * y)^2 - (x + y)
```

**Teste (x = 2, y = 3):** ((2 + 2)·3) / (10·(2 + 8)) = 12/100 → no Clojure da JVM, **`3/25`** (razão simplificada); (3·3)² − (2 + 3) = 81 − 5 = **`76.0`** (`Math/pow` devolve `double`). Para exibir a divisão em decimal, use `(float ...)`.

**Vantagem do `def`:** vincula um **nome** a um valor lido **uma única vez**, que pode então ser **reutilizado** em várias expressões. Sem `def`, seria preciso embutir `(read)` em cada expressão — `(println (- (+ (read) (read)) 10))` —, o que "dificulta a utilização do mesmo valor em diferentes pontos do programa" (p.19): o usuário teria de digitar x e y de novo para cada cálculo.

**Erro comum:** escrever (3·y)² como `(* 3 y 2)`, que dá 6y.

## Q8

**Assunto:** estrutura do programa lógico. **Fonte:** Aula15 p.6–7, p.14–18.

**Resposta-modelo:**

- **Estrutura:** os programas lógicos são expressos em **lógica simbólica**, como um conjunto de sentenças chamadas **proposições**. Em Prolog, a base de conhecimento tem **fatos** (proposições assumidas verdadeiras) e **regras**. A execução é disparada por **consultas**, e os resultados são produzidos por um **processo de inferência lógica**: o sistema busca, por unificação, as instanciações que tornam a consulta verdadeira. O programador descreve **o quê**, e não **como**.
- **Três necessidades da lógica formal:**
  1. **Expressar proposições.**
  2. **Expressar os relacionamentos** entre proposições.
  3. **Descrever como novas proposições podem ser inferidas** a partir de outras assumidas como verdadeiras.
- A base da programação lógica é o **cálculo de predicados de primeira ordem**.

## Q9

**Assunto:** proposicional × primeira ordem. **Fonte:** Aula15 p.7–12.

**Resposta-modelo:**

- **Lógica proposicional:** trabalha com **proposições** (afirmações verdadeiras ou falsas), representadas por **constantes** e combinadas por **conectivos** (¬, ∧, ∨, ↔, →), cujo resultado é calculado por tabelas-verdade. Cada proposição é **indivisível**: "João é homem" é só um símbolo p.
- **Cálculo de predicados de primeira ordem:** acrescenta elementos que permitem falar de **relações** e de **generalizações**:
  - **Predicados:** expressam relações entre entidades (constantes ou variáveis), como `homem(joao)` e `mae(mary, X)`.
  - **Variáveis:** permitem enunciar princípios gerais; uma variável pode ser substituída por diferentes constantes.
  - **Quantificadores:** indicam quantas constantes podem ser associadas a uma variável. Variáveis só aparecem precedidas deles.
- **Exemplos:**
  - **Universal:** ∀X.(mulher(X) → humano(X)) — "para todo X, se X é mulher, X é humano".
  - **Existencial:** ∃X.(mae(mary, X) ∧ homem(X)) — "existe um X tal que Mary é mãe de X e X é homem".

## Q10

**Assunto:** termos e proposições em Prolog. **Fonte:** Aula15 p.14–17.

**Resposta-modelo:**

- **Termo composto** = um **functor** (termo de predicado: termo simples constante que representa uma relação) + uma **lista de parâmetros** (termos simples, constantes ou variáveis). Em `gosta(joao, maria)`, o functor é `gosta` e os parâmetros são `joao` e `maria`. Não há semântica intrínseca nos termos: o significado é atribuído pelo programador.
- **Proposição atômica** é a que tem **um único** termo composto. A mesma forma sintática serve a dois papéis:
  - **Fato:** proposição **assumida como verdadeira**, escrita na base. Exemplos: `homem(joao).` e `pai(joao, maria).`
  - **Consulta:** proposição cuja **verdade deve ser verificada**, feita no prompt ou no programa. Exemplos: `?- homem(joao).` → `true`/`false`; `?- pai(X, maria).` → por **unificação**, o sistema encontra `X = joao`.

## Q11

**Assunto:** consultas Prolog. **Fonte:** Aula15 p.17, p.19–20.

<!-- teste: consulta="pai(joao, X)." saida-contem="X = ana\nX = maria\nX = carlos" -->
```prolog
pai(joao, ana).
pai(joao, maria).
pai(joao, carlos).
pai(carlos, renata).
```

| Pergunta | Consulta | Retorno esperado |
| --- | --- | --- |
| a) João é pai de Renata? | `?- pai(joao, renata).` | `false` — não há esse fato; Renata é filha de Carlos |
| b) Quem é o pai de Ana? | `?- pai(X, ana).` | `X = joao.` |
| c) Quem são os filhos de João? | `?- pai(joao, X).` | `X = ana ;` `X = maria ;` `X = carlos.` — uma resposta por vez, pedindo a próxima com `;` |

**Explicação:** em (b) e (c), a variável ocupa posições diferentes: no 1º argumento, pergunta-se o **pai**; no 2º, o **filho**. O mesmo fato responde às duas perguntas por **unificação**, e as respostas sucessivas de (c) vêm do **retrocesso** (*backtracking*) sobre os fatos.

**[Explicação elaborada]** Para obter todos os filhos de uma vez, como lista, use `findall`, que aparece no Exemplo 2 da Aula15 (p.21): `?- findall(X, pai(joao, X), L).` → `L = [ana, maria, carlos]` (Aula15 p.21).
