<!-- nav:topo -->
[Início](../README.md) › [06 - Revisões e Sínteses](README.md) · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# Resumo geral da disciplina

> **[Explicação elaborada]** Visão integrada das 15 aulas, escrita para ser lida de uma vez antes das avaliações. Cada parágrafo aponta para o resumo detalhado da aula, onde estão as fontes (`AulaXX p.N`). Legenda: [Convenções](../README.md#convenções-de-marcação).

## O fio condutor

A disciplina responde a uma pergunta: **por que existem tantas linguagens, e o que as distingue?** A resposta é construída em três camadas:

1. **Como uma linguagem é definida e executada** — sintaxe, semântica, implementação (Aulas 02–05).
2. **Com que materiais se constrói um programa** — variáveis, tipos, estruturas, ponteiros (Aulas 05–08).
3. **De que maneira se pensa a solução** — os quatro paradigmas: imperativo, orientado a objetos, funcional e lógico (Aulas 09–15).

Um **paradigma** é um modelo de pensamento sobre como resolver problemas com computador ([Aula 02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md)). Linguagens concretas pertencem predominantemente a um paradigma, mas muitas são **multiparadigma**. O objetivo da disciplina é saber **reconhecer** os construtos de cada paradigma e **escolher** o mais adequado a cada problema ([objetivos](../00%20-%20Planejamento%20e%20Organização/objetivos-da-disciplina.md)).

---

## Unidade 1 — Fundamentos das linguagens (Aulas 01–08)

**Evolução e paradigmas ([Aula 02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md)).**
- **Exemplo de abertura:** o mesmo problema (ler dois números e verificar se o segundo é o dobro do primeiro) aparece em Pascal, Java e Prolog. Mostra que a mesma tarefa é expressa de formas muito diferentes.
- **Os quatro paradigmas:**
  - imperativo: comandos que alteram o estado;
  - orientado a objetos: objetos que trocam mensagens;
  - funcional: composição de funções;
  - lógico: fatos, regras e inferência.
- **Restrições de projeto** (p.15–16): arquitetura (von Neumann); configuração técnica (área de aplicação, sistema operacional, IDE, preferências da comunidade); padrões; sistemas legados (exemplo: C++ em relação ao C; contraexemplo: Java em relação ao C++).
- **Critérios de avaliação:** legibilidade, facilidade de escrita, confiabilidade e custo.
- **Gerações de linguagens:** da linguagem de máquina às linguagens declarativas. As figuras do slide divergem sobre as últimas gerações.

**Implementação ([Aula 03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)).** Um programa de alto nível precisa ser traduzido. Há três formas:
- **Compilação** (C, C++): rápida, mas presa à plataforma.
- **Interpretação pura** (Python, PHP, JavaScript, na classificação do slide; o CPython, na verdade, compila para bytecode): portável, mas lenta.
- **Híbrida** (Java, C#): o fonte vira um código intermediário (bytecode/CIL), executado por uma máquina virtual (JVM/CLR). Une portabilidade e bom desempenho.

O computador é visto como camadas de **computadores virtuais** (Sebesta, Fig. 1.2).

**Sintaxe ([Aula 04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)).** A sintaxe é a **forma** dos programas; a semântica, o seu **significado**. A sintaxe tem três níveis:
- **léxico:** lexemas agrupados em tokens segundo padrões;
- **concreto:** tokens combinados em comandos, descritos por BNF;
- **abstrato:** árvore com a estrutura essencial.

A aula também trata das regras de formação de **nomes**: sensibilidade a maiúsculas e minúsculas, palavras reservadas e palavras-chave.

**Semântica e variáveis ([Aula 05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)).** A variável é a abstração central do imperativo e tem **seis atributos**: nome, endereço, valor, tipo, tempo de vida e escopo.
- **Escopo estático:** resolvido pelo texto do programa.
- **Escopo dinâmico:** resolvido pela pilha de chamadas. Prejudica a legibilidade.
- **Tempo de vida:** quando a variável existe na memória.
- **Escopo:** onde ela é visível.

A variável local `static` mostra que escopo e tempo de vida são coisas diferentes. A **semântica estática** (verificável na compilação) se distingue da **dinâmica** (comportamento em execução).

**Tipos ([Aula 06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) e [Aula 07](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)).** O tipo define o conjunto de valores e as operações permitidas. Há dois eixos independentes:
- **Estática × dinâmica:** quando o tipo é definido.
- **Forte × fraca:** quanto a linguagem tolera operações entre tipos diferentes. A **coerção** enfraquece a tipagem.

Exemplos: C é estática e fraca; Java, estática e forte; PHP, dinâmica e fraca; Python, dinâmica e forte.

Tipos compostos:
- **enumerações**;
- **registros** (`struct`);
- **matrizes**: em C, armazenadas por linhas (*row-major*) e acessadas por fórmula de endereço (Fortran usa *column-major*; em Java, uma matriz é um vetor de vetores);
- **strings**.

**Ponteiros ([Aula 08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)).**
- Um ponteiro guarda um **endereço**.
- A memória se divide em código, área estática, heap, área livre e pilha.
- A alocação **dinâmica** (`new`/`malloc`) cria dados sem nome no heap, acessíveis só por ponteiros. É a base de listas, pilhas e árvores.
- A passagem por referência (`&` em C++, ponteiros em C) permite que a função altere a variável do chamador.

---

## Unidade 2 — Paradigma imperativo (Aulas 09–11)

**Origem e estrutura ([Aula 09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md)).**
- O imperativo é a abstração da **arquitetura de von Neumann**: as variáveis abstraem as células de memória, e a atribuição abstrai o fluxo entre memória e CPU.
- Uma linguagem imperativa é **Turing-completa** se tem variáveis, inteiros, aritmética, atribuição, sequência, condição e desvio.
- A programação **não estruturada** usa `goto`.
- **Dijkstra (1968)** mostrou que o `goto` destrói a relação entre o texto do programa e sua execução ([resumo do artigo](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)).
- **Böhm e Jacopini** já haviam provado que sequência, seleção e repetição bastam.
- Daí veio a **programação estruturada**.

**Abstração ([Aula 10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md)).**
- A **abstração procedural** decompõe o problema em funções por refinamento sucessivo (exemplo: ordenação de dez números). Traz organização e reuso, mas não garante **baixo acoplamento** nem **alta coesão**.
- A **abstração de dados** (TDA) reúne a representação e as operações de um tipo e oculta a representação. É a ponte para a OO.

**Subprogramas ([Aula 11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)).**
- Os subprogramas são o mecanismo da abstração procedural, com parâmetros formais e reais.
- Há quatro modelos de passagem: **valor**, **resultado**, **valor-resultado** e **referência**. Em C#: sem modificador = valor; `out` = semântica de resultado (saída), implementada por referência; `ref` = referência (entrada e saída); `in`/`ref readonly` = referência só de leitura. C# não oferece valor-resultado; um exemplo é o `in out` de Ada para escalares.
- Escolher o modelo é um compromisso entre segurança (cópia) e eficiência (referência).

---

## Unidade 3 — Paradigma orientado a objetos (Aulas 12–13)

**Classes e encapsulamento ([Aula 12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)).**
- **Motivação:** sistemas grandes, reuso e manutenção.
- **Fio da aula:** uma **pilha** reescrita várias vezes:
  - tudo no `main`;
  - com métodos `push` e `pop`;
  - como classe `Pilha` com atributos privados;
  - com lista encadeada;
  - em C++, com vetor e com lista encadeada.
  O cliente não muda quando a representação muda.
- **Classe:** TDA com encapsulamento e controle de acesso (`public`, `private`, `protected`).
- **Ciclo de vida:** construtor e destrutor (C++, com `delete`) × coleta de lixo (Java).

**Herança e polimorfismo ([Aula 13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)).**
- **Herança** simples (Java, C#) ou múltipla (C++). O exemplo é a impressora multifuncional; Java substitui a herança múltipla por **interfaces**.
- **Polimorfismo estático** (sobrecarga): decidido na compilação.
- **Polimorfismo dinâmico** (sobrescrita com vinculação tardia): decidido pelo tipo real do objeto, em execução. O exemplo é a hierarquia de contas bancárias.
- **Classes abstratas** e **interfaces** definem contratos.

---

## Unidade 4 — Paradigmas funcional e lógico (Aulas 14–15)

**Funcional ([Aula 14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)).**
- **Origem:** as funções matemáticas e a crítica de Backus ao estilo de von Neumann. LISP foi a primeira linguagem funcional.
- **No modelo puro:** sem variáveis mutáveis, sem atribuição, sem laços — logo, sem efeitos colaterais. A repetição é feita por recursão.
- **Linguagens puras:** Haskell, Miranda. **Impuras:** LISP, Scheme, Clojure.
- **Clojure:**
  - notação **prefixa** (`(+ 1 2)`);
  - divisão exata com `Ratio`;
  - `quot` e `rem` para quociente e resto;
  - `def` para nomear valores;
  - predicados numéricos.

**Lógico ([Aula 15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)).**
- **Abordagem declarativa:** o programador diz **o que** deseja, e um mecanismo de inferência encontra a resposta.
- **Base teórica:** lógica proposicional e lógica de predicados de primeira ordem.
- **Prolog:**
  - **fatos**, **regras** e **consultas**;
  - **unificação**: `pai(X, maria)` → `X = joao`;
  - `findall` para coletar soluções;
  - hipótese do **mundo fechado** **[Complemento]**: o que não se consegue provar é falso.

---

## Ideias que atravessam a disciplina

| Ideia | Onde aparece |
| --- | --- |
| **Abstração** — esconder detalhes para lidar com a complexidade | Linguagens de alto nível (02), máquinas virtuais (03), funções (10), TDA (10, 12), classes (12), interfaces (13) |
| **Estado e sua mudança** | Atributos da variável (05), von Neumann (09), passagem de parâmetros (11), objetos (12); ausência de estado no funcional (14) |
| **Vinculação (*binding*) e momento em que ocorre** | Compilação × execução (03), escopo estático × dinâmico (05), tipagem estática × dinâmica (06), sobrecarga × sobrescrita (13) |
| **Legibilidade × flexibilidade** | Critérios de avaliação (02), escopo dinâmico (05), coerção (06), `goto` (09) |
| **Procedural × declarativo** | Classificação dos paradigmas (02, 15) |

Para revisar por unidade, use as [revisões por unidade](Revisões%20por%20Unidade/). Para treinar, use as [questões integradoras](questoes-integradoras.md) e as [listas do professor](../02%20-%20Listas%20de%20Exercícios/README.md).


<!-- nav:rodape -->

---

**Links para esta página (4):** [06 — Revisões e Sínteses](README.md) · [Revisão da Unidade 4 — Paradigmas funcional e lógico (Aulas…](Revisões%20por%20Unidade/unidade-4-funcional-e-logico.md) · [Guia de estudo para as avaliações](guia-de-estudo-para-provas.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../README.md)

<!-- /nav:rodape -->
