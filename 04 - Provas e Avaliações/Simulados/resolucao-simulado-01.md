<!-- nav:topo -->
[Início](../../README.md) › [04 - Provas e Avaliações](../README.md) › [Simulados](README.md) · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Simulado 01 · Resolução comentada

> **[Resolução elaborada]** Resolução do [simulado autoral](simulado-01.md). **Não é gabarito oficial do professor.** Os trechos de código foram compilados e executados.

## Gabarito da Parte A

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| b | b | c | b | c | b | c | b | b | c |

---

## Parte A — comentários

**1 — b.** O `javac` gera **bytecode**, que é independente de plataforma; a JVM o interpreta (e pode compilá-lo com JIT). (a) é compilação pura. (c) a JVM não lê código-fonte. (d) a híbrida é, em geral, mais rápida que a interpretação pura. → [Aula 03](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

**2 — b.** Todos os lexemas formam tokens válidos; o erro é a **estrutura** (parêntese sem fechar). É o exemplo do slide. → [Aula 04](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

**3 — c.** Estático: `f` foi definida no nível global, então seu `n` não local é o global (10). Dinâmico: procura-se `n` na pilha de chamadas; o chamador `g` tem `n = 20`. O C usa escopo estático:

<!-- teste: saida-contem="10" -->
```c
#include <stdio.h>
int n = 10;
void f(void) { printf("%d\n", n); }
void g(void) { int n = 20; (void) n; f(); }
int main(void) { g(); return 0; }
```

**4 — b.** Java define os tipos na compilação e recusa conversões com perda sem *cast*; PHP define os tipos em execução e faz coerção entre string e número. → [Aula 06](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)

**5 — c.** Por linhas: endereço = base + (i · nº de colunas + j) · tamanho = 1000 + (2 · 4 + 1) · 4 = 1000 + 36 = **1036**. Verificação em C (o deslocamento independe do endereço real):

<!-- teste: saida-contem="deslocamento = 36" -->
```c
#include <stdio.h>
int main(void) {
    int m[3][4];
    long desl = (char*)&m[2][1] - (char*)&m[0][0];
    printf("deslocamento = %ld bytes (sizeof(int) = %zu)\n", desl, sizeof(int));
    return 0;
}
```

**6 — b.** `new int[5]` aloca 5 inteiros no **heap**; o ponteiro é uma variável local, na **pilha**. A liberação é com `delete[] v`. Não confunda com `new int(5)`, que aloca **um** inteiro com valor 5 (o erro do slide da [Aula 08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)).

**7 — c.** O artigo defende **abolir** o `goto` das linguagens de alto nível, por destruir os índices textuais e dinâmicos. (a) é a formulação do slide, menos precisa. (d) a prova é de Böhm e Jacopini. → [resumo do artigo](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)

**8 — b.** `out` = semântica de saída, implementada por referência; o compilador exige atribuição antes do retorno. (c) descreve `in`. → [Aula 11](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

**9 — b.** (a) troca sobrecarga por sobrescrita. (c) Java tem herança simples de classes. (d) interfaces só têm constantes. → [Aula 13](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

**10 — c.** O único fato que unifica com `pai(X, renata)` é `pai(carlos, renata)`.

<!-- teste: consulta="pai(X, renata)." saida-contem="X = carlos" -->
```prolog
pai(joao, ana).
pai(joao, carlos).
pai(carlos, renata).
```

---

## Parte B — respostas-modelo

### 11

**Conceitos:** arquitetura de von Neumann, modelo imperativo. **Fontes:** Aula02; Aula09 [p.3–7](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/README.md#página-3).

Na arquitetura de von Neumann, **dados e instruções ficam na mesma memória**, separada da **CPU**, e as instruções são buscadas e executadas em sequência (ciclo busca–decodifica–executa), com tráfego constante entre memória e processador. As linguagens imperativas são **abstrações diretas** dessa máquina:

- **Variáveis** abstraem as **células de memória** (nome → endereço).
- A **atribuição** abstrai o movimento de dados entre a CPU e a memória: calcula na CPU e grava o resultado numa célula.
- A **repetição** (laços) é a forma eficiente de executar sequências de instruções armazenadas lado a lado na memória, usando desvios.

Por isso o estado do programa é o conteúdo da memória num instante, e a computação é uma sequência de mudanças desse estado. A dependência desse "gargalo" entre CPU e memória foi a crítica de Backus que motivou o paradigma funcional (Aula14).

### 12

**Conceitos:** abstração de dados, TDA, encapsulamento. **Fontes:** Aula10 [p.15–18](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/01%20-%20Slides%20Originais/README.md#página-15); Aula12.

O conceito é o **tipo abstrato de dados** com **encapsulamento**. O `main` só conhece a **interface** da pilha (`push`, `pop`, `vazia`), e a **representação** (vetor ou lista encadeada) fica oculta, inacessível aos clientes. Trocar a representação não muda a interface, logo não afeta quem a usa.

- **Baixo acoplamento:** o `main` depende só das operações, não dos detalhes internos. Mudanças na implementação não se propagam.
- **Alta coesão:** tudo que diz respeito à pilha (dados e operações) está reunido numa única unidade, com uma responsabilidade.

**Erro comum:** dizer que o conceito é a abstração **procedural**. A abstração procedural sozinha não oculta a representação dos dados e não favorece baixo acoplamento nem alta coesão.

### 13

**Conceitos:** modelos de passagem. **Fonte:** Aula11 [p.13–19](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/01%20-%20Slides%20Originais/README.md#página-13).

| Modo | Impresso | Justificativa |
| --- | --- | --- |
| (a) Por valor | **1 2** | `a` e `b` são cópias; a troca acontece nas cópias e se perde ao retornar |
| (b) Por referência | **2 1** | `a` e `b` são apelidos de `x` e `y`; a troca acontece nas próprias variáveis |
| (c) Por valor-resultado | **2 1** | `a` e `b` recebem cópias (1, 2), trocam (2, 1) e, no retorno, os valores são **copiados de volta** para `x` e `y` |

Simulação de (a) e (b) em C, com cópia e com ponteiros:

<!-- teste: saida-contem="valor: 1 2|referencia: 2 1" -->
```c
#include <stdio.h>
void trocaValor(int a, int b)        { int t = a; a = b; b = t; (void)a; (void)b; }
void trocaReferencia(int *a, int *b) { int t = *a; *a = *b; *b = t; }
int main(void) {
    int x = 1, y = 2;
    trocaValor(x, y);       printf("valor: %d %d\n", x, y);
    trocaReferencia(&x, &y); printf("referencia: %d %d\n", x, y);
    return 0;
}
```

(b) e (c) só dão resultados diferentes quando há *aliasing* entre parâmetros, ou quando o subprograma acessa o argumento por outro caminho (por exemplo, como variável global). Na própria `troca`, `troca(x, x)` dá o mesmo resultado nos dois modelos. A diferença aparece, por exemplo, em `p(a, a)` com `x ← x + 1; y ← y * 10` e `a = 2`: 30 por referência e 20 (ou 3) por valor-resultado. Ver o [resumo da Aula 11, §5](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md#5-modelos-de-passagem-de-parâmetros-semânticos-e-de-implementação-p1318).

### 14

**Conceitos:** notação prefixa, aninhamento, tipo `Ratio`. **Fonte:** Aula14 [p.13–20](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/01%20-%20Slides%20Originais/README.md#página-13).

Expressão: `(/ (* (+ 7 3) (- 7 3)) 2)` → (10 · 4) / 2 = **20**.

<!-- teste: saida-contem="20" -->
```clojure
(println (/ (* (+ 7 3) (- 7 3)) 2))
```

`(/ 7 2)` em Clojure (na JVM) resulta em **`7/2`**, um número do tipo **`Ratio`** (fração exata), e não em `3`. Clojure não trunca a divisão de inteiros como C e Java. Para o quociente inteiro, usa-se `(quot 7 2)` → 3; para o resto, `(rem 7 2)` → 1; para decimal, `(/ 7.0 2)` → 3.5.

> **[Atenção]** No ClojureScript (usado nos testes deste repositório), não existe `Ratio`, e `(/ 7 2)` dá `3.5`. Na prova, use o comportamento do Clojure da aula (JVM).

### 15

**Conceitos:** modelagem OO × lógica, abordagem declarativa. **Fontes:** Aulas 12, 14 e 15.

**Orientado a objetos:** classes `Pessoa` (com subclasses `Gerente`, `Visitante`…), `Sala`, `Andar`. Cada classe teria um método `podeAcessar(Sala)`, sobrescrito nas subclasses (polimorfismo). As regras ficam **espalhadas** no código dos métodos, e uma regra nova exige alterar ou criar classes. O programador codifica **como** verificar cada caso.

**Lógico:** as pessoas, cargos e salas viram **fatos**, e cada política vira uma **regra**. O motor de inferência responde consultas como `pode_acessar(ana, s204)` e também `pode_acessar(Quem, s204)` — **quem** pode entrar —, sem código extra.

<!-- teste: consulta="pode_acessar(Quem, s204)." saida-contem="Quem = ana" -->
```prolog
cargo(ana, gerente).      andar_pessoa(ana, 2).
cargo(bruno, visitante).
sala(s204, 2).            sala(recepcao, 0).

pode_acessar(P, S) :- cargo(P, gerente), andar_pessoa(P, A), sala(S, A).
pode_acessar(P, recepcao) :- cargo(P, visitante).
```

**Escolha:** para o **motor de regras**, o paradigma **lógico**, porque as políticas são justamente fatos e regras, ficam declaradas num só lugar, são fáceis de auditar e alterar, e a mesma base responde perguntas em várias direções. A OO continua adequada para o **restante** do sistema (interface, persistência, integração). Combinar os dois é a ideia de linguagens e sistemas multiparadigma.


<!-- nav:rodape -->

---

[Simulado 02 · Resolução comentada](resolucao-simulado-02.md) →

**Links para esta página (2):** [04 — Provas e Avaliações](../README.md) · [Simulado 01 — Paradigmas de Linguagens de Programação](simulado-01.md)

<!-- /nav:rodape -->
