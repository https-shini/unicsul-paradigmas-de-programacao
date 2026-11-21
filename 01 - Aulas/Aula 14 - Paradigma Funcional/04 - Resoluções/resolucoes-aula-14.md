# Aula 14 — Paradigma Funcional · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-14.md`](../03%20-%20Exercícios/exercicios-aula-14.md).
> **Validação:** os programas foram executados com **nbb (ClojureScript)**. Os resultados indicados para o **Clojure da JVM** — razões como `10/3` e reais impressos como `3.0` — seguem a especificação da linguagem, porque o ClojureScript representa números de outra forma (veja o aviso no [resumo](../02%20-%20Resumo%20Teórico/resumo-aula-14.md)).

## E1

Nos **anos 1960**, motivada pelas necessidades da **Inteligência Artificial**: computação simbólica, prova de teoremas, sistemas baseados em regras e processamento de linguagem natural. A primeira linguagem funcional foi o **LISP** (p.7).

## E2

- **Puras:** não aceitam variáveis (estado), atribuição nem laços, e portanto não têm efeitos colaterais. Exemplos: **Haskell** e **Miranda**.
- **Impuras:** aceitam esses recursos. Exemplos: **LISP, Scheme, Clojure, Elixir, Erlang** (p.9).

## E3

**Resposta: b.** `quot` dá o quociente inteiro: 17 = 3·5 + 2. `(/ 17 5)` daria `17/5`, e `(rem 17 5)` daria 2.

## E4

1. Um conjunto de funções primitivas.
2. Uma operação de aplicação de função.
3. Formas funcionais para criar funções complexas a partir das primitivas.
4. Estruturas para representar os dados usados como parâmetros e resultados (p.12).

## E5

| Infixa | Prefixada |
| --- | --- |
| a) 4 · (x + 1) | `(* 4 (+ x 1))` |
| b) (a − b) / (a + b) | `(/ (- a b) (+ a b))` |
| c) x² + 2x + 1 | `(+ (* x x) (* 2 x) 1)` ou `(+ (Math/pow x 2) (* 2 x) 1)` |
| d) \|y − 10\| | `(Math/abs (- y 10))` |

**Dica:** em (c), `+` aceita três argumentos de uma vez — não é preciso aninhar dois `+`.

## E6

Sem efeitos colaterais, o resultado de uma função depende **só dos seus argumentos**. Para entender `f(3)`, basta ler `f`, sem rastrear o que outras partes do programa alteraram antes. E testar é simples: mesma entrada, mesma saída.

Contraexemplo imperativo:

<!-- teste: saida-contem="primeira: 1|segunda: 2" -->
```c
#include <stdio.h>
int contador = 0;                          /* estado global */
int proximo(void) { return ++contador; }   /* efeito colateral: altera o global */

int main(void) {
    printf("primeira: %d\n", proximo());   /* 1 */
    printf("segunda: %d\n", proximo());    /* 2: mesma chamada, resultado diferente! */
    return 0;
}
```

`proximo()` sem argumentos devolve valores diferentes a cada chamada. Para saber o resultado, é preciso conhecer **toda a história** de execução — e qualquer outra função que mexa em `contador` pode quebrar o raciocínio. Isso reduz a confiabilidade.

## E7 — Atividade 1 (original, p.17)

| Expressão | Cálculo | Clojure JVM |
| --- | --- | --- |
| `(+ 2 10)` | 2 + 10 | `12` |
| `(- 20 7 4)` | (20 − 7) − 4 | `9` |
| `(* 5 2 3)` | 5 · 2 · 3 | `30` |
| `(/ 60 6 5)` | (60 / 6) / 5 | `2` (divisão exata: dá inteiro) |
| `(- 30 (* 3 4))` | 30 − 12 | `18` |
| `(Math/sqrt 9)` | √9 | `3.0` |
| `(Math/pow 4 2)` | 4² | `16.0` |

<!-- teste: saida-contem="12\n9\n30\n2\n18\n3" -->
```clojure
(println (+ 2 10))
(println (- 20 7 4))
(println (* 5 2 3))
(println (/ 60 6 5))
(println (- 30 (* 3 4)))
(println (Math/sqrt 9))
(println (Math/pow 4 2))
```

**Observação:** com vários argumentos, `-` e `/` operam **da esquerda para a direita**: `(- 20 7 4)` = (20 − 7) − 4.

## E8 — Atividade 2 (original, p.20)

<!-- teste: entrada="2 3" saida-contem="-5\n8\n12\n3/25\n76.0" saida-contem-cljs="-5\n8\n12\n0.12\n76" -->
```clojure
(println "Digite os valores de x e y:")
(def x (read))
(def y (read))
(println (- (+ x y) 10))                        ; x + y - 10
(println (+ x (* 2 y)))                         ; x + 2*y
(println (* (+ x 2) y))                         ; (x + 2) * y
(println (/ (* (+ x 2) y) (* 10 (+ x 8))))      ; (x + 2) * y / [10 * (x + 8)]
(println (- (Math/pow (* 3 y) 2) (+ x y)))      ; (3*y)^2 - (x + y)
```

**Teste com x = 2, y = 3:**

| Expressão | Valor | Clojure JVM imprime |
| --- | --- | --- |
| x + y − 10 | −5 | `-5` |
| x + 2y | 8 | `8` |
| (x + 2)·y | 12 | `12` |
| (x + 2)·y / [10·(x + 8)] | 12/100 | **`3/25`** (razão simplificada); com `float`, `0.12` |
| (3y)² − (x + y) | 81 − 5 | `76.0` (`Math/pow` devolve `double`) |

**Por que `def`:** x e y aparecem em várias expressões. Com `(read)` embutido em cada uma, o usuário teria de digitar os valores de novo a cada linha (p.19).

**Erro comum:** escrever `(* 3 y 2)` para (3y)², o que dá 6y, não 9y². O quadrado exige `(Math/pow (* 3 y) 2)` ou `(* (* 3 y) (* 3 y))`.

## E9

| Expressão | Saída (JVM) | Explicação |
| --- | --- | --- |
| `(/ 10 4)` | `5/2` | Não é exata, então vira razão simplificada |
| `(/ 10 5)` | `2` | Exata, então dá inteiro |
| `(float (/ 1 3))` | `0.33333334` | `float` tem precisão simples (32 bits) |
| `(rem -7 3)` | `-1` | `rem` segue o sinal do dividendo (−7 = −2·3 − 1). **[Complemento]** `(mod -7 3)` daria `2` |
| `(not (= 3 3.0))` | `true` | Em Clojure, `=` entre inteiro e real é **falso** (categorias numéricas diferentes); `(== 3 3.0)` seria verdadeiro |

> **[Complemento]** O último item mostra que `=` em Clojure é igualdade de **valor e categoria**. Para comparar só numericamente, existe `==`.

## E10

<!-- teste: saida-contem="120\n120\n3628800" -->
```clojure
;; Versão recursiva: a repetição vem da própria definição matemática
;;   n! = 1           se n <= 1
;;   n! = n * (n-1)!  caso contrário
(defn fatorial [n]
  (if (<= n 1)
    1
    (* n (fatorial (dec n)))))

;; Versão com forma funcional: reduce aplica * sobre a sequência 1..n
(defn fatorial-reduce [n]
  (reduce * 1 (range 1 (inc n))))

(println (fatorial 5))          ; 120
(println (fatorial-reduce 5))   ; 120
(println (fatorial 10))         ; 3628800
```

**Comparação com a versão imperativa (Aula 10):**

| Imperativo (C) | Funcional (Clojure) |
| --- | --- |
| `long long f = 1; for (i = 2; i <= k; i++) f *= i;` | `(* n (fatorial (dec n)))` ou `(reduce * (range 1 (inc n)))` |
| Uma variável `f` muda de valor a cada iteração | Nenhum valor muda; cada chamada produz um novo valor |
| Precisa de laço e atribuição | Usa recursão ou uma forma funcional |

Isso materializa o "modelo puro sem variável, atribuição e laço" (p.8). **[Complemento]** Para n grandes, a recursão direta pode estourar a pilha; Clojure oferece `recur` para recursão de cauda.

## E11

A OO usa o **mesmo modelo de execução** do imperativo: dentro dos métodos há variáveis mutáveis, atribuições, decisões e laços — a OO muda **onde** o código fica (classes) e **quem** acessa os dados (encapsulamento). O funcional muda o **próprio modelo de computação**: em vez de uma sequência de comandos que altera o estado da memória (von Neumann), o programa é uma **composição de funções** que produzem valores, sem estado mutável no modelo puro. Por isso o slide diz que o funcional parte de "outra base, diferente da arquitetura de von Neumann" (p.6).
