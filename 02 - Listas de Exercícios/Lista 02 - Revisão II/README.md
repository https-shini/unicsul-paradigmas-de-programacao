<!-- nav:topo -->
[Início](../../README.md) › [02 - Listas de Exercícios](../README.md) › **Lista 02** · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Lista 02 — Revisão II ("Exercícios – Revisão II")

> **Original:** [`Aula16b_ExRevisao2.pdf`](01%20-%20Enunciado%20Original/Aula16b_ExRevisao2.pdf) (1 página). Lista de revisão disponibilizada pelo professor.
> **Resolução comentada:** [`resolucao-lista-02.md`](02%20-%20Resolução/resolucao-lista-02.md) — **[Resolução elaborada]**, não é gabarito oficial.

## Assuntos e aulas relacionadas

A lista percorre **toda a disciplina**, na ordem das aulas. As 12 questões são **discursivas** e quase todas pedem **diferenciar ou comparar** conceitos.

| Questão | Assunto | Aulas |
| --- | --- | --- |
| Q1 | Os quatro paradigmas: modelagem e resolução | [02](../../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md#5-os-quatro-paradigmas-p913), [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#2-procedural--declarativa-p35) |
| Q2 | Compilação, interpretação, híbrido; código intermediário e VM | [03](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) |
| Q3 | Sintaxe léxica, concreta e abstrata; lexema e token | [04](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md#4-os-três-níveis-de-sintaxe-p7) |
| Q4 | Escopo estático × dinâmico | [05](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md#45-escopo-p912) |
| Q5 | Tipagem estática × dinâmica; forte × fraca; coerção | [06](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) |
| Q6 | Alocação estática × dinâmica; regiões de memória; ponteiros | [08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#5-alocação-estática--dinâmica-p1213) |
| Q7 | Turing-completude; do `goto` à programação estruturada (Dijkstra) | [09](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md), [09a](../../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) |
| Q8 | Abstração de processos × de dados; coesão; acoplamento; TDA | [10](../../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md), [12](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) |
| Q9 | Os quatro modelos de passagem de parâmetros | [08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md), [11](../../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md#5-modelos-de-passagem-de-parâmetros-semânticos-e-de-implementação-p1318) |
| Q10 | Encapsulamento; modificadores; destrutores × coleta de lixo | [12](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) |
| Q11 | Herança simples × múltipla; interfaces; polimorfismo estático × dinâmico | [13](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) |
| Q12 | Funcional × lógico | [14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md), [15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) |

## Enunciados (transcrição fiel do original)

**[Material original]**

1. Diferencie os quatro principais paradigmas de programação (Imperativo, Orientado a Objetos, Funcional e Lógico) quanto à abordagem utilizada para a modelagem e resolução de problemas computacionais.
2. Compare os processos de compilação, interpretação pura e implementação híbrida, destacando o papel do código intermediário e das máquinas virtuais (como a JVM) na portabilidade e execução de programas.
3. Explique a diferença entre sintaxe léxica, sintaxe concreta e sintaxe abstrata, exemplificando o papel de lexemas e tokens na estruturação formal de uma linguagem de programação.
4. Diferencie escopo estático (léxico) de escopo dinâmico na resolução de nomes de variáveis não locais, explicando por que o escopo dinâmico tende a reduzir a legibilidade e a confiabilidade dos programas.
5. Conceitue tipagem estática versus tipagem dinâmica e explique como o nível de exigência sobre conversões implícitas (coerção) determina se uma linguagem é considerada mais fortemente ou mais fracamente tipada.
6. Diferencie alocação estática de alocação dinâmica de memória em relação ao momento em que ocorrem, às regiões de memória utilizadas (segmento estático, pilha e heap) e à relação das estruturas dinâmicas com o uso de ponteiros.
7. Explique o conceito de completude de Turing no contexto das linguagens imperativas e discorra sobre a transição da programação não estruturada (baseada em comandos goto/jump) para a programação estruturada defendida por Edsger Dijkstra.
8. Compare abstração de processos (procedural) e abstração de dados, explicando os conceitos de coesão, acoplamento e o papel dos Tipos Abstratos de Dados (TDA) na organização e manutenção de software.
9. Diferencie os modelos semânticos de passagem de parâmetros (por valor, por resultado, por valor-resultado e por referência), apontando as implicações de cada abordagem quanto ao consumo de memória e aos efeitos colaterais no argumento real.
10. Explique o papel do encapsulamento e dos modificadores de acesso (public, private e protected) na proteção do estado dos objetos, comparando também o gerenciamento de memória dinâmico entre C++ (destrutores) e Java (coleta de lixo).
11. Diferencie herança simples de herança múltipla (bem como o uso de interfaces como alternativa em Java) e explique a distinção entre polimorfismo estático (sobrecarga) e polimorfismo dinâmico (sobrescrita com vinculação tardia).
12. Compare as características fundamentais do paradigma funcional (imutabilidade, ausência de efeitos colaterais e funções puras versus impuras) com as do paradigma lógico (programação declarativa, cálculo de predicados de primeira ordem, fatos, consultas e unificação).


<!-- nav:rodape -->

---

← [Lista 01](../Lista%2001%20-%20Revisão%20I/README.md)

**Links para esta página (11):** [Cronograma](../../00%20-%20Planejamento%20e%20Organização/cronograma.md) · [Aula 15 · Resumo](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md) · [Lista 02 · Resolução](02%20-%20Resolução/resolucao-lista-02.md) · [02 — Listas de Exercícios](../README.md) · [04 — Provas e Avaliações](../../04%20-%20Provas%20e%20Avaliações/README.md) · [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-1-fundamentos.md) · [Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)](../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-2-imperativo.md) · [Revisão da Unidade 3 — Paradigma orientado a objetos (Aulas…](../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-3-orientacao-a-objetos.md) · [Revisão da Unidade 4 — Paradigmas funcional e lógico (Aulas…](../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-4-funcional-e-logico.md) · [P1 — Interpretador de expressões](../../09%20-%20Projetos%20Práticos/P1%20-%20Interpretador%20de%20Expressões/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../README.md)

<!-- /nav:rodape -->
