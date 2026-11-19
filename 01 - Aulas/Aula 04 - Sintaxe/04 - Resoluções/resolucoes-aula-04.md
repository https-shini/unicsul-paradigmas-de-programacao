# Aula 04 — Sintaxe · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-04.md`](../03%20-%20Exercícios/exercicios-aula-04.md). O código do E10 foi executado com Python 3.

## E1

Sintaxe é a **forma** das expressões, sentenças e unidades de programa; semântica é o **significado** delas (Sebesta, citado na p.4). Um programa pode estar sintaticamente correto e ainda ter significado errado — por exemplo, `dobro := n1 * n2` no exemplo Pascal da Aula 02.

## E2

- **Lexema:** sequência concreta de caracteres do fonte (`soma1`).
- **Token:** categoria a que o lexema pertence (identificador).
- **Padrão:** regra que descreve a forma dos lexemas daquela categoria ("letra seguida de letras/dígitos").

## E3

**Resposta: d.** Os métodos formais citados (p.6) são expressões regulares, autômatos finitos e gramáticas livres de contexto. Fluxogramas descrevem algoritmos, não a sintaxe de uma linguagem.

## E4

| Lexema | Token |
| --- | --- |
| `for` | palavra reservada |
| `(` `)` `;` `[` `]` | símbolos especiais |
| `i`, `printf`, `vet` | identificadores |
| `=` | símbolo especial (atribuição — o slide o lista em símbolos especiais) |
| `0`, `10` | constantes |
| `<`, `++` | operadores |
| `"%d"` | string |
| `,` | símbolo especial (separador; não aparece na lista do slide, mas pertence ao grupo) |

> **[Atenção]** O slide coloca `=` entre os símbolos especiais e `==` entre os operadores. Siga essa classificação nas questões da disciplina.

## E5

1. **Nenhum erro.**
2. **Erro sintático:** todos os tokens são válidos, mas o parêntese não fecha. É o mesmo caso do slide `x = (y + 10 * z;`.
3. **Erro léxico:** `@` não é um caractere válido de nenhum token de C, então o analisador léxico não consegue classificá-lo.
4. **Erro sintático:** em C, a condição do `if` precisa estar entre parênteses — `if (x > 0)`. Os tokens existem, mas a sequência não forma um `if` válido.

## E6

A **palavra reservada** nunca pode ser usada como identificador (`int`, `for` em C). A **palavra-chave** só é especial em certos contextos e pode virar identificador em outros (Fortran, p.14). Exemplo: em Fortran, `INTEGER REAL` declara uma variável chamada `REAL` do tipo inteiro. Quem lê precisa decidir pelo contexto se `REAL` é tipo ou variável, o que prejudica a legibilidade.

## E7

**a) Tokens (14):** `r` `=` `(` `a` `+` `b` `)` `*` `(` `c` `-` `d` `)` `;`

**b) Árvore sintática abstrata:**

```text
        =
       / \
      r   *
         / \
        +   -
       / \ / \
      a  b c  d
```

**c)** Na sintaxe **concreta**, os parênteses são necessários para forçar a soma e a subtração antes da multiplicação, já que, sem eles, `a + b * c - d` teria outro significado. Na sintaxe **abstrata**, a ordem de avaliação já está codificada na **estrutura da árvore**: os nós `+` e `-` estão abaixo do `*`. Os parênteses se tornam redundantes, e por isso a sintaxe abstrata "não se preocupa com pontuação e parênteses" (p.7).

## E8

- **1ª linha:** `2147483647`, sempre igual — é o **valor** (r-value) de `x`, o maior `int` de 32 bits.
- **2ª linha:** um número grande (o **endereço** de `x`, l-value), que **muda** a cada execução.
- **Por que muda:** o sistema operacional sorteia a posição da pilha a cada execução (ASLR, **[Complemento]**). A variável `x` é uma abstração de células de memória (p.19): o nome é fixo, mas as células podem ser outras.
- **Observação técnica:** o formato correto para endereços é `%p` (ver a [Aula 08](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)).

## E9

Em Perl, o símbolo inicial (*sigil*) indica o **tipo do valor obtido**, não o tipo da variável declarada. Um elemento de um vetor é um **escalar**, então usa `$`: `$cidades[0]`. Já `@cidades` denota o vetor inteiro. Isso mostra que, em Perl, o nome carrega informação de tipo — uma regra léxica que ajuda o leitor, mas exige aprender a convenção.

## E10

<!-- teste: entrada="soma = x + 10;" saida-contem="soma -> identificador|= -> simbolo especial|10 -> constante|; -> simbolo especial|+ -> operador" -->
```python
import re

RESERVADAS = {"int", "float", "char", "double", "if", "else", "for", "while", "return", "void"}

# Ordem importa: padrões mais longos primeiro (== antes de =, ++ antes de +).
PADROES = [
    ("string",            r'"[^"]*"'),
    ("constante",         r'\d+\.\d+|\d+'),
    ("nome",              r'[A-Za-z_]\w*'),
    ("operador",          r'\+\+|--|==|!=|<=|>=|[+\-*/%<>]'),
    ("simbolo especial",  r'[=&()\[\]{};,]'),
    ("espaco",            r'\s+'),
]
REGEX = re.compile("|".join(f"(?P<g{i}>{p})" for i, (_, p) in enumerate(PADROES)))

def analisar(linha):
    pos = 0
    while pos < len(linha):
        m = REGEX.match(linha, pos)
        if not m:
            raise SyntaxError(f"erro lexico: caractere invalido {linha[pos]!r} na posicao {pos}")
        grupo = PADROES[int(m.lastgroup[1:])][0]
        lexema = m.group()
        if grupo == "nome":
            grupo = "palavra reservada" if lexema in RESERVADAS else "identificador"
        if grupo != "espaco":
            print(f"{lexema} -> {grupo}")
        pos = m.end()

analisar(input())
```

**Como funciona:**

- Cada grupo de token vira um **padrão** (expressão regular).
- O laço tenta casar um padrão na posição atual: o trecho casado é o **lexema** e o nome do padrão é o **token**.
- Identificadores e palavras reservadas têm o **mesmo padrão**; a distinção é feita consultando a tabela `RESERVADAS` — é assim que analisadores reais fazem.
- Um caractere que não casa com nada (como `@`) gera **erro léxico**, que é o caso 3 do E5.

Saída para `soma = x + 10;`:

```text
soma -> identificador
= -> simbolo especial
x -> identificador
+ -> operador
10 -> constante
; -> simbolo especial
```

## E11

```text
<atrib> ::= <id> = <expr> ;
<expr>  ::= <expr> + <termo> | <termo>
<termo> ::= <termo> * <fator> | <fator>
<fator> ::= ( <expr> ) | <id> | <num>
```

**Por que `*` tem precedência:** para chegar a um `+`, a derivação passa por `<expr>`; os `*` são gerados mais abaixo, em `<termo>`. Assim, em `a + b * c`, o `b * c` vira uma subárvore de `<termo>` que é filha do `+`, e portanto é avaliada antes. A recursão à esquerda (`<expr> ::= <expr> + ...`) dá associatividade à esquerda: `a + b + c` = `(a + b) + c`.
