# Aula 15 — Paradigma Lógico · Resumo teórico

> **Fonte:** [`Aula15_Paradigma Lógico.pdf`](../01%20-%20Slides%20Originais/Aula15_Paradigma%20Lógico.pdf) (25 páginas). Título interno: "Aula 16 – Paradigma Lógico". Apoio indicado: Sebesta (9ª ed.), seções 16.6 a 16.6.5; Tucker & Noonan, cap. 15 (p.24).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF.
> **Validação:** os programas Prolog foram executados com o **Tau-Prolog** (implementação em JavaScript), em lugar do SWI-Prolog usado em aula. O comportamento de fatos, consultas, `findall` e `( -> ; )` é o mesmo. A saída do Tau-Prolog termina com `false.` quando não há mais soluções.

---

## 1. Objetivos (p.2)

**[Material original]** Diferenciar programação procedural e declarativa; revisar conceitos básicos e a representação de sentenças lógicas usando lógica proposicional e cálculo de predicados; representar proposições atômicas em Prolog.

> **[Atenção]** A p.25 é uma cópia solta deste slide de objetivos, colocada depois da bibliografia.

## 2. Procedural × declarativa (p.3–5)

**[Material original]**

- Os quatro paradigmas são: Imperativo, Orientado a Objetos, Funcional e Lógico. A principal semelhança entre os três primeiros é que **"todos especificam os passos que levam à solução"**.
- **Abordagens de programação:** procedural e declarativa.
- Na abordagem **declarativa**, especificam-se **os resultados desejados (o que deve ser feito)**, e não os procedimentos para produzi-los (como deve ser feito).

**Classificação do professor (p.5):**

| Paradigma | Abordagem |
| --- | --- |
| Imperativo | Procedural |
| Orientado a objetos | Procedural |
| Funcional | Procedural |
| **Lógico** | **Declarativo** |

Outras linguagens declarativas conhecidas: **HTML, CSS e SQL** — "nenhuma delas é linguagem de programação".

> **[Atenção] — classificação divergente na literatura.** Muitos autores classificam o paradigma **funcional** como **declarativo**, ao lado do lógico, porque um programa funcional descreve **o que** calcular (uma composição de funções) sem especificar a ordem de mudanças de estado. Para a disciplina, vale a classificação do slide: **funcional = procedural**. Numa questão discursiva, siga o slide e, se houver espaço, mencione a divergência.

**[Explicação elaborada] — o mesmo problema nas duas abordagens:** "quem são os filhos de João?"

| Procedural (imperativo, pseudocódigo) | Declarativo (Prolog) |
| --- | --- |
| `para cada registro r em pais: se r.pai == "joao": imprima r.filho` | `?- pai(joao, X).` |
| O programador diz **como** percorrer e filtrar | O programador diz **o que** quer; o motor de inferência acha as respostas |

**[Complemento]** O SQL ilustra bem a ideia: `SELECT filho FROM pais WHERE pai = 'joao'` declara o resultado, e o banco de dados decide como buscá-lo.

## 3. Fundamentos: lógica simbólica (p.6–7)

**[Material original]**

- Os programas lógicos são expressos na forma de **lógica simbólica**, e os resultados são produzidos por um **processo de inferência lógica**.
- A lógica simbólica atende às **três necessidades da lógica formal**:
  1. **expressar proposições**;
  2. **expressar os relacionamentos** entre as proposições;
  3. **descrever como novas proposições podem ser inferidas** a partir de outras assumidas como verdadeiras.
- A lógica simbólica se divide em **lógica proposicional** e **lógica (cálculo) de predicados de primeira ordem**.
- O **cálculo de predicados de primeira ordem é a base** da programação lógica.

## 4. Lógica proposicional (p.8–10)

**[Material original]**

- **Proposição:** declaração afirmativa que é sabidamente **verdadeira ou falsa**.
- **Constantes:** símbolos que representam as proposições.
- **Conectivos lógicos:** operadores que combinam proposições e permitem calcular o resultado do sistema formal.

**Operadores (p.9):**

| Operador | Símbolo | Leitura |
| --- | --- | --- |
| Negação | ¬a | não a |
| Conjunção | a ∧ b | a e b |
| Disjunção | a ∨ b | a ou b |
| Equivalência | a ↔ b | a é equivalente a b |
| Implicação | a → b | a implica b |

**Tabela-verdade (p.10):**

| P | Q | ¬P | P∧Q | P∨Q | P⇒Q | P⇔Q |
| --- | --- | --- | --- | --- | --- | --- |
| F | F | V | F | F | V | V |
| F | V | V | F | V | V* | F |
| V | F | F | F | V | F | F |
| V | V | F | V | V | V | V |

**[Explicação elaborada]**

- A **implicação** P ⇒ Q só é **falsa** quando P é verdadeira e Q é falsa. O asterisco do slide marca um caso contraintuitivo (F ⇒ V = V): de uma premissa falsa, qualquer conclusão é "verdadeira" — **verdade por vacuidade**. Exemplo: "se chover, levo guarda-chuva" não é desmentido num dia sem chuva, leve eu guarda-chuva ou não.
- A **equivalência** P ⇔ Q é verdadeira quando P e Q têm o **mesmo** valor.
- Os símbolos variam entre slides (`^ v ↔ →` na p.9; `∧ ∨ ⇔ ⇒` na p.10), mas significam o mesmo.

## 5. Lógica de predicados de primeira ordem (p.11–12)

**[Material original]** Acrescenta à proposicional:

- **Predicados:** termos que expressam a **relação entre entidades**, sejam constantes ou variáveis.
- **Variáveis:** permitem construir **regras que enunciam princípios gerais** — uma variável pode ser substituída por diferentes constantes.
- **Quantificadores:** símbolos associados às variáveis que indicam **quantas constantes** podem ser associadas a elas.

Variáveis só aparecem nas proposições **precedidas por quantificadores** (p.12):

| Quantificador | Notação | Leitura | Exemplo do slide |
| --- | --- | --- | --- |
| Universal | ∀X.P | "Para todo X, P é verdadeiro" | ∀X.(mulher(X) → humano(X)) — toda mulher é humana |
| Existencial | ∃X.P | "Existe um valor de X tal que P é verdadeiro" | ∃X.(mae(mary,X) ∧ homem(X)) — Mary é mãe de algum homem |

**[Explicação elaborada]** A lógica proposicional só consegue dizer "João é homem" como uma proposição indivisível (p). Com predicados, escreve-se `homem(joao)` e se generaliza com variáveis: ∀X.(homem(X) → mortal(X)). É essa capacidade de falar sobre **relações** e **todos/algum** que permite programar.

## 6. Prolog (p.13)

**[Material original]**

- O cálculo de predicados de primeira ordem constitui a base da programação lógica.
- **Prolog** é a principal linguagem que implementa o paradigma lógico.
- Desenvolvimento iniciado na **década de 1970**, nas universidades de **Edimburgo** e **Aix-Marseille**.
- Nos anos 1980, o interesse cresceu com o anúncio, pelo governo japonês, dos **computadores de quinta geração**. Com o "abandono silencioso" desse projeto, o interesse por Prolog também diminuiu.

## 7. Proposições, termos, fatos e consultas (p.14–18)

**[Material original]**

- Os programas são constituídos de sentenças, que na programação lógica se chamam **proposições**.
- No cálculo de predicados, as proposições podem ser:
  - **atômicas**, quando possuem **apenas um termo composto**;
  - **compostas**, quando possuem **vários termos compostos**.
- Um **termo composto** é formado por:
  - um termo simples constante, o **functor** ou **termo de predicado**, que representa uma relação matemática;
  - outros termos simples, constantes ou variáveis, que formam a **lista de parâmetros** do termo de predicado.
  - Exemplos: `homem(joao)`, `gosta(joao,maria)`, `gosta(joao, X)`.
- **"Não há uma semântica intrínseca nos termos."**

**[Explicação elaborada]** Em `gosta(joao, maria)`, o functor é `gosta`, e os parâmetros são `joao` e `maria`. "Não há semântica intrínseca" significa que o Prolog **não sabe** o que "gosta" quer dizer, nem se `gosta(joao, maria)` significa "João gosta de Maria" ou o contrário. O **programador** define o significado e deve usá-lo de forma consistente. Convenções de Prolog: **constantes** (átomos) começam com **minúscula** (`joao`); **variáveis**, com **maiúscula** (`X`, `Pai`).

**Fatos e consultas (p.16–17)** — as proposições atômicas servem a dois papéis:

| Papel | Definição | Exemplos |
| --- | --- | --- |
| **Fato** | Proposição **assumida como verdadeira** | `homem(joao).` — João é homem; `pai(joao, maria).` — João é pai de Maria |
| **Consulta** (objetivo) | Proposição cuja **verdade deve ser verificada** | `homem(joao).` → true/false; `pai(joao, maria).` → true/false; `pai(X, maria).` → **por unificação**, encontra X que torna a proposição verdadeira |

> **[Atenção]** Nos slides (p.16–17), alguns fatos aparecem com espaço entre o nome e o parêntese, como `pai (joao, maria).`. Em Prolog isso é **erro de sintaxe**: o functor deve vir colado ao `(`. Escreva `pai(joao, maria).`

**Interação (p.18):** depois de definir fatos e regras, pode-se interagir com o programa **digitando consultas no prompt** do interpretador ou **criando um programa** que faz consultas pré-determinadas.

**[Explicação elaborada] — unificação:** é o processo de tornar dois termos **iguais** atribuindo valores às variáveis. Para responder `pai(X, maria)`, o Prolog percorre os fatos **na ordem** e tenta casar `pai(X, maria)` com cada um. `pai(joao, maria)` casa se **X = joao**, então essa é a resposta. Se o usuário pedir mais soluções (`;`), o Prolog **volta** e continua procurando — é o *backtracking*. **[Complemento]** O mecanismo completo de execução de Prolog combina unificação, **resolução** (a regra de inferência) e **backtracking** (busca em profundidade com retrocesso). O material cita só a unificação.

**Mundo fechado [Complemento]:** se não consegue **provar** uma consulta a partir dos fatos, o Prolog responde `false`. `homem(pedro)` é `false` não porque Pedro "não é homem", mas porque isso **não está na base**.

## 8. Exemplos e atividades (p.19–23)

### Exemplo 1 — consultas no SWI-Prolog online (p.19)

**[Material original]** Usando <https://swish.swi-prolog.org/>, especificar os fatos e fazer as consultas.

<!-- teste: consulta="homem(X)." saida-contem="X = joao|X = jose" -->
```prolog
homem(joao).
homem(jose).
mulher(maria).
gosta(joao,maria).
```

| Consulta | Resposta | Por quê |
| --- | --- | --- |
| `homem(joao).` | `true` | O fato existe |
| `homem(pedro).` | `false` | Nada na base permite provar |
| `homem(X).` | `X = joao ; X = jose` | Unifica com cada fato `homem/1`, na ordem |
| `mulher(X).` | `X = maria` | |
| `gosta(joao,X).` | `X = maria` | |
| `gosta(jose,X).` | `false` | Nenhum fato `gosta(jose, _)` |

### Atividade 1 (p.20)

**[Material original]** Com os fatos `pai(joao,ana). pai(joao,maria). pai(joao,carlos). pai(carlos,renata).`, criar consultas para: João é pai de Carlos? João é pai de Renata? Quem é o pai de Ana? Quem é o filho de Carlos?

<!-- teste: consulta="pai(X, ana)." saida-contem="X = joao" -->
```prolog
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).
```

| Pergunta | Consulta | Resposta |
| --- | --- | --- |
| João é pai de Carlos? | `pai(joao, carlos).` | `true` |
| João é pai de Renata? | `pai(joao, renata).` | `false` — Renata é filha de Carlos, ou seja, **neta** de João |
| Quem é o pai de Ana? | `pai(X, ana).` | `X = joao` |
| Quem é o filho de Carlos? | `pai(carlos, X).` | `X = renata` |

**[Explicação elaborada]** O **mesmo fato** `pai/2` responde perguntas em **direções diferentes** — "quem é o pai de…" (variável no 1º argumento) e "quem é filho de…" (variável no 2º). Num programa imperativo, seriam duas funções de busca. Isso mostra o poder do declarativo.

### Exemplo 2 — programa no OneCompiler (p.21)

**[Material original]**

<!-- teste: consulta="main." saida-contem="Joao eh homem? Sim|Pedro eh homem? Nao|Quem eh homem? [joao,jose]|Quem eh mulher? [maria]|Joao gosta de quem? [maria]|Jose gosta de quem? []" -->
```prolog
/*Fatos*/
homem(joao).
homem(jose).
mulher(maria).
gosta(joao,maria).

/* Inicialização do programa*/
:- initialization(main).

main :-
    /*Consultas*/
    write('Joao eh homem? '),
    (homem(joao) -> write('Sim') ; write('Nao')), nl,
    write('Pedro eh homem? '),
    (homem(pedro) -> write('Sim') ; write('Nao')), nl,
    findall(X, homem(X), ListaHomens),
    write('Quem eh homem? '), write(ListaHomens), nl,
    findall(X, mulher(X), ListaMulheres),
    write('Quem eh mulher? '), write(ListaMulheres), nl,
    findall(X, gosta(joao,X), ListaGostaJoao),
    write('Joao gosta de quem? '), write(ListaGostaJoao), nl,
    findall(X, gosta(jose,X), ListaGostaJose),
    write('Jose gosta de quem? '), write(ListaGostaJose), nl.
```

**Saída:**

```text
Joao eh homem? Sim
Pedro eh homem? Nao
Quem eh homem? [joao,jose]
Quem eh mulher? [maria]
Joao gosta de quem? [maria]
Jose gosta de quem? []
```

**[Explicação elaborada]**

| Construção | Significado |
| --- | --- |
| `:- initialization(main).` | Diretiva: ao carregar o programa, executar `main` |
| `main :- ... .` | **Regra**: "`main` é verdadeiro se todos os objetivos do corpo forem satisfeitos" |
| `,` | Conjunção ("e"): objetivos em sequência |
| `( C -> A ; B )` | Se C pode ser provado (tem solução), executa A; senão, B |
| `findall(X, Objetivo, Lista)` | Reúne **todas** as soluções de X numa lista — `[]` se não houver nenhuma |
| `write/1`, `nl/0` | Escreve um termo; pula linha |

### Exemplo 3 — lendo do teclado (p.22)

**[Material original]** "É possível utilizar o comando `read` para ler um valor do teclado a ser utilizado nas consultas. Além disso, é possível salvar o resultado das consultas em uma variável para uso posterior."

```prolog
/*Fatos*/
homem(joao).
homem(jose).
mulher(maria).
gosta(joao,maria).

/* Inicialização do programa*/
:- initialization(main).

main :-
    /*Consultas*/
    write('Digite um nome para verificar se eh um homem: '),
    read(Nome), nl,
    (homem(Nome) -> Resultado = 'Sim' ; Resultado = 'Nao'),
    write(Nome), write(' eh um homem? '), write(Resultado), nl.
```

**[Explicação elaborada]**

- `read(Nome)` lê um **termo** Prolog, então o usuário deve digitar o nome **seguido de ponto**: `joao.`.
- `Resultado = 'Sim'` é **unificação**, não atribuição: a variável `Resultado`, ainda livre, passa a valer `'Sim'`. Uma variável Prolog, uma vez ligada, **não muda** dentro da mesma tentativa de prova.

### Atividade 2 (p.23)

**[Material original]** No OneCompiler, especificar os fatos `pai/2` e criar um programa que leia dois nomes: para o primeiro, mostrar o **pai** (cada pessoa tem um único pai); para o segundo, mostrar os **filhos**. Solução testada em [resolucoes-aula-15.md](../04%20-%20Resoluções/resolucoes-aula-15.md#e8--atividade-2-original-p23).

## 9. Lógico × imperativo — quadro-resumo

**[Explicação elaborada]**

| Aspecto | Imperativo | Lógico |
| --- | --- | --- |
| Abordagem | Procedural: **como** | Declarativa: **o que** |
| Programa | Sequência de comandos | Base de fatos (e regras) + consultas |
| Execução | Ordem textual dos comandos, alterando a memória | **Inferência**: o motor tenta provar a consulta por unificação (e *backtracking*) |
| Variável | Célula de memória mutável | Incógnita a ser descoberta por unificação; não muda depois de ligada |
| Resultado | O que o programa imprime ou grava | As **instanciações** que tornam a consulta verdadeira |
| Base teórica | Arquitetura de von Neumann | Cálculo de predicados de 1ª ordem |

## 10. Conexões e pontos para a prova

- O primeiro contato com Prolog foi na [Aula 02](../../Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md#prolog-p7) (regra `verifica_dobro`, com `:-`, `is` e `=:=`).
- O funcional ([Aula 14](../../Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)) é o outro paradigma que não segue von Neumann.
- **A Lista 01 cobra esta aula diretamente** ([Q1, Q8–Q11](../../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/02%20-%20Resolução/resolucao-lista-01.md#q8)); a [Lista 02, Q12](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q12) compara funcional e lógico.
- **Decorar:** procedural × declarativa e a classificação dos 4 paradigmas; as 3 necessidades da lógica formal; proposicional × 1ª ordem (predicados, variáveis, quantificadores ∀/∃); a estrutura do termo composto; fato × consulta; escrever consultas sobre `pai/2`.

---

**Anterior:** [Aula 14](../../Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) · **Revisão:** [Lista 01](../../../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/README.md) · [Lista 02](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md)
