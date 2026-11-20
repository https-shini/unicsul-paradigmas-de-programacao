# 05 — Materiais Complementares

Catálogo geral das leituras e ferramentas de apoio. As indicações específicas de cada aula, com comentários mais detalhados, estão em `05 - Materiais Complementares/materiais-complementares.md` dentro da pasta da aula.

> **Política:** o repositório **não copia** livros ou materiais de terceiros. O único PDF externo incluído é o artigo de Dijkstra, distribuído pelo professor como material da Aula 09 ([`Aula09a_ArtigoDijkstra68.pdf`](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf)). Os demais itens são referências ou links.

## A. Indicados pelo professor

**[Material original]** — bibliografia complementar do plano de ensino (Aula01 p.9). Detalhes em [bibliografia.md](../00%20-%20Planejamento%20e%20Organização/bibliografia.md).

| Título | Autor | Tipo | Acesso | Assunto (aulas) | Por que ler |
| --- | --- | --- | --- | --- | --- |
| *Go To Statement Considered Harmful* (1968) | E. W. Dijkstra | Artigo | [PDF no repositório](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf) · [resumo](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) | Programação estruturada (09) | Texto fundador da programação estruturada; é cobrado nas listas de revisão |
| *The Scheme Programming Language*, 4. ed. | K. Dybvig | Livro on-line | <https://www.scheme.com/tspl4/> | Funcional (14) | Scheme é da família LISP, como o Clojure; mostra a sintaxe prefixa e a recursão com mais profundidade |
| *Introduction to Programming Using Java*, v. 6 | D. J. Eck | Livro on-line | [PDF](http://math.hws.edu/eck/cs124/downloads/javanotes6-linked.pdf) | OO em Java (12–13) | Caps. sobre classes, herança e interfaces, na linguagem usada nas aulas |
| *An Introduction to Prolog Programming* | U. Endriss | Apostila | [PDF](https://staff.fnwi.uva.nl/u.endriss/teaching/pss/prolog.pdf) | Lógico (15) | Explica unificação, recursão e *backtracking*, que a aula apresenta só em parte |
| *Functional Programming in Scheme* | K. Normark | Apostila | [PDF](http://people.cs.aau.dk/~normark/prog3-03/pdf/all.pdf) | Funcional (14) | Funções de ordem superior e composição, que aprofundam a p.22 da Aula 14 |

## B. Complementos do repositório

**[Complemento]** — sugestões deste repositório, **não indicadas pelo professor**.

### Livros

| Título | Autor | Assunto (aulas) | Por que ler |
| --- | --- | --- | --- |
| *Conceitos de Linguagens de Programação* (capítulos não citados nos slides) | R. W. Sebesta | Todas | Caps. 3–4 (sintaxe e análise léxica), 6 (tipos e ponteiros), 8 (estruturas de controle), 16 (cálculo de predicados): fundamentam pontos que os slides tratam rapidamente |
| *Compiladores: princípios, técnicas e ferramentas* | Aho, Lam, Sethi, Ullman | Implementação, sintaxe (03–04) | Referência clássica para as fases de compilação e a análise léxica |
| *Padrões de Projeto* | Gamma, Helm, Johnson, Vlissides | OO (13) | Origem dos padrões citados na Aula 13 |
| *Programming in Prolog* | Clocksin, Mellish | Lógico (15) | Introdução clássica ao Prolog |
| *Algoritmos: Teoria e Prática*, cap. 10 | Cormen et al. | Estruturas dinâmicas (08, 12) | Pilhas, filas e listas encadeadas, usadas nos exemplos de ponteiros e OO |
| *Engenharia de Software* (conceitos de projeto) | R. Pressman | Acoplamento e coesão (10) | Independência funcional, base das limitações da abstração procedural |

### Artigos clássicos

| Referência | Assunto (aulas) | Por que ler |
| --- | --- | --- |
| Böhm, C.; Jacopini, G. "Flow diagrams, Turing machines and languages with only two formation rules". *Comm. ACM* 9(5), 1966 | Programação estruturada (09) | Prova de que sequência, seleção e repetição bastam; é a referência que Dijkstra cita |
| Wirth, N. "Program Development by Stepwise Refinement". *Comm. ACM* 14(4), 1971 | Abstração procedural (10) | Apresenta o refinamento sucessivo usado no exemplo de ordenação |
| Backus, J. "Can Programming Be Liberated from the von Neumann Style?". *Comm. ACM* 21(8), 1978 | Funcional (09, 14) | Palestra do Prêmio Turing citada na Aula 14; crítica ao "gargalo de von Neumann" |
| E. W. Dijkstra Archive | Programação estruturada (09) | <https://www.cs.utexas.edu/~EWD/>: manuscritos originais de Dijkstra |

### Documentação oficial

| Documento | Assunto (aulas) |
| --- | --- |
| [Java Tutorials — Classes and Objects](https://docs.oracle.com/javase/tutorial/java/javaOO/) · [Interfaces and Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/) · [Enum Types](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) · [Arrays](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html) | OO, tipos compostos (07, 12–13) |
| [Java Language Specification e JVM Specification](https://docs.oracle.com/javase/specs/) | Tipos, conversões, bytecode (03, 06) |
| [cppreference — `new`](https://en.cppreference.com/w/cpp/language/new) · [destrutores](https://en.cppreference.com/w/cpp/language/destructor) · [classes derivadas](https://en.cppreference.com/w/cpp/language/derived_class) | Ponteiros e OO em C++ (08, 12–13) |
| [Microsoft Learn — parâmetros de método em C#](https://learn.microsoft.com/pt-br/dotnet/csharp/language-reference/keywords/method-parameters) | `ref`, `out`, `in` (11) |
| [Perl — `perlsub`](https://perldoc.perl.org/perlsub) | `my` × `local`, escopo estático × dinâmico (05) |
| [Learn Clojure](https://clojure.org/guides/learn/clojure) · [números em Clojure](https://clojure.org/reference/data_structures#Numbers) | Funcional (14) |
| [Manual do SWI-Prolog](https://www.swi-prolog.org/pldoc/) | Lógico (15) |

### Ferramentas para praticar

| Ferramenta | Uso | Aulas |
| --- | --- | --- |
| OneCompiler | Compilador on-line usado nas aulas para Clojure e Prolog | 14–15 |
| [SWISH](https://swish.swi-prolog.org/) | SWI-Prolog no navegador, usado na Aula 15 | 15 |
| [nbb](https://github.com/babashka/nbb) | ClojureScript no Node.js; usado para validar o código deste repositório | 14 |
| [Tau-Prolog](http://tau-prolog.org/) | Prolog em JavaScript; usado para validar o código deste repositório | 15 |
| GCC / G++ / JDK | Compiladores de C, C++ e Java para os exemplos das Aulas 04–13 | 04–13 |
