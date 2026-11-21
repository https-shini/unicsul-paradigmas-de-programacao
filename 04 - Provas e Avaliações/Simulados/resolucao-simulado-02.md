<!-- nav:topo -->
[Início](../../README.md) › [04 - Provas e Avaliações](../README.md) › [Simulados](README.md) · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Simulado 02 · Resolução comentada

> **[Resolução elaborada]** Resolução do [simulado autoral](simulado-02.md). **Não é gabarito oficial do professor.** Os trechos de código foram compilados e executados.

## Gabarito da Parte A

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| b | a | c | b | b | b | c | b | a | b |

---

## Parte A — comentários

**1 — b.** A **simplicidade** é uma das características que influenciam a legibilidade: quanto mais formas de fazer a mesma coisa, mais o leitor precisa conhecer (Sebesta 1.3; quadro de critérios no [resumo da Aula 02](../../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md)). A multiplicidade pode até ajudar a **escrita**, mas não a leitura.

**2 — a.** A análise **léxica** agrupa os caracteres em lexemas e os classifica em tokens; a sintática organiza os tokens em árvore ([Aula 03](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)).

**3 — c.** `soma` (identificador), `=`, `x` (identificador), `+`, `10` (constante), `;` → **6** tokens ([Aula 04](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)).

**4 — b.** `static` numa local mantém o **escopo local** e estende o **tempo de vida** ao programa inteiro: o valor sobrevive entre chamadas ([Aula 05](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)).

<!-- teste: saida-contem="1\n2\n3" -->
```c
#include <stdio.h>
void conta(void) {
    static int contador = 0;   /* inicializada uma única vez */
    contador++;
    printf("%d\n", contador);
}
int main(void) { conta(); conta(); conta(); return 0; }
```

**5 — b.** `my` cria variável de escopo **estático (léxico)**; `local` salva o valor de uma global e o substitui durante a execução do bloco, visível pelas funções chamadas — escopo **dinâmico**. **[Complemento]** A Aula05 ([p.9–12](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/01%20-%20Slides%20Originais/README.md#página-9)) só diz que Perl permite declarar variáveis com escopo dinâmico; as palavras `my` e `local` são a sintaxe da linguagem para os dois casos.

**6 — b.** Coerção é a conversão **implícita**. A conversão explícita (`(int) x`) é um *cast* ([Aula 06](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)).

**7 — c.** O registro é **heterogêneo** e acessado por nome de campo (`aluno.nota`); a matriz é **homogênea** e acessada por índice ([Aula 07](../../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)).

**8 — b.** `p` guarda o endereço de `x`; `*p = 5` escreve no endereço apontado, ou seja, em `x` ([Aula 08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)).

**9 — a.** É o refinamento sucessivo (*top-down*) da abstração procedural ([Aula 10](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md)).

**10 — b.** O formal aparece no **cabeçalho** do subprograma; o real (argumento), na **chamada**. Qualquer expressão pode ser argumento numa passagem por valor ([Aula 11](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)).

---

## Parte B — respostas-modelo

## 11

**Conceitos:** implementação (Aula03 [p.8–14](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/01%20-%20Slides%20Originais/README.md#página-8)); tipagem estática × dinâmica (Aula06 [p.9–14](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/01%20-%20Slides%20Originais/README.md#página-9)).

- O conceito **decisivo** é a **tipagem**. Em Java (tipagem **estática**), o tipo de cada variável é conhecido na compilação, e o compilador verifica **todas** as operações do programa, inclusive as de ramos que raramente executam.
- Em Python (tipagem **dinâmica**), o tipo só é conhecido quando o valor existe, em execução. O erro só aparece quando aquela linha roda — no último dia do mês.
- A **implementação** influencia, mas não decide: compiladores costumam fazer verificação estática, e interpretadores não. Porém Python também é compilado para bytecode e, mesmo assim, não detecta o erro, porque não há tipos declarados para verificar.
- **Consequência:** a tipagem estática aumenta a **confiabilidade** (erros detectados antes da execução); a dinâmica dá mais flexibilidade de escrita e exige mais testes.

## 12

**Conceitos:** escopo estático × dinâmico (Aula05 [p.9–12](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/01%20-%20Slides%20Originais/README.md#página-9)).

**(a)** Em C (escopo **estático**), `mostra` foi definida no nível global; seu `x` não local é sempre o **global**:

<!-- teste: saida-contem="1\n1" -->
```c
#include <stdio.h>
int x = 1;
void mostra(void) { printf("%d\n", x); }
void a(void) { int x = 2; (void) x; mostra(); }
void b(void) { int x = 3; (void) x; a(); }
int main(void) { b(); mostra(); return 0; }
```

Imprime **1** e **1**.

**(b)** Com escopo **dinâmico**, `x` é procurado na pilha de chamadas, da chamada mais recente para a mais antiga:

| Chamada | Pilha (topo à direita) | `x` encontrado | Imprime |
| --- | --- | --- | --- |
| `main → b → a → mostra` | main, b (x=3), a (x=2), mostra | o de `a` | **2** |
| `main → mostra` | main, mostra | o global | **1** |

Imprimiria **2** e **1**. A mesma função `mostra` exibe valores diferentes conforme quem a chamou — por isso o escopo dinâmico prejudica a legibilidade.

## 13

**Conceitos:** alocação dinâmica, ponteiros, regiões de memória (Aula08 [p.12–14](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/01%20-%20Slides%20Originais/README.md#página-12)).

<!-- teste: entrada="5" saida-contem="0 1 4 9 16" -->
```c
#include <stdio.h>
#include <stdlib.h>

int *quadrados(int n) {
    int *v = malloc(n * sizeof(int));   /* vetor no HEAP */
    if (v == NULL) return NULL;
    for (int i = 0; i < n; i++)
        v[i] = i * i;
    return v;                           /* o vetor sobrevive ao fim da função */
}

int main(void) {
    int n;
    scanf("%d", &n);
    int *q = quadrados(n);              /* q: variável local, na PILHA */
    if (q == NULL) return 1;
    for (int i = 0; i < n; i++)
        printf("%d%s", q[i], i < n - 1 ? " " : "\n");
    free(q);                            /* libera a área do heap */
    return 0;
}
```

- O **vetor** fica no **heap**: foi criado em tempo de execução, com tamanho decidido pela entrada, e não tem nome próprio — só é acessível pelo ponteiro.
- As variáveis `n`, `q` e `i` (e o `v` dentro da função) ficam na **pilha**.
- Devolver o ponteiro funciona porque a área do heap continua existindo depois que `quadrados` retorna; um vetor **local** (`int v[n];`) seria destruído no retorno.
- **Erro comum:** esquecer o `free`, causando vazamento de memória.

## 14

**Conceitos:** programação não estruturada × estruturada (Aula09 [p.16–22](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/README.md#página-16)); artigo de Dijkstra.

<!-- teste: entrada="10" saida-contem="55" -->
```c
#include <stdio.h>
int main(void) {
    int n, s = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        s = s + i;
    printf("%d\n", s);
    return 0;
}
```

**Por que é mais fácil de entender:** na versão estruturada, o progresso do programa é descrito por duas coordenadas simples — a **posição no texto** (estamos no corpo do `for`) e o **número da repetição** (o valor de `i`). Isso permite afirmar, em qualquer ponto, o que `s` contém: a soma de 1 a `i − 1`. Na versão com `goto`, o laço existe, mas está escondido nos saltos, e o leitor precisa reconstruí-lo a partir dos rótulos. Dijkstra chama isso de perda da correspondência entre o **texto estático** e o **processo dinâmico**.

## 15

**Conceitos:** abstração procedural, acoplamento e coesão (Aula10 [p.4–16](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/01%20-%20Slides%20Originais/README.md#página-4)).

<!-- teste: entrada="7 8 9" saida-contem="8.0|Aprovado" -->
```c
#include <stdio.h>

float media(float n1, float n2, float n3) {          /* uma responsabilidade: calcular */
    return (n1 + n2 + n3) / 3;
}

const char *situacao(float m) {                      /* uma responsabilidade: classificar */
    if (m >= 6) return "Aprovado";
    if (m >= 4) return "Exame";
    return "Reprovado";
}

int main(void) {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    float m = media(a, b, c);
    printf("Media: %.1f\nSituacao: %s\n", m, situacao(m));
    return 0;
}
```

- **Abstração procedural:** quem chama `situacao` não precisa saber os limites (6 e 4), só a interface: recebe uma média e devolve um texto. Mudar a regra (por exemplo, exame a partir de 5) altera só essa função.
- **Coesão alta:** cada função faz uma única coisa.
- **Com notas globais:** `media` e `situacao` passariam a ler e escrever variáveis compartilhadas, em vez de receber parâmetros. Isso cria **acoplamento por dados globais** (*common coupling*, na classificação de Stevens, Myers e Constantine): qualquer função pode alterar as notas, e entender ou testar uma função exige conhecer todas as outras que usam as mesmas variáveis.


<!-- nav:rodape -->

---

← [Simulado 01 · Resolução comentada](resolucao-simulado-01.md) · [Simulado 03 · Resolução comentada](resolucao-simulado-03.md) →

**Links para esta página (2):** [04 — Provas e Avaliações](../README.md) · [Simulado 02 — Fundamentos e paradigma imperativo (Aulas 02–…](simulado-02.md)

<!-- /nav:rodape -->
