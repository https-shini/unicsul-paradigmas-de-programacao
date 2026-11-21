# Mapas conceituais

> **[Explicação elaborada]** Mapas em [Mermaid](https://mermaid.js.org/), renderizados automaticamente pelo GitHub. Cada mapa resume as relações entre os conceitos de uma parte da disciplina; os detalhes estão nos resumos das aulas indicadas. Legenda: [Convenções](../README.md#convenções-de-marcação).

## Sumário

1. [Mapa geral da disciplina](#1-mapa-geral-da-disciplina)
2. [Da linguagem à execução](#2-da-linguagem-à-execução-aulas-0304)
3. [A variável e seus atributos](#3-a-variável-e-seus-atributos-aulas-0508)
4. [Sistemas de tipos](#4-sistemas-de-tipos-aulas-0607)
5. [Do imperativo à orientação a objetos](#5-do-imperativo-à-orientação-a-objetos-aulas-0913)
6. [Passagem de parâmetros](#6-passagem-de-parâmetros-aulas-08-e-11)
7. [Paradigmas funcional e lógico](#7-paradigmas-funcional-e-lógico-aulas-1415)

---

## 1. Mapa geral da disciplina

```mermaid
flowchart TB
    PLP["Paradigmas de Linguagens de Programação"]
    PLP --> FUND["Fundamentos<br/>Aulas 02–08"]
    PLP --> PAR["Paradigmas<br/>Aulas 09–15"]

    FUND --> EVO["Evolução e critérios<br/>(02)"]
    FUND --> IMP["Implementação<br/>(03)"]
    FUND --> SIN["Sintaxe<br/>(04)"]
    FUND --> SEM["Semântica e variáveis<br/>(05)"]
    FUND --> TIP["Tipos e tipos compostos<br/>(06–07)"]
    FUND --> PON["Ponteiros e memória<br/>(08)"]

    PAR --> PROC["Abordagem procedural"]
    PAR --> DECL["Abordagem declarativa"]
    PROC --> IMPE["Imperativo<br/>(09–11)"]
    PROC --> OO["Orientado a objetos<br/>(12–13)"]
    PROC --> FUN["Funcional<br/>(14)*"]
    DECL --> LOG["Lógico<br/>(15)"]

    IMPE -- "TDA e encapsulamento" --> OO
    SEM -. "variável = célula de memória" .-> IMPE
    PON -. "objetos no heap" .-> OO
```

\* Classificação do professor (Aula15 p.3–5). Boa parte da literatura classifica o funcional como declarativo.

## 2. Da linguagem à execução (Aulas 03–04)

```mermaid
flowchart LR
    SRC["Programa-fonte"] --> LEX["Análise léxica<br/>lexemas → tokens"]
    LEX --> SINT["Análise sintática<br/>tokens → árvore"]
    SINT --> SEMA["Análise semântica<br/>tipos, declarações"]
    SEMA --> GER{"Implementação"}
    GER -- "Compilação" --> MAQ["Código de máquina<br/>executado pela CPU"]
    GER -- "Híbrida" --> BC["Bytecode / CIL"] --> VM["Máquina virtual<br/>JVM / CLR (+ JIT)"]
    GER -- "Interpretação pura" --> INT["Interpretador executa<br/>instrução a instrução"]
```

## 3. A variável e seus atributos (Aulas 05–08)

```mermaid
flowchart TB
    VAR(("Variável"))
    VAR --> N["Nome<br/>regras de identificadores (04)"]
    VAR --> E["Endereço<br/>célula de memória; ponteiros (08)"]
    VAR --> V["Valor<br/>conteúdo da célula"]
    VAR --> T["Tipo<br/>valores e operações (06)"]
    VAR --> TV["Tempo de vida<br/>QUANDO existe"]
    VAR --> ES["Escopo<br/>ONDE é visível"]
    ES --> EST["Estático<br/>pelo texto"]
    ES --> DIN["Dinâmico<br/>pela pilha de chamadas"]
    TV --> R1["Estático: programa inteiro"]
    TV --> R2["Pilha: duração da chamada"]
    TV --> R3["Heap: de new até delete / GC"]
```

## 4. Sistemas de tipos (Aulas 06–07)

```mermaid
flowchart TB
    TIPO["Sistema de tipos"]
    TIPO --> QUANDO["Quando o tipo é definido?"]
    TIPO --> FORCA["Quão exigente é?"]
    TIPO --> CAT["Categorias de tipos"]
    QUANDO --> SE["Estática: na compilação<br/>C, Java"]
    QUANDO --> DI["Dinâmica: na execução<br/>Python, PHP"]
    FORCA --> FO["Forte: detecta os erros de tipo; pouca coerção implícita<br/>Java, Python"]
    FORCA --> FR["Fraca: muita coerção implícita<br/>C, PHP"]
    CAT --> PRIM["Primitivos<br/>int, float, char, boolean"]
    CAT --> COMP["Compostos (07)"]
    COMP --> ENUM["Enumeração"]
    COMP --> REG["Registro / struct"]
    COMP --> MAT["Matriz<br/>row-major em C"]
    COMP --> STR["String"]
```

## 5. Do imperativo à orientação a objetos (Aulas 09–13)

```mermaid
flowchart TB
    VN["Arquitetura de von Neumann"] --> IMP["Paradigma imperativo<br/>variáveis + atribuição + repetição"]
    IMP --> NE["Não estruturado<br/>goto"]
    NE -- "Böhm-Jacopini 1966<br/>Dijkstra 1968" --> EST["Programação estruturada<br/>sequência, seleção, repetição"]
    EST --> AP["Abstração procedural<br/>funções, refinamento sucessivo"]
    AP -- "limites: acoplamento e coesão" --> AD["Abstração de dados<br/>TDA + encapsulamento"]
    AD --> CL["Classe e objeto"]
    CL --> HER["Herança<br/>simples, múltipla, interfaces"]
    CL --> ENC["Modificadores de acesso"]
    CL --> CICLO["Construtor, destrutor, GC"]
    HER --> POL["Polimorfismo"]
    POL --> PE["Estático: sobrecarga"]
    POL --> PD["Dinâmico: sobrescrita"]
```

## 6. Passagem de parâmetros (Aulas 08 e 11)

```mermaid
flowchart LR
    P["Passagem de parâmetros"] --> ENT["Entrada"]
    P --> SAI["Saída"]
    P --> ES["Entrada e saída"]
    ENT --> VAL["Por valor<br/>cópia"]
    SAI --> RES["Por resultado<br/>C# out"]
    ES --> VR["Por valor-resultado<br/>cópia na ida e na volta"]
    ES --> REF["Por referência<br/>endereço; C# ref, C++ &"]
    REF --> RO["Só leitura<br/>C# in / ref readonly"]
```

## 7. Paradigmas funcional e lógico (Aulas 14–15)

```mermaid
flowchart TB
    subgraph F["Funcional (14)"]
        FM["Funções matemáticas"] --> FP["Sem estado mutável<br/>sem efeitos colaterais"]
        FP --> REC["Recursão no lugar de laços"]
        FM --> COMPF["Composição e aplicação"]
        COMPF --> CLJ["Clojure: notação prefixa<br/>(+ x (* 2 y))"]
        FM --> PURA["Puras: Haskell, Miranda"]
        FM --> IMPURA["Impuras: LISP, Scheme, Clojure"]
    end
    subgraph L["Lógico (15)"]
        LP["Lógica de predicados"] --> BASE["Base de conhecimento"]
        BASE --> FAT["Fatos<br/>pai(joao, ana)."]
        BASE --> REG["Regras<br/>avo(X,Z) :- pai(X,Y), pai(Y,Z)."]
        CONS["Consulta<br/>?- pai(X, ana)."] --> UNI["Unificação +<br/>backtracking"]
        BASE --> UNI
        UNI --> RESP["Resposta<br/>X = joao"]
    end
    VN2["Crítica ao modelo de von Neumann"] -.-> F
    VN2 -.-> L
```
