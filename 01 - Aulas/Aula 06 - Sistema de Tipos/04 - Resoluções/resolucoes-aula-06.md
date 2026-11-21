<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 06](../README.md) › [04 - Resoluções](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 06 — Sistema de Tipos · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-06.md`](../03%20-%20Exercícios/exercicios-aula-06.md). Os programas foram compilados e executados (gcc, javac, php, python3); os erros de compilação e de execução descritos foram reproduzidos.

## E1

- **Tipo de dado:** conjunto de valores + conjunto de operações pré-definidas sobre eles ([p.3](../01%20-%20Slides%20Originais/README.md#página-3)).
- **Sistema de tipos:** definição precisa das associações entre o tipo de uma variável, seus valores e as operações possíveis ([p.4](../01%20-%20Slides%20Originais/README.md#página-4)).
- **Erro de tipo:** erro causado por uma operação tentada sobre um tipo para o qual ela não está definida ([p.4](../01%20-%20Slides%20Originais/README.md#página-4)).

## E2

- **Primitivos:** existem na máquina e não derivam de outros — `int`, `double`, `char`, `boolean`.
- **Compostos:** construídos a partir de outros — vetores/matrizes, registros (`struct`), enumerações, strings (em C), classes/objetos.

## E3

**Resposta: d.** Em Java, o tamanho é especificado pela linguagem ([p.7](../01%20-%20Slides%20Originais/README.md#página-7)). Em C, C++ e Pascal, a linguagem define só o mínimo.

## E4

| Linguagem | Tipagem |
| --- | --- |
| Ada | Estática |
| PHP | Dinâmica |
| C++ | Estática |
| JavaScript | Dinâmica |
| Java | Estática |
| Perl | Dinâmica |

## E5

| Quesito | Estática | Dinâmica | Por quê |
| --- | --- | --- | --- |
| Velocidade | Maior | Menor | Com tipos conhecidos em compilação, o código gerado executa a operação direto; na dinâmica, cada operação verifica tipos em execução |
| Verificação de erros | Compilação | Execução | Na estática, o compilador recusa operações inválidas; na dinâmica, o erro só aparece quando aquela linha roda |
| Simplicidade de escrita | Menor | Maior | A dinâmica dispensa declarações |
| Leitura e depuração | Maior | Menor | As declarações documentam o código e muitos erros são pegos cedo |

## E6

1. **Conversão implícita (coerção):** a linguagem converte tipos sem o programador pedir. Operações que deveriam ser erros de tipo passam despercebidas e podem perder informação (`int res = 2.5 + 3` → 5 em C).
2. **Exposição de ponteiros como valores numéricos:** se um endereço pode ser tratado como número (somado, convertido para `int`, reinterpretado), o programa consegue ler uma região de memória como se fosse de outro tipo, burlando o sistema de tipos.

## E7

| Item | Resultado | Explicação |
| --- | --- | --- |
| a) C | `2` | Conversão **implícita** de `double` para `int`, truncando |
| b) Java | **Não compila** | "possible lossy conversion from double to int" |
| c) Java | `2` | Conversão **explícita** (*cast*), aceita |
| d) C | `3 3.500000` | `/` sobrecarregado: inteiro com inteiro dá divisão inteira; real com inteiro dá divisão real |

## E8

**Incorreta.** "Dinâmica" diz **quando** o tipo é definido (em execução); "fraca" diz **quão tolerante** a linguagem é com tipos misturados. São eixos independentes ([p.15](../01%20-%20Slides%20Originais/README.md#página-15)).

Python é dinâmica, mas recusa `10 + "20"` com `TypeError` — portanto é **forte**:

<!-- teste: saida-contem="TypeError" -->
```python
try:
    print(10 + "20")
except TypeError as e:
    print("TypeError:", e)   # unsupported operand type(s) for +: 'int' and 'str'
```

| | Forte | Fraca |
| --- | --- | --- |
| **Estática** | Java, Ada | C, C++ |
| **Dinâmica** | Python | PHP, JavaScript |

## E9 — Atividade da p.20

### PHP (original da p.19)

Resultado: `x eh integer`, `y eh string`, `w eh double`, `Resultado(x+y+w): 40.2` — o PHP converte `"20"` sozinho.

### C — tentativa literal

<!-- teste: compilacao-falha="sim" erro-contem="invalid operands" -->
```c
#include <stdio.h>

int main(void) {
    int x = 10;
    char *y = "20";          /* em C, "20" é um vetor de char (ponteiro) */
    double w = 10.2;
    double z = x + y + w;    /* x + y vira aritmética de PONTEIRO; ponteiro + double = erro */
    printf("%f\n", z);
    return 0;
}
```

O gcc recusa: `invalid operands to binary +`. Note o detalhe: `x + y` é **aceito** e produz um ponteiro deslocado 10 posições. É a "exposição de ponteiros como valores numéricos" ([p.21](../01%20-%20Slides%20Originais/README.md#página-21)), um traço de tipagem fraca. O erro só aparece ao somar o ponteiro com `double`.

### C — versão que funciona (conversão explícita)

<!-- teste: saida-contem="x eh int|y eh char* (string)|w eh double|Resultado(x+y+w): 40.2" -->
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 10;
    char *y = "20";
    double w = 10.2;
    printf("x eh int\ny eh char* (string)\nw eh double\n");  /* C não tem gettype: o tipo é fixo e conhecido */
    double z = x + atoi(y) + w;          /* conversão string -> int feita pelo programador */
    printf("Resultado(x+y+w): %.1f\n", z);
    return 0;
}
```

### Python

<!-- teste: saida-contem="x eh <class 'int'>|y eh <class 'str'>|w eh <class 'float'>|TypeError" -->
```python
x = 10
y = "20"
w = 10.2
print("x eh", type(x))
print("y eh", type(y))
print("w eh", type(w))
try:
    z = x + y + w
    print("Resultado(x+y+w):", z)
except TypeError as erro:
    print("TypeError:", erro)              # Python recusa int + str
print("Resultado com conversao:", x + int(y) + w)   # 40.2
```

### Comparação

| Linguagem | Comportamento | Força |
| --- | --- | --- |
| PHP | Converte implicitamente e calcula 40.2 | **Mais fraca** |
| C | Aceita `int + char*` (ponteiro), recusa `ponteiro + double`; exige `atoi` | Intermediária: estática, mas com coerções e ponteiros expostos |
| Python | `TypeError` em execução; exige `int(y)` | **Mais forte** |

## E10

O processador só soma valores de **mesma representação** em registradores: inteiro em complemento de dois e real em IEEE 754 têm bits diferentes, e somá-los "crus" daria lixo. O compilador, na verificação de tipos, percebe a mistura `int + float` e **insere uma conversão**: no código intermediário, `t1 = float(a); c = t1 + b;`; no assembly, a instrução `cvtdq2ps` converte o inteiro antes do `add` ([p.23–24](../01%20-%20Slides%20Originais/README.md#página-23)). A conversão existe, mas é **implícita** para o programador.

## E11

- **A favor (slide, [p.17](../01%20-%20Slides%20Originais/README.md#página-17)):** Perl detecta e trata erros de tipo em execução e diferencia escalares, vetores e hashes pelos *sigils* (`$`, `@`, `%`).
- **Contra (critério da [p.21](../01%20-%20Slides%20Originais/README.md#página-21)):** Perl faz **conversão implícita** entre string e número, exatamente como o PHP:

<!-- teste: saida-contem="30" -->
```perl
my $x = 10;
my $y = "20";
print $x + $y, "\n";   # 30: a string "20" vira número sem pedido do programador
```

Pelo critério da conversão implícita, Perl seria **fracamente** tipada. A divergência ilustra o aviso da [p.21](../01%20-%20Slides%20Originais/README.md#página-21): não há consenso entre autores.

## E12

<!-- teste: saida-contem="sizeof(int) = 4|sizeof(long) =" -->
```c
#include <stdio.h>

int main(void) {
    printf("sizeof(char) = %zu\n", sizeof(char));
    printf("sizeof(int) = %zu\n", sizeof(int));
    printf("sizeof(long) = %zu\n", sizeof(long));
    printf("sizeof(long long) = %zu\n", sizeof(long long));
    return 0;
}
```

No Linux 64 bits com gcc, imprime `sizeof(long) = 8`; com o compilador da Microsoft no Windows 64 bits, imprime **4**. O padrão C só garante mínimos (`long` com pelo menos 32 bits) e a relação `sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)`. Cada compilador escolhe o tamanho real para sua plataforma — exatamente o que diz a [p.7](../01%20-%20Slides%20Originais/README.md#página-7). Em Java, `long` tem 8 bytes em qualquer plataforma.


<!-- nav:rodape -->

---

**Aula 06:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-06.md) · [Exercícios](../03%20-%20Exercícios/exercicios-aula-06.md) · **Resoluções** · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 05 · Resoluções](../../Aula%2005%20-%20Semântica/04%20-%20Resoluções/resolucoes-aula-05.md) · [Aula 07 · Resoluções](../../Aula%2007%20-%20Tipos%20Compostos/04%20-%20Resoluções/resolucoes-aula-07.md) →

**Links para esta página (5):** [Aula 06 · Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-06.md) · [Aula 06 · Exercícios](../03%20-%20Exercícios/exercicios-aula-06.md) · [Aula 06 · visão geral](../README.md) · [03 — Trabalhos e Projetos](../../../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
