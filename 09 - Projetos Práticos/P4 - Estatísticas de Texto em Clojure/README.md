<!-- nav:topo -->
[Início](../../README.md) › [09 - Projetos Práticos](../README.md) › **P4** · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# P4 — Estatísticas de texto em Clojure

> **[Exercício autoral]** Projeto prático elaborado para este repositório. **Não é trabalho do professor** e não vale nota. A pasta `solucao/` é uma **[Resolução elaborada]**, não gabarito oficial.

| | |
| --- | --- |
| **Linguagem** | Clojure (roda também no nbb, a versão ClojureScript usada nos testes locais) |
| **Aula** | 14 (paradigma funcional) |
| **Duração sugerida** | 2 a 3 horas |
| **Testes** | 9 testes com 32 asserções em `testes/estatisticas_test.clj` (`clojure.test`) |

## Objetivo

Analisar um texto — contar palavras, achar as mais frequentes, medir comprimentos — usando **só funções puras**: nenhuma variável é reatribuída, e cada função devolve um valor novo em vez de alterar o que recebeu. É o exercício que mostra, na prática, o que a Aula 14 quer dizer com "computação como avaliação de funções".

```clojure
(relatorio "O gato e o rato. O rato roeu a roupa do rei de Roma!")
;; => {:total 14, :distintas 11, :media 2.642857142857143, :maior "roupa",
;;     :top3 [["rato" 2] ["gato" 1] ["rei" 1]]}
```

## Conceitos da disciplina aplicados

| Conceito | Onde aparece | Resumo |
| --- | --- | --- |
| Função pura, ausência de efeitos colaterais, imutabilidade | todas as funções; teste `t9` | [Aula 14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) |
| Recursão no lugar do laço | `contar` | [Aula 14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) |
| Funções de ordem superior (`map`, `filter`/`remove`, `reduce`, `sort-by`) | `frequencias`, `sem-stopwords`, `mais-frequentes` | [Aula 14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) |
| Notação prefixa e composição (`->>`) | `mais-frequentes`, `relatorio` | [Aula 14](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) |
| Imperativo × funcional | comparação abaixo | [Quadros comparativos](../../06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md) |

## Requisitos

| | Função | O que faz |
| --- | --- | --- |
| **R1** | `(palavras texto)` | vetor de palavras em minúsculas, sem pontuação; acentos preservados |
| **R2** | `(contar ps)` | tamanho da lista **por recursão** (sem `count` e sem `loop`) |
| **R3** | `(frequencias ps)` | mapa palavra → ocorrências, com `reduce` (sem usar `frequencies`) |
| **R4** | `(sem-stopwords ps)` | remove as palavras do conjunto `stopwords` |
| **R5** | `(mais-frequentes n freq)` | os `n` pares `[palavra qtd]` mais frequentes; empate em ordem alfabética |
| **R6** | `(comprimento-medio ps)` · `(maior-palavra ps)` | média de letras (`double`; 0.0 se vazia) · a primeira palavra mais longa (`nil` se vazia) |
| **R7** | `(indice-alfabetico ps)` | `sorted-map` letra → palavras distintas |
| **R8** | `(relatorio texto)` | combina tudo num mapa `{:total :distintas :media :maior :top3}` |

**Restrição:** nada de `def` dentro de função, `atom`, `swap!` ou qualquer outra forma de estado mutável.

## Imperativo × funcional

A mesma contagem de frequências, nos dois estilos:

```python
# imperativo (Python): um dicionário é ALTERADO a cada passo
freq = {}
for p in palavras:
    freq[p] = freq.get(p, 0) + 1
```

```clojure
;; funcional (Clojure): cada passo do reduce devolve um mapa NOVO; nada é alterado
(reduce (fn [m p] (update m p (fnil inc 0))) {} palavras)
```

No estilo imperativo, o resultado é o **estado final** de uma variável. No funcional, é o **valor de uma expressão** — por isso a mesma chamada sempre dá o mesmo resultado (transparência referencial), e o teste `t9` pode comparar `(relatorio texto)` com ele mesmo.

## Como testar

```bash
python3 ferramentas/testar_projetos.py P4      # junta inicial/estatisticas.clj com os testes e executa
```

Para experimentar no terminal: `clojure -M -i inicial/estatisticas.clj -r` abre um REPL com o arquivo carregado. Sem o Clojure instalado, `node ferramentas/node_modules/nbb/cli.js` abre um REPL do nbb (depois de `npm ci` em `ferramentas/`).

## Critérios de autoavaliação

| Critério | Peso |
| --- | :-: |
| Todos os testes passam | 40% |
| Nenhum estado mutável; cada função depende só dos argumentos | 25% |
| Uso adequado de `map`/`filter`/`reduce` em vez de recursão manual onde ela não é pedida | 15% |
| `contar` recursiva com caso base correto | 10% |
| Docstrings que dizem o que cada função recebe e devolve | 10% |

## Extensões

1. **Bigramas:** pares de palavras consecutivas mais frequentes (`partition 2 1`).
2. **Recursão de cauda:** reescreva `contar` com `loop`/`recur` e explique por que ela não estoura a pilha com listas enormes.
3. **Leitura de arquivo** na JVM (`slurp`), mantendo a parte de E/S **separada** das funções puras.
4. **Haskell:** reescreva `frequencias` e `mais-frequentes` em Haskell, a linguagem pura citada na Aula 14, e compare.

## Para refletir

- Por que `(first p)` foi evitada em `indice-alfabetico`? O que isso revela sobre a diferença entre a JVM e o JavaScript como plataformas?
- Clojure é classificada como **impura** (Aula 14 [p.9](../../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/01%20-%20Slides%20Originais/README.md#página-9)). O que, na linguagem, permitiria quebrar a restrição deste projeto?
- `sem-stopwords` passa um **conjunto** para `remove`. Que propriedade das funções de primeira classe torna isso possível?


<!-- nav:rodape -->

---

← [P3 — Acervo da biblioteca em Java](../P3%20-%20Acervo%20da%20Biblioteca%20em%20Java/README.md) · [P5 — Grade curricular em Prolog](../P5%20-%20Grade%20Curricular%20em%20Prolog/README.md) →

**Links para esta página (1):** [09 — Projetos Práticos](../README.md)

<!-- /nav:rodape -->
