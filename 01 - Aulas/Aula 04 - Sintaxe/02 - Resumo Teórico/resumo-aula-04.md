# Aula 04 — Sintaxe · Resumo teórico

> **Fonte:** [`Aula04_Sintaxe.pdf`](../01%20-%20Slides%20Originais/Aula04_Sintaxe.pdf) (21 páginas) — "Introdução à Sintaxe das Linguagens de Programação". Apoio indicado: Tucker & Noonan, seções 4.1 e 4.2; Sebesta (9ª ed.), seções 3.1, 3.2, 5.1 e 5.2 (p.21).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF.

---

## 1. Objetivos (p.2)

**[Material original]** Revisar sintaxe e semântica; diferenciar sintaxe léxica de sintaxe concreta; compreender para que serve a gramática de uma linguagem; definir para que servem os nomes.

## 2. Sintaxe × semântica (p.3–4)

**[Material original]** Retoma a definição de linguagem da Aula 02 e cita Sebesta: "A **sintaxe** de uma linguagem de programação é a forma de suas expressões, sentenças e unidades de programa. Sua **semântica** é o significado dessas expressões e unidades de programa."

A sintaxe é descrita por um conjunto de regras que deve ser entendido por quatro públicos: quem cria a linguagem, os avaliadores iniciais, os implementadores (quem escreve o compilador) e os usuários (programadores).

**[Explicação elaborada]** Exemplo em português: "O gato comeu o peixe" e "O peixe comeu o gato" têm a **mesma sintaxe** (sujeito–verbo–objeto) e **significados diferentes**. "Gato o peixe o comeu" viola a sintaxe. Em programação: `x = y / z;` é sintaticamente válido em C, mas, se `z` valer 0, o significado (divisão por zero) é um problema semântico.

## 3. Como especificar a sintaxe (p.5–6)

**[Material original]** "Linguagem natural ou formal?" Métodos **formais** são usados desde o **Algol**, nos anos 1960. Um código-fonte é "apenas uma grande cadeia de caracteres", e a sintaxe é definida por:

- expressões regulares;
- autômatos finitos;
- gramáticas livres de contexto.

**Gramática** é uma **metalinguagem** que define quais cadeias de caracteres formam um programa sintaticamente correto.

**[Complemento] — como isso se divide:** expressões regulares e autômatos finitos descrevem a **sintaxe léxica** (como reconhecer um número ou um identificador). Gramáticas livres de contexto descrevem a **sintaxe concreta** (estrutura aninhada de expressões e comandos). A notação usual para gramáticas é a **BNF** (Backus-Naur Form), criada justamente para o Algol 60, como a Aula 05 (p.3) menciona. Exemplo de gramática em BNF para expressões aritméticas:

```text
<expr>   ::= <expr> + <termo> | <expr> - <termo> | <termo>
<termo>  ::= <termo> * <fator> | <termo> / <fator> | <fator>
<fator>  ::= ( <expr> ) | <id> | <num>
```

Cada regra diz como um símbolo **não terminal** (entre `< >`) pode ser substituído. Os **terminais** (`+`, `(`, `id`) são os tokens produzidos pela análise léxica. A ordem das regras já codifica a **precedência**: `*` liga mais forte que `+` porque `<termo>` está "abaixo" de `<expr>`.

## 4. Os três níveis de sintaxe (p.7)

**[Material original]**

| Nível | Definição |
| --- | --- |
| **Léxica** | Regras para os símbolos básicos: identificadores, literais, operadores e pontuação. |
| **Concreta** | A representação real do programa, usando os símbolos léxicos como alfabeto. |
| **Abstrata** | Considera apenas as informações essenciais, sem detalhes como pontuação e parênteses. |

**[Explicação elaborada]** Para `a = (b + c) * 2;`:

- **Léxico:** `a` · `=` · `(` · `b` · `+` · `c` · `)` · `*` · `2` · `;` — dez tokens.
- **Concreto:** a sequência forma um comando de atribuição válido: identificador, `=`, expressão, `;`. Os parênteses são necessários para que a soma seja feita antes.
- **Abstrato:** a árvore abaixo. Os parênteses desaparecem porque a estrutura da árvore já expressa a ordem, e o `;` também desaparece.

```text
      =
     / \
    a   *
       / \
      +   2
     / \
    b   c
```

## 5. Lexema, token e padrão (p.8–9)

**[Material original]**

- **Lexema:** sequência de caracteres do programa-fonte.
- **Token:** classificação dos lexemas que se encaixam em determinado padrão.
- **Padrão:** descrição da forma que os lexemas podem assumir.

**Na linguagem C, os tokens se dividem em seis grupos (p.9):**

| Lexemas | Grupo do token |
| --- | --- |
| `n`, `soma1`, `main`, `strcpy` | identificador |
| `int`, `float`, `if`, `for`, `return` | palavra-chave ou reservada |
| `10`, `12.5`, `-5` | constante |
| `"Digite um número"` | string |
| `= & ( ) [ ] { } ;` | símbolos especiais |
| `+ - * / % ++ -- == > < !=` | operadores |

**[Explicação elaborada]** Analogia: o **padrão** é a regra ("começa com letra, seguida de letras ou dígitos"), o **token** é a categoria ("identificador") e o **lexema** é a ocorrência concreta (`soma1`).

> **[Atenção]** O slide lista `-5` como constante. Na análise léxica real de C, `-5` são **dois tokens**: o operador unário `-` e a constante `5`. O exemplo serve para ilustrar valores constantes; não leve ao pé da letra numa questão de análise léxica.

## 6. Sintaxe concreta (p.10)

**[Material original]** Determina como os tokens podem ser agrupados para formar estruturas (comandos) válidas. Exemplos:

| Código | Válido? | Por quê |
| --- | --- | --- |
| `soma = x + 10;` | Sim | Atribuição bem formada |
| `if (x > 10) {soma = 0;}` | Sim | Seleção bem formada |
| `x = (y + 10 * z;` | **Não** | Todos os tokens são válidos, mas o parêntese não fecha |

**[Explicação elaborada]** O terceiro exemplo é o mais importante: é **lexicamente correto e sintaticamente errado**. Quem detecta o erro é o analisador sintático, não o léxico.

## 7. Tamanho das gramáticas (p.11)

**[Material original]** Pascal ≈ 5 páginas; C ≈ 6; **C++ ≈ 22**; Java ≈ 14. A construção de gramáticas e seu uso na análise sintática ficam para Teoria da Computação (5ª fase) e Compiladores (6ª fase).

**[Explicação elaborada]** O tamanho da gramática é um indicador de **complexidade** da linguagem. C++ é quase quatro vezes maior que C — reflexo da restrição de "sistemas legados" (Aula 02): manteve tudo de C e acrescentou classes, templates, sobrecarga etc.

## 8. Nomes e identificadores (p.12–18)

**[Material original]** Nomes (identificadores) identificam variáveis, tipos definidos pelo usuário, funções etc. No exemplo da p.13:

```c
int quantidade;
int soma(int a, int b){
    return a + b;
}
```

Os identificadores são `quantidade`, `soma`, `a` e `b`; `int` e `return` são palavras reservadas.

**Perguntas que toda linguagem precisa responder (p.14):**

1. Quais são as regras de formação dos nomes?
2. Os nomes são sensíveis à capitalização (*case sensitive*)?
3. Os termos especiais são palavras **reservadas** ou **palavras-chave**?

| Conceito | Definição (p.14) |
| --- | --- |
| Palavra reservada | Tem significado especial e **não pode** ser usada como identificador. |
| Palavra-chave | Tem significado especial **apenas em contextos específicos** e pode ser identificador em outros (Fortran). |

**[Complemento]** Exemplo clássico em Fortran: `INTEGER REAL` declara uma variável chamada `REAL` do tipo inteiro, e `REAL INTEGER` declara uma variável `INTEGER` do tipo real. Isso é legal porque `REAL` e `INTEGER` são palavras-chave, não reservadas — e é péssimo para a legibilidade.

**Regras léxicas de formação (p.15–16):**

- Em geral, o nome começa com letra e segue com letras ou dígitos; algumas linguagens aceitam `_`.
- **PHP:** variáveis começam com `$` (`$nome = "IFSC"; echo $nome;`).
- **Perl:** o símbolo inicial indica o tipo — `$` escalar, `@` vetor, `%` hash:
  ```perl
  @cidades = ("Lages", "Florianópolis", "Correia Pinto");
  print "$cidades[0]\n";   # Lages
  ```
  > **[Complemento]** Repare que, para acessar **um elemento** do vetor `@cidades`, usa-se `$cidades[0]`, porque o elemento é um escalar.
- **Ruby:** `@` indica variável de instância; `@@`, variável de classe.

**Tamanho dos nomes (p.17):** as primeiras linguagens usavam só maiúsculas e limitavam o tamanho — **6 caracteres** no FORTRAN. FORTRAN 95: 31. C: nomes internos sem limite, mas só os **63** primeiros caracteres são significativos; nomes externos, até 31. Java, C# e Ada: sem limite.

**Case sensitivity (p.18):** Pascal e Ada **não** diferenciam maiúsculas de minúsculas; C, C++ e Java diferenciam. Prós e contras apresentados para debate:

| Argumento | Sinal (slide) |
| --- | --- |
| Força a padronização | (+) |
| Dificulta a escrita | (−) |
| Prejudica a legibilidade | (−) ??? |
| Permite associar nomes parecidos com capitalizações diferentes | (+ ou −) ??? |

**[Explicação elaborada]** As interrogações indicam pontos controversos. Em Java, a convenção `Pessoa` (classe) × `pessoa` (variável) usa a diferença a favor da legibilidade. Já `soma`, `Soma` e `SOMA` como três variáveis distintas prejudicam muito a leitura.

## 9. Variável (p.19)

**[Material original]** "Uma variável é uma **abstração** de uma ou mais **células de memória** identificada por um **nome**." A Aula 05 detalha os seis atributos da variável.

## 10. Exemplo 1 (p.20)

**[Material original]** Implementar em C, executar três vezes, anotar e comparar os resultados:

```c
#include <stdio.h>
int main(void) {
    int x = 2147483647;
    printf("%d \n", x);
    printf("%ld \n", &x);
    return 0;
}
```

**[Explicação elaborada]**

- `2147483647` = 2³¹ − 1, o **maior valor** de um `int` de 32 bits.
- O primeiro `printf` mostra o **valor** de `x` (sempre igual).
- O segundo mostra o **endereço** de `x` (`&x`), que normalmente **muda a cada execução**.
- A comparação revela que o nome `x` está ligado a dois atributos distintos — **endereço** e **valor** —, base da Aula 05 (l-value × r-value) e da Aula 08 (ponteiros).

> **[Complemento]** O endereço muda porque os sistemas operacionais modernos usam ASLR (*Address Space Layout Randomization*), que sorteia onde a pilha do programa é carregada. O especificador correto para imprimir um ponteiro é `%p`; usar `%ld` com `&x` é comportamento indefinido pelo padrão C (o compilador emite aviso), embora funcione na maioria dos sistemas de 64 bits.

## 11. Conexões e pontos para a prova

- Fase **léxica** e **sintática** do compilador ([Aula 03](../../Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md#3-compilação-p89)).
- A variável continua na [Aula 05](../../Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md).
- Cobrado na [Lista 02, Q3](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q3): sintaxe léxica, concreta e abstrata; lexema e token.
- Saber dar o exemplo `x = (y + 10 * z;` (lexicamente válido, sintaticamente inválido).
- Saber a diferença entre palavra reservada e palavra-chave.

---

**Anterior:** [Aula 03](../../Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) · **Próxima:** [Aula 05 — Semântica](../../Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)
