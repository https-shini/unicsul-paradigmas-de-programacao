<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 03](../README.md) › [04 - Resoluções](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 03 — Implementação das Linguagens · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-03.md`](../03%20-%20Exercícios/exercicios-aula-03.md). Os códigos do E9 foram compilados e executados durante a elaboração deste repositório (C com gcc, Java com javac/java, Python 3).

## E1

| Forma | Definição (slides) | Exemplos |
| --- | --- | --- |
| Compilação | Fonte → código de máquina de uma plataforma, salvo em executável ([p.8](../01%20-%20Slides%20Originais/README.md#página-8)) | Fortran, C, C++, Pascal |
| Interpretação | Interpretador simula a máquina, traduz e executa ao mesmo tempo ([p.10](../01%20-%20Slides%20Originais/README.md#página-10)) | Lisp, JavaScript, PHP, Python |
| Híbrida | Compilador gera código intermediário, executado por um interpretador ([p.12](../01%20-%20Slides%20Originais/README.md#página-12)) | Java, C#, VB.NET |

## E2

**Resposta: b.** A compilação traduz tudo antes; a híbrida traduz antes para o intermediário; a montagem é a tradução de Assembly.

## E3

A **linguagem** é o conjunto de termos e regras sintáticas e semânticas (Aula 02). O **ambiente** é o conjunto de ferramentas que apoia o desenvolvimento — editor, compilador, ligador, bibliotecas, modelos ([p.16](../01%20-%20Slides%20Originais/README.md#página-16)). Exemplo: Java é linguagem; IntelliJ e VS Code são ambientes.

## E4

1. **Analisador léxico** → unidades léxicas (tokens).
2. **Analisador sintático** → árvores de análise sintática.
3. **Gerador de código intermediário e analisador semântico** → código intermediário verificado.
4. **Otimização** (opcional) → código intermediário melhorado.
5. **Gerador de código** → linguagem de máquina.

**Erro comum:** colocar a semântica antes da sintaxe. Só é possível verificar significado depois de conhecer a estrutura.

## E5

A tabela de símbolos guarda os atributos dos identificadores: nome, tipo, escopo, endereço. O léxico a alimenta com os nomes encontrados; a análise semântica a consulta para saber se um nome foi declarado e qual é seu tipo; o gerador de código, para saber onde cada variável está na memória. Por isso aparece ligada a várias fases na figura da [p.9](../01%20-%20Slides%20Originais/README.md#página-9).

## E6

O compilador Java (`javac`) gera **bytecode**, independente de processador e sistema operacional. Quem traduz o bytecode para a máquina real é a **JVM**, e cada plataforma tem a sua. O mesmo `.class` roda onde houver JVM. Já o compilador C gera **código de máquina** de uma arquitetura e de um sistema específicos (formato de executável, chamadas de sistema, conjunto de instruções), então é preciso recompilar para cada plataforma.

## E7

| Critério | Compilação | Interpretação pura | Híbrida |
| --- | --- | --- | --- |
| Velocidade | Alta: tradução feita uma vez, executa código nativo | Baixa: decodifica cada instrução sempre que executa | Média: interpreta um código já simplificado, e com JIT se aproxima do nativo |
| Portabilidade | Baixa: executável preso à plataforma | Alta: basta o interpretador | Alta: basta a VM |
| Erros antes de executar | Muitos: sintaxe e semântica estática | Quase nenhum (Aula 05, [p.17](../../Aula%2005%20-%20Semântica/01%20-%20Slides%20Originais/README.md#página-17)) | Os da etapa de compilação |
| Depuração | Mais difícil: o executável não é o fonte | Fácil: o erro aponta a linha do fonte | Intermediária |

## E8

**Segundo o slide ([p.10](../01%20-%20Slides%20Originais/README.md#página-10)):** Python é exemplo de linguagem **interpretada** — é a resposta esperada na disciplina.

**[Complemento]** Na implementação CPython, o fonte é compilado internamente para **bytecode** (arquivos `.pyc` em `__pycache__`), executado pela máquina virtual do CPython. Tecnicamente, isso é um esquema híbrido. A afirmação "nunca gera código intermediário" está, portanto, **incorreta** para o CPython, embora a classificação didática como "interpretada" se mantenha, porque o processo é transparente para o programador.

## E9 — Atividade da p.17

> O slide pede uma linguagem; o enunciado do repositório pede duas, de grupos diferentes. C, Python e Java são do Grupo 1; Perl é do Grupo 2.

**Lógica comum:** ler o primeiro valor e usá-lo para inicializar `maior` e `menor` — evita inventar "infinitos" —, acumular a soma e, no fim, dividir por 10.

### C (Grupo 1, compilada)

<!-- teste: entrada="5 3 9 1 7 2 8 6 4 10" saida-contem="Media: 5.50|Maior: 10.00|Menor: 1.00" -->
```c
#include <stdio.h>

int main(void) {
    double x, soma = 0, maior = 0, menor = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%lf", &x);
        if (i == 0) { maior = menor = x; }      /* primeiro valor inicializa */
        if (x > maior) maior = x;
        if (x < menor) menor = x;
        soma += x;
    }
    printf("Media: %.2f\nMaior: %.2f\nMenor: %.2f\n", soma / 10, maior, menor);
    return 0;
}
```

### Python (Grupo 1, interpretada)

<!-- teste: entrada="5\n3\n9\n1\n7\n2\n8\n6\n4\n10" saida-contem="Media: 5.50|Maior: 10.00|Menor: 1.00" -->
```python
nums = [float(input()) for _ in range(10)]   # lê 10 valores
print(f"Media: {sum(nums) / len(nums):.2f}")
print(f"Maior: {max(nums):.2f}")
print(f"Menor: {min(nums):.2f}")
```

### Java (referência para a comparação, híbrida)

<!-- teste: entrada="5 3 9 1 7 2 8 6 4 10" saida-contem="Media: 5.50|Maior: 10.00|Menor: 1.00" -->
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double soma = 0, maior = 0, menor = 0;
        for (int i = 0; i < 10; i++) {
            double x = in.nextDouble();
            if (i == 0) { maior = x; menor = x; }
            maior = Math.max(maior, x);
            menor = Math.min(menor, x);
            soma += x;
        }
        System.out.printf("Media: %.2f%nMaior: %.2f%nMenor: %.2f%n", soma / 10, maior, menor);
    }
}
```

### Perl (Grupo 2, interpretada)

<!-- teste: entrada="5\n3\n9\n1\n7\n2\n8\n6\n4\n10" saida-contem="Media: 5.50|Maior: 10.00|Menor: 1.00" -->
```perl
use strict;
use warnings;

my ($soma, $maior, $menor) = (0, undef, undef);
for my $i (1 .. 10) {
    my $x = <STDIN>;
    chomp $x;
    $maior = $x if !defined $maior || $x > $maior;
    $menor = $x if !defined $menor || $x < $menor;
    $soma += $x;
}
printf "Media: %.2f\nMaior: %.2f\nMenor: %.2f\n", $soma / 10, $maior, $menor;
```

**Teste:** com a entrada `5 3 9 1 7 2 8 6 4 10`, as quatro versões imprimem `Media: 5.50`, `Maior: 10.00`, `Menor: 1.00`.

**Diferenças em relação ao Java:**

| Aspecto | C | Python | Perl | Java |
| --- | --- | --- | --- | --- |
| Estrutura mínima | Função `main` | Nenhuma: o script roda de cima para baixo | Nenhuma (script) | Classe com `public static void main` |
| Declaração de tipos | Obrigatória (`double`) | Não há (tipagem dinâmica) | Não há; sigilo `$` indica escalar | Obrigatória |
| Leitura | `scanf` com especificador de formato | `input()` + conversão `float()` | `<STDIN>` + `chomp` | Objeto `Scanner` |
| Recursos prontos | Nenhum: laço manual | `sum`, `max`, `min` sobre listas | Laço manual | `Math.max`/`Math.min` |
| Implementação | Compilada (`gcc` → executável nativo) | Interpretada (slide) | Interpretada (o `perl` compila internamente para uma árvore de opcodes) | Híbrida (`javac` → bytecode → JVM) |

## E10

O programador Scheme "enxerga" uma **máquina Scheme**: escreve expressões e vê os resultados, como se o hardware avaliasse Scheme diretamente. Na verdade, o **interpretador Scheme** é um programa que roda sobre o **sistema operacional**, que por sua vez usa o **interpretador de macroinstruções** (microcódigo) para chegar à **máquina pura**. Cada camada oferece à de cima um "computador virtual" mais conveniente — abstração em camadas.


<!-- nav:rodape -->

---

**Aula 03:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-03.md) · [Exercícios](../03%20-%20Exercícios/exercicios-aula-03.md) · **Resoluções** · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 02 · Resoluções](../../Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/04%20-%20Resoluções/resolucoes-aula-02.md) · [Aula 04 · Resoluções](../../Aula%2004%20-%20Sintaxe/04%20-%20Resoluções/resolucoes-aula-04.md) →

**Links para esta página (5):** [Aula 03 · Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-03.md) · [Aula 03 · Exercícios](../03%20-%20Exercícios/exercicios-aula-03.md) · [Aula 03 · visão geral](../README.md) · [03 — Trabalhos e Projetos](../../../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
