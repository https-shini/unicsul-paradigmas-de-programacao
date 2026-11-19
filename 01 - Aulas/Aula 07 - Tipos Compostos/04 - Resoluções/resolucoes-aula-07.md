# Aula 07 — Tipos Compostos · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-07.md`](../03%20-%20Exercícios/exercicios-aula-07.md). Os programas foram compilados e executados (javac, gcc, g++).

## E1

| Tipo | Elementos | Acesso |
| --- | --- | --- |
| Enumeração | Valores nomeados de um conjunto fechado | Pelo nome (`Turno.MATUTINO`) |
| Estrutura/registro | Heterogêneos | Pelo nome do campo (`p.idade`) |
| Vetor/matriz | Homogêneos | Pelo índice (`v[3]`, `m[i][j]`) |
| Objeto | Dados de tipos diferentes + métodos | Pelos métodos (e campos, conforme a visibilidade) |

## E2

Facilitam a **legibilidade** do código e **reduzem a chance de erro** (p.4), porque restringem os valores possíveis da variável.

## E3

**Resposta: c.** Fortran indexa de 1 a N; C, C++ e Java, de 0 a N−1; em Pascal e Ada, o programador define (p.11).

## E4

**Registro:** agrupa campos de tipos diferentes, sem comportamento. **Classe:** agrupa campos **e** funções (métodos), com controle de acesso, herança e polimorfismo (p.6 e p.9). Java "não suporta estruturas diretamente" porque não tem a palavra `struct` nem um tipo registro separado: o que seria um registro é escrito como uma classe só com atributos. A Aula 12 (p.22) confirma: em Java e Smalltalk, "todas as abstrações devem ser construídas como classes".

## E5

| Item | Linguagem | Dimensões | Elementos |
| --- | --- | --- | --- |
| a | C/C++ | 4 | 2×2×2×2 = **16** |
| b | C/C++ | 2 | 10×20 = **200** |
| c | Pascal | 1 | 100 (índices 1..100) |
| d | C | 1 | 30 `char`: string de até 29 letras + `'\0'` |

## E6

**`p2.idade` continua 20.** Em C++, a atribuição entre `struct`s copia o **conteúdo** de cada campo (semântica de valor): `p1` e `p2` são blocos de memória independentes. Mudar `p1.idade` depois não afeta `p2`.

**Contraste:** com objetos Java, `p2 = p1` faria as duas variáveis apontarem para o mesmo objeto, e `p2.idade` passaria a 99 (Aula 08, Exemplo 3).

<!-- teste: saida-contem="p2.idade = 20" -->
```cpp
#include <iostream>
struct Pessoa { char nome[30]; int idade; char sexo; };

int main() {
    Pessoa p1 = {"Ana", 20, 'F'}, p2;
    p2 = p1;            // cópia campo a campo
    p1.idade = 99;      // altera só p1
    std::cout << "p2.idade = " << p2.idade << "\n";   // 20
    return 0;
}
```

## E7

Armazenamento por linhas (*row-major*): o deslocamento de `x[i][j]` em elementos é `i × 20 + j`.

- Deslocamento = 3 × 20 + 5 = **65 elementos**.
- Em bytes = 65 × 4 = **260**.
- Endereço = 1000 + 260 = **1260**.

## E8 — Exercício da p.14 (original)

**Modelagem:** `float[][][] notas = new float[2][4][3]` → `[disciplina][aluno][avaliação]`.

<!-- teste: entrada="7 8 9 4 5 6 5 5 5 8 10 7 7 7 7 6 8 8 7 8 9 1 10 10" saida-contem="Media do aluno 3 na disciplina 0: 8.33|Media do aluno 1 na disciplina 1: 7.33|Media do aluno 3 nas primeiras avaliacoes: 4.50" -->
```java
import java.util.Scanner;

public class Notas {
    static final int DISC = 2, ALUNOS = 4, AVAL = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        float[][][] notas = new float[DISC][ALUNOS][AVAL];   // uma única variável

        // Leitura: disciplina -> aluno -> avaliação
        for (int d = 0; d < DISC; d++) {
            System.out.println("*****Digite as notas da disciplina " + d + "*****");
            for (int a = 0; a < ALUNOS; a++) {
                for (int k = 0; k < AVAL; k++) {
                    System.out.print("Aluno " + a + ", avaliacao " + k + ": ");
                    notas[d][a][k] = in.nextFloat();
                }
            }
        }

        // (a) média final de cada aluno em cada disciplina
        for (int d = 0; d < DISC; d++) {
            for (int a = 0; a < ALUNOS; a++) {
                float soma = 0;
                for (int k = 0; k < AVAL; k++) soma += notas[d][a][k];
                System.out.printf("%nMedia do aluno %d na disciplina %d: %.2f", a, d, soma / AVAL);
            }
        }

        // (b) média na primeira avaliação (k = 0) de cada aluno em todas as disciplinas
        for (int a = 0; a < ALUNOS; a++) {
            float soma = 0;
            for (int d = 0; d < DISC; d++) soma += notas[d][a][0];
            System.out.printf("%nMedia do aluno %d nas primeiras avaliacoes: %.2f", a, soma / DISC);
        }
        System.out.println();
    }
}
```

**Raciocínio:**

- Três laços aninhados percorrem as três dimensões na leitura.
- Para (a), fixa-se disciplina e aluno e soma-se na dimensão das avaliações.
- Para (b), fixa-se o aluno e a avaliação `0` e soma-se na dimensão das disciplinas — repare que a ordem dos laços muda: o aluno fica do lado de fora.
- A divisão `soma / AVAL` é `float / int` → `float`, então as casas decimais são preservadas.

**Teste com os dados da p.15:**

| Aluno | Média disc. 0 | Média disc. 1 | Média 1ª avaliação |
| --- | --- | --- | --- |
| 0 | 8.00 | 7.00 | 7.00 |
| 1 | 5.00 | 7.33 | 5.00 |
| 2 | 5.00 | 8.00 | 6.00 |
| 3 | 8.33 | 7.00 | 4.50 |

A saída do slide mostra "8", "7" e "4" nos casos 8.33, 7.33 e 4.50, porque truncou as médias (ver [Atenção no resumo](../02%20-%20Resumo%20Teórico/resumo-aula-07.md#8-exercício-e-desafio-p1416)). Em sistemas configurados em português, `%.2f` usa vírgula: `8,33`.

**Erro comum:** declarar `int` para a soma ou dividir `int / int` (dá divisão inteira); ou usar três matrizes separadas, quando o enunciado exige uma única variável.

## E9 — Desafio da p.16 (original)

Acrescenta-se uma dimensão para o semestre: `float[][][][] notas = new float[2][2][4][3]` → `[semestre][disciplina][aluno][avaliação]`.

<!-- teste: entrada="7 8 9 4 5 6 5 5 5 8 10 7 7 7 7 6 8 8 7 8 9 1 10 10 10 10 10 9 9 9 8 8 8 7 7 7 6 6 6 5 5 5 4 4 4 3 3 3" saida-contem="Semestre 0 - media do aluno 3 na disciplina 0: 8.33|Semestre 1 - media do aluno 0 na disciplina 0: 10.00|Semestre 1 - media do aluno 3 nas primeiras avaliacoes: 5.00" -->
```java
import java.util.Scanner;

public class NotasSemestres {
    static final int SEM = 2, DISC = 2, ALUNOS = 4, AVAL = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        float[][][][] notas = new float[SEM][DISC][ALUNOS][AVAL];   // 4 dimensões, 48 notas

        for (int s = 0; s < SEM; s++)
            for (int d = 0; d < DISC; d++)
                for (int a = 0; a < ALUNOS; a++)
                    for (int k = 0; k < AVAL; k++)
                        notas[s][d][a][k] = in.nextFloat();

        for (int s = 0; s < SEM; s++) {
            for (int d = 0; d < DISC; d++)
                for (int a = 0; a < ALUNOS; a++) {
                    float soma = 0;
                    for (int k = 0; k < AVAL; k++) soma += notas[s][d][a][k];
                    System.out.printf("Semestre %d - media do aluno %d na disciplina %d: %.2f%n", s, a, d, soma / AVAL);
                }
            for (int a = 0; a < ALUNOS; a++) {
                float soma = 0;
                for (int d = 0; d < DISC; d++) soma += notas[s][d][a][0];
                System.out.printf("Semestre %d - media do aluno %d nas primeiras avaliacoes: %.2f%n", s, a, soma / DISC);
            }
        }
    }
}
```

**Raciocínio:** a lógica do E8 fica dentro de um laço externo por semestre. Cada nova "categoria" de agrupamento vira uma nova dimensão da matriz.

## E10

Strings em C terminam com o caractere nulo `'\0'`, que marca o fim do texto. Em `char nome[10]`, uma das 10 posições fica reservada para ele, sobrando 9 caracteres úteis. Copiar 10 letras (por exemplo, com `strcpy`) grava o `'\0'` na 11ª posição, **fora do vetor**: é um *buffer overflow*, comportamento indefinido que pode corromper outras variáveis. C não verifica limites de vetor — uma das razões de ser menos confiável (Aula 02, critérios; Aula 06, tipagem).

## E11

- **C:** `enum` é só um conjunto de constantes `int`. Uma variável `enum turno t = 42;` compila, sem verificação de que 42 é um turno válido.
- **Java:** `enum` é um tipo próprio. `Turno t = 42;` **não compila**, e só os valores declarados são aceitos.

A implementação de Java é **mais fortemente tipada**: rejeita operações e atribuições fora do conjunto de valores do tipo, sem conversão implícita a partir de inteiros (critério da Aula 06, p.21).
