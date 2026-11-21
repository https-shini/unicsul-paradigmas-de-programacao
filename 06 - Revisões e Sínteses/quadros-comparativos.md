<!-- nav:topo -->
[Início](../README.md) › [06 - Revisões e Sínteses](README.md) · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# Quadros comparativos

> **[Explicação elaborada]** Tabelas de síntese construídas a partir dos resumos das aulas. Cada quadro indica as fontes (`AulaXX p.N`). As listas de revisão do professor pedem sobretudo para **diferenciar** e **comparar**: estes quadros são o material mais direto para isso.
> Legenda: [Convenções](../README.md#convenções-de-marcação).

## Sumário

1. [Os quatro paradigmas](#1-os-quatro-paradigmas)
2. [Um mesmo problema nos quatro paradigmas](#2-um-mesmo-problema-nos-quatro-paradigmas)
3. [Implementação das linguagens](#3-implementação-das-linguagens)
4. [Níveis de sintaxe](#4-níveis-de-sintaxe)
5. [Escopo e tempo de vida](#5-escopo-e-tempo-de-vida)
6. [Sistemas de tipos](#6-sistemas-de-tipos)
7. [Regiões de memória e alocação](#7-regiões-de-memória-e-alocação)
8. [Passagem de parâmetros](#8-passagem-de-parâmetros)
9. [Programação não estruturada × estruturada](#9-programação-não-estruturada--estruturada)
10. [Abstração procedural × abstração de dados](#10-abstração-procedural--abstração-de-dados)
11. [Herança, interfaces e polimorfismo](#11-herança-interfaces-e-polimorfismo)
12. [Gerenciamento de objetos: C++ × Java](#12-gerenciamento-de-objetos-c--java)
13. [Funcional × imperativo × lógico](#13-funcional--imperativo--lógico)

---

## 1. Os quatro paradigmas

**Fontes:** Aula02 [p.9–13](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/01%20-%20Slides%20Originais/README.md#página-9); Aula09; Aula12; Aula14; Aula15 [p.3–5](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/01%20-%20Slides%20Originais/README.md#página-3).

| Aspecto | Imperativo | Orientado a objetos | Funcional | Lógico |
| --- | --- | --- | --- | --- |
| Ideia central | Sequência de comandos que alteram o estado | Objetos (estado + comportamento) que trocam mensagens | Aplicação e composição de funções matemáticas | Fatos e regras; inferência responde consultas |
| Unidade de modelagem | Variável e procedimento | Classe e objeto | Função | Predicado (fato/regra) |
| Como executa | Comando após comando, com desvios e laços | Chamadas de métodos entre objetos | Avaliação de expressões | Unificação e *backtracking* |
| Estado | Explícito e mutável | Encapsulado nos objetos | Ausente no modelo puro (imutabilidade) | Variáveis lógicas ligadas uma única vez |
| Repetição | Laços (`for`, `while`) | Laços nos métodos | Recursão e funções de ordem superior | Recursão |
| Abordagem (professor) | Procedural | Procedural | Procedural | **Declarativa** |
| Relação com von Neumann | Abstração direta | Herdada do imperativo | Foge do modelo | Foge do modelo |
| Linguagens nas aulas | C, Pascal, C# | Java, C++ | Clojure | Prolog |
| Construto típico | `x = x + 1;` | `pilha.push(5);` | `(+ x (* 2 y))` | `avo(X, Z) :- pai(X, Y), pai(Y, Z).` |

> **[Atenção]** A classificação do funcional como **procedural** é a da Aula15 [p.3–5](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/01%20-%20Slides%20Originais/README.md#página-3). Grande parte da literatura o classifica como **declarativo**. Ver [erratas](erratas-e-inconsistencias.md).

## 2. Um mesmo problema nos quatro paradigmas

**[Exercício autoral]** Fatorial de 5, para comparar a forma de pensar. Todos os trechos foram executados.

**Imperativo (C):** estado (`f`) alterado passo a passo por um laço.

<!-- teste: saida-contem="120" -->
```c
#include <stdio.h>
int main(void) {
    int f = 1;
    for (int i = 2; i <= 5; i++) f = f * i;   /* atribuição + repetição */
    printf("%d\n", f);
    return 0;
}
```

**Orientado a objetos (Java):** o cálculo é responsabilidade de um objeto, que encapsula o seu estado.

<!-- teste: saida-contem="120" -->
```java
class Calculadora {
    private long ultimo;                          // estado encapsulado
    long fatorial(int n) {
        ultimo = 1;
        for (int i = 2; i <= n; i++) ultimo *= i;
        return ultimo;
    }
}
public class Main {
    public static void main(String[] args) {
        Calculadora c = new Calculadora();       // objeto
        System.out.println(c.fatorial(5));       // mensagem
    }
}
```

**Funcional (Clojure):** nenhuma variável é alterada; o resultado é uma expressão recursiva.

<!-- teste: saida-contem="120" -->
```clojure
(defn fatorial [n]
  (if (<= n 1)
    1
    (* n (fatorial (- n 1)))))
(println (fatorial 5))
```

**Lógico (Prolog):** declara-se **o que** é o fatorial; o motor de inferência encontra o valor.

<!-- teste: consulta="fatorial(5, F)." saida-contem="F = 120" -->
```prolog
fatorial(0, 1).
fatorial(N, F) :- N > 0, N1 is N - 1, fatorial(N1, F1), F is N * F1.
```

## 3. Implementação das linguagens

**Fonte:** Aula03 [p.8–14](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/01%20-%20Slides%20Originais/README.md#página-8).

| | Compilação | Interpretação pura | Híbrida |
| --- | --- | --- | --- |
| Tradução | Todo o programa, antes da execução | Instrução a instrução, durante a execução | Fonte → código intermediário (compilação); intermediário → execução (interpretação/JIT) |
| Resultado | Executável em código de máquina | Nenhum arquivo traduzido | Bytecode (`.class`) / CIL |
| Velocidade | Alta | Baixa | Intermediária (alta com JIT) |
| Portabilidade | Baixa: um executável por plataforma | Alta: basta o interpretador | Alta: basta a VM |
| Erros | Muitos detectados antes da execução | Só durante a execução | Muitos detectados na compilação |
| Exemplos (slides) | C, C++, Fortran, Pascal | Python, JavaScript, PHP, Lisp | Java (JVM), C#, VB.NET (CLR) |

## 4. Níveis de sintaxe

**Fonte:** Aula04 [p.5–10](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/01%20-%20Slides%20Originais/README.md#página-5).

| Nível | Trata de | Unidade | Formalismo | Erro típico |
| --- | --- | --- | --- | --- |
| Léxica | Formação dos símbolos | Lexema → token | Expressões regulares | `int 1x;` (identificador inválido) |
| Concreta | Combinação de tokens em comandos | Comando, expressão | Gramática livre de contexto (BNF) | `x = (y + 10 * z;` |
| Abstrata | Estrutura essencial, sem pontuação | Árvore sintática abstrata | Árvore | — (representação interna) |

## 5. Escopo e tempo de vida

**Fonte:** Aula05 [p.5–13](../01%20-%20Aulas/Aula%2005%20-%20Semântica/01%20-%20Slides%20Originais/README.md#página-5) (escopo e tempo de vida são atributos da variável).

| | Escopo estático (léxico) | Escopo dinâmico |
| --- | --- | --- |
| Critério de resolução | Posição no **texto** (ancestral textual) | **Sequência de chamadas** em execução |
| Quando é resolvido | Compilação | Execução |
| Legibilidade | Alta: basta ler o código | Baixa: depende de quem chamou |
| Linguagens | C, Java, Pascal, a maioria | APL, LISP antigo; Perl (`local`) e Common LISP como opção |

| Conceito | Pergunta que responde | Exemplo |
| --- | --- | --- |
| **Escopo** | **Onde** no código o nome é visível? | Variável local é visível só no bloco |
| **Tempo de vida** | **Quando** a variável existe na memória? | Local `static` em C: escopo local, tempo de vida do programa inteiro |

## 6. Sistemas de tipos

**Fonte:** Aula06 [p.9–21](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/01%20-%20Slides%20Originais/README.md#página-9).

| | Tipagem **forte** (exigente) | Tipagem **fraca** (permissiva, coerção) |
| --- | --- | --- |
| **Estática** (tipo na compilação) | Java, Ada | C, C++ |
| **Dinâmica** (tipo na execução) | Python | PHP, JavaScript, Perl\* |

\*O slide da p.17 lista Perl como forte; pelo critério da p.21 ela seria mais fraca. Ver [erratas](erratas-e-inconsistencias.md).

| Teste | C | Java | Python | PHP |
| --- | --- | --- | --- | --- |
| `int r = 2.5 + 3;` / equivalente | Compila; `r = 5` (coerção) | Erro de compilação sem `(int)` | — | — |
| `10 + "20"` | — | `"1020"` (concatenação) | `TypeError` | `30` (coerção) |

## 7. Regiões de memória e alocação

**Fonte:** Aula08 [p.12–14](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/01%20-%20Slides%20Originais/README.md#página-12).

| Região | O que guarda | Alocação | Liberação |
| --- | --- | --- | --- |
| Código | Instruções do programa | Carga do programa | Fim do programa |
| Estático | Globais e locais `static` | Compilação | Fim do programa |
| Heap | Dados criados com `new`/`malloc` | Execução, explícita | `delete`/`free` ou coleta de lixo |
| Pilha | Locais, parâmetros, endereço de retorno | Chamada da função | Retorno da função |

## 8. Passagem de parâmetros

**Fontes:** Aula11 [p.13–19](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/01%20-%20Slides%20Originais/README.md#página-13); Aula08 [p.7–11](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/01%20-%20Slides%20Originais/README.md#página-7).

| Modelo | Semântica | Mecanismo | Altera o argumento? | Exemplo |
| --- | --- | --- | --- | --- |
| Por valor | Entrada | Cópia do valor | Não | C (padrão), Java (sempre; para objetos, copia a referência), C# sem modificador |
| Por resultado | Saída | Cópia no retorno | Sim, no retorno | C# `out` (implementado por referência) |
| Por valor-resultado | Entrada e saída | Cópia na entrada e no retorno | Sim, no retorno | Ada `in out` para escalares |
| Por referência | Entrada e saída | Endereço (caminho de acesso) | Sim, imediatamente | C++ `&`, C# `ref`, C com ponteiros |

| Modificador C# | Semântica | Precisa estar inicializado antes? | Método pode alterar? |
| --- | --- | --- | --- |
| *(nenhum)* | Valor | Sim | Só a cópia |
| `ref` | Referência | Sim | Sim |
| `out` | Saída | Não | Deve atribuir |
| `in` / `ref readonly` | Referência só de leitura | Sim | Não |

## 9. Programação não estruturada × estruturada

**Fontes:** Aula09 [p.16–22](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/README.md#página-16); artigo de Dijkstra.

| | Não estruturada | Estruturada |
| --- | --- | --- |
| Controle de fluxo | `goto`/`jump` para rótulos ou linhas | Sequência, seleção e repetição em blocos |
| Correspondência texto × execução | Perdida | Preservada (índices textuais e dinâmicos) |
| Legibilidade e manutenção | Baixa ("código espaguete") | Alta |
| Linguagens | Assembly, BASIC antigo, Fortran antigo | Pascal, C, Java |
| Fundamento | — | Böhm e Jacopini (1966), Dijkstra (1968) |

## 10. Abstração procedural × abstração de dados

**Fontes:** Aula10; Aula12 [p.17–22](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/01%20-%20Slides%20Originais/README.md#página-17).

| | Abstração procedural (processos) | Abstração de dados (TDA) |
| --- | --- | --- |
| O que esconde | **Como** um cálculo é feito | **Como** um tipo é representado |
| O que expõe | Assinatura da função (entrada e saída) | Operações do tipo |
| Unidade | Função/procedimento | Tipo + operações (classe) |
| Acoplamento e coesão | Não favorece baixo acoplamento nem alta coesão | Favorece baixo acoplamento e alta coesão |
| Paradigma | Imperativo | Base da OO |

## 11. Herança, interfaces e polimorfismo

**Fonte:** Aula13 [p.3–13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/01%20-%20Slides%20Originais/README.md#página-3).

| | Herança simples | Herança múltipla | Interfaces (Java) |
| --- | --- | --- | --- |
| Quantas bases | Uma superclasse | Várias superclasses | Uma superclasse + várias interfaces |
| O que se herda | Atributos e métodos | Atributos e métodos | O contrato (assinaturas) |
| Linguagens | Java, C# | C++, Python | Java, C# |
| Problemas | — | Complexidade, eficiência, ambiguidade (diamante) | Implementar todos os métodos |

| | Sobrecarga (polimorfismo estático) | Sobrescrita (polimorfismo dinâmico) |
| --- | --- | --- |
| Definição | Mesmo nome, **parâmetros diferentes** | Subclasse **redefine** método herdado, mesma assinatura |
| Onde | Na mesma classe (ou herdada) | Entre superclasse e subclasse |
| Escolha da versão | Compilação, pela assinatura | Execução, pelo tipo **real** do objeto |

| | Classe abstrata | Interface (modelo clássico) |
| --- | --- | --- |
| Instanciável | Não | Não |
| Atributos de instância | Sim | Não (só constantes) |
| Métodos com corpo | Sim, misturados com abstratos | Não no modelo clássico; desde o Java 8, sim (`default` e `static`) |
| Quantas por classe | Uma (`extends`) | Várias (`implements`) |

## 12. Gerenciamento de objetos: C++ × Java

**Fonte:** Aula12 [p.28–30](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/01%20-%20Slides%20Originais/README.md#página-28).

| | C++ | Java |
| --- | --- | --- |
| Criação | Na pilha (`Pilha p;`) ou no heap (`new Pilha()`) | Sempre no heap (`new`) |
| Liberação | Manual: `delete` (heap) ou fim do bloco (pilha) | Automática: coleta de lixo |
| Destrutor | `~Pilha()`, chamado na liberação | Não há destrutor |
| Risco | Vazamento de memória, ponteiro pendente | Menor controle sobre o momento da liberação |

## 13. Funcional × imperativo × lógico

**Fontes:** Aula14 [p.7–12](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/01%20-%20Slides%20Originais/README.md#página-7); Aula15 [p.3–5](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/01%20-%20Slides%20Originais/README.md#página-3) e [p.11–18](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/01%20-%20Slides%20Originais/README.md#página-11).

| | Imperativo | Funcional | Lógico |
| --- | --- | --- | --- |
| Programa é | Sequência de comandos | Conjunto de funções | Conjunto de fatos e regras |
| Variável | Célula de memória mutável | Nome de um valor (imutável) | Incógnita ligada por unificação |
| Atribuição | Central | Ausente (no modelo puro) | Ausente; usa unificação |
| Repetição | Laços | Recursão | Recursão |
| Efeitos colaterais | Comuns | Ausentes (puro) | Restritos (E/S) |
| O programador diz | **Como** fazer | **Que** funções compor | **O que** é verdade |
| Base teórica | Máquina de von Neumann | Funções matemáticas (cálculo lambda) | Lógica de predicados |


<!-- nav:rodape -->

---

**Links para esta página (9):** [Objetivos da disciplina](../00%20-%20Planejamento%20e%20Organização/objetivos-da-disciplina.md) · [Lista 02 · Resolução](../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md) · [Flashcards (Anki)](Flashcards/README.md) · [06 — Revisões e Sínteses](README.md) · [Guia de estudo para as avaliações](guia-de-estudo-para-provas.md) · [P4 — Estatísticas de texto em Clojure](../09%20-%20Projetos%20Práticos/P4%20-%20Estatísticas%20de%20Texto%20em%20Clojure/README.md) · [P5 — Grade curricular em Prolog](../09%20-%20Projetos%20Práticos/P5%20-%20Grade%20Curricular%20em%20Prolog/README.md) · [Exemplo de anotação: pilha encadeada × pilha em vetor](../10%20-%20Caderno%20de%20Anotações/exemplo-de-anotacao.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../README.md)

<!-- /nav:rodape -->
