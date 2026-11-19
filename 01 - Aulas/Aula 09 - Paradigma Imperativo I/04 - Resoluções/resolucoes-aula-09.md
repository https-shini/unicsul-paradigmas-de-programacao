# Aula 09 — Paradigma Imperativo I · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-09.md`](../03%20-%20Exercícios/exercicios-aula-09.md). Os programas C foram compilados e executados com gcc; o BASIC foi analisado sem execução.

## E1

Variáveis, números inteiros, operações aritméticas, atribuição, sequenciamento de comandos baseado em memória, condições e comandos de ramificação (`goto`) (p.9).

## E2

Quaisquer quatro de: expressões e atribuição; estruturas de controle (sequencial, seleção, repetição); entrada/saída; manipulação de exceções e erros; abstração procedural; suporte de biblioteca para estruturas de dados (p.10).

## E3

**Resposta: c.** `:=` é o estilo Algol68 (Pascal, Ada, Eiffel). `=` é o estilo Fortran (C, Java); `==` é comparação em C/Java.

## E4

| Von Neumann | Imperativo |
| --- | --- |
| Células de memória | Variáveis |
| Processador grava o resultado na memória | Atribuição |
| Busca e execução de uma instrução por vez | Sequência de comandos |
| Desvio do contador de programa | `goto`, seleção, repetição |
| Unidade lógica e aritmética | Expressões |

## E5

- **Não estruturada:** controla o fluxo com `goto`/`jump` para linhas ou rótulos. Exemplos: Assembly, BASIC clássico.
- **Estruturada:** usa blocos de seleção e repetição e subprogramas; suporta `goto` sem depender dele, e o objetivo é a legibilidade. Exemplos: Pascal, C, Ada.

## E6

Rastreamento:

| Linha | X | Saída |
| --- | --- | --- |
| 10 | 1 | |
| 20 | 1 | 1 |
| 30 | 2 | |
| 40 | 2 < 20 → GOTO 20 | |
| 20 | 2 | 2 |
| … | 4, 8, 16 | 4, 8, 16 |
| 30 | 32 | |
| 40 | 32 ≥ 20 → segue | |
| 50 | | FIM |

**Saída:** `1 2 4 8 16 FIM`, cada valor numa linha.

## E7 — Atividade 1 (original)

**Descrição:** imprime os inteiros de 0 a 9. O rótulo `repete` marca o início do corpo; depois de imprimir e incrementar, o `if` volta ao rótulo enquanto `x < 10`. É um laço **pós-testado**: executa e depois testa.

**Versão do professor (`while`):** imprime 0 a 9 — mesmo resultado.

**Equivalência exata:** a tradução fiel é `do { printf("%d\n", x); x++; } while (x < 10);`. As versões com `goto` e `while` diferem quando a condição é **falsa logo de início**. Com `int x = 10;`:

- `goto`/`do-while` imprime `10` (executa uma vez antes de testar);
- `while` não imprime nada.

<!-- teste: saida-contem="goto: 10|do-while: 10|while: (nada)" -->
```c
#include <stdio.h>
int main(void) {
    int x;

    x = 10;                                   /* versão com goto */
repete: printf("goto: %d\n", x);
    x++;
    if (x < 10) goto repete;

    x = 10;                                   /* do-while: também pós-testado */
    do { printf("do-while: %d\n", x); x++; } while (x < 10);

    x = 10;                                   /* while: pré-testado */
    int imprimiu = 0;
    while (x < 10) { printf("while: %d\n", x); x++; imprimiu = 1; }
    if (!imprimiu) printf("while: (nada)\n");
    return 0;
}
```

## E8 — Atividade 2 (original)

<!-- teste: entrada="5 -3 8 -1 2 7 -6 4 9 -2" saida-contem="Positivos: 6|Negativos: 4" -->
```c
#include <stdio.h>

int main(void) {
    int n, cont = 0, pos = 0, neg = 0;

le:                                  /* "início do laço" sem usar for/while */
    if (cont == 10) goto fim;        /* já leu 10 números */
    scanf("%d", &n);
    if (n == 0) goto sair;           /* 0 interrompe sem mensagem */
    if (n > 0) pos++;
    else neg++;
    cont++;
    goto le;                         /* volta para ler o próximo */

fim:
    printf("Positivos: %d\nNegativos: %d\n", pos, neg);
sair:
    return 0;
}
```

**Raciocínio:**

1. Sem `for`/`while`, a repetição é construída com um **rótulo** (`le`) e um `goto` incondicional no final do "corpo".
2. A **condição de parada** (10 leituras) é testada no começo, com `goto fim`.
3. O **0** desvia direto para `sair`, que fica **depois** do `printf`, então nada é impresso.
4. O rótulo `fim` cai naturalmente em `sair`, encerrando o programa.

**Testes:** `5 -3 8 -1 2 7 -6 4 9 -2` → Positivos: 6, Negativos: 4. `3 -1 0` → termina sem imprimir nada.

**Erro comum:** colocar o `printf` depois de `sair`, o que imprime a contagem mesmo quando o usuário digita 0.

## E9

<!-- teste: entrada="5 -3 8 -1 2 7 -6 4 9 -2" saida-contem="Positivos: 6|Negativos: 4" -->
```c
#include <stdio.h>

int main(void) {
    int n, pos = 0, neg = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &n);
        if (n == 0) return 0;        /* encerra sem mensagem */
        if (n > 0) pos++; else neg++;
    }
    printf("Positivos: %d\nNegativos: %d\n", pos, neg);
    return 0;
}
```

A versão estruturada é mais curta e o fluxo é visível na indentação. O `return 0` dentro do laço é uma "saída de alarme" — o tipo de desvio que, segundo o artigo, Hoare recomendava como único uso aceitável do `go to`.

## E10 — Perguntas sobre o artigo de Dijkstra

**a)** O **índice textual** é um ponteiro para um lugar no texto do programa, entre duas ações, e basta para descrever o progresso em programas com sequência e condicionais. O **índice dinâmico** é um contador associado a cada laço ativo, que registra o número da iteração corrente. Com procedimentos e laços aninhados, o progresso é descrito por uma sequência mista de índices textuais e dinâmicos.

**b)** Porque o **significado** do valor de uma variável depende justamente do ponto do processo em que estamos. Usar variáveis para definir o progresso seria circular: precisaríamos do progresso para interpretar a variável e da variável para definir o progresso.

**c)** Que a mesma variável `n` tem significados diferentes conforme o ponto da execução. Logo após alguém entrar, e antes do incremento, `n` vale "pessoas na sala − 1". Para raciocinar sobre o programa, é preciso saber exatamente onde o processo está, o que os índices textuais e dinâmicos fornecem e o `go to` destrói.

**d)** **Böhm e Jacopini** provaram, matematicamente, que o `go to` é **logicamente supérfluo**: qualquer fluxograma pode ser expresso com sequência, seleção e repetição. **Dijkstra** explicou **por que** o `go to` é **prejudicial** — uma questão de inteligibilidade e de nossa limitação para acompanhar processos dinâmicos — e advertiu que a tradução mecânica de Böhm e Jacopini não produz programas mais claros.

## E11

| Slide | Artigo |
| --- | --- |
| "Uso excessivo de `goto`" | Defende a **abolição** do `go to` em linguagens de alto nível |
| Dijkstra "mostrou" que tudo pode ser escrito com laços | A prova é de **Böhm e Jacopini**; Dijkstra só a cita |
| — | A conversão **mecânica** não é recomendada |

A frase do slide é um resumo didático aceitável, mas **suaviza** a posição de Dijkstra e **atribui a ele** um resultado de outros autores. Numa resposta discursiva sobre o artigo, convém usar a versão do artigo.
