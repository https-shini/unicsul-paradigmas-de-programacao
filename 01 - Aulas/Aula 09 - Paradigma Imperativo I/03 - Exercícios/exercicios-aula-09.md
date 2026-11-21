# Aula 09 — Paradigma Imperativo I · Exercícios

> **[Exercício autoral]**, exceto o E7 e o E8 (Atividades 1 e 2 originais, p.21 e p.24). Base: [`Aula09_ParadigmaImperativo1.pdf`](../01%20-%20Slides%20Originais/Aula09_ParadigmaImperativo1.pdf) e [`Aula09a_ArtigoDijkstra68.pdf`](../01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf). Resoluções: [`resolucoes-aula-09.md`](../04%20-%20Resoluções/resolucoes-aula-09.md)

## Básico

**E1.** Quais são os requisitos para que uma linguagem imperativa seja completa quanto a Turing?

**E2.** Cite quatro características que surgiram com a evolução das linguagens imperativas.

**E3.** (Objetiva) Qual operador de atribuição é usado em Pascal e Ada?
a) `=`  b) `==`  c) `:=`  d) `<-`

## Intermediário

**E4.** Relacione cada elemento da arquitetura de von Neumann com uma construção das linguagens imperativas.

**E5.** Diferencie programação estruturada de não estruturada e dê um exemplo de linguagem de cada grupo.

**E6.** (Interpretação de código) Qual é a saída do programa BASIC abaixo?

```basic
10 LET X = 1
20 PRINT X
30 LET X = X * 2
40 IF X < 20 THEN GOTO 20
50 PRINT "FIM"
```

## Avançado

**E7 — Atividade 1 (original, p.21).** Descreva o que faz o programa e reescreva-o sem `goto`. *Acréscimo autoral:* a versão com `while` é exatamente equivalente? Em que situação as duas dariam resultados diferentes?

```c
#include <stdio.h>   /* acrescentado: o slide omite o cabeçalho */
int main() {
    int x = 0;
repete: printf("%d\n", x);
    x++;
    if (x < 10)
        goto repete;
    return 0;
}
```

**E8 — Atividade 2 (original, p.24).** Usando o comando `goto`, crie um programa que leia 10 números inteiros e mostre, no final, quantos são positivos e quantos são negativos. Se o usuário digitar 0, o programa deve terminar sem mensagem. Não use estruturas de repetição.

**E9.** Reescreva o programa do E8 de forma estruturada (sem `goto`), em C.

## Aprofundamento

**E10 — Sobre o artigo de Dijkstra.**
a) O que é um índice textual? E um índice dinâmico?\
b) Por que não podemos usar os valores das variáveis como coordenadas do progresso?\
c) O que o exemplo da contagem de pessoas na sala demonstra?\
d) Qual é a diferença entre a contribuição de Böhm e Jacopini e a de Dijkstra?

**E11.** O slide resume que Dijkstra mostrou que "o uso excessivo de `goto` era prejudicial". Compare essa frase com o que o artigo realmente afirma.
