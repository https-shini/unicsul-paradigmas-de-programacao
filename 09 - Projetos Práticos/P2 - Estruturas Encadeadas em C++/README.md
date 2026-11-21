# P2 — Estruturas encadeadas em C++: pilha e fila

> **[Exercício autoral]** Projeto prático elaborado para este repositório. **Não é trabalho do professor** e não vale nota. A pasta `solucao/` é uma **[Resolução elaborada]**, não gabarito oficial.

| | |
| --- | --- |
| **Linguagem** | C++17 |
| **Aulas** | 07 (vetores), 08 (ponteiros, heap, `new`/`delete`), 12 (TDA, encapsulamento, construtor e destrutor) |
| **Duração sugerida** | 3 a 4 horas |
| **Testes** | 29 verificações em `testes/testes.cpp`, compiladas com **AddressSanitizer** |

## Objetivo

A Aula 12 termina com uma pilha encadeada em C++ (p.30): `new` para cada nó, destrutor que percorre a lista, `delete p1` no fim do `main`. Neste projeto você escreve essa pilha **sem vazar memória**, uma segunda pilha com **vetor dinâmico** e a mesma interface, e uma **fila** encadeada. Os testes rodam com o *AddressSanitizer*, que acusa vazamento, `delete` duplo e acesso fora do vetor — os erros típicos de quem gerencia memória à mão.

## Conceitos da disciplina aplicados

| Conceito | Onde aparece | Resumo |
| --- | --- | --- |
| Heap × pilha de execução; `new`/`delete`; vazamento; ponteiro pendente | todos os `.cpp` | [Aula 08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) |
| `new int[n]` × `new int(n)` (errata 14) | `PilhaVetor` | [Aula 08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) |
| Vetor de tamanho fixo × alocação dinâmica | crescimento da `PilhaVetor` | [Aula 07](../../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md) |
| TDA, encapsulamento, independência de representação | `Pilha` × `PilhaVetor` com a mesma interface | [Aula 12](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) |
| Construtor, destrutor, ciclo de vida do objeto | `~Pilha()`, `~Fila()` | [Aula 12](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) |
| *Aliasing* (dois nomes para a mesma memória) | cópia rasa × profunda | [Aula 08](../../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) |

## Estrutura

```text
P2 - Estruturas Encadeadas em C++/
├── inicial/      ← ESQUELETO: os .hpp estão prontos; complete os .cpp (procure os TODO)
├── solucao/      ← resolução de referência
└── testes/testes.cpp
```

Os cabeçalhos (`pilha.hpp`, `pilha_vetor.hpp`, `fila.hpp`) definem a interface e **não devem mudar** — os testes dependem deles. O `main.cpp` é uma demonstração no estilo do slide.

## Requisitos

- **R1. `Pilha::push`** cria um nó no heap que aponta para o topo atual.
- **R2. `pop` e `topo`** em pilha vazia lançam `std::underflow_error`. **[Atenção]** o slide devolve `-1`, o que impede empilhar o valor −1; a exceção separa o erro do dado.
- **R3. Destrutor** libera todos os nós restantes. Cada `pop` libera o seu nó.
- **R4. `PilhaVetor`** guarda os dados em `new int[capacidade]` e libera com `delete[]`.
- **R5.** Quando a `PilhaVetor` enche, ela aloca um vetor com o **dobro** da capacidade, copia os valores e libera o antigo.
- **R6. `Fila`** encadeada com ponteiros para o **início** (remoção) e o **fim** (inserção), ambas em tempo constante. Ao esvaziar, `fim_` volta a `nullptr`.
- **R7. Cópia profunda da `Pilha`** (construtor de cópia e `operator=`): a cópia tem **novos** nós, e `p = p` não pode apagar a pilha. As outras classes **proíbem** a cópia (`= delete`). Por quê? Ver "Para refletir".

## Como testar

```bash
python3 ferramentas/testar_projetos.py P2          # compila inicial/*.cpp + testes, com sanitizers
cd "09 - Projetos Práticos/P2 - Estruturas Encadeadas em C++/inicial"
g++ -std=c++17 -Wall *.cpp -o demo && ./demo       # a demonstração
```

Se os testes passarem mas aparecer `ERROR: LeakSanitizer: detected memory leaks`, faltou um `delete`. A mensagem mostra a linha do `new` cujo nó não foi liberado.

## Critérios de autoavaliação

| Critério | Peso |
| --- | :-: |
| Todos os testes passam **sem** relato do AddressSanitizer | 45% |
| `new`/`delete` e `new[]`/`delete[]` sempre em pares; nenhum ponteiro usado depois do `delete` | 20% |
| Cópia profunda correta, inclusive na autoatribuição | 15% |
| `Pilha` e `PilhaVetor` passam nos **mesmos** testes sem mudar o cliente | 10% |
| Código legível: nomes, comentários nos pontos delicados (fila esvaziando, realocação) | 10% |

## Extensões

1. **Modelo:** transforme `Pilha` em `template <class T>` e use-a com `std::string`.
2. **Ponteiros inteligentes:** reescreva a pilha com `std::unique_ptr<Nodo>`. O destrutor ainda é necessário?
3. **Fila circular** em vetor (`inicio`, `fim`, `% capacidade`) — compare com a Questão 11 do [simulado 03](../../04%20-%20Provas%20e%20Avaliações/Simulados/simulado-03.md), em Java.
4. **Movimento:** implemente o construtor de movimento (`Pilha(Pilha&&)`) e meça a diferença ao devolver uma pilha grande de uma função.

## Para refletir

- O que aconteceria com a cópia **rasa** padrão do C++ (`Pilha b = a;` copiando só o ponteiro `topo_`) quando `a` e `b` saíssem de escopo?
- Em Java, a pilha encadeada da Aula 12 não tem destrutor. Quem libera os nós? Quais as vantagens e os custos de cada abordagem (Aula 12 p.28)?
- Por que `PilhaVetor` dobra a capacidade em vez de somar 1? Pense em quantas cópias são feitas para empilhar *n* elementos.
