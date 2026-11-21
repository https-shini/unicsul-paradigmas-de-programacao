<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 06](../README.md) › [02 - Resumo Teórico](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 06 — Sistema de Tipos · Resumo teórico

> **Fonte:** [`Aula06_Tipos.pdf`](../01%20-%20Slides%20Originais/Aula06_Tipos.pdf) (26 páginas). Apoio indicado: Tucker & Noonan, seções 5.1 e 5.2; Sebesta (9ª ed.), cap. 5 ([p.26](../01%20-%20Slides%20Originais/README.md#página-26)).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF. Os códigos marcados como testados foram executados (gcc, javac, php, python3).

---

## 1. Objetivos (p.2)

**[Material original]** Conceituar tipo e sistema de tipos; diferenciar tipagem **estática** de **dinâmica**; diferenciar tipagem **forte** de **fraca**.

## 2. Conceitos fundamentais (p.3–4)

**[Material original]**

- **Tipo de dado:** conjunto de **valores** + conjunto de **operações** pré-definidas que podem ser realizadas sobre eles.
  - **Primitivos (básicos):** correspondem aos tipos disponíveis nas máquinas atuais e **não são definidos a partir de outros**.
  - **Compostos:** construídos a partir de primitivos ou de outros compostos (ver [Aula 07](../../Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)).
- **Sistema de tipos:** definição precisa das associações entre o **tipo de uma variável**, seus **valores** e as **operações possíveis** sobre eles.
- **Erro de tipo:** qualquer erro que surja porque uma operação é tentada sobre um tipo para o qual ela **não está definida**.

**[Explicação elaborada]** O tipo `int` é o conjunto {…, −1, 0, 1, …} (limitado pelos bits) mais as operações `+ − * / %`. Aplicar `%` a dois `double` em C é erro de tipo, porque `%` não está definido para reais nessa linguagem.

## 3. Evolução histórica (p.5)

**[Material original]**

1. **Primeiras versões do Fortran:** poucos tipos para representar todas as informações.
2. **COBOL:** permitiu definir a **precisão de decimais** e criou os **registros**.
3. **PL/I:** aumentou a flexibilidade do COBOL, com muitos tipos novos.
4. **ALGOL 68:** oferece alguns tipos básicos e **operadores para definir novos tipos** — novas estruturas, um prelúdio da POO.

## 4. Tipos básicos e seus tamanhos (p.6–8)

**[Material original]** Tamanhos em bytes:

| Categoria | C/C++ | Java |
| --- | --- | --- |
| Inteiro | byte (1), short (2), int (4), long (8) | byte (1), short (2), int (4), long (8) |
| Real | float (4), double (8) | float (4), double (8) |
| Caractere | char (**1**) | char (**2**) |
| Booleano | bool (1, C++) | boolean (1) |

- Cada linguagem é livre para escolher nomes e tamanhos, mas em geral suportam os mesmos tipos básicos com tamanhos parecidos.
- **Em Java, o tamanho é especificado pela linguagem.**
- **Em C/C++ e Pascal, a linguagem define o tamanho mínimo**, e o desenvolvedor do compilador escolhe o tamanho real.

> **[Atenção] / [Complemento]**
> - C/C++ não têm um tipo chamado `byte`; o equivalente é `char`/`signed char`/`unsigned char`.
> - Em C, `long` tem 8 bytes no Linux 64 bits e **4** no Windows 64 bits — exatamente o efeito de "tamanho definido pelo compilador".
> - O `char` de Java ocupa 2 bytes porque representa uma unidade UTF-16 (Unicode).
> - O tamanho de `boolean` em Java não é fixado pela especificação da linguagem; o "1" do slide é a representação usual.

**Estouro — overflow ([p.8](../01%20-%20Slides%20Originais/README.md#página-8)):** "Algumas linguagens geram uma **interrupção** e outras não, apenas **armazenam o resultado errado**." O problema se agrava em ponto flutuante, armazenado em notação científica (1432 = 1,432 × 10³). Os detalhes ficam para Cálculo Numérico.

> **[Atenção]** O slide começa sem dizer qual é o problema: é o *overflow*, quando o valor extrapola a faixa do tipo.

**[Explicação elaborada] — o que acontece no overflow:**

<!-- teste: saida-contem="max = 2147483647|max + 1 = -2147483648" -->
```c
#include <stdio.h>
#include <limits.h>

int main(void) {
    int max = INT_MAX;                 /* 2147483647 */
    unsigned int u = (unsigned int)max + 1u;
    printf("max = %d\n", max);
    printf("max + 1 = %d\n", (int)u); /* "dá a volta": -2147483648 */
    return 0;
}
```

C não interrompe a execução e simplesmente guarda o valor que "deu a volta" — é o caso de "armazenar o resultado errado". **[Complemento]** Rigorosamente, `INT_MAX + 1` com `int` é comportamento indefinido em C; o código acima faz a conta em `unsigned` para mostrar o efeito típico de forma segura. Em Java, `Integer.MAX_VALUE + 1` também dá a volta, sem exceção, mas `Math.addExact` lança `ArithmeticException`. Em Python, inteiros não estouram (precisão arbitrária).

## 5. Tipagem estática × dinâmica (p.9–14)

**[Material original]** Toda linguagem implementa um dos dois formatos:

| | Tipagem estática | Tipagem dinâmica |
| --- | --- | --- |
| Quando o tipo é definido | Na **declaração**, em tempo de compilação; **não muda** durante a execução | Em **tempo de execução**, conforme o **valor atribuído** |
| Exemplos (slides) | C/C++, Java, Ada | Perl, Python, PHP, JavaScript |

**Exemplo em PHP ([p.12](../01%20-%20Slides%20Originais/README.md#página-12)):**

<!-- teste: saida-contem="x eh integer|x eh double|x eh string|z eh string" -->
```php
<?php
$x = 10;
echo "x eh " . gettype($x) . PHP_EOL;     // integer
$x = 10.2;
echo "x eh " . gettype($x) . PHP_EOL;     // double
$x = "Universidade Cruzeiro Do Sul";
echo "x eh " . gettype($x) . PHP_EOL;     // string
$z = $x;
echo "Resultado: $z" . PHP_EOL;
echo "z eh " . gettype($z) . PHP_EOL;     // string
?>
```

**O mesmo em Python ([p.13](../01%20-%20Slides%20Originais/README.md#página-13)):**

<!-- teste: saida-contem="x eh <class 'int'>|x eh <class 'float'>|x eh <class 'str'>" -->
```python
x = 10
print("x eh", type(x))     # <class 'int'>
x = 10.2
print("x eh", type(x))     # <class 'float'>
x = "Universidade Cruzeiro do Sul"
print("x eh", type(x))     # <class 'str'>
z = x
print(z)
print("z eh", type(x))     # [Atenção] no slide está type(x); o esperado seria type(z)
```

> **[Atenção]** A última linha do slide usa `type(x)` no lugar de `type(z)`. O resultado é o mesmo, porque `z` e `x` referenciam o mesmo objeto, mas o código não testa o que o texto diz.

**[Explicação elaborada]** Nas duas linguagens, a **mesma variável** `x` assume três tipos ao longo da execução. Na tipagem dinâmica, o tipo é um atributo do **valor**, não da variável. Em C ou Java, `x` declarada como `int` seria `int` para sempre.

**Quadro comparativo do professor ([p.14](../01%20-%20Slides%20Originais/README.md#página-14)):**

| Quesito | Tipagem estática | Tipagem dinâmica |
| --- | --- | --- |
| Velocidade de execução | Maior | Menor |
| Verificação por erros | Compilação | Execução |
| Simplicidade de escrita | Menor | Maior |
| Facilidade de leitura e depuração | Maior | Menor |

**[Explicação elaborada] — por quê:**

- A estática é **mais rápida** porque o compilador já sabe os tipos e gera instruções específicas; na dinâmica, cada operação precisa verificar os tipos em execução.
- A estática é **mais fácil de ler** porque a declaração documenta o que a variável guarda.
- A dinâmica é **mais simples de escrever**, já que não há declarações.

## 6. Força de tipagem (p.15–21)

**[Material original]**

- **Independentemente** de ser estática ou dinâmica, a linguagem pode ser mais ou menos exigente nas operações que envolvem tipos diferentes.
- **Quanto mais exigente, mais fortemente tipada.**
- **Fortemente tipada:** o sistema de tipos possibilita que **todos os erros de tipo sejam detectados**, em compilação ou em execução. Exemplos do slide: **Ada, Java e Perl**.
- **A coerção enfraquece a tipagem.**
- **C/C++ não são tão fortemente tipadas** por possuírem o tipo `union` e realizarem diversas conversões implícitas.
- **Os dois critérios principais de tipagem fraca ([p.21](../01%20-%20Slides%20Originais/README.md#página-21)):** **conversão implícita** e **exposição de ponteiros como valores numéricos**.
- Não há 100% de consenso entre autores ao comparar linguagens ([p.21](../01%20-%20Slides%20Originais/README.md#página-21)).

### 6.1 Java ou C? (p.16)

<!-- teste: saida-contem="res = 5" -->
```c
#include <stdio.h>

int main(void) {
    double x = 2.5;
    int y = 3;
    int res = x + y;          /* 5.5 é convertido IMPLICITAMENTE para int -> 5 */
    printf("res = %d\n", res);
    return 0;
}
```

Em Java, a mesma linha **não compila**:

<!-- teste: compilacao-falha="sim" erro-contem="lossy conversion" -->
```java
public class Main {
    public static void main(String[] args) {
        double x = 2.5;
        int y = 3;
        int res = x + y;      // erro: incompatible types: possible lossy conversion from double to int
        System.out.println(res);
    }
}
```

A correção em Java é tornar a conversão **explícita**: `int res = (int) (x + y);`, que resulta em 5. **Conclusão:** Java tem tipagem mais forte que C, porque recusa a conversão implícita que perde informação.

### 6.2 Conversão implícita × explícita (p.18)

| Linguagem | Código | Tipo de conversão |
| --- | --- | --- |
| C++ | `double y = 2.6; int x = y;` | Implícita (x = 2, sem aviso obrigatório) |
| Java | `double y = 2.6; int x = (int) y;` | Explícita (*cast*): x = 2 |

### 6.3 Exemplo PHP e atividade (p.19–20)

<!-- teste: saida-contem="x eh integer|y eh string|w eh double|Resultado(x+y+w): 40.2" -->
```php
<?php
$x = 10;
$y = "20";
$w = 10.2;
echo "x eh " . gettype($x) . PHP_EOL;     // integer
echo "y eh " . gettype($y) . PHP_EOL;     // string
echo "w eh " . gettype($w) . PHP_EOL;     // double
$z = $x + $y + $w;                         // "20" vira 20 automaticamente
echo "Resultado(x+y+w): $z" . PHP_EOL;     // 40.2
?>
```

A atividade da [p.20](../01%20-%20Slides%20Originais/README.md#página-20) pede o mesmo em C e em Python e uma comparação. Soluções testadas em [resolucoes-aula-06.md](../04%20-%20Resoluções/resolucoes-aula-06.md#e9--atividade-da-p20). Resumo:

| Linguagem | O que acontece com `10 + "20" + 10.2` | Conclusão |
| --- | --- | --- |
| PHP | Converte a string sozinho → 40.2 | **Mais fraca** |
| C | `"20"` é um `char*`; somar ponteiro com `double` **não compila** | Intermediária: exige conversão manual (`atoi`) |
| Python | `TypeError` em execução | **Mais forte** (e dinâmica!) |

> **[Atenção] — Perl na lista de fortemente tipadas ([p.17](../01%20-%20Slides%20Originais/README.md#página-17)).** Perl, como o PHP, faz conversão implícita entre string e número (`"20" + 10` vale 30), o que, pelo critério da própria [p.21](../01%20-%20Slides%20Originais/README.md#página-21), a tornaria **mais fraca**. É um exemplo da falta de consenso que o slide menciona. Em prova, cite a lista do professor e, se houver espaço, a ressalva.

### 6.4 Os dois eixos são independentes

**[Explicação elaborada]** Combinando estática/dinâmica com forte/fraca:

| | Forte | Fraca |
| --- | --- | --- |
| **Estática** | Java, Ada | C, C++ |
| **Dinâmica** | Python | PHP, JavaScript |

Erro clássico de prova: achar que "dinâmica" significa "fraca". Python é dinâmica **e** forte.

## 7. O que o processador faz (p.22–24)

**[Material original]** O código `int a; float b, c; c = a + b;` está correto? O que acontece quando o processador executa a operação?

- O processador opera com **registradores**, e só valores de **representação compatível** podem participar de uma operação aritmética.

**[Explicação elaborada]** Inteiro em complemento de dois e real em ponto flutuante IEEE 754 têm bits completamente diferentes.

- É **responsabilidade do compilador** converter o que o programador escreveu para algo executável.
- **Verificação de tipos** = analisar se os tipos dos operandos são aceitos pelos operadores e **realizar as conversões necessárias**.

| Código-fonte | Código intermediário | Assembly |
| --- | --- | --- |
| `int a;` `float b, c;` `c = a + b;` | `t1 = float(a)` <br> `c = t1 + b;` | `ldr R0, a` <br> `cvtdq2ps R0, R0` <br> `ldr R1, b` <br> `add R2, R0, R1` <br> `str c, R2` |

**[Explicação elaborada]** O compilador insere a conversão `float(a)` no código intermediário, que vira a instrução `cvtdq2ps` (*convert doubleword integers to packed single-precision floats*). Só depois a soma é feita entre dois reais. Essa conversão **implícita** é uma coerção. Esta em particular, de alargamento (`int` → `float`), também é feita por Java. O que torna C mais fraca na seção 6 são as conversões implícitas que **perdem informação** (`double` → `int`, [p.16](../01%20-%20Slides%20Originais/README.md#página-16) e [p.18](../01%20-%20Slides%20Originais/README.md#página-18)), o `union` e a exposição de ponteiros como números ([p.17](../01%20-%20Slides%20Originais/README.md#página-17) e [p.21](../01%20-%20Slides%20Originais/README.md#página-21)).

> **[Atenção]** O assembly do slide é ilustrativo: mistura mnemônicos estilo ARM (`ldr`, `str`, `add`) com uma instrução SSE de x86 (`cvtdq2ps`). Numa máquina real, a soma de dois `float` usaria uma instrução de ponto flutuante (`fadd`/`vadd.f32` no ARM, `addss` no x86), e não o `add` inteiro.

## 8. Sobrecarga de operadores (p.25)

**[Material original]** "Sobrecarga" descreve que um símbolo, comando, função ou operador pode ser usado para tarefas diferentes. Um operador é **sobrecarregado** quando seu significado varia conforme o tipo dos operandos ou do resultado. Exemplo: `+ - * /` aceitam inteiros ou reais e retornam inteiros ou reais.

**[Explicação elaborada]** Em C, `7 / 2` vale 3 (divisão inteira) e `7.0 / 2` vale 3.5 (divisão real): o mesmo símbolo `/` executa operações de máquina diferentes conforme os tipos. Em Java, `+` também concatena strings (`"a" + 1` → `"a1"`). A sobrecarga é uma forma de **polimorfismo estático** — conceito que reaparece na [Aula 13](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md).

## 9. Conexões e pontos para a prova

- Tipos são um dos seis atributos da variável ([Aula 05](../../Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)); a verificação de tipos é a fase semântica do compilador ([Aula 03](../../Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)).
- Ponteiros expostos como números ([Aula 08](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)) são o segundo critério de tipagem fraca.
- Cobrado na [Lista 02, Q5](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q5).
- **Decorar:** estática/dinâmica = *quando*; forte/fraca = *quão exigente*. Exemplos C × Java (5 × erro) e PHP × Python (40.2 × `TypeError`).

---

**Anterior:** [Aula 05](../../Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) · **Próxima:** [Aula 07 — Tipos Compostos](../../Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)


<!-- nav:rodape -->

---

**Aula 06:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · **Resumo** · [Exercícios](../03%20-%20Exercícios/exercicios-aula-06.md) · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-06.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 05 · Resumo](../../Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) · [Aula 07 · Resumo](../../Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md) →

**Links para esta página (15):** [Aula 05 · Resumo](../../Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) · [Aula 06 · visão geral](../README.md) · [Aula 07 · Resumo](../../Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md) · [Aula 08 · Resumo](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) · [Aula 10 · Resoluções](../../Aula%2010%20-%20Paradigma%20Imperativo%20II/04%20-%20Resoluções/resolucoes-aula-10.md) · [Aula 13 · Resumo](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) · [Lista 02](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md) · [03 — Trabalhos e Projetos](../../../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Simulado 01 · Resolução comentada](../../../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md) · [Simulado 02 · Resolução comentada](../../../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-02.md) · [Revisão da Unidade 1 — Fundamentos das linguagens (Aulas 01…](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-1-fundamentos.md) · [Resumo geral da disciplina](../../../06%20-%20Revisões%20e%20Sínteses/resumo-geral-da-disciplina.md) · [Glossário](../../../07%20-%20Glossário/glossario.md) · [P1 — Interpretador de expressões](../../../09%20-%20Projetos%20Práticos/P1%20-%20Interpretador%20de%20Expressões/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
