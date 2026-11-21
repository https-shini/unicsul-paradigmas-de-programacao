<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 14](../README.md) › [02 - Resumo Teórico](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 14 — Paradigma Funcional · Resumo teórico

> **Fonte:** [`Aula14_ParadigmaFuncional.pdf`](../01%20-%20Slides%20Originais/Aula14_ParadigmaFuncional.pdf) (24 páginas). Título interno: "Aula 15 – Paradigma Funcional". Apoio indicado: Sebesta (9ª ed.), seções 15.1 a 15.5 e 15.9 a 15.10; Tucker & Noonan, cap. 14 ([p.24](../01%20-%20Slides%20Originais/README.md#página-24)).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF.
> **Validação:** não há Clojure (JVM) no ambiente usado para montar este repositório. Os trechos marcados foram executados com o **nbb** (ClojureScript sobre Node.js), que usa a mesma sintaxe. **Diferenças de representação:** no Clojure da JVM, `(/ 10 3)` dá a razão `10/3` e `(Math/sqrt 9)` imprime `3.0`; no ClojureScript, dão `3.3333333333333335` e `3`. Os resultados do Clojure da JVM indicados abaixo seguem a especificação da linguagem.

---

## 1. Objetivos (p.2)

**[Material original]** Compreender as características básicas do paradigma funcional; conhecer as principais linguagens funcionais; compreender a sintaxe das funções primitivas de **Clojure**; criar pequenos programas em Clojure.

## 2. Ponto de partida: o que já sabemos (p.3–6)

**[Material original]**

- **Elementos fundamentais do imperativo:** variáveis, atribuições e expressões; estruturas de controle (sequencial, seleção e repetição); comandos de E/S; abstração procedural.
- As linguagens imperativas foram projetadas para **usar eficientemente os recursos da arquitetura de von Neumann** (Figura 1.1 de Sebesta).
- **"A forma como o paradigma OO trata esses fundamentos é muito diferente do imperativo? Não**, pois as diferenças principais estão na **forma como o programa é organizado (abstração)** e não nos comandos."
- "Existem outras bases, diferentes da arquitetura de von Neumann, que podem ser usadas para o projeto de linguagens. Os dois paradigmas mais conhecidos são o **Funcional** e o **Lógico**."

**[Explicação elaborada]** Imperativo e OO compartilham o **mesmo modelo de execução** (estado mutável em células de memória). O funcional parte de outra base: a **matemática das funções**.

## 3. Origem e ideia central (p.7–8)

**[Material original]**

- Surgiu na **década de 1960**, motivado por necessidades da **Inteligência Artificial**: computação simbólica, provas de teoremas, sistemas baseados em regras e processamento de linguagem natural.
- **LISP** foi a primeira linguagem funcional.
- A computação é vista como uma **função matemática que mapeia entradas em saídas**.
- No **modelo puro**, **não há variável** (controle de estado), **atribuição** nem **laço de repetição**, embora algumas linguagens aceitem esses recursos.
- **Não há efeitos colaterais**, o que torna o programa **mais legível e confiável**, como destacou **John Backus** ao receber o prêmio Turing da ACM em 1977.

> **[Atenção]** O slide diz que Backus recebeu o prêmio "pelo seu trabalho como Fortran" (provavelmente "com o Fortran"). **[Complemento]** Backus foi premiado pelo Fortran e pela notação BNF. Na palestra de aceitação, *Can Programming Be Liberated from the von Neumann Style?*, criticou o estilo imperativo e defendeu a programação funcional.

**[Explicação elaborada] — o que é "efeito colateral":** qualquer mudança que uma função provoca **fora** do cálculo do seu resultado — alterar uma variável global, modificar um parâmetro, escrever na tela ou num arquivo. Sem efeitos colaterais:

- **Mesma entrada → mesma saída, sempre.** `(+ 2 3)` vale 5 em qualquer momento do programa. É a **transparência referencial**: uma chamada pode ser substituída pelo seu resultado.
- Não é preciso rastrear "o que mudou antes" para entender uma expressão — o oposto do problema que Dijkstra apontou no `goto`, em que o significado de uma variável dependia do ponto da execução ([Aula 09a](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)).

**Exemplo comparativo [Complemento]:**

| Imperativo (estado mutável) | Funcional (sem estado) |
| --- | --- |
| `soma = 0; for (i = 1; i <= n; i++) soma = soma + i;` | `(reduce + (range 1 (inc n)))` |
| A variável `soma` muda de valor a cada passo | Nenhum valor é alterado; o resultado é composto por funções |

<!-- teste: saida-contem="55" -->
```clojure
;; Soma de 1 a 10 sem variável mutável nem laço:
;; range gera (1 2 ... 10), e reduce aplica + acumulando.
(println (reduce + (range 1 11)))   ; 55
```

## 4. Puras × impuras; onde o funcional aparece (p.9–10)

**[Material original]**

| | Linguagens funcionais **puras** | Linguagens funcionais **impuras** |
| --- | --- | --- |
| Definição | **Não** aceitam variáveis, atribuição e laços | **Possuem** variáveis, atribuição e laços |
| Exemplos | **Haskell**, **Miranda** | **LISP**, **Scheme**, **Clojure**, **Elixir**, **Erlang** |

- O **Java 8** incluiu programação funcional em sua definição.
- **JavaScript, Python e C#** permitem **funções ou expressões lambda**, conceito ligado à programação funcional.
- Em geral, as linguagens funcionais são **interpretadas**, mas **podem ser compiladas**.
- Alguns autores usam **"linguagem aplicativa"** como sinônimo de linguagem funcional.

**[Complemento]** Uma **lambda** é uma função anônima, escrita como valor: `x -> x * 2` em Java, `lambda x: x * 2` em Python, `(fn [x] (* x 2))` em Clojure. Funções tratadas como valores podem ser passadas para outras funções (**funções de alta ordem**), como `map` e `filter`. O material cita lambdas, mas não desenvolve esses conceitos.

## 5. A linguagem Clojure (p.11)

**[Material original]**

- Surgiu em **2005**, como um **dialeto do LISP**, o que facilita a compreensão para quem já usou LISP ou variações como Common Lisp.
- É executada na **JVM** por padrão, mas tem versões para outros ambientes de execução.
- É usada em ambientes corporativos; **Walmart** e **Nubank** são exemplos de grandes empresas que a utilizam (o slide grafa "Wallmart").

> **[Complemento]** Rich Hickey começou o desenvolvimento em 2005; o lançamento público foi em 2007. A versão para JavaScript chama-se **ClojureScript**, a usada para validar os trechos deste repositório.

## 6. O que uma linguagem funcional pura fornece (p.12 e p.22)

**[Material original]** O slide aparece **duas vezes** na aula:

1. Um conjunto de **funções primitivas**.
2. Uma **operação de aplicação da função**.
3. Um conjunto de **formas funcionais** para criar funções complexas a partir das primitivas.
4. **Estruturas para representar os dados** usados como parâmetros e valores calculados pelas funções.

**[Explicação elaborada] — os quatro itens em Clojure:**

1. **Primitivas:** `+`, `-`, `*`, `/`, `quot`, `rem`, `=`, `even?`…
2. **Aplicação:** a lista `(f a b)` aplica `f` aos argumentos `a` e `b` — é toda a sintaxe.
3. **Formas funcionais:** combinam funções, como `comp` (composição), `map` e `reduce`. Exemplo: `((comp inc inc) 5)` vale 7.
4. **Estruturas de dados:** listas `(1 2 3)`, vetores `[1 2 3]`, mapas `{:a 1}`.

## 7. Sintaxe prefixada e funções primitivas de Clojure (p.13–21)

**[Material original]** Grupos de primitivas: **entrada e saída**, **numéricas** e **predicados numéricos** (comparações).

**[Explicação elaborada] — a regra única da sintaxe:** tudo é `(operador argumento1 argumento2 ...)`. O operador vem **antes** (notação **prefixada**), e os parênteses delimitam a aplicação. Expressões aninhadas são avaliadas **de dentro para fora**: os argumentos são avaliados antes de a função ser aplicada.

| Infixa (matemática) | Prefixada (Clojure) |
| --- | --- |
| 2 + 10 | `(+ 2 10)` |
| 5 · 2 · 3 | `(* 5 2 3)` — vários argumentos |
| 10 − 3 · 5 | `(- 10 (* 3 5))` |
| x + y − 10 | `(- (+ x y) 10)` |

### 7.1 Entrada e saída (p.14)

**[Material original]** `(read-line)`, `(print expressão)`, `(println expressão)`. "O que acontece ao executar o código abaixo?"

```clojure
(println "Digite um valor:")
(println "Valor digitado:" (read-line))
```

**[Explicação elaborada]** Imprime "Digite um valor:", **espera** o usuário digitar e só então imprime "Valor digitado: …". No segundo `println`, o argumento `(read-line)` precisa ser avaliado **antes** de o `println` ser aplicado. `print` não pula linha; `println` pula.

### 7.2 Funções numéricas (p.15–16)

**[Material original]** `+ - * /` e os exemplos abaixo. Valores conforme o **Clojure da JVM** — **[Explicação elaborada]**:

| Expressão | Resultado | Explicação |
| --- | --- | --- |
| `(+ 2 10)` | `12` | |
| `(* 5 2 3)` | `30` | Aceita vários argumentos |
| `(- 10 (* 3 5))` | `-5` | `(* 3 5)` = 15; 10 − 15 |
| `(/ 10 3)` | **`10/3`** | Divisão entre inteiros que não é exata gera um **racional** (tipo `Ratio`), sem perda de precisão |
| `(float (/ 10 3))` | `3.3333333` | Converte a razão para ponto flutuante |
| `(quot 10 3)` | `3` | **Quociente** inteiro |
| `(rem 10 3)` | `1` | **Resto** |

**Funções da biblioteca `Math` do Java ([p.16](../01%20-%20Slides%20Originais/README.md#página-16))** — Clojure roda na JVM e acessa classes Java com `Classe/metodo`:

| Expressão | Resultado (JVM) |
| --- | --- |
| `(Math/pow 2 3)` | `8.0` |
| `(Math/sqrt 16)` | `4.0` |
| `(Math/abs -5)` | `5` |
| `(Math/floor 3.7)` | `3.0` |
| `(Math/ceil 3.1)` | `4.0` |
| `(Math/round 3.6)` | `4` |
| `(max 10 3 7)` | `10` (função do Clojure) |
| `(min 10 3 7)` | `3` (função do Clojure) |

**Atividade 1 ([p.17](../01%20-%20Slides%20Originais/README.md#página-17)):** calcular e depois programar no OneCompiler, um valor por linha. Respostas na [resolução](../04%20-%20Resoluções/resolucoes-aula-14.md#e7--atividade-1-original-p17).

### 7.3 Leitura de valores e `def` (p.18–19)

**[Material original]**

- `(read)` e `(read-line)` leem dados do usuário e os associam ao cálculo.
- A função x + y − 10 pode ser escrita como `(- (+ x y) 10)`:

```clojure
(println "Digite os valores de x e y")
(println "Resultado: " (- (+ (read) (read)) 10))
```

- "Essa abordagem, embora facilite a legibilidade, **dificulta a utilização do mesmo valor em diferentes pontos** do programa."
- O comando **`def`** permite **vincular um nome a um valor**: `(def nome valor)`, `(def pi 3.14159)`, `(def x (read))`.

> **[Atenção]** O slide da [p.18](../01%20-%20Slides%20Originais/README.md#página-18) escreve `(- (+ x y) 10))`, com um parêntese **a mais** no final.

**[Explicação elaborada]**

- `(read)` lê um valor e o interpreta como dado Clojure: `5` vira o número 5. `(read-line)` devolve o texto digitado como **string**.
- Sem `def`, cada `(read)` lê um valor **novo**. Para usar x em duas expressões, seria preciso digitá-lo duas vezes.
- `def` cria um **vínculo** nome → valor. Não é uma "variável" no sentido imperativo: o valor não é reatribuído ao longo do cálculo. **[Complemento]** Tecnicamente, `def` cria uma *var* global, que pode ser redefinida, mas o estilo funcional evita isso.

**Atividade 2 ([p.20](../01%20-%20Slides%20Originais/README.md#página-20)):** ler x e y e mostrar, um por linha: x + y − 10; x + 2·y; (x + 2)·y; (x + 2)·y / [10·(x + 8)]; (3·y)² − (x + y). Solução testada na [resolução](../04%20-%20Resoluções/resolucoes-aula-14.md#e8--atividade-2-original-p20). Na [p.20](../01%20-%20Slides%20Originais/README.md#página-20), "(3 * y)2" significa (3y)²: o expoente aparece formatado como subscrito.

### 7.4 Predicados numéricos (p.21, 23)

**[Material original]**

- Comparações: `=`, `>`, `<`, `>=`, `<=`.
- "Não existe o comparador diferente; deve-se usar o `=` negado (`not`)."
- `even?` (é par?), `odd?` (é ímpar?), `zero?` (é zero?).

**Exemplo ([p.23](../01%20-%20Slides%20Originais/README.md#página-23)):**

<!-- teste: entrada="4" saida-contem="Maior que zero:  true|Diferente de zero:  true|Par:  true" -->
```clojure
(println "Digite o valor de x: ")
(def x (read))
(println "Maior que zero: " (> x 0))
(println "Diferente de zero: " (not (= x 0)))
(println "Par: " (even? x))
```

> **[Atenção]** Clojure **tem** a função `not=`: `(not= x 0)` equivale a `(not (= x 0))`. Em prova, use a forma do slide e, se quiser, cite `not=`.

**[Explicação elaborada]** O `?` no fim do nome é **convenção** de Clojure para funções que devolvem booleano (predicados). Para x = 4: `true`, `true`, `true`; para x = −3: `false`, `true`, `false`.

## 8. Funcional × imperativo — quadro-resumo

**[Explicação elaborada]**

| Aspecto | Imperativo | Funcional (modelo puro) |
| --- | --- | --- |
| Base | Arquitetura de von Neumann | Funções matemáticas |
| Unidade de programa | Comando (altera estado) | Expressão (produz valor) |
| Variável | Célula de memória mutável | Nome vinculado a um valor (`def`) |
| Repetição | Laços (`for`, `while`) | Recursão e funções como `reduce`/`map` **[Complemento]** |
| Efeitos colaterais | Comuns | Ausentes |
| Composição | Sequência de comandos | Composição de funções |
| Execução usual | Compilada | Em geral interpretada |

## 9. Conexões e pontos para a prova

- Von Neumann ([Aula 09](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md)) é o contraponto; o [lógico](../../Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) é o outro paradigma fora desse modelo.
- **Atenção à classificação do professor:** na Aula 15 ([p.5](../../Aula%2015%20-%20Paradigma%20Lógico/01%20-%20Slides%20Originais/README.md#página-5)), o funcional aparece como **procedural**, e não declarativo.
- Cobrado na [Lista 01, Q2–Q7](../../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/02%20-%20Resolução/resolucao-lista-01.md#q3) e na [Lista 02, Q12](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q12).
- **Decorar:** puras (Haskell, Miranda) × impuras (LISP, Scheme, Clojure, Elixir, Erlang); os 4 componentes; o contexto histórico (anos 1960, IA, LISP); Clojure (2005, dialeto de LISP, JVM, Walmart/Nubank); `/` × `quot` × `rem`; `def`.

---

**Anterior:** [Aula 13](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) · **Próxima:** [Aula 15 — Paradigma Lógico](../../Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)


<!-- nav:rodape -->

---

**Aula 14:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · **Resumo** · [Exercícios](../03%20-%20Exercícios/exercicios-aula-14.md) · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-14.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 13 · Resumo](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) · [Aula 15 · Resumo](../../Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) →

**Links para esta página (14):** [Aula 09 · Resumo](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [Aula 11 · Resoluções](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md) · [Aula 13 · Resumo](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) · [Aula 14 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-14.md) · [Aula 14 · visão geral](../README.md) · [Aula 15 · Resumo](../../Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) · [Lista 01](../../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/README.md) · [Lista 02](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md) · [03 — Trabalhos e Projetos](../../../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Revisão da Unidade 4 — Paradigmas funcional e lógico (Aulas…](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-4-funcional-e-logico.md) · [Resumo geral da disciplina](../../../06%20-%20Revisões%20e%20Sínteses/resumo-geral-da-disciplina.md) · [Glossário](../../../07%20-%20Glossário/glossario.md) · [P4 — Estatísticas de texto em Clojure](../../../09%20-%20Projetos%20Práticos/P4%20-%20Estatísticas%20de%20Texto%20em%20Clojure/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
