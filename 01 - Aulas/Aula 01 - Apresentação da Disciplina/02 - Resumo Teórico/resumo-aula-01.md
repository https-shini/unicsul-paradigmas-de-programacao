# Aula 01 — Apresentação da Disciplina · Resumo teórico

> **Fonte:** [`Aula01_Intro.pdf`](../01%20-%20Slides%20Originais/Aula01_Intro.pdf) (9 páginas) — "Apresentação da Disciplina (Plano de ensino)", Prof. Álvaro A. Colombero Prado, 2º semestre de 2026.
> **Legenda das marcações:** ver [Convenções do repositório](../../../README.md#convenções-de-marcação). Citações no formato `p.N` indicam a página do PDF.

---

## 1. Para que serve esta aula

A Aula 01 não traz conteúdo técnico. Ela apresenta o **contrato da disciplina**: o que será estudado, com que objetivo, como você será avaliado e quais livros sustentam o curso. Entender isso cedo ajuda a planejar o semestre e a saber onde está o peso das avaliações.

## 2. O professor (p.2)

**[Material original]** Prof. Álvaro A. Colombero Prado — graduado em Sistemas de Informação (2010), pós-graduado em Engenharia de Software (2011), mestre em Engenharia de Produção (2013). Leciona em Análise e Desenvolvimento de Sistemas, Ciência da Computação e Sistemas de Informação.

## 3. Ementa (p.3)

**[Material original]** A ementa tem cinco blocos:

1. Apresentação dos principais paradigmas de programação.
2. Fundamentação e aprofundamento dos elementos essenciais do **paradigma imperativo**.
3. Conceituação e detalhamento de elementos da **orientação a objetos**.
4. Apresentação do **paradigma funcional** e do **paradigma baseado em lógica**.
5. Discussão sobre **linguagens híbridas** e outros paradigmas.

**[Explicação elaborada]** Repare no peso relativo: o imperativo é *fundamentado e aprofundado*, a OO é *conceituada e detalhada*, enquanto funcional e lógico são *apresentados*. Isso se confirma na distribuição das aulas: três aulas de imperativo (09–11), duas de OO (12–13) e uma de cada um dos outros dois (14–15).

> **[Atenção]** A ementa contém o erro de digitação "doaradigma" (= "do paradigma").

## 4. Objetivos (p.4)

**[Material original]**

| Dimensão | Objetivo |
| --- | --- |
| Cognitivo | Reconhecer as características de cada paradigma e identificar os construtos das linguagens, associando-os ao seu paradigma. |
| Habilidades | Construir programas em diferentes linguagens, materializando aspectos importantes do paradigma predominante. |
| Atitudes | Ser capaz de decidir, entre paradigmas diferentes, o mais adequado para cada aplicação. |

**[Explicação elaborada]** Os três objetivos sobem de nível: *reconhecer* (saber o que é), *construir* (saber fazer) e *decidir* (saber escolher). As listas de revisão da disciplina cobram sobretudo o primeiro nível — diferenciar e explicar conceitos —, com algumas questões de construção em Clojure e Prolog.

## 5. Conteúdo programático (p.5)

**[Material original]** Introdução à disciplina; tipos e variáveis; paradigma imperativo (estruturado); paradigma orientado a objetos; paradigma funcional; paradigma de programação em lógica; tópicos adicionais.

**[Explicação elaborada]** Mapeamento para as aulas deste repositório:

| Item do conteúdo | Aulas |
| --- | --- |
| Introdução | [01](../../Aula%2001%20-%20Apresentação%20da%20Disciplina/), [02](../../Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/), [03](../../Aula%2003%20-%20Implementação%20das%20Linguagens/) |
| Tipos e variáveis | [04](../../Aula%2004%20-%20Sintaxe/), [05](../../Aula%2005%20-%20Semântica/), [06](../../Aula%2006%20-%20Sistema%20de%20Tipos/), [07](../../Aula%2007%20-%20Tipos%20Compostos/), [08](../../Aula%2008%20-%20Ponteiros/) |
| Paradigma imperativo (estruturado) | [09](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/), [10](../../Aula%2010%20-%20Paradigma%20Imperativo%20II/), [11](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/) |
| Orientado a objetos | [12](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/), [13](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/) |
| Funcional | [14](../../Aula%2014%20-%20Paradigma%20Funcional/) |
| Programação em lógica | [15](../../Aula%2015%20-%20Paradigma%20Lógico/) |
| Revisão | [Lista 01](../../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/), [Lista 02](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/) |

"Tópicos adicionais" e "linguagens híbridas" não têm aula própria no material disponível; aparecem de forma transversal (Java 8 com lambdas, linguagens multiparadigma, implementação híbrida na Aula 03).

## 6. Sistema de avaliação (p.6–7)

**[Material original]**

| Componente | Valor | Composição |
| --- | --- | --- |
| A1 | 5,0 | Prova Regimental (PR ou PRI) |
| A2 | 5,0 | Avaliação Parcial (3,0) + Exercícios (2,0) |
| **Nota final** | **10,0** | **A1 + A2** |

Regras do fluxograma (p.7):

1. Se **A1 + A2 ≥ 6,0** → aprovado.
2. Quem **não obtiver pelo menos 1 ponto na A1 ou na A2** está reprovado e **não pode** fazer a Avaliação Final (AF).
3. Caso contrário, faz a **AF**, que vale 5,0 e **substitui a menor nota** (A1 ou A2).
4. Se **AF + maior nota ≥ 6,0** → aprovado; senão, reprovado.
5. Frequência inferior a **75%** reprova, independentemente das notas.

**[Explicação elaborada]** Consequências práticas:

- Como a AF substitui a menor nota e vale 5,0, quem precisa da AF tem de somar ao menos 6,0 com a **maior** das duas notas. Exemplo: A1 = 4,5 e A2 = 1,0 → precisa de AF ≥ 1,5. Exemplo: A1 = 2,0 e A2 = 1,5 → precisa de AF ≥ 4,0.
- Tirar menos de 1,0 em qualquer uma das partes elimina a chance de AF — por isso a parte de Exercícios (2,0) da A2 funciona como "seguro".
- A AF só faz sentido se a maior nota for ≥ 1,0 (pois 1,0 + 5,0 = 6,0).

> **[Atenção]** O slide da p.6 rotula como "Noite" os horários 08h30–09h45 / 09h55–11h10, que são matutinos. Provavelmente é resíduo de outro plano de ensino. O fluxograma da p.7 é creditado a "Slide, Prof. Ledón, 2014".

## 7. Bibliografia (p.8–9)

**[Material original]** Detalhada em [`bibliografia.md`](../../../00%20-%20Planejamento%20e%20Organização/bibliografia.md).

- **Básica:** Ascencio & Campos, *Fundamentos da programação de computadores* (Pearson, 2007); Sebesta, *Conceitos de Linguagens de Programação* (Bookman, 2018); Silva et al., *Paradigmas de programação* (SAGAH, 2019).
- **Complementar:** Dijkstra, *Go To Statement Considered Harmful* (CACM, 1968); Dybvig, *The Scheme Programming Language*; Eck, *Introduction to Programming Using Java*; Endriss, *An Introduction to Prolog Programming*; Normark, *Functional Programming in Scheme*.

**[Explicação elaborada]** A bibliografia complementar antecipa a trilha do curso: Dijkstra → programação estruturada (Aula 09); Java → OO (Aulas 12–13); Scheme → funcional (Aula 14); Prolog → lógico (Aula 15). Nas aulas, o professor cita com frequência Sebesta (9ª ed.) e Tucker & Noonan como material de apoio, com as seções indicadas em cada aula.

## 8. Pontos para levar desta aula

- A disciplina é sobre **reconhecer, construir e escolher** paradigmas.
- O imperativo é o eixo mais aprofundado; funcional e lógico são introdutórios.
- A AF **substitui a menor nota**; é preciso ≥ 1,0 em A1 **e** em A2 para ter direito a ela.

---

**Próxima aula:** [Aula 02 — Evolução das Linguagens e Paradigmas](../../Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md)
