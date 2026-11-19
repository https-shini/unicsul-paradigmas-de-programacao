# Aula 15 — Paradigma Lógico · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-15.md`](../03%20-%20Exercícios/exercicios-aula-15.md). Os programas e as consultas foram executados no **Tau-Prolog**, que termina a lista de respostas com `false.` quando não há mais soluções. No SWI-Prolog, a última resposta aparece seguida de ponto final.

## E1

- **Procedural:** especifica **os passos** (o como) para chegar à solução.
- **Declarativa:** especifica **o resultado desejado** (o quê), e um mecanismo de inferência encontra a solução.
- **Classificação do professor (p.5):** imperativo, OO e funcional são **procedurais**; o lógico é **declarativo**.

## E2

1. Expressar proposições.
2. Expressar os relacionamentos entre proposições.
3. Descrever como novas proposições podem ser inferidas a partir das assumidas como verdadeiras (p.6).

## E3

**Resposta: b.** Escrita na base, a proposição atômica é um **fato** (assumida verdadeira). A mesma proposição digitada no prompt (`?- pai(joao, ana).`) seria uma **consulta**.

## E4

| P | Q | ¬Q | P ∧ ¬Q | (P ∧ ¬Q) ⇒ P |
| --- | --- | --- | --- | --- |
| F | F | V | F | V |
| F | V | F | F | V |
| V | F | V | V | V |
| V | V | F | F | V |

**É uma tautologia** — verdadeira em todas as linhas. A implicação só seria falsa com antecedente V e consequente F. Quando o antecedente (P ∧ ¬Q) é V, P também é V, então esse caso nunca ocorre.

## E5

- **(a)** ∀X.(aluno(X) → estuda(X))
- **(b)** ∃X.(aluno(X) ∧ gosta(X, prolog))
- **(c)** ∀X.∀Y.(pai(X, Y) → homem(X))

**Erro comum:** em (b), usar "→" com "∃": ∃X.(aluno(X) → gosta(X, prolog)) seria verdadeiro bastando existir **alguém que não é aluno**, porque a implicação com antecedente falso é verdadeira. Com o existencial, usa-se ∧.

## E6

| Termo | Functor | Parâmetros |
| --- | --- | --- |
| a) `gosta(joao, X)` | `gosta` | `joao` (constante), `X` (variável) |
| b) `aula(plp, segunda, 19)` | `aula` | três constantes |
| c) `pai(P, renata)` | `pai` | `P` (variável), `renata` (constante) |

Em Prolog, variáveis começam com **maiúscula** e constantes (átomos), com **minúscula**.

## E7 — Atividade 1 (original, p.20)

<!-- teste: consulta="pai(carlos, X)." saida-contem="X = renata" -->
```prolog
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).
```

| Pergunta | Consulta | Resposta | Raciocínio |
| --- | --- | --- | --- |
| João é pai de Carlos? | `?- pai(joao, carlos).` | `true` | O fato existe |
| João é pai de Renata? | `?- pai(joao, renata).` | `false` | Não há esse fato; Renata é filha de Carlos (neta de João) |
| Quem é o pai de Ana? | `?- pai(X, ana).` | `X = joao` | Unifica com `pai(joao, ana)` |
| Quem é o filho de Carlos? | `?- pai(carlos, X).` | `X = renata` | Unifica com `pai(carlos, renata)` |

## E8 — Atividade 2 (original, p.23)

<!-- teste: consulta="mostra(ana, joao)." saida-contem="Pai de ana: joao|Filhos de joao: [ana,maria,carlos]" -->
```prolog
/* Fatos */
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).

:- initialization(main).

main :-
    write('Digite o primeiro nome (termine com ponto): '), read(Nome1),
    write('Digite o segundo nome (termine com ponto): '),  read(Nome2),
    mostra(Nome1, Nome2).

/* Separado do main para poder ser testado sem leitura do teclado */
mostra(Nome1, Nome2) :-
    (   pai(Pai, Nome1)                       % cada pessoa tem um único pai
    ->  write('Pai de '), write(Nome1), write(': '), write(Pai)
    ;   write(Nome1), write(' nao tem pai cadastrado')
    ), nl,
    findall(Filho, pai(Nome2, Filho), Filhos), % reúne TODOS os filhos
    write('Filhos de '), write(Nome2), write(': '), write(Filhos), nl.
```

**Exemplo de execução** (digitando `ana.` e `joao.`; em teste, consultou-se `mostra(ana, joao)` diretamente):

```text
Pai de ana: joao
Filhos de joao: [ana,maria,carlos]
```

**Raciocínio:**

1. `read/1` lê um termo, então o usuário digita `ana.` — com ponto e em minúscula, porque `Ana` seria lido como variável.
2. **Pai:** consulta `pai(Pai, Nome1)`, com a variável no 1º argumento. O `->` pega a **primeira** solução, o que basta porque cada pessoa tem um único pai. O ramo `;` trata quem não tem pai na base (por exemplo, `joao`).
3. **Filhos:** `findall` coleta **todas** as soluções de `pai(Nome2, Filho)`, com a variável no 2º argumento, numa lista. Para alguém sem filhos, devolve `[]`, sem falhar.
4. O mesmo fato `pai/2` responde às duas perguntas apenas mudando **qual argumento é variável** — a essência do declarativo.

**Erros comuns:**

- Digitar `Ana.` com maiúscula: vira variável e unifica com qualquer coisa.
- Usar `pai(Nome2, Filho)` sem `findall`: mostra só o primeiro filho.

## E9

**`?- pai(X, maria).`**

1. O Prolog percorre os fatos `pai/2` **na ordem** em que aparecem.
2. `pai(joao, ana)`: para unificar com `pai(X, maria)`, X = joao, mas `ana ≠ maria` → **falha**.
3. `pai(joao, maria)`: X = joao e `maria = maria` → **sucesso**. Responde `X = joao`.
4. Se o usuário pedir mais (`;`), ele **retrocede** (*backtracking*) e tenta `pai(joao, carlos)` e `pai(carlos, renata)`, que falham → `false`.

**`?- pai(joao, X).`** com todas as soluções: unifica com `pai(joao, ana)` → `X = ana`; `;` → `pai(joao, maria)` → `X = maria`; `;` → `pai(joao, carlos)` → `X = carlos`; `;` → `pai(carlos, renata)` falha (`carlos ≠ joao`) → fim.

<!-- teste: consulta="pai(joao, X)." saida-contem="X = ana\nX = maria\nX = carlos" -->
```prolog
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).
```

## E10

<!-- teste: consulta="avo(joao, N)." saida-contem="N = renata" -->
```prolog
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).

% A é avô de N se A é pai de alguém (P) que é pai de N.
avo(A, N) :- pai(A, P), pai(P, N).

% X e Y são irmãos se têm o mesmo pai e são pessoas diferentes.
irmao(X, Y) :- pai(P, X), pai(P, Y), X \== Y.
```

**Consultas:**

| Pergunta | Consulta | Resposta |
| --- | --- | --- |
| Quem é neto de João? | `?- avo(joao, N).` | `N = renata` |
| Quem são os irmãos de Ana? | `?- irmao(ana, Y).` | `Y = maria ; Y = carlos` |

<!-- teste: consulta="irmao(ana, Y)." saida-contem="Y = maria\nY = carlos" -->
```prolog
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).
irmao(X, Y) :- pai(P, X), pai(P, Y), X \== Y.
```

**Raciocínio:**

- Uma **regra** `Cabeça :- Corpo.` diz que "a cabeça é verdadeira **se** o corpo for". As vírgulas são **e**.
- Em `avo/2`, a variável `P` liga os dois fatos: o Prolog procura um `P` que seja filho de `A` e pai de `N`.
- Em `irmao/2`, `X \== Y` impede que alguém seja considerado irmão de si mesmo.
- **Aprofundamento:** regras com `:-` só aparecem no material na [Aula 02](../../Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md#prolog-p7). Elas são a forma de expressar a terceira necessidade da lógica formal: **inferir** proposições novas (`avo(joao, renata)`) a partir das existentes.

## E11

- **Mundo fechado:** o Prolog só considera verdadeiro o que consegue **provar** a partir da base. `homem(pedro)` não está na base nem pode ser deduzido, então a resposta é `false` — que significa "não provável com o que sei", e não "falso no mundo real".
- **Sem semântica intrínseca (p.15):** para o Prolog, `homem` e `pedro` são só símbolos. Ele não "sabe" o que é ser homem; só compara símbolos e unifica termos. O significado é dado pelo programador, que precisa manter consistência — por exemplo, sempre `pai(Pai, Filho)`, nunca às vezes `pai(Filho, Pai)`.
