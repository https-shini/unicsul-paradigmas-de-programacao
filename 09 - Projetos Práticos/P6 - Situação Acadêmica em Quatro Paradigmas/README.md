<!-- nav:topo -->
[Início](../../README.md) › [09 - Projetos Práticos](../README.md) › **P6** · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# P6 — Situação acadêmica em quatro paradigmas

> **[Exercício autoral]** Projeto prático elaborado para este repositório. **Não é trabalho do professor** e não vale nota. A pasta `solucao/` é uma **[Resolução elaborada]**, não gabarito oficial.

| | |
| --- | --- |
| **Linguagens** | C (imperativo), Java (orientado a objetos), Clojure (funcional), Prolog (lógico) |
| **Aulas** | 01 (regra de avaliação), 09–11, 12–13, 14 e 15 — é o projeto de **encerramento** da disciplina |
| **Duração sugerida** | 1 hora por linguagem, mais a comparação |
| **Testes** | os mesmos **18 casos** de `casos.csv` nas quatro linguagens (mais 4 de nota mínima; Java tem também 4 de validação) |

## Objetivo

Implementar **a mesma regra** nos quatro paradigmas da disciplina e comparar as soluções. A regra é uma que você conhece bem: a de aprovação da própria UNICSUL, apresentada na Aula 01. A pergunta mais frequente das listas — "diferencie os paradigmas" — fica muito mais fácil de responder depois de escrever o mesmo programa quatro vezes.

## A regra (Aula 01 p.6–7)

**[Material original]** A1 = Prova Regimental (5,0); A2 = Avaliação Parcial (3,0) + Exercícios (2,0). A1 + A2 ≥ 6,0 aprova. Quem não consegue pelo menos 1 ponto na A1 ou na A2 está reprovado e não pode fazer a AF. A AF vale 5,0 e substitui a menor nota; com AF + maior nota ≥ 6,0, aprovado. Frequência abaixo de 75% reprova. Detalhes na [ementa](../../00%20-%20Planejamento%20e%20Organização/ementa.md#avaliação).

**[Explicação elaborada]** Em forma de algoritmo, na ordem em que as condições são testadas:

| # | Condição | Situação |
| :-: | --- | --- |
| 1 | frequência < 75% | REPROVADO POR FALTA |
| 2 | A1 + A2 ≥ 6 | APROVADO |
| 3 | A1 < 1 ou A2 < 1 | REPROVADO (sem direito à AF) |
| 4 | ainda não fez a AF | AF (nota mínima = 6 − maior nota) |
| 5 | AF + maior nota ≥ 6 | APROVADO NA AF |
| 6 | caso contrário | REPROVADO NA AF |

> **[Atenção]** "Quem não conseguir pelo menos 1 ponto na A1 ou A2" admite duas leituras: (a) menos de 1 ponto em **qualquer uma** das notas impede a AF; (b) só impede quem tem menos de 1 ponto nas **duas**. Este projeto segue a leitura (a), a mesma da ementa do repositório. Na leitura (b), a regra 3 seria redundante: com as duas notas abaixo de 1, nem a AF máxima (5,0) alcançaria 6. Confirme a regra vigente com a coordenação. Se a sua leitura for outra, mude a regra 3 **e** os casos em `casos.csv`, e regenere os testes.

## Como cada paradigma representa os dados

| | C | Java | Clojure | Prolog |
| --- | --- | --- | --- | --- |
| **Entrada** | quatro `double` | objeto `Desempenho` (atributos `private final`) | mapa `{:a1 :a2 :af :freq}` | quatro argumentos |
| **"Não fez a AF"** | valor sentinela `SEM_AF` (−1) | `Double af = null` | `:af nil` | átomo `nenhuma` |
| **Resultado** | `const char *` | `String` | palavra-chave (`:aprovado-na-af`) | átomo (`aprovado_na_af`) |
| **Validação** | nenhuma (responsabilidade de quem chama) | no construtor (`IllegalArgumentException`) | — | — |
| **Controle** | `if` em sequência com `return` | métodos que se apoiam uns nos outros | `cond` (uma expressão) | uma cláusula por situação |

## Estrutura

```text
P6 - Situação Acadêmica em Quatro Paradigmas/
├── casos.csv                 ← os casos de teste, com comentário — a "especificação"
├── inicial/{c,java,clojure,prolog}/   ← ESQUELETOS
├── solucao/{c,java,clojure,prolog}/   ← resoluções de referência
└── testes/
    ├── gerar_testes.py       ← gera os quatro arquivos abaixo a partir de casos.csv
    ├── testes.c · TestesSituacao.java · situacao_test.clj · testes.pl
```

## Requisitos

- **R1. C** — `situacao.c`: implemente `situacao()` e `nota_minima_af()` declaradas em `situacao.h`.
- **R2. Java** — `Desempenho.java`: valide as notas no construtor e implemente `notaMinimaAF()`, `podeFazerAF()` e `situacao()`.
- **R3. Clojure** — `situacao.clj`: funções puras `situacao` (recebe o mapa) e `nota-minima-af`.
- **R4. Prolog** — `situacao.pl`: `situacao/5` com **uma resposta só** para cada consulta, e `nota_minima_af/3`.
- **R5. Comparação** — escreva, num arquivo `comparacao.md` na sua pasta, uma tabela com, para cada linguagem: número de linhas da regra, como a ordem das condições é garantida, como o "sem AF" é representado e o que aconteceria com uma nota inválida.

## Como testar

```bash
python3 ferramentas/testar_projetos.py P6                       # as quatro linguagens
python3 ferramentas/testar_projetos.py P6 --linguagem prolog    # só uma: c, java, clojure ou prolog
```

Depois de mudar `casos.csv`: `python3 "09 - Projetos Práticos/P6 - Situação Acadêmica em Quatro Paradigmas/testes/gerar_testes.py"`.

## Critérios de autoavaliação

| Critério | Peso |
| --- | :-: |
| Os testes passam nas quatro linguagens | 40% |
| Cada versão usa o estilo do seu paradigma (por exemplo: sem `if` encadeado imitando C dentro do Prolog) | 25% |
| A comparação (R5) aponta diferenças concretas, com trechos do seu código | 25% |
| Casos novos acrescentados a `casos.csv` para situações que você achou mal cobertas | 10% |

## Extensões

1. **Turma inteira:** leia um arquivo com vários alunos e mostre quantos estão em cada situação — em Clojure, `frequencies` + `map`; em Prolog, `findall`; em C, um vetor de `struct`.
2. **Quinta linguagem:** Python ou C# (com `double?` para a AF ausente, como na Aula 11).
3. **Notas em décimos:** troque `double` por inteiros (35 = 3,5) e discuta a representação de ponto flutuante da Aula 06.
4. **Explicação:** em Prolog, faça `por_que(A1, A2, AF, Freq, Motivo)` devolver a regra que decidiu a situação.

## Para refletir

- Em C e em Java, a **ordem** dos `if` faz parte da regra. Em Prolog, a solução de referência repete condições (`Freq >= 75`, `A1 + A2 < 6`) em várias cláusulas. Por quê? Qual seria a alternativa com corte (`!`) e o que se perde?
- Qual versão você entregaria a alguém que só conhece a regra, e não programação? Isso tem a ver com "declarativo × procedural" (Aula 15 [p.3–5](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/01%20-%20Slides%20Originais/README.md#página-3))?
- O `null` do Java e o `nil` do Clojure resolvem o mesmo problema que o `-1` do C. Que erros cada solução permite?


<!-- nav:rodape -->

---

← [P5 — Grade curricular em Prolog](../P5%20-%20Grade%20Curricular%20em%20Prolog/README.md)

**Links para esta página (1):** [09 — Projetos Práticos](../README.md)

<!-- /nav:rodape -->
