<!-- nav:topo -->
[Início](../README.md) › **09 - Projetos Práticos** · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# 09 — Projetos Práticos

> **[Exercício autoral]** Projetos elaborados para este repositório, para aplicar o conteúdo da disciplina em programas de verdade. **Não são trabalhos do professor** e não valem nota. Trabalhos oficiais, quando houver, ficam em [03 - Trabalhos e Projetos](../03%20-%20Trabalhos%20e%20Projetos/README.md). As pastas `solucao/` são **[Resolução elaborada]**, não gabarito.

## Os projetos

| # | Projeto | Linguagem | Aulas | O que você constrói |
| :-: | --- | --- | --- | --- |
| P1 | [Interpretador de expressões](P1%20-%20Interpretador%20de%20Expressões/README.md) | Python | 03–06 | Analisador léxico, sintático (BNF), interpretador e compilador para uma máquina virtual de pilha |
| P2 | [Estruturas encadeadas em C++](P2%20-%20Estruturas%20Encadeadas%20em%20C++/README.md) | C++ | 07, 08, 12 | Pilha e fila com ponteiros e `new`/`delete`, sem vazar memória (testes com AddressSanitizer) |
| P3 | [Acervo da biblioteca em Java](P3%20-%20Acervo%20da%20Biblioteca%20em%20Java/README.md) | Java | 12, 13 | Hierarquia com classe abstrata, interface, sobrecarga, sobrescrita e polimorfismo |
| P4 | [Estatísticas de texto em Clojure](P4%20-%20Estatísticas%20de%20Texto%20em%20Clojure/README.md) | Clojure | 14 | Análise de texto só com funções puras, recursão e `map`/`filter`/`reduce` |
| P5 | [Grade curricular em Prolog](P5%20-%20Grade%20Curricular%20em%20Prolog/README.md) | Prolog | 15 | Regras sobre pré-requisitos: o que cada aluno pode cursar, dependências, formatura |
| P6 | [Situação acadêmica em quatro paradigmas](P6%20-%20Situação%20Acadêmica%20em%20Quatro%20Paradigmas/README.md) | C, Java, Clojure, Prolog | 01, 09–15 | A regra de aprovação da UNICSUL implementada quatro vezes, para comparar os paradigmas |

**Ordem sugerida:** acompanhe as aulas — P1 depois da Aula 05, P2 depois da 08, P3 depois da 13, P4 depois da 14, P5 depois da 15 — e termine com o P6, que serve de revisão para a prova.

## Como cada projeto está organizado

```text
Pn - Nome/
├── README.md       ← enunciado: objetivo, conceitos (com links para os resumos), requisitos R1…Rn,
│                     como testar, critérios de autoavaliação, extensões e perguntas para refletir
├── projeto.json    ← descreve os testes para a ferramenta
├── inicial/        ← ESQUELETO que compila, com TODO onde você deve programar
├── solucao/        ← resolução de referência, comentada
└── testes/         ← testes automáticos
```

## Testes automáticos

Uma única ferramenta roda os testes de qualquer projeto, em qualquer linguagem:

```bash
python3 ferramentas/testar_projetos.py --listar               # lista os projetos e as linguagens
python3 ferramentas/testar_projetos.py P1                     # testa P1/inicial — o seu código
python3 ferramentas/testar_projetos.py P6 --linguagem java    # só uma das suítes
python3 ferramentas/testar_projetos.py P3 --alvo ~/meu-p3     # testa outra pasta
python3 ferramentas/testar_projetos.py P2 --alvo solucao      # testa a resolução de referência
python3 ferramentas/verificar.py projeto P4                   # o mesmo, pelo verificador de exercícios
```

O resultado de cada suíte é **OK** (tudo passou), **FALHA** (os testes rodaram e algum falhou), **ERRO** (não compilou ou não chegou a rodar) ou **PULADO** (a linguagem não está instalada). No [Codespaces](../README.md#código-e-validação), todas as linguagens já vêm instaladas.

Sugestão de trabalho: copie `inicial/` para uma pasta sua (ou crie um *branch*), programe e rode os testes com `--alvo`. Assim, `inicial/` continua limpo para recomeçar.

> **No CI:** a cada *push*, o GitHub Actions confere que as seis soluções passam em todos os testes e que os esqueletos de `inicial/` continuam compilando.

## Relação com as avaliações

Os projetos não substituem as listas do professor, mas treinam exatamente o que elas cobram:

| Pergunta típica das listas | Projeto que a responde na prática |
| --- | --- |
| Compilação × interpretação × híbrida; fases do compilador | P1 |
| BNF, precedência, análise léxica e sintática | P1 |
| Alocação estática × dinâmica; ponteiros; heap | P2 |
| TDA, encapsulamento, independência de representação | P2, P3 |
| Classe abstrata × interface; sobrecarga × sobrescrita; polimorfismo | P3 |
| Funções puras, imutabilidade, recursão, ordem superior | P4 |
| Fatos, regras, consultas, unificação, recursão em Prolog | P5 |
| Diferencie os paradigmas imperativo, OO, funcional e lógico | P6 |


<!-- nav:rodape -->

---

← [08 — Referências e Fontes](../08%20-%20Referências%20e%20Fontes/README.md) · [10 - Caderno de Anotações](../10%20-%20Caderno%20de%20Anotações/README.md) →

**Links para esta página (3):** [Acompanhamento de estudo](../00%20-%20Planejamento%20e%20Organização/acompanhamento.md) · [03 — Trabalhos e Projetos](../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../README.md)

<!-- /nav:rodape -->
