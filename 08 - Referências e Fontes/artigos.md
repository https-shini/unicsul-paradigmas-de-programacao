<!-- nav:topo -->
[Início](../README.md) › [08 - Referências e Fontes](README.md) · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# Artigos clássicos

> Legenda: 🎓 indicado pelo professor · ➕ complemento do repositório. Formato das referências: ABNT NBR 6023:2018. Links conferidos em 19/11/2026. Marcações: [Convenções](../README.md#convenções-de-marcação).

> Os artigos da ACM Digital Library podem ser localizados pelo DOI. Muitos estão em acesso aberto ou disponíveis pela rede da universidade; quando o próprio autor oferece uma cópia, o link aparece em **Acesso**.

## Sumário

- [1. Artigo indicado pelo professor](#1-artigo-indicado-pelo-professor)
- [2. Computabilidade e arquitetura](#2-computabilidade-e-arquitetura)
- [3. Definição de linguagens e sintaxe](#3-definição-de-linguagens-e-sintaxe)
- [4. Programação estruturada e o debate sobre o `goto`](#4-programação-estruturada-e-o-debate-sobre-o-goto)
- [5. Abstração, modularidade e tipos abstratos de dados](#5-abstração-modularidade-e-tipos-abstratos-de-dados)
- [6. Tipos e polimorfismo](#6-tipos-e-polimorfismo)
- [7. Paradigmas e programação funcional](#7-paradigmas-e-programação-funcional)
- [8. Programação lógica](#8-programação-lógica)

## 1. Artigo indicado pelo professor

**[Material original]** Aula01 [p.9](../01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/01%20-%20Slides%20Originais/README.md#página-9) e Aula 09.

### A01 — Dijkstra (1968)

DIJKSTRA, Edsger W. Go to statement considered harmful. **Communications of the ACM**, New York, v. 11, n. 3, p. 147-148, mar. 1968. DOI: [10.1145/362929.362947](https://doi.org/10.1145/362929.362947).

- **Origem:** 🎓 Indicado pelo professor
- **Acesso:** [PDF no repositório](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf) · [resumo](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) · [versão aberta](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD215.html) · [DOI](https://doi.org/10.1145/362929.362947)
- **Aulas:** [01](../01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/README.md) · [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md)
- **Por que ler:** O texto da Aula 09: o `goto` impede descrever o andamento do programa por índices textuais e dinâmicos. Há cópia do PDF no repositório e resumo na Aula 09.
- **Observação:** Publicado como carta ao editor; o título original de Dijkstra era *A case against the GO TO statement* (EWD215).


## 2. Computabilidade e arquitetura

**[Complemento]**

### A02 — Turing (1937)

TURING, Alan M. On computable numbers, with an application to the Entscheidungsproblem. **Proceedings of the London Mathematical Society**, London, v. s2-42, n. 1, p. 230-265, 1937. DOI: [10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1112/plms/s2-42.1.230)
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md)
- **Por que ler:** Define a máquina de Turing e a noção de função computável — o fundamento da "completude de Turing" da Aula 09.
- **Observação:** Lido em novembro de 1936; o volume é datado de 1936–1937.

### A03 — von Neumann (1945)

VON NEUMANN, John. **First draft of a report on the EDVAC**. Philadelphia: Moore School of Electrical Engineering, University of Pennsylvania, 1945.

- **Origem:** ➕ Complemento do repositório
- **Acesso:** Biblioteca da universidade ou acervos de história da computação.
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md) · [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/README.md)
- **Por que ler:** Descreve a arquitetura de programa armazenado (memória única para dados e instruções) que o paradigma imperativo abstrai e que Backus criticou.
- **Observação:** Relatório da Moore School of Electrical Engineering, University of Pennsylvania (jun. 1945).


## 3. Definição de linguagens e sintaxe

**[Complemento]**

### A04 — Backus (1960)

BACKUS, John W. et al. Report on the algorithmic language ALGOL 60. **Communications of the ACM**, New York, v. 3, n. 5, p. 299-314, maio 1960. DOI: [10.1145/367236.367262](https://doi.org/10.1145/367236.367262).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/367236.367262)
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/README.md) · [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/README.md)
- **Por que ler:** Primeira definição de linguagem com a sintaxe descrita em BNF; introduziu também blocos e escopo léxico.
- **Observação:** Editado por Peter Naur. Versão revisada: Communications of the ACM, v. 6, n. 1, 1963.


## 4. Programação estruturada e o debate sobre o `goto`

**[Complemento]**

### A05 — Böhm (1966)

BÖHM, Corrado; JACOPINI, Giuseppe. Flow diagrams, Turing machines and languages with only two formation rules. **Communications of the ACM**, New York, v. 9, n. 5, p. 366-371, maio 1966. DOI: [10.1145/355592.365646](https://doi.org/10.1145/355592.365646).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/355592.365646)
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md)
- **Por que ler:** Prova que sequência, seleção e repetição bastam para expressar qualquer fluxograma — o resultado que Dijkstra cita e que o slide atribui a ele.

### A06 — Knuth (1974)

KNUTH, Donald E. Structured programming with go to statements. **ACM Computing Surveys**, New York, v. 6, n. 4, p. 261-301, dez. 1974. DOI: [10.1145/356635.356640](https://doi.org/10.1145/356635.356640).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/356635.356640)
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md)
- **Por que ler:** Contraponto equilibrado a Dijkstra: examina casos em que o `goto` deixa o código mais claro ou eficiente e discute o que é, de fato, programação estruturada.

### A07 — Rubin (1987)

RUBIN, Frank. "GOTO considered harmful" considered harmful. **Communications of the ACM**, New York, v. 30, n. 3, p. 195-196, mar. 1987. DOI: [10.1145/214748.315722](https://doi.org/10.1145/214748.315722).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/214748.315722)
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md)
- **Por que ler:** Carta que reabriu o debate vinte anos depois, defendendo o `goto`; mostra que a questão foi discutida por décadas.

### A08 — Wirth (1971)

WIRTH, Niklaus. Program development by stepwise refinement. **Communications of the ACM**, New York, v. 14, n. 4, p. 221-227, abr. 1971. DOI: [10.1145/362575.362577](https://doi.org/10.1145/362575.362577).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/362575.362577)
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md) · [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/README.md)
- **Por que ler:** Apresenta o refinamento sucessivo — a técnica do exemplo de ordenação da Aula 10 — com o problema das oito rainhas.


## 5. Abstração, modularidade e tipos abstratos de dados

**[Complemento]**

### A09 — Parnas (1972)

PARNAS, David L. On the criteria to be used in decomposing systems into modules. **Communications of the ACM**, New York, v. 15, n. 12, p. 1053-1058, dez. 1972. DOI: [10.1145/361598.361623](https://doi.org/10.1145/361598.361623).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/361598.361623)
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/README.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/README.md)
- **Por que ler:** Origem do princípio de ocultação de informação: cada módulo esconde uma decisão de projeto. É a ideia por trás do TDA e do encapsulamento.
- **Observação:** Parnas não usa os termos acoplamento e coesão; eles vêm de A10.

### A10 — Stevens (1974)

STEVENS, Wayne P.; MYERS, Glenford J.; CONSTANTINE, Larry L. Structured design. **IBM Systems Journal**, Armonk, v. 13, n. 2, p. 115-139, 1974. DOI: [10.1147/sj.132.0115](https://doi.org/10.1147/sj.132.0115).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1147/sj.132.0115)
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/README.md)
- **Por que ler:** Artigo que popularizou os conceitos de acoplamento e coesão usados na Aula 10 para avaliar a abstração procedural.

### A11 — Liskov (1974)

LISKOV, Barbara; ZILLES, Stephen. Programming with abstract data types. **ACM SIGPLAN Notices**, New York, v. 9, n. 4, p. 50-59, abr. 1974. DOI: [10.1145/942572.807045](https://doi.org/10.1145/942572.807045).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/942572.807045)
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/README.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/README.md)
- **Por que ler:** Define tipo abstrato de dados como um tipo caracterizado apenas pelas suas operações e mostra como uma linguagem pode suportá-lo — a ponte entre as Aulas 10 e 12.


## 6. Tipos e polimorfismo

**[Complemento]**

### A12 — Cardelli (1985)

CARDELLI, Luca; WEGNER, Peter. On understanding types, data abstraction, and polymorphism. **ACM Computing Surveys**, New York, v. 17, n. 4, p. 471-523, dez. 1985. DOI: [10.1145/6041.6042](https://doi.org/10.1145/6041.6042).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/6041.6042)
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/README.md) · [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/README.md)
- **Por que ler:** Classifica os tipos de polimorfismo (sobrecarga, coerção, inclusão, paramétrico) e discute tipagem estática e forte. Aprofunda as Aulas 06 e 13.


## 7. Paradigmas e programação funcional

**[Complemento]**

### A13 — Floyd (1979)

FLOYD, Robert W. The paradigms of programming. **Communications of the ACM**, New York, v. 22, n. 8, p. 455-460, ago. 1979. DOI: [10.1145/359138.359140](https://doi.org/10.1145/359138.359140).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/359138.359140)
- **Aulas:** [02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/README.md)
- **Por que ler:** Palestra do Prêmio Turing que popularizou o termo "paradigmas de programação" e defende que o programador domine vários deles — o tema da Aula 02.

### A14 — McCarthy (1960)

MCCARTHY, John. Recursive functions of symbolic expressions and their computation by machine, part I. **Communications of the ACM**, New York, v. 3, n. 4, p. 184-195, abr. 1960. DOI: [10.1145/367177.367199](https://doi.org/10.1145/367177.367199).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/367177.367199)
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/README.md)
- **Por que ler:** Artigo que apresenta o LISP, a primeira linguagem funcional e ancestral do Clojure.

### A15 — Backus (1978)

BACKUS, John. Can programming be liberated from the von Neumann style? A functional style and its algebra of programs. **Communications of the ACM**, New York, v. 21, n. 8, p. 613-641, ago. 1978. DOI: [10.1145/359576.359579](https://doi.org/10.1145/359576.359579).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [DOI](https://doi.org/10.1145/359576.359579)
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md) · [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/README.md)
- **Por que ler:** Palestra do Prêmio Turing citada na Aula 14: critica o "gargalo de von Neumann" das linguagens imperativas e propõe um estilo funcional.

### A16 — Hughes (1989)

HUGHES, John. Why functional programming matters. **The Computer Journal**, Oxford, v. 32, n. 2, p. 98-107, abr. 1989. DOI: [10.1093/comjnl/32.2.98](https://doi.org/10.1093/comjnl/32.2.98).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [versão aberta](https://www.cse.chalmers.se/~rjmh/Papers/whyfp.html) · [DOI](https://doi.org/10.1093/comjnl/32.2.98)
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/README.md)
- **Por que ler:** Argumenta que a vantagem do funcional não é "não ter atribuição", e sim a modularidade obtida com funções de ordem superior e avaliação preguiçosa.
- **Observação:** O autor disponibiliza o texto em sua página.

### A17 — Hickey (2020)

HICKEY, Rich. A history of Clojure. **Proceedings of the ACM on Programming Languages**, New York, v. 4, n. HOPL, p. 71:1-71:46, jun. 2020. DOI: [10.1145/3386321](https://doi.org/10.1145/3386321).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [versão aberta](https://clojure.org/about/history) · [DOI](https://doi.org/10.1145/3386321)
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/README.md)
- **Por que ler:** O criador do Clojure explica as decisões de projeto: dialeto de LISP, hospedado na JVM, com dados imutáveis. Confirma que o projeto começou em 2005 e foi lançado em 2007.
- **Observação:** Acesso aberto.


## 8. Programação lógica

**[Complemento]**

### A18 — Kowalski (1979)

KOWALSKI, Robert. Algorithm = logic + control. **Communications of the ACM**, New York, v. 22, n. 7, p. 424-436, jul. 1979. DOI: [10.1145/359131.359136](https://doi.org/10.1145/359131.359136).

- **Origem:** ➕ Complemento do repositório
- **Acesso:** [versão aberta](https://www.doc.ic.ac.uk/~rak/papers/algorithm%20=%20logic%20+%20control.pdf) · [DOI](https://doi.org/10.1145/359131.359136)
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/README.md)
- **Por que ler:** Divide um algoritmo em lógica (o que é verdade) e controle (como buscar a resposta) — a essência da abordagem declarativa da Aula 15.
- **Observação:** O autor disponibiliza o PDF em sua página.

### A19 — Colmerauer (1993)

COLMERAUER, Alain; ROUSSEL, Philippe. The birth of Prolog. **ACM SIGPLAN Notices**, New York, v. 28, n. 3, p. 37-52, mar. 1993.

- **Origem:** ➕ Complemento do repositório
- **Acesso:** Biblioteca da universidade ou acervos de história da computação.
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/README.md)
- **Por que ler:** História do Prolog contada pelos criadores (Marselha, 1972): processamento de linguagem natural, demonstração automática de teoremas e resolução.
- **Observação:** Apresentado na conferência HOPL-II.


<!-- nav:rodape -->

---

**Links para esta página (3):** [05 — Materiais Complementares](../05%20-%20Materiais%20Complementares/README.md) · [08 — Referências e Fontes](README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../README.md)

<!-- /nav:rodape -->
