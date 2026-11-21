<!-- nav:topo -->
[Início](../../README.md) › [04 - Provas e Avaliações](../README.md) › [Simulados](README.md) · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Simulado 01 — Paradigmas de Linguagens de Programação

> **[Exercício autoral]** Simulado elaborado para este repositório. **Não é prova do professor** e não antecipa o conteúdo das avaliações. Cobre as Aulas 02–15.
> **Sugestão:** 100 minutos, sem consulta. Depois, confira na [resolução comentada](resolucao-simulado-01.md).

---

## Parte A — Questões objetivas (1 ponto cada)

**1.** (Aula 03) Sobre a implementação híbrida de Java, assinale a alternativa correta.

- a) O compilador `javac` gera código de máquina nativo para o processador em uso.
- b) O bytecode é independente de plataforma e é executado pela JVM.
- c) A JVM é um compilador que traduz o código-fonte Java diretamente.
- d) Por ser híbrida, a execução em Java é sempre mais lenta que a interpretação pura.

**2.** (Aula 04) No comando C `x = (y + 10 * z;`, é correto afirmar:

- a) Há erro léxico, porque `(` não é um token válido.
- b) Há erro sintático: os tokens são válidos, mas a sequência não forma um comando.
- c) Há erro semântico de tipo.
- d) Não há erro: o compilador fecha o parêntese automaticamente.

**3.** (Aula 05) Considere:

```c
#include <stdio.h>
int n = 10;
void f(void) { printf("%d", n); }
void g(void) { int n = 20; f(); }
int main(void) { g(); return 0; }
```

Com **escopo estático** e com **escopo dinâmico**, o programa imprimiria, respectivamente:

- a) 10 e 10
- b) 20 e 20
- c) 10 e 20
- d) 20 e 10

**4.** (Aula 06) Qual par classifica corretamente as linguagens?

- a) C: dinâmica e forte · Python: estática e fraca
- b) Java: estática e forte · PHP: dinâmica e fraca
- c) Python: dinâmica e fraca · Java: estática e fraca
- d) PHP: estática e forte · C: dinâmica e fraca

**5.** (Aula 07) Uma matriz `int m[3][4]` em C, armazenada por linhas (*row-major*), com 4 bytes por elemento e endereço-base 1000. O endereço de `m[2][1]` é:

- a) 1024
- b) 1028
- c) 1036
- d) 1044

**6.** (Aula 08) Em C++, `int* v = new int[5];` aloca:

- a) Um inteiro com valor 5, na pilha.
- b) Cinco inteiros no heap; o ponteiro `v` (variável local) fica na pilha.
- c) Cinco inteiros no segmento estático.
- d) Um vetor que é liberado automaticamente ao fim da função.

**7.** (Aula 09) No artigo de 1968, Dijkstra argumenta que o `goto`:

- a) deve ser usado com moderação, sem uso excessivo.
- b) é logicamente necessário em linguagens imperativas.
- c) dificulta encontrar coordenadas que descrevam o progresso do processo, e deveria ser abolido das linguagens de alto nível.
- d) foi provado dispensável pelo próprio Dijkstra no artigo.

**8.** (Aula 11) Em C#, um parâmetro declarado com `out`:

- a) é passado por valor e não altera o argumento.
- b) corresponde à semântica de saída: o método deve atribuir um valor a ele antes de retornar.
- c) só pode ser lido, nunca alterado.
- d) é idêntico a `in`.

**9.** (Aula 13) Sobre polimorfismo, assinale a correta.

- a) Na sobrecarga, a versão chamada é escolhida em tempo de execução pelo tipo real do objeto.
- b) Na sobrescrita com vinculação dinâmica, a versão chamada é escolhida pelo tipo real do objeto, em tempo de execução.
- c) Java permite herança múltipla de classes com `extends A, B`.
- d) Uma interface Java (no modelo clássico) contém atributos de instância.

**10.** (Aula 15) Com os fatos `pai(joao, ana). pai(joao, carlos). pai(carlos, renata).`, a consulta `pai(X, renata).` responde:

- a) `false.`
- b) `X = joao.`
- c) `X = carlos.`
- d) `X = ana ; X = carlos.`

---

## Parte B — Questões discursivas (2 pontos cada)

**11.** (Aulas 02 e 09) Explique por que as linguagens imperativas são chamadas de "linguagens de von Neumann". Relacione variáveis, atribuição e repetição com os componentes dessa arquitetura.

**12.** (Aulas 10 e 12) Uma pilha foi implementada primeiro com um vetor e depois com uma lista encadeada, sem alterar o `main` que a utiliza. Explique que conceito permitiu isso e quais propriedades de projeto (acoplamento e coesão) ele favorece.

**13.** (Aula 11) Considere o pseudocódigo abaixo, em que `troca` recebe `a` e `b`:

```text
procedimento troca(a, b): temp ← a; a ← b; b ← temp
x ← 1; y ← 2; troca(x, y); escreva(x, y)
```

Diga o que é impresso se a passagem for (a) por valor; (b) por referência; (c) por valor-resultado. Justifique.

**14.** (Aula 14) Escreva em Clojure uma expressão que calcule `(a + b) · (a − b) / 2` com `a = 7` e `b = 3`, e diga o valor resultante. Depois, explique por que `(/ 7 2)` em Clojure não resulta em `3`.

**15.** (Aulas 12, 14 e 15) Um sistema de controle de acesso precisa decidir se uma pessoa pode entrar em uma sala, com base em regras como "gerentes acessam qualquer sala do seu andar" e "visitantes só acessam a recepção". Compare como esse problema seria modelado nos paradigmas orientado a objetos e lógico. Qual você escolheria para o **motor de regras**? Justifique.


<!-- nav:rodape -->

---

[Simulado 02 — Fundamentos e paradigma imperativo (Aulas 02–…](simulado-02.md) →

**Links para esta página (6):** [02 — Listas de Exercícios](../../02%20-%20Listas%20de%20Exercícios/README.md) · [04 — Provas e Avaliações](../README.md) · [Simulado 01 · Resolução comentada](resolucao-simulado-01.md) · [06 — Revisões e Sínteses](../../06%20-%20Revisões%20e%20Sínteses/README.md) · [Guia de estudo para as avaliações](../../06%20-%20Revisões%20e%20Sínteses/guia-de-estudo-para-provas.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../README.md)

<!-- /nav:rodape -->
