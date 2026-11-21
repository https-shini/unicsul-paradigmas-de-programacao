# Paradigmas de Linguagens de Programação — UNICSUL

Repositório de estudo da disciplina **Paradigmas de Linguagens de Programação** do curso de Ciência da Computação da Universidade Cruzeiro do Sul (2º semestre de 2026, Prof. Álvaro A. Colombero Prado).

Reúne os **materiais originais** da disciplina, preservados sem alteração, e, para cada aula, um **resumo teórico** aprofundado, **exercícios** em quatro níveis, **resoluções comentadas** com código testado e **materiais complementares**. Inclui também revisões integradas, glossário, três simulados, quadros comparativos, flashcards, apostila em PDF e **seis projetos práticos** com testes automáticos. Todo o código é executado no CI a cada alteração.

> **Importante:** resumos, exercícios e resoluções foram **elaborados para este repositório** e não substituem as aulas nem são material oficial do professor. As resoluções **não são gabaritos oficiais**. Ver [Convenções de marcação](#convenções-de-marcação).

## Sumário

- [Sobre a disciplina](#sobre-a-disciplina)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Aulas](#aulas)
- [Listas, avaliações e revisão](#listas-avaliações-e-revisão)
- [Como usar este repositório](#como-usar-este-repositório)
- [Convenções de marcação](#convenções-de-marcação)
- [Projetos práticos](#projetos-práticos)
- [Código e validação](#código-e-validação)
- [Direitos e licença](#direitos-e-licença)

## Sobre a disciplina

**Ementa** (plano de ensino, `Aula01_Intro.pdf` p.3): apresentação dos principais paradigmas de programação. Fundamentação e aprofundamento dos elementos essenciais do paradigma imperativo. Conceituação e detalhamento de elementos da orientação a objetos. Apresentação do paradigma funcional e do paradigma baseado em lógica. Discussão sobre linguagens híbridas e outros paradigmas de programação.

**Objetivos** (p.4):
- **Cognitivo:** reconhecer as características de cada paradigma e associar os construtos das linguagens ao seu paradigma.
- **Habilidade:** construir programas em diferentes linguagens que materializem o paradigma predominante.
- **Atitude:** decidir, entre paradigmas diferentes, o mais adequado para cada aplicação.

**Avaliação** (p.6–7): A1 = Prova Regimental (5,0); A2 = Avaliação Parcial (3,0) + Exercícios (2,0). Nota final = A1 + A2, aprovação com 6,0 e frequência mínima de 75%.

**Linguagens usadas nas aulas:** C, C++, Java, C#, Pascal, PHP, Python, Perl, Clojure e Prolog.

Detalhes em [`00 - Planejamento e Organização`](00%20-%20Planejamento%20e%20Organização/README.md): [ementa e avaliação](00%20-%20Planejamento%20e%20Organização/ementa.md) · [objetivos](00%20-%20Planejamento%20e%20Organização/objetivos-da-disciplina.md) · [cronograma](00%20-%20Planejamento%20e%20Organização/cronograma.md) · [bibliografia](00%20-%20Planejamento%20e%20Organização/bibliografia.md) · [acompanhamento](00%20-%20Planejamento%20e%20Organização/acompanhamento.md) · [inventário dos originais](00%20-%20Planejamento%20e%20Organização/inventario-dos-materiais.md).

## Estrutura do repositório

```text
.
├── 00 - Planejamento e Organização/   ementa, objetivos, cronograma, bibliografia, acompanhamento, inventário
├── 01 - Aulas/
│   └── Aula NN - Tema/
│       ├── 01 - Slides Originais/      PDF do professor, sem alterações
│       ├── 02 - Resumo Teórico/        resumo didático com referências às páginas
│       ├── 03 - Exercícios/            básico, intermediário, avançado, aprofundamento
│       ├── 04 - Resoluções/            resoluções comentadas, separadas dos exercícios
│       └── 05 - Materiais Complementares/
├── 02 - Listas de Exercícios/          listas de revisão do professor + resoluções
├── 03 - Trabalhos e Projetos/          atividades propostas nos slides + modelo para trabalhos
├── 04 - Provas e Avaliações/           regras de avaliação + três simulados autorais
├── 05 - Materiais Complementares/      roteiro de leitura por unidade e ferramentas
├── 06 - Revisões e Sínteses/           resumo geral, unidades, mapas, quadros, erratas, flashcards, apostila PDF
├── 07 - Glossário/                     glossário alfabético
├── 08 - Referências e Fontes/          livros, artigos e documentação oficial (ABNT + BibTeX)
├── 09 - Projetos Práticos/             seis projetos com esqueleto, testes e resolução de referência
├── codigo/                             todos os programas dos Markdown, um por arquivo (gerado)
├── ferramentas/                        testes, autocorreção, geradores e instalação do ambiente
├── .devcontainer/                      ambiente do Codespaces com todas as linguagens
└── .github/workflows/                  CI: executa todo o código e valida links e diagramas
```

| Pasta | Conteúdo |
| --- | --- |
| [00 - Planejamento e Organização](00%20-%20Planejamento%20e%20Organização/README.md) | Informações gerais da disciplina e controle de estudo |
| [01 - Aulas](#aulas) | As 15 aulas, cada uma com as cinco subpastas padronizadas |
| [02 - Listas de Exercícios](02%20-%20Listas%20de%20Exercícios/README.md) | Lista 01 (Revisão I) e Lista 02 (Revisão II), originais do professor |
| [03 - Trabalhos e Projetos](03%20-%20Trabalhos%20e%20Projetos/README.md) | Não há trabalhos oficiais no material; reúne as 14 atividades das aulas |
| [04 - Provas e Avaliações](04%20-%20Provas%20e%20Avaliações/README.md) | Não há provas oficiais no material; inclui três simulados autorais com resolução |
| [05 - Materiais Complementares](05%20-%20Materiais%20Complementares/README.md) | Roteiro de leitura por unidade, ferramentas para praticar e indicações comentadas de cada aula |
| [06 - Revisões e Sínteses](06%20-%20Revisões%20e%20Sínteses/README.md) | Resumo geral, unidades, mapas conceituais, quadros, guia de estudo, questões integradoras, erratas (40 pontos), [flashcards Anki](06%20-%20Revisões%20e%20Sínteses/Flashcards/README.md) e [apostila em PDF](06%20-%20Revisões%20e%20Sínteses/Apostila/README.md) |
| [07 - Glossário](07%20-%20Glossário/glossario.md) | 95 termos em ordem alfabética, com referência às aulas |
| [08 - Referências e Fontes](08%20-%20Referências%20e%20Fontes/README.md) | 26 livros e 19 artigos (todos os indicados pelo professor + complementos), documentação oficial de 10 linguagens, índice por aula e arquivo BibTeX |
| [09 - Projetos Práticos](09%20-%20Projetos%20Práticos/README.md) | Seis projetos autorais (Python, C++, Java, Clojure, Prolog e um em quatro linguagens), com testes automáticos |
| [codigo/](codigo/README.md) | Os programas dos resumos e resoluções, um por arquivo, prontos para executar |

## Aulas

A numeração segue o **nome dos arquivos** do professor. A partir de `Aula09`, o título interno dos slides está uma unidade à frente ("Aula 10"…"Aula 16"); ver [cronograma](00%20-%20Planejamento%20e%20Organização/cronograma.md).

| Aula | Tema | Resumo | Exercícios | Resoluções |
| --- | --- | --- | --- | --- |
| [01](01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/README.md) | Apresentação da disciplina | [resumo](01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/02%20-%20Resumo%20Teórico/resumo-aula-01.md) | [exercícios](01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/03%20-%20Exercícios/exercicios-aula-01.md) | [resoluções](01%20-%20Aulas/Aula%2001%20-%20Apresentação%20da%20Disciplina/04%20-%20Resoluções/resolucoes-aula-01.md) |
| [02](01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/README.md) | Evolução das linguagens e paradigmas | [resumo](01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md) | [exercícios](01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/03%20-%20Exercícios/exercicios-aula-02.md) | [resoluções](01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/04%20-%20Resoluções/resolucoes-aula-02.md) |
| [03](01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/README.md) | Implementação das linguagens | [resumo](01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) | [exercícios](01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/03%20-%20Exercícios/exercicios-aula-03.md) | [resoluções](01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/04%20-%20Resoluções/resolucoes-aula-03.md) |
| [04](01%20-%20Aulas/Aula%2004%20-%20Sintaxe/README.md) | Sintaxe | [resumo](01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) | [exercícios](01%20-%20Aulas/Aula%2004%20-%20Sintaxe/03%20-%20Exercícios/exercicios-aula-04.md) | [resoluções](01%20-%20Aulas/Aula%2004%20-%20Sintaxe/04%20-%20Resoluções/resolucoes-aula-04.md) |
| [05](01%20-%20Aulas/Aula%2005%20-%20Semântica/README.md) | Semântica | [resumo](01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) | [exercícios](01%20-%20Aulas/Aula%2005%20-%20Semântica/03%20-%20Exercícios/exercicios-aula-05.md) | [resoluções](01%20-%20Aulas/Aula%2005%20-%20Semântica/04%20-%20Resoluções/resolucoes-aula-05.md) |
| [06](01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/README.md) | Sistema de tipos | [resumo](01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) | [exercícios](01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/03%20-%20Exercícios/exercicios-aula-06.md) | [resoluções](01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md) |
| [07](01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/README.md) | Tipos compostos | [resumo](01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md) | [exercícios](01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/03%20-%20Exercícios/exercicios-aula-07.md) | [resoluções](01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/04%20-%20Resoluções/resolucoes-aula-07.md) |
| [08](01%20-%20Aulas/Aula%2008%20-%20Ponteiros/README.md) | Ponteiros | [resumo](01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) | [exercícios](01%20-%20Aulas/Aula%2008%20-%20Ponteiros/03%20-%20Exercícios/exercicios-aula-08.md) | [resoluções](01%20-%20Aulas/Aula%2008%20-%20Ponteiros/04%20-%20Resoluções/resolucoes-aula-08.md) |
| [09](01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/README.md) | Paradigma imperativo I + artigo de Dijkstra | [resumo](01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [artigo](01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) | [exercícios](01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/03%20-%20Exercícios/exercicios-aula-09.md) | [resoluções](01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/04%20-%20Resoluções/resolucoes-aula-09.md) |
| [10](01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/README.md) | Paradigma imperativo II | [resumo](01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) | [exercícios](01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/03%20-%20Exercícios/exercicios-aula-10.md) | [resoluções](01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/04%20-%20Resoluções/resolucoes-aula-10.md) |
| [11](01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/README.md) | Paradigma imperativo III | [resumo](01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md) | [exercícios](01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/03%20-%20Exercícios/exercicios-aula-11.md) | [resoluções](01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md) |
| [12](01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/README.md) | Orientação a objetos I | [resumo](01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) | [exercícios](01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/03%20-%20Exercícios/exercicios-aula-12.md) | [resoluções](01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/04%20-%20Resoluções/resolucoes-aula-12.md) |
| [13](01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/README.md) | Orientação a objetos II | [resumo](01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) | [exercícios](01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/03%20-%20Exercícios/exercicios-aula-13.md) | [resoluções](01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md) |
| [14](01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/README.md) | Paradigma funcional (Clojure) | [resumo](01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) | [exercícios](01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/03%20-%20Exercícios/exercicios-aula-14.md) | [resoluções](01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/04%20-%20Resoluções/resolucoes-aula-14.md) |
| [15](01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/README.md) | Paradigma lógico (Prolog) | [resumo](01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) | [exercícios](01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/03%20-%20Exercícios/exercicios-aula-15.md) | [resoluções](01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/04%20-%20Resoluções/resolucoes-aula-15.md) |

## Listas, avaliações e revisão

- **Listas do professor:** [Lista 01 — Revisão I](02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/README.md) (11 questões, foco em funcional e lógico) · [Lista 02 — Revisão II](02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md) (12 questões, disciplina inteira).
- **Simulados autorais**, cada um com resolução separada: [01](04%20-%20Provas%20e%20Avaliações/Simulados/simulado-01.md) (disciplina inteira) · [02](04%20-%20Provas%20e%20Avaliações/Simulados/simulado-02.md) (Aulas 02–11) · [03](04%20-%20Provas%20e%20Avaliações/Simulados/simulado-03.md) (Aulas 12–15).
- **Para estudar em qualquer lugar:** [flashcards Anki](06%20-%20Revisões%20e%20Sínteses/Flashcards/README.md) (143 cartões) · [apostila e caderno de exercícios em PDF](06%20-%20Revisões%20e%20Sínteses/Apostila/README.md).
- **Revisão:**
  - [Resumo geral](06%20-%20Revisões%20e%20Sínteses/resumo-geral-da-disciplina.md) · [Revisões por unidade](06%20-%20Revisões%20e%20Sínteses/README.md#revisões-por-unidade) · [Mapas conceituais](06%20-%20Revisões%20e%20Sínteses/mapas-conceituais.md)
  - [Quadros comparativos](06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md) · [Guia de estudo](06%20-%20Revisões%20e%20Sínteses/guia-de-estudo-para-provas.md) · [Questões integradoras](06%20-%20Revisões%20e%20Sínteses/questoes-integradoras.md)
  - [Erratas do material](06%20-%20Revisões%20e%20Sínteses/erratas-e-inconsistencias.md) · [Glossário](07%20-%20Glossário/glossario.md)
- **Fontes:** [livros](08%20-%20Referências%20e%20Fontes/livros.md) · [artigos](08%20-%20Referências%20e%20Fontes/artigos.md) · [documentação oficial](08%20-%20Referências%20e%20Fontes/documentacao-oficial.md) · [referências por aula](08%20-%20Referências%20e%20Fontes/README.md#referências-por-aula)

## Como usar este repositório

1. **Durante o semestre**, para cada aula:
   - abra os slides originais;
   - leia o resumo;
   - faça os exercícios **sem** consultar as resoluções;
   - só então confira.
   Registre o progresso em [acompanhamento.md](00%20-%20Planejamento%20e%20Organização/acompanhamento.md).
2. **Para praticar**, faça os [projetos práticos](09%20-%20Projetos%20Práticos/README.md) à medida que as aulas avançam, e confira suas soluções dos exercícios com `python3 ferramentas/verificar.py` (ver [Código e validação](#código-e-validação)).
3. **Antes das avaliações**, siga o [guia de estudo](06%20-%20Revisões%20e%20Sínteses/guia-de-estudo-para-provas.md): resumo geral → revisões por unidade → flashcards → listas do professor → simulados.
4. **Em caso de dúvida conceitual**, consulte o [glossário](07%20-%20Glossário/glossario.md) e as [erratas](06%20-%20Revisões%20e%20Sínteses/erratas-e-inconsistencias.md). Os slides têm alguns erros e divergências, todos apontados.
5. **Para incluir material novo:**
   - coloque o original, sem renomear, na pasta `01 - Slides Originais` (ou `01 - Enunciado Original`);
   - registre-o no [inventário](00%20-%20Planejamento%20e%20Organização/inventario-dos-materiais.md);
   - siga a mesma estrutura de cinco subpastas.

## Convenções de marcação

Todo conteúdo produzido para o repositório indica sua origem com uma das marcações abaixo.

| Marcação | Significado |
| --- | --- |
| **[Material original]** | Conteúdo extraído dos slides ou PDFs do professor, transcrito ou parafraseado com fidelidade, sempre com a página (`p.N`) |
| **[Explicação elaborada]** | Explicação didática produzida para o repositório, a partir do material original |
| **[Complemento]** | Informação que **não está** no material do professor (literatura, documentação oficial, versões mais recentes das linguagens) |
| **[Atenção]** | Erro, inconsistência ou divergência no material, ou ponto que exige cuidado; consolidados em [erratas](06%20-%20Revisões%20e%20Sínteses/erratas-e-inconsistencias.md) |
| **[Exercício autoral]** | Exercício criado para o repositório, não proposto pelo professor |
| **[Resolução elaborada]** | Resolução produzida para o repositório. **Não é gabarito oficial** |

**Outras convenções:**

- `AulaXX p.N` = página N do PDF da aula XX (numeração do arquivo PDF, que inclui a capa).
- Os exercícios de cada aula seguem quatro níveis: **Básico**, **Intermediário**, **Avançado/Prática** e **Aprofundamento**. As atividades propostas pelo professor aparecem identificadas como "(original)".
- As resoluções ficam **sempre** em arquivo separado dos enunciados.

## Projetos práticos

Seis projetos autorais aplicam o conteúdo em programas completos. Cada um tem enunciado com requisitos, esqueleto em `inicial/`, testes automáticos e resolução de referência em `solucao/` — ver [09 - Projetos Práticos](09%20-%20Projetos%20Práticos/README.md).

| Projeto | Linguagem | Aulas |
| --- | --- | --- |
| P1 · Interpretador de expressões (léxico, BNF, interpretador, bytecode e VM) | Python | 03–06 |
| P2 · Pilha e fila encadeadas, sem vazamento de memória | C++ | 07, 08, 12 |
| P3 · Acervo da biblioteca: classe abstrata, interface, polimorfismo | Java | 12, 13 |
| P4 · Estatísticas de texto com funções puras | Clojure | 14 |
| P5 · Grade curricular e pré-requisitos | Prolog | 15 |
| P6 · A regra de aprovação da UNICSUL em quatro paradigmas | C, Java, Clojure, Prolog | 01, 09–15 |

## Código e validação

Todo programa dos resumos, resoluções, listas, simulados e revisões é **compilado e executado automaticamente**. Um comentário HTML invisível antes de cada bloco (`<!-- teste: ... -->`) registra a entrada usada e a saída esperada; os mesmos programas estão em [`codigo/`](codigo/README.md), um por arquivo.

**Ambiente pronto:** abra o repositório no **GitHub Codespaces** (botão *Code › Codespaces*). O contêiner de [`.devcontainer/`](.devcontainer/devcontainer.json) instala as nove linguagens com o mesmo script do CI, [`ferramentas/instalar-ambiente.sh`](ferramentas/instalar-ambiente.sh), que também funciona num Ubuntu/WSL.

| Linguagem | No CI e no Codespaces | Sem a ferramenta oficial |
| --- | --- | --- |
| C / C++ | GCC / G++ (`-std=c11` / `-std=c++17`) | — |
| Java | OpenJDK 21 | — |
| C# | .NET SDK 10 | o teste é pulado |
| Python, PHP, Perl | interpretadores oficiais | — |
| Clojure | Clojure CLI (JVM) | [nbb](https://github.com/babashka/nbb) (ClojureScript); diferenças como o tipo `Ratio` estão anotadas |
| Prolog | SWI-Prolog | [Tau-Prolog](http://tau-prolog.org/) |

**Ferramentas** (pasta [`ferramentas/`](ferramentas/)):

| Comando | Para quê |
| --- | --- |
| `python3 ferramentas/verificar.py 14 E8 minha.clj` | **Autocorreção:** roda a sua solução de um exercício contra os casos da resolução (`--listar` mostra todos) |
| `python3 ferramentas/testar_projetos.py P1` | Testes dos projetos práticos (sobre `inicial/`; `--alvo` para outra pasta) |
| `python3 ferramentas/rodar.py codigo/aula-14/...` | Executa qualquer programa de `codigo/` |
| `python3 ferramentas/testar_codigo.py` | Executa e confere todos os blocos de código do repositório |
| `python3 ferramentas/verificar_links.py` · `node ferramentas/verificar_mermaid.mjs` · `python3 ferramentas/verificar_bib.py` | Links e âncoras internos, sintaxe dos diagramas Mermaid, BibTeX × catálogo |
| `python3 ferramentas/gerar_codigo.py` · `ferramentas/geradores/*.py` | Regeneram `codigo/`, glossário, flashcards, referências e apostila a partir dos Markdown |

O [workflow de validação](.github/workflows/validacao.yml) roda tudo isso a cada *push* e *pull request*. Os diagramas são escritos em [Mermaid](https://mermaid.js.org/), que o GitHub renderiza nativamente.

## Direitos e licença

- Os **materiais originais** (pastas `01 - Slides Originais` e `01 - Enunciado Original`) são de autoria do professor da disciplina, e o artigo de Dijkstra pertence aos seus detentores. Livros e artigos de terceiros **não** são copiados: o catálogo em `08 - Referências e Fontes` traz apenas as referências e links para versões distribuídas legalmente. Estão aqui **apenas para estudo**, sem alteração, e **não** são cobertos pela licença deste repositório.
- O **conteúdo elaborado** (resumos, exercícios, resoluções, revisões, glossário) é distribuído sob a [licença MIT](LICENSE).
