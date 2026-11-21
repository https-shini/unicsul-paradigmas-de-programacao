#!/usr/bin/env python3
"""Gera a pasta '08 - Referências e Fontes' (livros.md, artigos.md, README.md, referencias.bib)
a partir de uma única base de dados, para manter ABNT, BibTeX e índice por aula consistentes."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "08 - Referências e Fontes")
ACESSO = "19 nov. 2026"
AULAS = {1:"Aula 01 - Apresentação da Disciplina",2:"Aula 02 - Evolução das Linguagens e Paradigmas",3:"Aula 03 - Implementação das Linguagens",4:"Aula 04 - Sintaxe",5:"Aula 05 - Semântica",6:"Aula 06 - Sistema de Tipos",7:"Aula 07 - Tipos Compostos",8:"Aula 08 - Ponteiros",9:"Aula 09 - Paradigma Imperativo I",10:"Aula 10 - Paradigma Imperativo II",11:"Aula 11 - Paradigma Imperativo III",12:"Aula 12 - Paradigma Orientado a Objetos I",13:"Aula 13 - Paradigma Orientado a Objetos II",14:"Aula 14 - Paradigma Funcional",15:"Aula 15 - Paradigma Lógico"}
TEMA = {1:"Apresentação",2:"Evolução e paradigmas",3:"Implementação",4:"Sintaxe",5:"Semântica",6:"Sistema de tipos",7:"Tipos compostos",8:"Ponteiros",9:"Imperativo I",10:"Imperativo II",11:"Imperativo III",12:"OO I",13:"OO II",14:"Funcional",15:"Lógico"}
P = lambda s: s.replace(" ", "%20")
def aula_link(n): return f"[{n:02d}](../01%20-%20Aulas/{P(AULAS[n])}/README.md)"

# ---------------------------------------------------------------- LIVROS
# origem: P = indicado pelo professor; C = complemento do repositório
LIVROS = [
 # grupo, id, origem, autores ABNT, autores BibTeX, título, subtítulo, edição, local, editora, ano, isbn, url, acesso, aulas, por que ler, nota
 ("basica","L01","P","ASCENCIO, Ana Fernanda Gomes; CAMPOS, Edilene Aparecida Veneruchi de","Ascencio, Ana Fernanda Gomes and Campos, Edilene Aparecida Veneruchi de",
  "Fundamentos da programação de computadores","algoritmos, Pascal, C/C++ e Java","2","São Paulo","Pearson Prentice Hall","2007","9788576051480",None,
  "Livro impresso; edições Pearson costumam estar na Biblioteca Virtual Pearson das instituições.",[1,2,7,9,10,11],
  "Revisão de algoritmos e programação imperativa em Pascal, C/C++ e Java — as mesmas linguagens dos exemplos das Aulas 02 e 07–11.",
  "Existe 3. ed. (2012, ISBN 9788564574168), com o mesmo conteúdo ampliado."),
 ("basica","L02","P","SEBESTA, Robert W.","Sebesta, Robert W.",
  "Conceitos de linguagens de programação",None,"11","Porto Alegre","Bookman","2018","9788582604687",None,
  "E-book do Grupo A (ISBN 9788582604694); costuma estar na plataforma Minha Biblioteca.",list(range(1,16)),
  "Livro-texto da disciplina. Cobre todos os temas: sintaxe, nomes e vinculações, tipos, controle, subprogramas, TDA, OO, funcional e lógico.",
  "É a edição citada no plano de ensino. Os slides citam seções da 9. ed. (L04); a numeração pode mudar entre edições."),
 ("basica","L03","P","SILVA, Fabricio Machado da; LEITE, Márcia Cristina Domingues; OLIVEIRA, Diego Bittencourt de","Silva, Fabricio Machado da and Leite, Márcia Cristina Domingues and Oliveira, Diego Bittencourt de",
  "Paradigmas de programação",None,None,"Porto Alegre","SAGAH","2019","9788533500426",None,
  "E-book; disponível na plataforma Minha Biblioteca.",[1,2,9,10,11,12,13,14,15],
  "Apresenta as linguagens agrupadas pelo paradigma em que se encaixam; leitura curta e em português para cada um dos quatro paradigmas.",None),
 ("slides","L04","P","SEBESTA, Robert W.","Sebesta, Robert W.",
  "Conceitos de linguagens de programação",None,"9","Porto Alegre","Bookman","2011","9788577807918",None,
  "Livro impresso (792 p.).",[2,4,5,6,9,10,11,12,14,15],
  "Edição usada nos slides de bibliografia das aulas (ex.: seções 1.3–1.5 na Aula 02; 3.1–3.2 na Aula 04; cap. 9 nas Aulas 09 e 11; 16.6 na Aula 15). Use esta edição para localizar as seções citadas.",None),
 ("slides","L05","P","TUCKER, Allen B.; NOONAN, Robert E.","Tucker, Allen B. and Noonan, Robert E.",
  "Linguagens de programação","princípios e paradigmas","2","São Paulo","McGraw-Hill","2008","9788577260447",None,
  "Livro impresso.",[2,4,5,6,9,10,11,12,14,15],
  "Segunda referência dos slides: seções 1.2 e 1.4 (Aula 02), 4.1–4.3 (Aulas 04–05), 5.1–5.2 (Aula 06), 9.1–9.4 (Aula 11), cap. 13–15 (Aulas 12, 14, 15). A Aula 10 cita a definição de encapsulamento deste livro.",
  "Os slides citam o ano de 2009; os catálogos de bibliotecas registram 2008 para a 2. ed. brasileira."),
 ("compl-prof","L06","P","DYBVIG, R. Kent","Dybvig, R. Kent",
  "The Scheme programming language",None,"4","Cambridge, MA","MIT Press","2009","9780262512985","https://www.scheme.com/tspl4/",
  "Texto integral on-line, reproduzido com autorização da editora.",[1,14],
  "Scheme é da família LISP, como o Clojure da Aula 14. Bom para ver a notação prefixa, listas e recursão com mais exemplos.",None),
 ("compl-prof","L07","P","ECK, David J.","Eck, David J.",
  "Introduction to programming using Java",None,"Version 9","Geneva, NY","Hobart and William Smith Colleges","2022",None,"https://math.hws.edu/javanotes/",
  "Livro aberto (licença Creative Commons BY-NC-SA 4.0), em HTML e PDF.",[1,7,12,13],
  "Capítulos sobre classes, objetos, herança, interfaces e vetores em Java, na linguagem das Aulas 07, 12 e 13.",
  "O professor cita a versão 6 (2014). A versão 9 (2022) é a última; o autor informa que não haverá novas atualizações."),
 ("compl-prof","L08","P","ENDRISS, Ulle","Endriss, Ulle",
  "An introduction to Prolog programming",None,None,"Amsterdam","Institute for Logic, Language and Computation, University of Amsterdam","2018",None,"https://staff.science.uva.nl/~ulle/teaching/pss/prolog.pdf",
  "Notas de aula em PDF, de acesso livre.",[1,15],
  "Introdução prática ao Prolog com exercícios: fatos, regras, unificação, recursão, listas e *backtracking* — aprofunda o que a Aula 15 mostra.",
  "Ano conforme o slide (Aula01 p.9). O PDF é revisado periodicamente pelo autor."),
 ("compl-prof","L09","P","NØRMARK, Kurt","Nørmark, Kurt",
  "Functional programming in Scheme","with web programming examples",None,"Aalborg","Department of Computer Science, Aalborg University","2003",None,"https://homes.cs.aau.dk/~normark/prog3-03/html/notes/index.html",
  "Notas de aula em HTML, de acesso livre.",[1,2,14],
  "Começa comparando os quatro paradigmas e depois desenvolve funções de ordem superior, recursão e ordem de avaliação.",
  "O link do slide (domínio people.cs.aau.dk) mudou; o endereço acima é o atual."),
 ("pt","L10","C","MELO, Ana Cristina Vieira de; SILVA, Flávio Soares Corrêa da","Melo, Ana Cristina Vieira de and Silva, Flávio Soares Corrêa da",
  "Princípios de linguagens de programação",None,None,"São Paulo","Blucher","2003","9788521203223",None,
  "Livro impresso.",[2,3,4,5,6],
  "Livro brasileiro sobre conceitos de linguagens; alternativa em português aos capítulos iniciais do Sebesta.",None),
 ("pt","L11","C","VAREJÃO, Flávio Miguel","Varejão, Flávio Miguel",
  "Linguagens de programação","conceitos e técnicas",None,"Rio de Janeiro","Campus","2004",None,None,
  "Livro impresso.",[2,5,6,7,8,11],
  "Referência nacional clássica em cursos de LP: amarrações, variáveis, tipos, modularização e passagem de parâmetros, com muitos exemplos em C e Java.",None),
 ("pt","L12","C","MELO, Gregório","Melo, Gregório",
  "Programação funcional","uma introdução em Clojure",None,"São Paulo","Casa do Código","2019","9788572540018",None,
  "Livro impresso e e-book.",[14],
  "Introdução ao paradigma funcional usando Clojure, em português — a mesma linguagem da Aula 14.",None),
 ("pt","L13","C","AHO, Alfred V. et al.","Aho, Alfred V. and Lam, Monica S. and Sethi, Ravi and Ullman, Jeffrey D.",
  "Compiladores","princípios, técnicas e ferramentas","2","São Paulo","Pearson Addison-Wesley","2008","9788588639249",None,
  "Livro impresso.",[3,4],
  "O \"livro do dragão\": fases de compilação, análise léxica (tokens, padrões, expressões regulares) e sintática.",None),
 ("pt","L14","C","GAMMA, Erich et al.","Gamma, Erich and Helm, Richard and Johnson, Ralph and Vlissides, John",
  "Padrões de projeto","soluções reutilizáveis de software orientado a objetos",None,"Porto Alegre","Bookman","2000",None,None,
  "Livro impresso.",[13],
  "Origem dos padrões de projeto citados na Aula 13; mostra herança, composição e polimorfismo aplicados.",None),
 ("pt","L15","C","CORMEN, Thomas H. et al.","Cormen, Thomas H. and Leiserson, Charles E. and Rivest, Ronald L. and Stein, Clifford",
  "Algoritmos","teoria e prática","3","Rio de Janeiro","Elsevier","2012","9788535236996",None,
  "Livro impresso.",[8,12],
  "Cap. 10 (estruturas de dados elementares): pilhas, filas e listas ligadas, a base da pilha encadeada das Aulas 08 e 12.",None),
 ("pt","L16","C","PRESSMAN, Roger S.; MAXIM, Bruce R.","Pressman, Roger S. and Maxim, Bruce R.",
  "Engenharia de software","uma abordagem profissional","9","Porto Alegre","AMGH","2021",None,None,
  "E-book na Minha Biblioteca (ISBN 9786558040118).",[10],
  "Capítulos de conceitos de projeto: modularidade, independência funcional, acoplamento e coesão.",None),
 ("aberto","L17","C","ABELSON, Harold; SUSSMAN, Gerald Jay; SUSSMAN, Julie","Abelson, Harold and Sussman, Gerald Jay and Sussman, Julie",
  "Structure and interpretation of computer programs",None,"2","Cambridge, MA","MIT Press","1996","9780262510875","https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-1.html",
  "Texto integral gratuito no site da MIT Press; também no repositório OAPEN (licença CC BY-SA).",[3,5,10,14],
  "Clássico do MIT (\"SICP\"). Ensina abstração procedural e de dados, funções de ordem superior e interpretadores usando Scheme.",None),
 ("aberto","L18","C","NYSTROM, Robert","Nystrom, Robert",
  "Crafting interpreters",None,None,"[S. l.]","edição do autor","2021",None,"https://craftinginterpreters.com/",
  "Versão web completa e gratuita; versões impressa e PDF pagas.",[3,4,5],
  "Constrói passo a passo um interpretador: análise léxica, gramática, árvore sintática, escopo, variáveis e bytecode. Mostra na prática as Aulas 03–05.",None),
 ("aberto","L19","C","BLACKBURN, Patrick; BOS, Johan; STRIEGNITZ, Kristina","Blackburn, Patrick and Bos, Johan and Striegnitz, Kristina",
  "Learn Prolog now!",None,None,"London","College Publications","2006","9781904987178","https://lpn.swi-prolog.org/",
  "Versão on-line gratuita, com os exemplos executáveis no navegador (SWISH).",[15],
  "Uma das introduções ao Prolog mais usadas em cursos: unificação, recursão, listas, aritmética e corte, com exercícios.",None),
 ("aberto","L20","C","HIGGINBOTHAM, Daniel","Higginbotham, Daniel",
  "Clojure for the brave and true","learn the ultimate language and become a better programmer",None,"San Francisco","No Starch Press","2015","9781593275914","https://braveclojure.com/clojure-for-the-brave-and-true/",
  "Leitura on-line gratuita no site do autor.",[14],
  "Introdução bem-humorada a Clojure: sintaxe, estruturas de dados imutáveis, funções puras e de ordem superior.",None),
 ("ref","L21","C","SCOTT, Michael L.","Scott, Michael L.",
  "Programming language pragmatics",None,"4","Waltham, MA","Morgan Kaufmann","2016","9780124104099",None,
  "Livro impresso e e-book.",[2,3,4,5,6,9,10,11,12,13],
  "Alternativa mais aprofundada ao Sebesta, que integra o projeto e a implementação de linguagens: compilação, nomes e escopos, tipos, subprogramas e OO.",
  "Há 5. ed. (2025), em coautoria com Jonathan Aldrich."),
 ("ref","L22","C","VAN ROY, Peter; HARIDI, Seif","Van Roy, Peter and Haridi, Seif",
  "Concepts, techniques, and models of computer programming",None,None,"Cambridge, MA","MIT Press","2004",None,None,
  "Livro impresso.",[2,14,15],
  "Apresenta os paradigmas como modelos que se somam (declarativo, com estado, concorrente, OO, relacional) — boa leitura para quem quer entender as linguagens multiparadigma.",None),
 ("ref","L23","C","PIERCE, Benjamin C.","Pierce, Benjamin C.",
  "Types and programming languages",None,None,"Cambridge, MA","MIT Press","2002",None,None,
  "Livro impresso.",[6],
  "Referência de pós-graduação em sistemas de tipos; para quem quer ir além da classificação estática/dinâmica e forte/fraca da Aula 06.",None),
 ("ref","L24","C","KERNIGHAN, Brian W.; RITCHIE, Dennis M.","Kernighan, Brian W. and Ritchie, Dennis M.",
  "The C programming language",None,"2","Englewood Cliffs","Prentice Hall","1988",None,None,
  "Livro impresso; há tradução em português.",[7,8,9,10],
  "Escrito pelos criadores do C: ponteiros, vetores, estruturas e alocação, com a precisão necessária para entender os exemplos das Aulas 07–10.",None),
 ("ref","L25","C","CLOCKSIN, William F.; MELLISH, Christopher S.","Clocksin, William F. and Mellish, Christopher S.",
  "Programming in Prolog",None,"5","Berlin","Springer","2003",None,None,
  "Livro impresso.",[15],
  "Texto clássico de introdução ao Prolog, base da sintaxe \"de Edimburgo\" usada pelos sistemas atuais.",None),
 ("ref","L26","C","BRATKO, Ivan","Bratko, Ivan",
  "Prolog programming for artificial intelligence",None,"4","Harlow","Pearson","2012",None,None,
  "Livro impresso.",[15],
  "Prolog aplicado a problemas de IA (busca, planejamento, sistemas especialistas); mostra onde o paradigma lógico é a melhor escolha.",None),
]
GRUPOS_L = [
 ("basica","1. Bibliografia básica do plano de ensino","**[Material original]** Aula01 p.8."),
 ("slides","2. Livros citados nos slides das aulas","**[Material original]** Slides de bibliografia das Aulas 02, 04–06, 09, 11, 12, 14 e 15."),
 ("compl-prof","3. Bibliografia complementar do plano de ensino","**[Material original]** Aula01 p.9. Todos têm versão on-line gratuita."),
 ("pt","4. Complementos em português","**[Complemento]** Não indicados pelo professor."),
 ("aberto","5. Complementos de acesso aberto (em inglês)","**[Complemento]** Leitura on-line gratuita e legal."),
 ("ref","6. Obras de referência para aprofundamento","**[Complemento]** Para quem quiser ir além do conteúdo da disciplina."),
]

# ---------------------------------------------------------------- ARTIGOS
ARTIGOS = [
 # grupo, id, origem, autores ABNT, autores BibTeX, título, periódico, local, vol, num, páginas, mês, ano, doi, url aberta, aulas, por que ler, nota
 ("prof","A01","P","DIJKSTRA, Edsger W.","Dijkstra, Edsger W.","Go to statement considered harmful","Communications of the ACM","New York","11","3","147-148","mar.","1968","10.1145/362929.362947","https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD215.html",[1,9],
  "O texto da Aula 09: o `goto` impede descrever o andamento do programa por índices textuais e dinâmicos. Há cópia do PDF no repositório e resumo na Aula 09.",
  "Publicado como carta ao editor; o título original de Dijkstra era *A case against the GO TO statement* (EWD215)."),
 ("comp","A02","C","TURING, Alan M.","Turing, Alan M.","On computable numbers, with an application to the Entscheidungsproblem","Proceedings of the London Mathematical Society","London","s2-42","1","230-265",None,"1937","10.1112/plms/s2-42.1.230",None,[9],
  "Define a máquina de Turing e a noção de função computável — o fundamento da \"completude de Turing\" da Aula 09.",
  "Lido em novembro de 1936; o volume é datado de 1936–1937."),
 ("comp","A03","C","VON NEUMANN, John","von Neumann, John","First draft of a report on the EDVAC",None,"Philadelphia","","","",None,"1945",None,None,[9,14],
  "Descreve a arquitetura de programa armazenado (memória única para dados e instruções) que o paradigma imperativo abstrai e que Backus criticou.",
  "Relatório da Moore School of Electrical Engineering, University of Pennsylvania (jun. 1945)."),
 ("sintaxe","A04","C","BACKUS, John W. et al.","Backus, John W. and Bauer, Friedrich L. and Green, Julien and Katz, C. and McCarthy, John and Perlis, Alan J. and Rutishauser, Heinz and Samelson, Klaus and Vauquois, Bernard and Wegstein, Joseph H. and van Wijngaarden, Adriaan and Woodger, Michael and Naur, Peter","Report on the algorithmic language ALGOL 60","Communications of the ACM","New York","3","5","299-314","maio","1960","10.1145/367236.367262",None,[4,5],
  "Primeira definição de linguagem com a sintaxe descrita em BNF; introduziu também blocos e escopo léxico.",
  "Editado por Peter Naur. Versão revisada: Communications of the ACM, v. 6, n. 1, 1963."),
 ("estruturada","A05","C","BÖHM, Corrado; JACOPINI, Giuseppe","Böhm, Corrado and Jacopini, Giuseppe","Flow diagrams, Turing machines and languages with only two formation rules","Communications of the ACM","New York","9","5","366-371","maio","1966","10.1145/355592.365646",None,[9],
  "Prova que sequência, seleção e repetição bastam para expressar qualquer fluxograma — o resultado que Dijkstra cita e que o slide atribui a ele.",None),
 ("estruturada","A06","C","KNUTH, Donald E.","Knuth, Donald E.","Structured programming with go to statements","ACM Computing Surveys","New York","6","4","261-301","dez.","1974","10.1145/356635.356640",None,[9],
  "Contraponto equilibrado a Dijkstra: examina casos em que o `goto` deixa o código mais claro ou eficiente e discute o que é, de fato, programação estruturada.",None),
 ("estruturada","A07","C","RUBIN, Frank","Rubin, Frank","\"GOTO considered harmful\" considered harmful","Communications of the ACM","New York","30","3","195-196","mar.","1987","10.1145/214748.315722",None,[9],
  "Carta que reabriu o debate vinte anos depois, defendendo o `goto`; mostra que a questão foi discutida por décadas.",None),
 ("estruturada","A08","C","WIRTH, Niklaus","Wirth, Niklaus","Program development by stepwise refinement","Communications of the ACM","New York","14","4","221-227","abr.","1971","10.1145/362575.362577",None,[9,10],
  "Apresenta o refinamento sucessivo — a técnica do exemplo de ordenação da Aula 10 — com o problema das oito rainhas.",None),
 ("abstracao","A09","C","PARNAS, David L.","Parnas, David L.","On the criteria to be used in decomposing systems into modules","Communications of the ACM","New York","15","12","1053-1058","dez.","1972","10.1145/361598.361623",None,[10,12],
  "Origem do princípio de ocultação de informação: cada módulo esconde uma decisão de projeto. É a ideia por trás do TDA e do encapsulamento.",
  "Parnas não usa os termos acoplamento e coesão; eles vêm de A10."),
 ("abstracao","A10","C","STEVENS, Wayne P.; MYERS, Glenford J.; CONSTANTINE, Larry L.","Stevens, Wayne P. and Myers, Glenford J. and Constantine, Larry L.","Structured design","IBM Systems Journal","Armonk","13","2","115-139",None,"1974","10.1147/sj.132.0115",None,[10],
  "Artigo que popularizou os conceitos de acoplamento e coesão usados na Aula 10 para avaliar a abstração procedural.",None),
 ("abstracao","A11","C","LISKOV, Barbara; ZILLES, Stephen","Liskov, Barbara and Zilles, Stephen","Programming with abstract data types","ACM SIGPLAN Notices","New York","9","4","50-59","abr.","1974","10.1145/942572.807045",None,[10,12],
  "Define tipo abstrato de dados como um tipo caracterizado apenas pelas suas operações e mostra como uma linguagem pode suportá-lo — a ponte entre as Aulas 10 e 12.",None),
 ("tipos","A12","C","CARDELLI, Luca; WEGNER, Peter","Cardelli, Luca and Wegner, Peter","On understanding types, data abstraction, and polymorphism","ACM Computing Surveys","New York","17","4","471-523","dez.","1985","10.1145/6041.6042",None,[6,13],
  "Classifica os tipos de polimorfismo (sobrecarga, coerção, inclusão, paramétrico) e discute tipagem estática e forte. Aprofunda as Aulas 06 e 13.",None),
 ("funcional","A13","C","FLOYD, Robert W.","Floyd, Robert W.","The paradigms of programming","Communications of the ACM","New York","22","8","455-460","ago.","1979","10.1145/359138.359140",None,[2],
  "Palestra do Prêmio Turing que popularizou o termo \"paradigmas de programação\" e defende que o programador domine vários deles — o tema da Aula 02.",None),
 ("funcional","A14","C","MCCARTHY, John","McCarthy, John","Recursive functions of symbolic expressions and their computation by machine, part I","Communications of the ACM","New York","3","4","184-195","abr.","1960","10.1145/367177.367199",None,[14],
  "Artigo que apresenta o LISP, a primeira linguagem funcional e ancestral do Clojure.",None),
 ("funcional","A15","C","BACKUS, John","Backus, John","Can programming be liberated from the von Neumann style? A functional style and its algebra of programs","Communications of the ACM","New York","21","8","613-641","ago.","1978","10.1145/359576.359579",None,[9,14],
  "Palestra do Prêmio Turing citada na Aula 14: critica o \"gargalo de von Neumann\" das linguagens imperativas e propõe um estilo funcional.",None),
 ("funcional","A16","C","HUGHES, John","Hughes, John","Why functional programming matters","The Computer Journal","Oxford","32","2","98-107","abr.","1989","10.1093/comjnl/32.2.98","https://www.cse.chalmers.se/~rjmh/Papers/whyfp.html",[14],
  "Argumenta que a vantagem do funcional não é \"não ter atribuição\", e sim a modularidade obtida com funções de ordem superior e avaliação preguiçosa.",
  "O autor disponibiliza o texto em sua página."),
 ("funcional","A17","C","HICKEY, Rich","Hickey, Rich","A history of Clojure","Proceedings of the ACM on Programming Languages","New York","4","HOPL","71:1-71:46","jun.","2020","10.1145/3386321","https://clojure.org/about/history",[14],
  "O criador do Clojure explica as decisões de projeto: dialeto de LISP, hospedado na JVM, com dados imutáveis. Confirma que o projeto começou em 2005 e foi lançado em 2007.",
  "Acesso aberto."),
 ("logico","A18","C","KOWALSKI, Robert","Kowalski, Robert","Algorithm = logic + control","Communications of the ACM","New York","22","7","424-436","jul.","1979","10.1145/359131.359136","https://www.doc.ic.ac.uk/~rak/papers/algorithm%20=%20logic%20+%20control.pdf",[15],
  "Divide um algoritmo em lógica (o que é verdade) e controle (como buscar a resposta) — a essência da abordagem declarativa da Aula 15.",
  "O autor disponibiliza o PDF em sua página."),
 ("logico","A19","C","COLMERAUER, Alain; ROUSSEL, Philippe","Colmerauer, Alain and Roussel, Philippe","The birth of Prolog","ACM SIGPLAN Notices","New York","28","3","37-52","mar.","1993",None,None,[15],
  "História do Prolog contada pelos criadores (Marselha, 1972): processamento de linguagem natural, demonstração automática de teoremas e resolução.",
  "Apresentado na conferência HOPL-II."),
]
GRUPOS_A = [
 ("prof","1. Artigo indicado pelo professor","**[Material original]** Aula01 p.9 e Aula 09."),
 ("comp","2. Computabilidade e arquitetura","**[Complemento]**"),
 ("sintaxe","3. Definição de linguagens e sintaxe","**[Complemento]**"),
 ("estruturada","4. Programação estruturada e o debate sobre o `goto`","**[Complemento]**"),
 ("abstracao","5. Abstração, modularidade e tipos abstratos de dados","**[Complemento]**"),
 ("tipos","6. Tipos e polimorfismo","**[Complemento]**"),
 ("funcional","7. Paradigmas e programação funcional","**[Complemento]**"),
 ("logico","8. Programação lógica","**[Complemento]**"),
]

def slug(h):
    h = h.strip().lower()
    h = ''.join(c for c in h if c.isalnum() or c in ' -_')
    return h.replace(' ', '-')

def sobrenome(autores):
    a = autores.split(";")[0].split(",")[0].strip()
    a = a.title().replace("Von ","von ").replace("Van ","Van ")
    return re.sub(r"\bMc([a-z])", lambda m: "Mc" + m.group(1).upper(), a)

def ed_abnt(ed):
    if not ed: return ""
    return (f"{ed}. ed. " if ed.isdigit() else f"{ed}. ")

def abnt_livro(e):
    _,_,_,aut,_,tit,sub,ed,loc,edit,ano,isbn,url,*_ = e
    s = f"{aut}{'' if aut.endswith('.') else '.'} **{tit}**" + (f": {sub}" if sub else "") + ". " + ed_abnt(ed) + f"{loc}: {edit}, {ano}."
    if isbn: s += f" ISBN {isbn}."
    if url: s += f" Disponível em: [{url}]({url}). Acesso em: {ACESSO}."
    return s

def abnt_artigo(e):
    _,_,_,aut,_,tit,per,loc,v,n,pg,mes,ano,doi,url,*_ = e
    if per is None:
        return f"{aut}{'' if aut.endswith('.') else '.'} **{tit}**. {loc}: Moore School of Electrical Engineering, University of Pennsylvania, {ano}."
    partes = [f"v. {v}"] if v else []
    if n: partes.append(f"n. {n}")
    if pg: partes.append(f"p. {pg}")
    data = f"{mes} {ano}" if mes else ano
    s = f"{aut}{'' if aut.endswith('.') else '.'} {tit}. **{per}**, {loc}, " + ", ".join(partes) + f", {data}."
    if doi: s += f" DOI: [{doi}](https://doi.org/{doi})."
    return s

def heading(e, kind):
    if kind == "L":
        return f"{e[1]} — {sobrenome(e[3])} ({e[10]})"
    return f"{e[1]} — {sobrenome(e[3])} ({e[12]})"

def selo(o): return "🎓 Indicado pelo professor" if o == "P" else "➕ Complemento do repositório"

HEAD = "> Legenda: 🎓 indicado pelo professor · ➕ complemento do repositório. Formato das referências: ABNT NBR 6023:2018. Links conferidos em 19/11/2026. Marcações: [Convenções](../README.md#convenções-de-marcação)."

def gen_livros():
    L = ["# Livros e notas de aula", "", HEAD, "",
         "> **[Atenção] — direitos autorais.** Os livros comerciais **não** estão no repositório. Use a biblioteca da universidade (física ou virtual) ou as versões gratuitas indicadas, que são distribuídas legalmente pelos próprios autores ou editoras.", "",
         "## Sumário", ""]
    for g, t, _ in GRUPOS_L:
        L.append(f"- [{t}](#{slug(t)})")
    for g, t, desc in GRUPOS_L:
        L += ["", f"## {t}", "", desc, ""]
        for e in [x for x in LIVROS if x[0] == g]:
            (_, i, o, aut, _, tit, sub, ed, loc, edit, ano, isbn, url, acesso, aulas, porque, nota) = e
            L += [f"### {heading(e,'L')}", "", abnt_livro(e), "",
                  f"- **Origem:** {selo(o)}",
                  f"- **Acesso:** {acesso}" + (f" [Abrir]({url})" if url else ""),
                  f"- **Aulas:** " + " · ".join(aula_link(a) for a in aulas),
                  f"- **Por que ler:** {porque}"]
            if nota: L.append(f"- **Observação:** {nota}")
            L.append("")
    return "\n".join(L).rstrip() + "\n"

def gen_artigos():
    L = ["# Artigos clássicos", "", HEAD, "",
         "> Os artigos da ACM Digital Library podem ser localizados pelo DOI. Muitos estão em acesso aberto ou disponíveis pela rede da universidade; quando o próprio autor oferece uma cópia, o link aparece em **Acesso**.", "",
         "## Sumário", ""]
    for g, t, _ in GRUPOS_A:
        L.append(f"- [{t}](#{slug(t)})")
    for g, t, desc in GRUPOS_A:
        L += ["", f"## {t}", "", desc, ""]
        for e in [x for x in ARTIGOS if x[0] == g]:
            (_, i, o, aut, _, tit, per, loc, v, n, pg, mes, ano, doi, url, aulas, porque, nota) = e
            acesso = []
            if i == "A01":
                acesso.append("[PDF no repositório](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf) · [resumo](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)")
            if url: acesso.append(f"[versão aberta]({url})")
            if doi: acesso.append(f"[DOI](https://doi.org/{doi})")
            L += [f"### {heading(e,'A')}", "", abnt_artigo(e), "",
                  f"- **Origem:** {selo(o)}",
                  f"- **Acesso:** " + (" · ".join(acesso) if acesso else "Biblioteca da universidade ou acervos de história da computação."),
                  f"- **Aulas:** " + " · ".join(aula_link(a) for a in aulas),
                  f"- **Por que ler:** {porque}"]
            if nota: L.append(f"- **Observação:** {nota}")
            L.append("")
    return "\n".join(L).rstrip() + "\n"

def bibkey(e, kind):
    ano = e[10] if kind == "L" else e[12]
    s = sobrenome(e[3]).lower()
    s = ''.join(c for c in s if c.isalpha())
    import unicodedata
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').replace("ø","o")
    return f"{s}{ano}{e[1].lower()}"

def bib_escape(t): return t.replace("&", r"\&")

def gen_bib():
    out = ["% Referências da disciplina Paradigmas de Linguagens de Programação (UNICSUL)",
           "% Gerado a partir da pasta 08 - Referências e Fontes. Codificação UTF-8 (use biblatex + biber, ou abnTeX2).", ""]
    for e in LIVROS:
        (_, i, o, aut, autb, tit, sub, ed, loc, edit, ano, isbn, url, acesso, aulas, porque, nota) = e
        f = [f"  author    = {{{autb}}}", f"  title     = {{{{{bib_escape(tit)}}}{(': ' + bib_escape(sub)) if sub else ''}}}"]
        if ed: f.append(f"  edition   = {{{ed}}}")
        f += [f"  address   = {{{loc}}}", f"  publisher = {{{bib_escape(edit)}}}", f"  year      = {{{ano}}}"]
        if isbn: f.append(f"  isbn      = {{{isbn}}}")
        if url: f += [f"  url       = {{{url}}}", f"  urldate   = {{2026-11-19}}"]
        f.append(f"  keywords  = {{{'professor' if o=='P' else 'complemento'}, {i}}}")
        out += [f"@book{{{bibkey(e,'L')},", ",\n".join(f), "}", ""]
    for e in ARTIGOS:
        (_, i, o, aut, autb, tit, per, loc, v, n, pg, mes, ano, doi, url, aulas, porque, nota) = e
        if per is None:
            f = [f"  author      = {{{autb}}}", f"  title       = {{{bib_escape(tit)}}}",
                 f"  institution = {{Moore School of Electrical Engineering, University of Pennsylvania}}",
                 f"  address     = {{{loc}}}", f"  year        = {{{ano}}}", f"  keywords    = {{complemento, {i}}}"]
            out += [f"@techreport{{{bibkey(e,'A')},", ",\n".join(f), "}", ""]
            continue
        f = [f"  author   = {{{autb}}}", f"  title    = {{{{{bib_escape(tit)}}}}}", f"  journal  = {{{per}}}", f"  year     = {{{ano}}}"]
        if v: f.append(f"  volume   = {{{v}}}")
        if n: f.append(f"  number   = {{{n}}}")
        if pg: f.append(f"  pages    = {{{pg.replace('-', '--')}}}")
        if doi: f.append(f"  doi      = {{{doi}}}")
        if url: f.append(f"  url      = {{{url}}}")
        f.append(f"  keywords = {{{'professor' if o=='P' else 'complemento'}, {i}}}")
        out += [f"@article{{{bibkey(e,'A')},", ",\n".join(f), "}", ""]
    return "\n".join(out)

def gen_readme():
    def refs_por_aula(n):
        ls = [f"[{e[1]}](livros.md#{slug(heading(e,'L'))})" for e in LIVROS if n in e[14]]
        ars = [f"[{e[1]}](artigos.md#{slug(heading(e,'A'))})" for e in ARTIGOS if n in e[15]]
        return ls, ars
    prof_l = sum(1 for e in LIVROS if e[2] == "P"); prof_a = sum(1 for e in ARTIGOS if e[2] == "P")
    L = ["# 08 — Referências e Fontes", "",
         "Catálogo de **todas as fontes bibliográficas** da disciplina: as obras indicadas pelo professor e as leituras complementares selecionadas para este repositório, com a referência completa (ABNT), a forma de acesso e as aulas em que cada uma ajuda.", "",
         "| Arquivo | Conteúdo | Itens |", "| --- | --- | :-: |",
         f"| [livros.md](livros.md) | Livros e notas de aula: bibliografia básica, livros citados nos slides, complementar do plano de ensino e complementos | {len(LIVROS)} ({prof_l} 🎓) |",
         f"| [artigos.md](artigos.md) | Artigos clássicos, do texto de Dijkstra indicado pelo professor aos fundadores de cada paradigma | {len(ARTIGOS)} ({prof_a} 🎓) |",
         "| [documentacao-oficial.md](documentacao-oficial.md) | Especificações e documentação oficial das linguagens usadas nas aulas | 10 linguagens |",
         f"| [referencias.bib](referencias.bib) | Todos os livros e artigos em BibTeX, para LaTeX, Zotero, Mendeley ou abnTeX2 | {len(LIVROS)+len(ARTIGOS)} |", "",
         "**Legenda:** 🎓 indicado pelo professor (**[Material original]**) · ➕ complemento do repositório (**[Complemento]**).", "",
         "## Referências por aula", "",
         "Para cada aula, os livros (`L`) e artigos (`A`) que ajudam a estudá-la. Os itens 🎓 aparecem primeiro na numeração (L01–L09, A01).", "",
         "| Aula | Tema | Livros | Artigos |", "| --- | --- | --- | --- |"]
    for n in range(1, 16):
        ls, ars = refs_por_aula(n)
        L.append(f"| {aula_link(n)} | {TEMA[n]} | {' · '.join(ls) or '—'} | {' · '.join(ars) or '—'} |")
    L += ["", "## Por onde começar", "",
          "1. **Livro-texto:** [L02 — Sebesta (2018)](livros.md#" + slug(heading(LIVROS[1],'L')) + "), ou a 9. ed. ([L04](livros.md#" + slug(heading(LIVROS[3],'L')) + ")) para seguir a numeração das seções citadas nos slides.",
          "2. **Em português, mais curto:** [L03 — Silva, Leite e Oliveira (2019)](livros.md#" + slug(heading(LIVROS[2],'L')) + ").",
          "3. **Leitura obrigatória da Aula 09:** [A01 — Dijkstra (1968)](artigos.md#" + slug(heading(ARTIGOS[0],'A')) + "), lido junto com [A05 — Böhm e Jacopini](artigos.md#" + slug(heading(ARTIGOS[4],'A')) + ") e o contraponto de [A06 — Knuth](artigos.md#" + slug(heading(ARTIGOS[5],'A')) + ").",
          "4. **Para praticar Clojure e Prolog:** [L20](livros.md#" + slug(heading(LIVROS[19],'L')) + ") e [L19](livros.md#" + slug(heading(LIVROS[18],'L')) + "), gratuitos e com exemplos executáveis.", "",
          "## Como citar", "",
          "- As referências seguem a **ABNT NBR 6023:2018** e podem ser copiadas para trabalhos acadêmicos. Confira as regras de formatação exigidas pela sua instituição.",
          "- O arquivo [`referencias.bib`](referencias.bib) traz os mesmos itens em BibTeX. A chave de cada entrada termina com o identificador do catálogo (ex.: `sebesta2018l02`).",
          "- Citação no texto (sistema autor-data): (SEBESTA, 2018, p. 123) ou Sebesta (2018).", "",
          "## Direitos autorais", "",
          "- O repositório **não** contém cópias de livros ou artigos de terceiros. A única exceção é o artigo de Dijkstra, que o professor distribuiu como material da Aula 09.",
          "- Os links de acesso aberto apontam para versões publicadas pelos próprios autores ou editoras.",
          "- Livros comerciais: consulte a biblioteca da Cruzeiro do Sul. A disponibilidade nas plataformas virtuais (Minha Biblioteca, Biblioteca Virtual Pearson) depende do contrato da instituição; confirme no portal do aluno.", "",
          "## Relação com as outras pastas", "",
          "- [`00 - Planejamento e Organização/bibliografia.md`](../00%20-%20Planejamento%20e%20Organização/bibliografia.md) registra a bibliografia **exatamente como está no plano de ensino**, com as seções citadas em cada aula.",
          "- [`05 - Materiais Complementares`](../05%20-%20Materiais%20Complementares/README.md) reúne o roteiro de leitura e as ferramentas para praticar.",
          "- Cada aula tem, em `05 - Materiais Complementares/materiais-complementares.md`, comentários sobre o que ler e por quê.", "",
          "## Como incluir uma referência", "",
          "1. Acrescente a entrada em `livros.md` ou `artigos.md`, no grupo adequado, com o próximo identificador livre.",
          "2. Inclua a mesma obra em `referencias.bib`.",
          "3. Atualize a tabela **Referências por aula** acima."]
    return "\n".join(L) + "\n"

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "livros.md"), "w").write(gen_livros())
open(os.path.join(OUT, "artigos.md"), "w").write(gen_artigos())
open(os.path.join(OUT, "referencias.bib"), "w").write(gen_bib())
open(os.path.join(OUT, "README.md"), "w").write(gen_readme())
print(len(LIVROS), "livros;", len(ARTIGOS), "artigos")
