# Questões integradoras · Resolução comentada

> **[Resolução elaborada]** Resolução das [questões integradoras](questoes-integradoras.md). **Não é gabarito oficial do professor.** Os trechos de código foram compilados e executados.

---

## QI1

**Conceitos:** verificação de tipos (Aula06 p.9–14) × método de implementação (Aula03 p.8–14).

- **Tipagem estática ou dinâmica** responde **quando** o tipo é vinculado à variável: na compilação ou na execução.
- **Implementação** responde **como** o programa é traduzido e executado.

As duas escolhas costumam andar juntas: um compilador é o lugar natural para verificar tipos antes da execução, e um interpretador simplifica a tipagem dinâmica. Mas uma não determina a outra:

- O código intermediário pode **guardar** tipos estáticos (o bytecode Java tem instruções tipadas, como `iadd` e `dadd`) ou **não guardar**.
- **[Complemento]** Exemplos:
  - **Python** é compilado para bytecode (`.pyc`) e mantém tipagem dinâmica.
  - **TypeScript** é verificado estaticamente e depois traduzido para JavaScript, que é interpretado ou compilado com JIT.
  - **LISP** tem compiladores para código nativo e continua dinamicamente tipado.

## QI2

**Conceitos:** escopo e tempo de vida (Aula05); regiões de memória (Aula08 p.12–14).

| Variável | Escopo | Tempo de vida | Região |
| --- | --- | --- | --- |
| `total` | Global (arquivo inteiro) | Programa inteiro | Estático |
| `chamadas` | Local a `soma` | **Programa inteiro** (`static`) | Estático |
| `x` | Local a `soma` (parâmetro) | Cada chamada de `soma` | Pilha |
| `p` | Local a `soma` | Cada chamada de `soma` | Pilha |
| `*p` (inteiro alocado) | Sem nome; acessível por `p` | De `malloc` até `free` | Heap |

Ao final, `total = 7` e `chamadas = 2`. `chamadas` é o exemplo clássico de escopo local com tempo de vida global.

<!-- teste: saida-contem="total = 7, chamadas = 2" -->
```c
#include <stdio.h>
#include <stdlib.h>
int total = 0;
int soma(int x) {
    static int chamadas = 0;
    int *p = malloc(sizeof(int));
    *p = x;
    total += *p;
    chamadas++;
    free(p);
    return chamadas;
}
int main(void) {
    soma(3);
    int c = soma(4);
    printf("total = %d, chamadas = %d\n", total, c);
    return 0;
}
```

## QI3

**Conceitos:** ponteiros (Aula08 p.7–11); modelos de passagem (Aula11 p.13–18).

<!-- teste: saida-contem="menor = 1, maior = 10" -->
```c
#include <stdio.h>

/* v e n: entrada; menor e maior: saída (simulada por ponteiros) */
void minmax(const int v[], int n, int *menor, int *maior) {
    *menor = *maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < *menor) *menor = v[i];
        if (v[i] > *maior) *maior = v[i];
    }
}

int main(void) {
    int dados[] = {9, 3, 7, 1, 8, 2, 10, 5, 4, 6};
    int mn, mx;
    minmax(dados, 10, &mn, &mx);
    printf("menor = %d, maior = %d\n", mn, mx);
    return 0;
}
```

- **`n`:** passagem **por valor**, com semântica de entrada.
- **`menor` e `maior`:** C só tem passagem por valor, mas passar **o valor de um endereço** (`&mn`) permite à função escrever na variável do chamador. Isso simula a passagem **por referência**; aqui, com semântica de **saída**, como o `out` do C#.
- **`v`:** o nome de um vetor, passado a uma função, **decai para um ponteiro** para o primeiro elemento. Só o endereço é copiado, não os elementos; o efeito é o de passagem por referência. `const` impede a função de alterar o vetor, o que dá semântica de entrada, como o `in` do C#.

## QI4

**Conceitos:** `goto` e programação estruturada (Aula09 p.16–22); artigo de Dijkstra.

**(a)** Soma os números **pares de 1 a 10**: 2 + 4 + 6 + 8 + 10 = **30**.

**(b)**

<!-- teste: saida-contem="30" -->
```c
#include <stdio.h>
int main(void) {
    int s = 0;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) s = s + i;
    }
    printf("%d\n", s);
    return 0;
}
```

**(c)** Na versão estruturada, o progresso do programa é descrito por coordenadas simples:

- o **índice textual**: em que linha do corpo do `for` estamos;
- o **índice dinâmico**: em que repetição, ou seja, o valor de `i`.

Com isso, é possível afirmar, por exemplo, que no início de cada repetição `s` contém a soma dos pares menores que `i`.

Na versão com `goto`, a mesma lógica existe, mas está **implícita** nos saltos. Para entender o fluxo, o leitor precisa reconstruir mentalmente o laço a partir dos rótulos. Com saltos arbitrários, essa reconstrução pode ser impossível. É isso que Dijkstra chama de perda da correspondência entre o texto estático e o processo dinâmico.

## QI5

**Conceitos:** acoplamento, coesão, TDA (Aula10 p.16–18); classes e encapsulamento (Aula12 p.18–27).

**Diagnóstico:**

- **Alto acoplamento:** todas as funções dependem dos três vetores globais. Mudar a representação, por exemplo trocar `float notas[]` por uma matriz de notas, obriga a alterar todas elas.
- **Baixa coesão:** os dados de um aluno estão espalhados em três estruturas sem relação explícita, ligados apenas pelo índice.
- **Sem encapsulamento:** qualquer função pode gravar uma nota inválida ou dessincronizar os vetores, por exemplo removendo um nome sem remover a nota.

**Proposta:**

<!-- teste: saida-contem="Ana: média 8.0|Nota inválida" -->
```java
import java.util.ArrayList;
import java.util.List;

class Aluno {
    private final String nome;                 // dados reunidos e ocultos
    private final List<Double> notas = new ArrayList<>();
    private int faltas;

    Aluno(String nome) { this.nome = nome; }

    void registrarNota(double n) {             // a classe valida o próprio estado
        if (n < 0 || n > 10) throw new IllegalArgumentException("Nota inválida: " + n);
        notas.add(n);
    }
    void registrarFalta() { faltas++; }
    double media() { return notas.stream().mapToDouble(Double::doubleValue).average().orElse(0); }
    String getNome() { return nome; }
}

class Turma {
    private final List<Aluno> alunos = new ArrayList<>();
    void matricular(Aluno a) { alunos.add(a); }
    void relatorio() {
        for (Aluno a : alunos) System.out.printf("%s: média %.1f%n", a.getNome(), a.media());
    }
}

public class Main {
    public static void main(String[] args) {
        Aluno ana = new Aluno("Ana");
        ana.registrarNota(7); ana.registrarNota(9);
        Turma t = new Turma(); t.matricular(ana); t.relatorio();
        try { ana.registrarNota(11); } catch (IllegalArgumentException e) { System.out.println(e.getMessage()); }
    }
}
```

> **[Atenção]** `printf("%.1f")` usa a localidade da JVM; em português, a saída pode ser `8,0`. O teste acima rodou com localidade em inglês.

Resultado:

- `Aluno` tem **alta coesão**: uma responsabilidade.
- `Turma` depende só da **interface** de `Aluno`, o que dá **baixo acoplamento**.
- Os dados ficam **encapsulados**: `private`, alterados só por métodos que validam.

## QI6

**Conceitos:** sobrecarga de operadores (Aula06 p.25); polimorfismo estático (Aula13 p.12); coerção (Aula06 p.15–21).

- `+` com `int`, `double` e `String` é **sobrecarga** de operador, ou seja, **polimorfismo estático**: o mesmo símbolo tem significados diferentes conforme os **tipos dos operandos**, e o compilador escolhe o significado na compilação.
- **Não é sobrescrita:** não há herança nem redefinição em subclasse.
- Em `"Total: " + 5` há **sobrecarga + conversão implícita**: como um operando é `String`, o compilador escolhe a concatenação e converte o `5` para `"5"`.
- **[Complemento]** É uma das poucas coerções que Java permite. Ela é segura, porque não perde informação. Por isso não contradiz a classificação de Java como fortemente tipada.

## QI7

**Conceitos:** paradigmas (Aula02), Clojure (Aula14), Prolog (Aula15). Resultado esperado: 1 + 4 + 9 + 16 = **30**.

**Imperativo (C):** o estado (`s`, `i`) muda a cada passo.

<!-- teste: saida-contem="30" -->
```c
#include <stdio.h>
int main(void) {
    int s = 0;
    for (int i = 1; i <= 4; i++) s = s + i * i;
    printf("%d\n", s);
    return 0;
}
```

**Funcional (Clojure):** nenhum valor é alterado; o resultado é uma composição de funções.

<!-- teste: saida-contem="30|30" -->
```clojure
(println (reduce + (map (fn [x] (* x x)) (range 1 5))))   ; formas funcionais

(defn soma-quadrados [n]                                   ; recursão
  (if (= n 0) 0 (+ (* n n) (soma-quadrados (- n 1)))))
(println (soma-quadrados 4))
```

**Lógico (Prolog):** define-se a **relação** entre `N` e a soma; o motor de inferência encontra o valor.

<!-- teste: consulta="soma_quadrados(4, S)." saida-contem="S = 30" -->
```prolog
soma_quadrados(0, 0).
soma_quadrados(N, S) :- N > 0, N1 is N - 1, soma_quadrados(N1, S1), S is S1 + N * N.
```

**Estado:**

- Em C, há variáveis mutáveis atualizadas por atribuição.
- Em Clojure, não há atribuição: cada chamada recebe valores novos, e o "acumulador" é o próprio resultado da recursão (ou do `reduce`).
- Em Prolog, as variáveis são **ligadas uma única vez** por unificação. `N1` e `S1` são variáveis novas a cada nível, e `is` apenas avalia uma expressão aritmética para ligá-la.

## QI8

**Conceitos:** critérios de avaliação (Aula02 p.17); von Neumann (Aula09); funcional (Aula14); lógico (Aula15).

**Onde a afirmação está certa:**

- O imperativo é uma **abstração direta** da arquitetura de von Neumann: variáveis são células de memória, a atribuição é a transferência de dados, e os laços são a forma eficiente de repetir instruções.
- Por isso tende a ter **bom desempenho** e um **custo** de implementação baixo.
- Também é o paradigma mais ensinado, o que o faz parecer "natural".

**Onde ela falha:**

- **"Natural para a máquina" não é "natural para o problema".** A Aula 02 avalia linguagens também por **legibilidade**, **facilidade de escrita** e **confiabilidade**.
- **O estado mutável espalhado dificulta o raciocínio.** É o que motivou a programação estruturada (Dijkstra) e, depois, o encapsulamento da OO.
- **A crítica de Backus** (Aula14) foi justamente que o estilo de von Neumann prende o programador ao "gargalo" palavra a palavra. O funcional elimina efeitos colaterais, o que facilita provar correção e paralelizar.
- **O lógico mostra outro caminho:** para certos problemas, é mais natural **descrever** o que é verdadeiro e deixar a inferência buscar a solução.

**Escolhas adequadas (exemplos):**

| Paradigma | Problema típico | Por quê |
| --- | --- | --- |
| Imperativo | Driver de dispositivo, sistema embarcado, rotina numérica de alto desempenho | Controle fino de memória e de desempenho |
| Orientado a objetos | Sistema de gestão com muitas entidades (clientes, pedidos, produtos) | Modela entidades com estado e comportamento; reuso por herança |
| Funcional | Processamento de grandes volumes de dados, transformações em *pipeline*, sistemas concorrentes | Funções puras são fáceis de compor, testar e paralelizar |
| Lógico | Sistemas especialistas, regras de negócio, verificação de configurações, consultas sobre relações | O conhecimento é declarado como fatos e regras, e a inferência responde perguntas em várias direções |

**Conclusão:** nenhum paradigma é "o mais natural" em absoluto. A adequação depende do problema. É exatamente o objetivo atitudinal da disciplina: decidir o paradigma mais adequado a cada aplicação (Aula01 p.4).
