# Aula 05 — Semântica · Resumo teórico

> **Fonte:** [`Aula05_Semantica.pdf`](../01%20-%20Slides%20Originais/Aula05_Semantica.pdf) (18 páginas) — "Introdução à Semântica das Linguagens de Programação". Apoio indicado: Tucker & Noonan, seção 4.3; Sebesta (9ª ed.), cap. 5 (p.18).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF.

---

## 1. Objetivos (p.2)

**[Material original]** Definir para que servem os nomes; identificar e explicar as **seis características de uma variável**; diferenciar análise semântica **estática** e **dinâmica**.

> **[Explicação elaborada]** O primeiro objetivo ("para que servem os nomes") já foi tratado na Aula 04; aqui ele é retomado como primeiro atributo da variável.

## 2. Sintaxe × semântica, de novo (p.3)

**[Material original]**

- **Sintaxe** é a forma da escrita. Sua descrição pode ser considerada simples e tem uma notação **universalmente aceita (BNF)**.
- **Semântica** é um conjunto de significados. Descrevê-la é difícil: **não há notação universalmente aceita**, e muitas linguagens explicam sua semântica de formas diferentes.

## 3. Formas de especificar a semântica (p.4)

**[Material original]**

| Nível | Forma |
| --- | --- |
| Informal | Descrição das regras em linguagem natural |
| Semiformal | Esquemas de tradução dirigidos pela sintaxe |
| Formal | Semântica **operacional**, **denotacional** e **axiomática** |

**[Complemento]** Uma linha sobre cada forma formal (Sebesta, seção 3.5):

| Semântica | Ideia | Exemplo de uso |
| --- | --- | --- |
| Operacional | Descreve o significado pelo **efeito de executar** o programa numa máquina (real ou abstrata), passo a passo | Manuais que explicam um `for` pelo equivalente em `while` |
| Denotacional | Mapeia cada construção para um **objeto matemático** (função de estados em estados) | Definição formal de linguagens funcionais |
| Axiomática | Usa **pré e pós-condições** lógicas para provar propriedades | `{x > 0} x = x - 1 {x >= 0}`, base da verificação formal |

## 4. Variável e seus seis atributos (p.5–13)

**[Material original]** A aula retoma o Exemplo 1 da Aula 04 (`printf("%d", x)` × `printf("%ld", &x)`) e define:

> "Uma variável é uma abstração de uma ou mais células de memória que possui: **Nome**, **Endereço (l-value)**, **Valor (r-value)**, **Tipo**, **Escopo** e **Tempo de vida**." (p.6)

### 4.1 Nome

Segue as regras sintáticas vistas na [Aula 04](../../Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md#8-nomes-e-identificadores-p1218).

### 4.2 Endereço — l-value (p.7)

**[Material original]** Indica o local da memória ao qual a variável está associada.

- Um **mesmo identificador** pode representar **posições diferentes** em partes diferentes da execução.
- **Variáveis diferentes** podem indicar o **mesmo endereço**.

**[Explicação elaborada]**

- **Mesmo nome, endereços diferentes:** uma variável local `i` de uma função ocupa uma posição a cada chamada; numa recursão, cada nível tem o seu `i`.
- **Nomes diferentes, mesmo endereço:** é o *aliasing*. Exemplos: `int &r = x;` em C++, um parâmetro por referência ou duas referências Java ao mesmo objeto (Aula 08, Exemplo 3).
- **Por que "l-value":** é o que aparece à esquerda (*left*) da atribuição. Em `x = 5`, usa-se o **endereço** de `x`.

### 4.3 Valor — r-value (p.7)

**[Material original]** Conteúdo da(s) célula(s) de memória associada(s) à variável.

**[Explicação elaborada]** "r-value" é o que aparece à direita (*right*). Em `y = x + 1`, usa-se o **valor** de `x`. Em `x = x + 1`, o mesmo nome aparece com os dois papéis: endereço à esquerda, valor à direita.

### 4.4 Tipo (p.8)

**[Material original]** Define a **faixa de valores**, o **número de células** de memória e o **conjunto de operadores** aplicáveis. Aprofundado na [Aula 06](../../Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md).

### 4.5 Escopo (p.9–12)

**[Material original]** Escopo é o **conjunto de comandos que podem acessar uma variável**.

- **Local** a um escopo: declarada dentro dele.
- **Não local:** acessível aos comandos, mesmo não tendo sido declarada ali.
- O escopo pode ser **estático** ou **dinâmico**.

#### Escopo estático (p.10–11)

**[Material original]**

- Definido **estaticamente**, conforme a **posição da declaração no código**.
- Algumas linguagens exigem declarar no início dos módulos; C++, Java e C# não exigem.

**[Complemento]** Pascal é um exemplo: as variáveis ficam na seção `var`, antes do `begin`.

- Divide-se em **global** e **local**. A global é declarada fora de qualquer função e é acessível a todas, **exceto** às que declaram uma local com o mesmo nome.
- **Regra de busca:** procura a declaração no bloco/função local. Se não encontrar, procura no **ancestral**, até o bloco mais abrangente. Se não encontrar em nenhum, é **erro**.
- A busca nos ancestrais pode gerar confusão em linguagens com **funções aninhadas**.
- Em C++, o operador `::` acessa a global quando há uma local homônima.

<!-- teste: saida-contem="local: 2|global: 1|bloco interno: 3|de volta: 2" -->
```cpp
#include <iostream>
int x = 1;                         // global

int main() {
    int x = 2;                     // local de main: esconde (sombreia) a global
    std::cout << "local: " << x << "\n";        // 2
    std::cout << "global: " << ::x << "\n";     // 1  -> operador de escopo
    {
        int x = 3;                 // bloco interno: esconde a de main
        std::cout << "bloco interno: " << x << "\n";  // 3
    }
    std::cout << "de volta: " << x << "\n";     // 2
    return 0;
}
```

#### Escopo dinâmico (p.12)

**[Material original]**

- Definido em função da **ordem de chamada dos subprogramas**, que pode variar entre execuções.
- Usado em **APL** e nas primeiras versões de **LISP**; **Perl** e **Common LISP** permitem declarar variáveis com escopo dinâmico, embora o padrão seja estático.
- Programas com escopo dinâmico são **menos confiáveis e mais difíceis de ler**.

**[Explicação elaborada] — o mesmo código, dois resultados.** Considere o pseudocódigo:

```text
x = "global"

funcao mostra():
    imprime(x)          # x não é local de mostra

funcao chamador():
    x = "do chamador"   # declara um x LOCAL de chamador
    mostra()

chamador()
```

| Regra | O que `mostra()` imprime | Por quê |
| --- | --- | --- |
| Escopo **estático** | `global` | `mostra` foi **escrita** no nível global; seu ancestral textual é o global. |
| Escopo **dinâmico** | `do chamador` | `mostra` foi **chamada** por `chamador`; a busca segue a pilha de chamadas. |

Com escopo dinâmico, só é possível saber a qual `x` a função se refere **executando** o programa — por isso a legibilidade e a confiabilidade caem.

### 4.6 Tempo de vida (p.13)

**[Material original]**

- É o tempo de **existência da variável em memória**.
- Em geral, escopo e tempo de vida estão relacionados.
- A **chamada a funções** modifica essa relação.
- **Modificadores** como `static`, em C, C++ e PHP, também alteram essa relação.

**[Explicação elaborada]**

- **Chamada a funções:** enquanto `main` chama `f`, as locais de `main` continuam **vivas** (estão na pilha), mas **fora do escopo** de `f`. Tempo de vida e escopo deixam de coincidir.
- **`static` em uma local:** a variável tem **escopo local** (só a função a enxerga), mas **tempo de vida do programa inteiro** — ela mantém o valor entre chamadas.

<!-- teste: saida-contem="chamada 1|chamada 2|chamada 3" -->
```c
#include <stdio.h>

void conta(void) {
    static int vezes = 0;   /* inicializada uma única vez; sobrevive entre chamadas */
    vezes++;
    printf("chamada %d\n", vezes);
}

int main(void) {
    conta(); conta(); conta();   /* imprime chamada 1, 2, 3 */
    return 0;
}
```

Sem `static`, a função imprimiria "chamada 1" três vezes.

## 5. Constantes nomeadas (p.14–16)

**[Material original]**

- É um nome vinculado a um valor **apenas uma vez**.
- Permitem parametrizar o programa, o que facilita a manutenção e melhora a legibilidade e a confiabilidade.
- Pascal e Fortran aceitam só **valores constantes**; C++ e Ada aceitam **expressões**.
- Palavras usadas: C/C++ `const`, Pascal `const`, Java `final`, C# `const` e `readonly`.

**Exemplo em Java (p.16):**

<!-- teste: entrada="2" saida-contem="Area: 12.5664|Comprimento: 12.5664" -->
```java
import java.util.Scanner;

class Main {
    static final float pi = 3.1416f;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o raio de uma circunferência: ");
        float raio = Float.valueOf(input.nextLine());
        float area = pi * raio * raio;
        float comprimento = 2 * pi * raio;
        System.out.println("Area: " + area);
        System.out.println("Comprimento: " + comprimento);
    }
}
```

**[Explicação elaborada]**

- `final` impede reatribuir `pi`; `static` faz a constante pertencer à classe, e não a cada objeto.
- O sufixo `f` é obrigatório porque `3.1416` sozinho é um literal `double`, e Java não converte `double` para `float` implicitamente (ver tipagem forte, Aula 06).
- Para raio 2, área e comprimento valem ambos 12,5664, pois π·2² = 2·π·2.
- Trocar a precisão de π exige mudar **uma linha** — essa é a vantagem de manutenção citada no slide.

> **[Complemento]** Em C#, `const` exige valor conhecido em compilação; `readonly` recebe o valor na declaração ou no construtor, em tempo de execução (pode vir de uma expressão calculada), e depois não pode mais ser alterado.

## 6. Semântica estática × dinâmica (p.17)

**[Material original]** A análise semântica pode ocorrer em dois momentos:

- **Estática:** o que pode ser verificado em **tempo de compilação**.
- **Dinâmica:** o que só pode ser verificado em **tempo de execução**.
- "Obs.: por definição, **não há verificação estática em linguagens interpretadas**!"

> **[Atenção]** A observação vale para um interpretador puro, que executa sem tradução prévia. As implementações de Python (CPython) e Perl são, na prática, híbridas e fazem verificações antes de executar: um `SyntaxError` em Python ou uma variável não declarada em Perl com `use strict` impedem a execução da primeira linha. Em prova, use a forma do professor e, se houver espaço, acrescente a ressalva.


**[Explicação elaborada]**

| Verificação | Estática ou dinâmica? |
| --- | --- |
| Variável usada sem declaração (C, Java) | Estática |
| Atribuir `double` a `int` sem *cast* (Java) | Estática |
| Divisão por zero com divisor lido do teclado | Dinâmica |
| Índice fora dos limites do vetor (Java lança exceção) | Dinâmica |
| Tipo errado em Python (`10 + "20"`) | Dinâmica (`TypeError` em execução) |

## 7. Conexões e pontos para a prova

- Os seis atributos fazem a ponte entre nomes (Aula 04), tipos (Aula 06) e memória (Aula 08).
- Escopo e tempo de vida reaparecem na [Aula 08](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) (alocação e regiões de memória) e na [Aula 10](../../Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) (variáveis globais aumentam o acoplamento).
- Cobrado na [Lista 02, Q4](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q4) (escopo estático × dinâmico).
- Decorar os **seis atributos** e a **regra de busca** do escopo estático.

---

**Anterior:** [Aula 04](../../Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) · **Próxima:** [Aula 06 — Sistema de Tipos](../../Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)
