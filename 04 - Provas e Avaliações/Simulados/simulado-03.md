<!-- nav:topo -->
[Início](../../README.md) › [04 - Provas e Avaliações](../README.md) › [Simulados](README.md) · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Simulado 03 — Orientação a objetos, funcional e lógico (Aulas 12–15)

> **[Exercício autoral]** Simulado elaborado para este repositório. **Não é prova do professor** e não antecipa o conteúdo das avaliações. Cobre as Unidades 3 e 4.
> **Sugestão:** 100 minutos, sem consulta. Depois, confira na [resolução comentada](resolucao-simulado-03.md). As questões de programação podem ser conferidas com `python3 ferramentas/verificar.py simulado-03 <número> sua_solucao`.

---

## Parte A — Questões objetivas (1 ponto cada)

**1.** (Aula 12) Qual modificador de acesso permite que um atributo seja acessado **somente pela própria classe**?

- a) `public`
- b) `protected`
- c) `private`
- d) nenhum: em Java todos os atributos são acessíveis

**2.** (Aula 12) Em Java, o que acontece com um objeto que **deixa de ser referenciado** por qualquer variável?

- a) É destruído imediatamente pelo destrutor.
- b) Pode ser liberado pela coleta de lixo da JVM.
- c) Permanece na memória até o fim do programa, sempre.
- d) Causa erro de compilação.

**3.** (Aula 13) Qual declaração é **válida** em Java?

- a) `class C extends A, B { }`
- b) `class C implements A extends B { }`
- c) `class C extends A implements I, J { }`
- d) `class C : public A, public B { }`

**4.** (Aula 13) Uma classe Java tem o método `abstract double area();`. Então:

- a) a classe pode ser instanciada normalmente.
- b) a classe deve ser declarada `abstract`, e as subclasses concretas devem implementar `area()`.
- c) o método é executado com corpo vazio.
- d) `area()` só pode ser chamado por métodos `static`.

**5.** (Aula 13) `void imprimir(int x)` e `void imprimir(String s)` na mesma classe são exemplo de:

- a) sobrescrita.
- b) sobrecarga.
- c) herança múltipla.
- d) vinculação dinâmica.

**6.** (Aula 14) Em Clojure, `(+ 1 2 3 4)` vale:

- a) `10`
- b) `(1 2 3 4)`
- c) erro: `+` aceita só dois argumentos
- d) `1234`

**7.** (Aula 14) Qual par está classificado corretamente?

- a) Haskell: impura · Clojure: pura
- b) Haskell: pura · Clojure: impura
- c) Haskell e Clojure: puras
- d) Haskell e Clojure: impuras

**8.** (Aula 14) Uma **função pura**:

- a) sempre recebe exatamente um argumento.
- b) devolve um resultado que depende só dos argumentos e não produz efeitos colaterais.
- c) não pode ser recursiva.
- d) só existe em linguagens orientadas a objetos.

**9.** (Aula 15) Na regra `avo(X, Z) :- pai(X, Y), pai(Y, Z).`, a vírgula significa:

- a) "ou" (disjunção).
- b) "e" (conjunção).
- c) "se e somente se".
- d) separação de argumentos sem valor lógico.

**10.** (Aula 15) A consulta `?- X is 3 * 4.` responde:

- a) `X = 3*4.`
- b) `X = 12.`
- c) `false.`
- d) erro: `is` só compara valores

---

## Parte B — Questões discursivas e de programação (2 pontos cada)

**11.** (Aula 12) Implemente em Java uma classe `Fila` de inteiros com **atributos privados** e os métodos `enfileirar(int)`, `desenfileirar()` e `vazia()`, usando um vetor circular de capacidade fixa. No `main`, enfileire 10, 20 e 30, desenfileire e imprima um valor, enfileire 40 e esvazie a fila imprimindo os valores. Explique como o encapsulamento protege o estado da fila.

**12.** (Aula 13) Crie uma classe abstrata `Forma` com o método abstrato `area()` e o método concreto `descricao()`, que devolve o nome da forma e a área. Crie `Retangulo` (base × altura) e `Circulo` (π·r²). No `main`, guarde um retângulo 2 × 3 e um círculo de raio 1 num vetor de `Forma` e imprima a descrição de cada um. Aponte no código onde há **polimorfismo dinâmico**.

**13.** (Aula 14) Em Clojure:
a) escreva uma função **recursiva** `soma-digitos` que some os dígitos de um inteiro não negativo (`(soma-digitos 1234)` → 10);\
b) usando `filter`, `map` e `reduce`, calcule a soma dos quadrados dos números **pares** de 1 a 10;\
c) explique por que a versão (b) não tem efeitos colaterais.

**14.** (Aula 15) Uma base Prolog descreve disciplinas e pré-requisitos:

```prolog
prerequisito(plp, algoritmos).
prerequisito(compiladores, plp).
prerequisito(compiladores, automatos).
aprovado(ana, algoritmos).
aprovado(ana, plp).
aprovado(bruno, algoritmos).
```

a) Escreva a regra `pode_cursar(Aluno, Disciplina)`: o aluno pode cursar a disciplina se foi aprovado em **todos** os seus pré-requisitos.\
b) Que resposta dá `?- pode_cursar(ana, compiladores).`? E `?- pode_cursar(bruno, plp).`? Justifique.\
c) Escreva a regra `depende(D, P)`: D depende de P **direta ou indiretamente** (recursiva). O que responde `?- depende(compiladores, algoritmos).`?

**15.** (Aulas 12, 14 e 15) Uma turma tem alunos com nome e média. Queremos a lista dos **aprovados** (média ≥ 6). Descreva — e esboce em código — como esse problema é resolvido nos paradigmas **orientado a objetos**, **funcional** e **lógico**. Em qual deles o programador diz "como" e em qual diz "o quê"?


<!-- nav:rodape -->

---

← [Simulado 02 — Fundamentos e paradigma imperativo (Aulas 02–…](simulado-02.md)

**Links para esta página (5):** [04 — Provas e Avaliações](../README.md) · [Simulado 03 · Resolução comentada](resolucao-simulado-03.md) · [06 — Revisões e Sínteses](../../06%20-%20Revisões%20e%20Sínteses/README.md) · [P2 — Estruturas encadeadas em C++: pilha e fila](../../09%20-%20Projetos%20Práticos/P2%20-%20Estruturas%20Encadeadas%20em%20C++/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../README.md)

<!-- /nav:rodape -->
