<!-- nav:topo -->
[Início](../README.md) › [06 - Revisões e Sínteses](README.md) · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# Questões integradoras

> **[Exercício autoral]** Questões que combinam conteúdos de **várias aulas**. Não são do professor. Resolução comentada em [resolucao-questoes-integradoras.md](resolucao-questoes-integradoras.md); tente responder antes de consultá-la.
> Níveis: 🟢 intermediário · 🟠 avançado · 🔴 aprofundamento.

---

**QI1 🟢 (Aulas 03, 06)** Java é estaticamente tipado e implementado de forma híbrida; Python é dinamicamente tipado e normalmente interpretado. Explique por que a **verificação de tipos** e o **método de implementação** são escolhas relacionadas, mas independentes. Dê um exemplo de linguagem compilada com tipagem dinâmica ou de linguagem interpretada com tipagem estática.

**QI2 🟢 (Aulas 05, 08)** Para cada variável do programa abaixo, indique **escopo**, **tempo de vida** e **região de memória**.

```c
#include <stdlib.h>
int total = 0;
void soma(int x) {
    static int chamadas = 0;
    int *p = malloc(sizeof(int));
    *p = x;
    total += *p;
    chamadas++;
    free(p);
}
int main(void) { soma(3); soma(4); return 0; }
```

**QI3 🟠 (Aulas 08, 11)** Escreva em C uma função `minmax` que receba um vetor e seu tamanho e devolva **ao mesmo tempo** o menor e o maior valor. Explique qual modelo de passagem cada parâmetro usa e por que C não precisa copiar o vetor.

**QI4 🟠 (Aulas 09, 10)** O trecho abaixo usa `goto`. (a) Descreva o que ele faz. (b) Reescreva-o de forma estruturada. (c) Relacione a reescrita com o argumento de Dijkstra sobre índices textuais e dinâmicos.

```c
int i = 1, s = 0;
inicio:
    if (i > 10) goto fim;
    if (i % 2 == 0) s = s + i;
    i++;
    goto inicio;
fim:
    printf("%d\n", s);
```

**QI5 🟠 (Aulas 10, 12)** Uma equipe implementou um cadastro de alunos em C com três vetores globais (`nomes`, `notas`, `faltas`) e funções que os acessam diretamente. Analise o projeto quanto a **acoplamento**, **coesão** e **encapsulamento**, e proponha a estrutura de uma classe Java `Aluno` e de uma classe `Turma` que resolvam os problemas.

**QI6 🟠 (Aulas 06, 13)** O operador `+` em Java soma inteiros, soma reais e concatena strings. Isso é sobrecarga, sobrescrita ou coerção? E em `"Total: " + 5`? Justifique com os conceitos das Aulas 06 e 13.

**QI7 🔴 (Aulas 02, 14, 15)** Calcule a soma dos quadrados dos números de 1 a 4 em três paradigmas: **imperativo** (C, com laço), **funcional** (Clojure, sem atribuição) e **lógico** (Prolog, com regra recursiva). Compare como cada versão trata o **estado**.

**QI8 🔴 (Aulas 02, 09, 12, 14, 15)** "O paradigma imperativo é o mais natural, porque corresponde ao modo como o computador funciona." Discuta a afirmação, considerando os critérios de avaliação da Aula 02 e os argumentos dos paradigmas funcional e lógico. Conclua indicando um tipo de problema em que **cada um** dos quatro paradigmas seria a escolha mais adequada.


<!-- nav:rodape -->

---

**Links para esta página (7):** [Objetivos da disciplina](../00%20-%20Planejamento%20e%20Organização/objetivos-da-disciplina.md) · [02 — Listas de Exercícios](../02%20-%20Listas%20de%20Exercícios/README.md) · [06 — Revisões e Sínteses](README.md) · [Guia de estudo para as avaliações](guia-de-estudo-para-provas.md) · [Questões integradoras · Resolução comentada](resolucao-questoes-integradoras.md) · [Resumo geral da disciplina](resumo-geral-da-disciplina.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../README.md)

<!-- /nav:rodape -->
