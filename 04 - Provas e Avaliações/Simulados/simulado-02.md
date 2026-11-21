# Simulado 02 — Fundamentos e paradigma imperativo (Aulas 02–11)

> **[Exercício autoral]** Simulado elaborado para este repositório. **Não é prova do professor** e não antecipa o conteúdo das avaliações. Cobre as Unidades 1 e 2.
> **Sugestão:** 100 minutos, sem consulta. Depois, confira na [resolução comentada](resolucao-simulado-02.md). As questões de programação podem ser conferidas com `python3 ferramentas/verificar.py simulado-02 <número> sua_solucao.c`.

---

## Parte A — Questões objetivas (1 ponto cada)

**1.** (Aula 02) Segundo os critérios de avaliação de linguagens, ter **muitas formas diferentes de expressar a mesma operação** (como `x++`, `++x`, `x += 1` e `x = x + 1`):

- a) melhora a legibilidade, porque o programador escolhe a forma de que mais gosta.
- b) tende a prejudicar a legibilidade, porque o leitor precisa conhecer todas as formas.
- c) não afeta nenhum critério, pois todas produzem o mesmo resultado.
- d) só afeta o custo de compilação.

**2.** (Aula 03) Qual fase de um compilador transforma a sequência de caracteres do programa-fonte em **tokens**?

- a) Análise léxica.
- b) Análise sintática.
- c) Otimização.
- d) Geração de código.

**3.** (Aula 04) Quantos tokens há no comando C `soma = x + 10;`?

- a) 4
- b) 5
- c) 6
- d) 7

**4.** (Aula 05) Uma variável declarada como `static int contador = 0;` **dentro** de uma função C tem:

- a) escopo global e tempo de vida da função.
- b) escopo local e tempo de vida do programa inteiro.
- c) escopo local e tempo de vida de cada chamada.
- d) escopo global e tempo de vida do programa inteiro.

**5.** (Aula 05) Em Perl, as declarações `my $x` e `local $x` correspondem, respectivamente, a:

- a) escopo dinâmico e escopo estático.
- b) escopo estático e escopo dinâmico.
- c) escopo estático nos dois casos.
- d) variável global e constante.

**6.** (Aula 06) **Coerção** é:

- a) a conversão de tipo escrita explicitamente pelo programador, como `(int) x`.
- b) a conversão de tipo feita implicitamente pela linguagem.
- c) um erro de tipo detectado na compilação.
- d) a declaração de uma variável sem tipo.

**7.** (Aula 07) Qual tipo composto agrupa elementos **de tipos diferentes**, acessados por **nome**?

- a) Matriz.
- b) Enumeração.
- c) Registro (`struct`).
- d) String.

**8.** (Aula 08) Após `int x = 1; int *p = &x; *p = 5;`, o valor de `x` é:

- a) 1
- b) 5
- c) o endereço de `p`
- d) indefinido

**9.** (Aula 10) Decompor um problema em funções cada vez mais simples, do geral para o específico, é a técnica de:

- a) refinamento sucessivo (abstração procedural).
- b) herança.
- c) coerção.
- d) unificação.

**10.** (Aula 11) Em `void f(int a) { ... }` chamada como `f(b + 1);`:

- a) `a` é o parâmetro real e `b + 1` é o parâmetro formal.
- b) `a` é o parâmetro formal e `b + 1` é o parâmetro real (argumento).
- c) ambos são parâmetros formais.
- d) `b + 1` não pode ser argumento, porque não é uma variável.

---

## Parte B — Questões discursivas e de programação (2 pontos cada)

**11.** (Aulas 03 e 06) Um programa Python tem um erro de tipo dentro de um `if` que só é executado no último dia do mês. Em Java, o mesmo erro seria detectado na hora de compilar. Explique, usando os conceitos de **implementação** (compilação × interpretação) e de **tipagem** (estática × dinâmica), por que isso acontece. Qual dos dois conceitos é o decisivo aqui?

**12.** (Aula 05) Considere o programa C abaixo.

```c
#include <stdio.h>
int x = 1;
void mostra(void) { printf("%d\n", x); }
void a(void) { int x = 2; mostra(); }
void b(void) { int x = 3; a(); }
int main(void) { b(); mostra(); return 0; }
```

a) O que o programa imprime em C?\
b) O que imprimiria se a linguagem usasse **escopo dinâmico**? Justifique cada linha.

**13.** (Aula 08) Escreva em C uma função `int *quadrados(int n)` que aloque **dinamicamente** um vetor de `n` inteiros, preencha-o com 0², 1², …, (n−1)² e devolva o ponteiro. No `main`, leia `n`, imprima os valores separados por espaço e libere a memória. Diga em que região de memória ficam o vetor e a variável ponteiro.

**14.** (Aula 09) O programa abaixo usa `goto`. Reescreva-o de forma **estruturada** (sem `goto`), lendo `n` da entrada e imprimindo a soma de 1 a `n`. Explique por que a versão estruturada é mais fácil de entender, segundo o argumento de Dijkstra.

```c
int n, i = 1, s = 0;
scanf("%d", &n);
laco:
    if (i > n) goto fim;
    s = s + i;
    i = i + 1;
    goto laco;
fim:
    printf("%d\n", s);
```

**15.** (Aula 10) Escreva em C um programa que leia três notas, calcule a média e informe a situação: **Aprovado** (média ≥ 6), **Exame** (4 ≤ média < 6) ou **Reprovado**. Use **abstração procedural**: pelo menos uma função para calcular a média e outra para decidir a situação. Depois, explique que tipo de acoplamento haveria se as notas fossem variáveis globais.
