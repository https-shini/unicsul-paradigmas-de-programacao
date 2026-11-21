<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 12](../README.md) › [03 - Exercícios](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 12 — Paradigma Orientado a Objetos I · Exercícios

> **[Exercício autoral]**, exceto o E7, que reúne as perguntas originais dos Exemplos 1a–1d ([p.8–14](../01%20-%20Slides%20Originais/README.md#página-8)). Base: [`Aula12_ParadigmaOrientadoObjetos1.pdf`](../01%20-%20Slides%20Originais/Aula12_ParadigmaOrientadoObjetos1.pdf). Resoluções: [`resolucoes-aula-12.md`](../04%20-%20Resoluções/resolucoes-aula-12.md)

## Básico

**E1.** O que foi a Crise de Software e quais três qualidades a OO buscava melhorar? Defina cada uma.

**E2.** Quais são os três recursos principais em que a POO se baseia?

**E3.** (Objetiva) Qual modificador permite o acesso apenas pela própria classe e por suas classes derivadas?
a) `public`  b) `private`  c) `protected`  d) `static`

## Intermediário

**E4.** Defina tipo de dado abstrato (Sebesta) e encapsulamento (Tucker e Noonan). Qual é a relação entre os dois?

**E5.** "Todas as instâncias compartilham o mesmo conjunto de métodos, mas cada instância tem seu próprio conjunto de atributos." Explique com um exemplo de duas pilhas.

**E6.** Quais são as duas formas de criar uma classe em C++? Qual é a vantagem de cada uma?

## Avançado

**E7 — Perguntas originais dos Exemplos 1a–1d.**
a) (1a) Há algum tipo de abstração no programa?\
b) (1b) A única forma de incluir e retirar elementos é por `push` e `pop`? O que isso significa em termos de abstração?\
c) (1c) É possível interagir com `vetPilha` no `main`? Se o armazenamento mudar para alocação encadeada, é preciso mudar o `main`?\
d) (1d) A troca para alocação encadeada exigiu mudanças no `main`? O que isso significa?

**E8.** (Programação) Implemente em Java uma classe `Fila` (o primeiro a entrar é o primeiro a sair) com `enfileirar(int)` e `desenfileirar()`, usando vetor circular e atributos privados. Escreva um `main` que funcione igual ao da pilha.

**E9.** Na pilha encadeada em C++, por que `pop` precisa fazer `delete` no nó removido, se o destrutor `~Pilha()` já libera os nós? O que aconteceria sem esse `delete`? Por que a versão Java não precisa disso?

## Aprofundamento

**E10.** As versões da pilha devolvem −1 quando ela está vazia. Que problema isso causa? Reescreva o `pop` da versão 1c usando exceção e ajuste o `main`.

**E11.** Explique por que a ausência de "mecanismos automáticos de inicialização e finalização" nos pacotes dos anos 1980 foi um problema e como construtores e destrutores o resolvem.


<!-- nav:rodape -->

---

**Aula 12:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-12.md) · **Exercícios** · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-12.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 11 · Exercícios](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/03%20-%20Exercícios/exercicios-aula-11.md) · [Aula 13 · Exercícios](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/03%20-%20Exercícios/exercicios-aula-13.md) →

**Links para esta página (4):** [Aula 12 · Resoluções](../04%20-%20Resoluções/resolucoes-aula-12.md) · [Aula 12 · visão geral](../README.md) · [Revisão da Unidade 3 — Paradigma orientado a objetos (Aulas…](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-3-orientacao-a-objetos.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
