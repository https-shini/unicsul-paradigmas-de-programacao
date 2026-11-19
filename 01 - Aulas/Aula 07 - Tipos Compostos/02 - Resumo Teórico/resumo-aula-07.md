# Aula 07 — Tipos Compostos · Resumo teórico

> **Fonte:** [`Aula07_Tipos Compostos.pdf`](../01%20-%20Slides%20Originais/Aula07_Tipos%20Compostos.pdf) (16 páginas). A aula não tem slide de bibliografia.
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF.

---

## 1. Objetivos (p.2)

**[Material original]** Identificar os principais tipos compostos; compreender o uso de variáveis do tipo `enum` e `struct`; revisar o conceito de matrizes e elaborar programas com matrizes de três ou mais dimensões.

## 2. O que são tipos compostos (p.3)

**[Material original]** Tipos formados a partir dos tipos básicos: **enumerações**, **estruturas ou registros**, **vetores e matrizes** e **objetos**.

**[Explicação elaborada]** Retomando a [Aula 06](../../Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#2-conceitos-fundamentais-p34): primitivos não são definidos a partir de outros; compostos são construídos a partir de primitivos ou de outros compostos. Uma matriz de registros, por exemplo, é um composto feito de compostos.

| Tipo composto | Elementos | Acesso | Ideia central |
| --- | --- | --- | --- |
| Enumeração | Lista fechada de valores nomeados | Pelo nome do valor | Restringir valores possíveis |
| Registro (`struct`/`record`) | Heterogêneos (tipos diferentes) | Pelo **nome do campo** | Agrupar dados relacionados |
| Vetor/matriz | Homogêneos (mesmo tipo) | Pelo **índice** | Coleção indexada |
| Objeto | Dados + comportamento | Por métodos | Encapsular estado e operações |

## 3. Enumerações (p.4–5)

**[Material original]** Restringem os valores que podem ser associados a uma variável, **facilitam a legibilidade** e **reduzem a chance de erro**.

**Exemplos em Java (p.5):**

<!-- teste: entrada="Ciencia da Computacao\nDireito" saida-contem="Turno de oferta: MATUTINO|Turno de oferta: VESPERTINO" -->
```java
import java.util.Scanner;

class Main {
    public enum Turno { MATUTINO, VESPERTINO, NOTURNO }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String curso1, curso2;
        Turno turno1, turno2;
        System.out.print("Digite o nome do curso 1: ");
        curso1 = input.nextLine();
        System.out.print("Digite o nome do curso 2: ");
        curso2 = input.nextLine();

        turno1 = Turno.MATUTINO;
        System.out.println("Curso 1: " + curso1);
        System.out.println("Turno de oferta: " + turno1);

        turno2 = Turno.VESPERTINO;
        System.out.println("Curso 2: " + curso2);
        System.out.println("Turno de oferta: " + turno2);
    }
}
```

<!-- teste: saida-contem="DOMINGO|SEGUNDA|SABADO" -->
```java
class Main {
    public enum Dia { DOMINGO, SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA, SABADO }

    public static void main(String[] args) {
        for (Dia d : Dia.values()) {   // values() devolve os valores na ordem declarada
            System.out.println(d);
        }
    }
}
```

**[Explicação elaborada]**

- Com `enum`, a variável `turno1` **só** pode receber `MATUTINO`, `VESPERTINO` ou `NOTURNO`. Escrever `turno1 = "Integral";` é **erro de compilação**. Com uma `String`, qualquer texto seria aceito — inclusive erros de digitação como `"Matutnio"`.
- `Turno.MATUTINO` é mais legível que um código mágico como `1`.
- **[Complemento]** Em C, `enum` é só um apelido para constantes inteiras (`enum turno {MATUTINO, VESPERTINO}` → 0, 1), e o compilador aceita atribuir qualquer `int`. Em Java, `enum` é um tipo de verdade, com verificação — mais um exemplo de tipagem mais forte em Java.

## 4. Estruturas ou registros (p.6–8)

**[Material original]**

- Tipos que **reúnem dados de diferentes tipos**, acessados pelos seus nomes (**campos**).
- **Java não suporta estruturas diretamente**: elas são tratadas como uma classe.
- Diferem das classes porque têm **apenas os campos (atributos)**, sem métodos e outras características da POO.

**C++ (p.7):**

<!-- teste: entrada="Ana\n20\nF" saida-contem="Ana tem 20 anos e é do sexo F" -->
```cpp
#include <iostream>
using namespace std;

int main() {
    struct Pessoa {
        char nome[30];
        int idade;
        char sexo;
    };
    struct Pessoa p1, p2;

    std::cout << "Digite o nome da pessoa: ";
    std::cin >> p1.nome;
    std::cout << "Digite a idade da pessoa: ";
    std::cin >> p1.idade;
    std::cout << "Digite o sexo da pessoa: ";
    std::cin >> p1.sexo;
    p2 = p1;                                    // copia TODOS os campos
    std::cout << p2.nome << " tem " << p2.idade << " anos e é do sexo " << p2.sexo << endl;
    return 0;
}
```

**Pascal (p.8):**

```pascal
Program Cadastro(output);
type
    pessoa = Record
        nome: string;
        idade: integer;
        sexo : char;
    End;
var
    p: pessoa;
begin
    write('Digite o nome: ');   readln(p.nome);
    write('Digite a idade: ');  readln(p.idade);
    write('Digite o sexo: ');   readln(p.sexo);
    writeln(p.nome, ' tem ', p.idade, ' anos e é do sexo ', p.sexo);
end.
```

**[Explicação elaborada]**

- Em C++, os dados são lidos em `p1` e impressos a partir de `p2`. Isso funciona porque `p2 = p1` **copia o conteúdo** de todos os campos — é **semântica de valor**. Depois da cópia, alterar `p1.idade` **não** muda `p2`.
- Compare com a [Aula 08, Exemplo 3](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-3--referências-a-objetos-em-java-p11): em Java, `p2 = p1` com objetos copia só a **referência**, e as duas variáveis passam a ser o mesmo objeto.
- Em C++, uma `struct` **pode** ter métodos (é quase igual a uma `class`, com membros públicos por padrão). A definição do slide ("apenas campos") descreve o uso tradicional de registros, herdado de C e Pascal.

## 5. Classes e objetos (p.9)

**[Material original]**

- **Classe:** declaração de tipo que **encapsula** dados (constantes ou variáveis) de diferentes tipos e **funções para manipular** essas variáveis.
- **Objeto:** instância de uma classe (uma variável).
- Possibilita **herança** e **polimorfismo**.

Aprofundado nas [Aulas 12](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) e [13](../../Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md). **Registro + funções + controle de acesso = classe.**

## 6. Matrizes (p.10–12)

**[Material original]**

- Conjuntos de **dados homogêneos** armazenados em uma mesma variável, acessados por **índices**.
- Uma dimensão (**vetores/arrays**) ou várias (matrizes bi, tri ou **n-dimensionais**).
- **Indexação:** C/C++ e Java vão de **0 a N−1**; Fortran, de **1 a N**; em Pascal e Ada, **o programador define** os limites.
- Java e C/C++ permitem definir o tamanho em **tempo de execução**, mas, uma vez criado, ele **não pode ser mudado**.
- Em C/C++, o vetor é acessível por **ponteiros**.

**Declarações (p.12):**

| Declaração | Linguagem | Significado |
| --- | --- | --- |
| `int a[50];` | C/C++ | Vetor de 50 inteiros (índices 0–49) |
| `float x[10][20];` | C/C++ | Matriz 10 × 20 |
| `int m[2][2][2][2];` | C/C++ | Matriz de **4 dimensões** (16 elementos) |
| `char nome[30];` | C | String de até 29 caracteres + `'\0'` |
| `int *numeros = NULL;` | C/C++ | Ponteiro, para alocar o vetor dinamicamente depois |
| `int[] numeros = new int[qtd];` | Java | Vetor com tamanho definido em execução |
| `x : array[1..100] of integer;` | Pascal | Vetor com índices de 1 a 100, escolhidos pelo programador |

**[Explicação elaborada] — como uma matriz fica na memória:** a memória é linear. Em C e Java, as linhas são guardadas uma após a outra (*row-major*). Para `float x[10][20]`, o elemento `x[i][j]` fica na posição `i*20 + j` a partir do início. Generalizando para N dimensões `[d1][d2]...[dn]`, cada índice é multiplicado pelo produto das dimensões à sua direita. **[Complemento]** Em Java, uma "matriz" é na verdade um vetor de vetores: cada linha é um objeto separado, e as linhas podem ter tamanhos diferentes.

## 7. Strings (p.13)

**[Material original]**

- **C:** tratada como **vetor de caracteres** (`char c;` é um caractere; `char nome[10];` é uma string).
- **Pascal:** possui o tipo `string`.
- **Java:** classe `String`.
- **C++:** classe `string`.

**[Explicação elaborada]** Em C, a string é composta (vetor) e termina com o caractere nulo `'\0'`. Por isso `char nome[10]` guarda no máximo 9 caracteres úteis. Em Java e C++, a classe esconde esses detalhes e oferece métodos (`length()`, `substring()`) — é um **tipo abstrato de dados** (Aula 10).

## 8. Exercício e desafio (p.14–16)

**[Material original] — Exercício (p.14):** o 8º semestre tem 2 disciplinas, com 4 alunos matriculados; em ambas houve 3 provas. Fazer em Java um programa que leia as 3 notas dos 4 alunos nas 2 disciplinas e as armazene em **uma única variável do tipo matriz de float**. O programa deve mostrar a média final de cada aluno em cada disciplina e a média na primeira avaliação de cada aluno em todas as disciplinas.

**[Material original] — Saída de exemplo (p.15):** execução com notas inteiras. Por exemplo, aluno 0 na disciplina 0: notas 7, 8 e 9 → "Média do aluno 0 na disciplina 0: 8".

> **[Atenção]**
> - A saída da p.15 foi gerada por um programa executado com `make` (C/C++), não Java, e mostra as médias **truncadas para inteiro**. Exemplo: aluno 3 na disciplina 0 tem notas 8, 10 e 7 → média 8,33, exibida como "8"; nas primeiras avaliações, (8 + 1)/2 = 4,5, exibida como "4". Como o enunciado pede matriz de **float**, as médias devem ser exibidas com casas decimais.
> - O exercício fala do **oitavo** semestre e o desafio (p.16) fala do **quarto e quinto**. É uma inconsistência do enunciado; não afeta a lógica.

**[Material original] — Desafio (p.16):** salvar na mesma matriz os dados do 4º e do 5º semestres (ambos com 2 disciplinas, 4 alunos e 3 avaliações).

**[Explicação elaborada] — modelagem:**

- Exercício: `float[][][] notas = new float[2][4][3];` → `[disciplina][aluno][avaliação]`, com 24 notas.
- Desafio: `float[][][][] notas = new float[2][2][4][3];` → `[semestre][disciplina][aluno][avaliação]`, com 48 notas. É a "matriz com três ou mais dimensões" do objetivo da aula.

Solução completa e testada em [resolucoes-aula-07.md](../04%20-%20Resoluções/resolucoes-aula-07.md#e8--exercício-da-p14-original).

## 9. Conexões e pontos para a prova

- Tipos compostos completam o sistema de tipos da [Aula 06](../../Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md).
- Vetores em C são acessados por ponteiros ([Aula 08](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)).
- Registros evoluem para classes ([Aula 12](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)); Java e Smalltalk não têm registros.
- Saber: registro = **heterogêneo + nome**; matriz = **homogênea + índice**; indexação 0..N−1 × 1..N × definida pelo programador.

---

**Anterior:** [Aula 06](../../Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) · **Próxima:** [Aula 08 — Ponteiros](../../Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)
