# Simulado 03 · Resolução comentada

> **[Resolução elaborada]** Resolução do [simulado autoral](simulado-03.md). **Não é gabarito oficial do professor.** Os trechos de código foram compilados e executados.

## Gabarito da Parte A

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| c | b | c | b | b | a | b | b | b | b |

---

## Parte A — comentários

**1 — c.** `private` restringe o acesso à própria classe; `protected` estende o acesso às subclasses (e, em Java, ao pacote). O encapsulamento da pilha da [Aula 12](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) depende disso: `vetPilha` e `topo` são `private`.

**2 — b.** Java faz **coleta de lixo automática**: um objeto sem referências *pode* ser liberado, mas o momento não é garantido. Quem tem destrutor chamado explicitamente com `delete` é o C++ (Aula12 p.28–30).

**3 — c.** Java permite herdar de **uma** classe e implementar **várias** interfaces, nessa ordem: `extends` antes de `implements`. A alternativa (a) seria herança múltipla de classes, que Java não tem; (d) é a sintaxe de C++ ([Aula 13](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)).

**4 — b.** Uma classe com método abstrato **precisa** ser declarada `abstract` e não pode ser instanciada; as subclasses **concretas** devem implementar o método (Aula13 p.13). **[Complemento]** Uma subclasse que também seja `abstract` pode deixar a implementação para as suas filhas.

**5 — b.** Mesmo nome, **listas de parâmetros diferentes**, na mesma classe: sobrecarga, resolvida em tempo de **compilação**. A sobrescrita redefine, na subclasse, um método com a mesma assinatura e é resolvida em execução.

**6 — a.** Em Clojure, `+` aceita qualquer número de argumentos: `(+ 1 2 3 4)` = 10. É uma vantagem da notação prefixa sobre a infixa (Aula14 p.13–14).

**7 — b.** Haskell é **pura** (sem efeitos colaterais fora de construções controladas); LISP, Scheme e Clojure são **impuras**, porque permitem atribuição e E/S diretas (Aula14 p.9).

**8 — b.** Função pura: o resultado depende **só dos argumentos**, e a chamada não altera nada fora dela. **[Complemento]** O termo não aparece nos slides com esse nome; ver o [glossário](../../07%20-%20Glossário/glossario.md).

**9 — b.** Em Prolog, a vírgula no corpo da regra é a **conjunção**: `avo(X, Z)` é verdadeiro se `pai(X, Y)` **e** `pai(Y, Z)` forem provados ([Aula 15](../../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)). A disjunção é o `;`.

**10 — b.** `is` **avalia** a expressão da direita e unifica o resultado com a esquerda: `X = 12`. Com `=`, a resposta seria `X = 3*4`, porque `=` só unifica termos, sem calcular.

<!-- teste: consulta="X is 3 * 4, Y = 3 * 4." saida-contem="X = 12" -->
```prolog
% arquivo vazio: a consulta usa só predicados predefinidos
```

---

## Parte B — respostas-modelo

## 11

**Conceitos:** TDA, encapsulamento, modificadores de acesso (Aula12 p.10–16).

<!-- teste: saida-contem="10\n20\n30\n40" -->
```java
class Fila {
    private final int[] itens = new int[4];   // representação OCULTA
    private int inicio = 0, fim = 0, tamanho = 0;

    public boolean vazia() { return tamanho == 0; }

    public void enfileirar(int x) {
        if (tamanho == itens.length) {
            System.out.println("Erro - fila cheia");
            return;
        }
        itens[fim] = x;
        fim = (fim + 1) % itens.length;       // volta ao início: vetor circular
        tamanho++;
    }

    public int desenfileirar() {
        if (vazia()) {
            System.out.println("Erro - fila vazia");
            return -1;
        }
        int x = itens[inicio];
        inicio = (inicio + 1) % itens.length;
        tamanho--;
        return x;
    }
}

public class Main {
    public static void main(String[] args) {
        Fila f = new Fila();
        f.enfileirar(10);
        f.enfileirar(20);
        f.enfileirar(30);
        System.out.println(f.desenfileirar());   // 10
        f.enfileirar(40);
        while (!f.vazia()) {
            System.out.println(f.desenfileirar());   // 20, 30, 40
        }
    }
}
```

- **Encapsulamento:** `inicio`, `fim` e `tamanho` precisam mudar **juntos**. Se fossem públicos, um cliente poderia escrever `f.tamanho = 0` sem mexer nos índices e deixar a fila num estado inconsistente. Com `private`, só os métodos da classe alteram o estado, e eles mantêm a coerência.
- **Independência da representação:** o `main` usa só `enfileirar`, `desenfileirar` e `vazia`. Trocar o vetor por uma lista encadeada, como na pilha 1d da Aula 12, não exigiria mudar o `main`.

## 12

**Conceitos:** classe abstrata, herança, polimorfismo e vinculação dinâmica (Aula13 p.12–14).

<!-- teste: saida-contem="Retangulo: area 6.00\nCirculo: area 3.14" -->
```java
import java.util.Locale;

abstract class Forma {
    private final String nome;
    protected Forma(String nome) { this.nome = nome; }

    public abstract double area();                    // sem corpo: cada subclasse define

    public String descricao() {                       // método concreto, herdado
        return String.format(Locale.ROOT, "%s: area %.2f", nome, area());
    }
}

class Retangulo extends Forma {
    private final double base, altura;
    Retangulo(double base, double altura) { super("Retangulo"); this.base = base; this.altura = altura; }
    @Override public double area() { return base * altura; }
}

class Circulo extends Forma {
    private final double raio;
    Circulo(double raio) { super("Circulo"); this.raio = raio; }
    @Override public double area() { return Math.PI * raio * raio; }
}

public class Main {
    public static void main(String[] args) {
        Forma[] formas = { new Retangulo(2, 3), new Circulo(1) };
        for (Forma f : formas) {
            System.out.println(f.descricao());        // polimorfismo dinâmico
        }
    }
}
```

- **Onde está o polimorfismo dinâmico:** em `descricao()`, a chamada `area()` é feita sobre um objeto do tipo declarado `Forma`. Qual `area()` executa — a do retângulo ou a do círculo — só é decidido **em execução**, pelo tipo real do objeto (vinculação tardia, Aula13 p.12). O mesmo vale para `f.descricao()` no laço.
- `new Forma("x")` não compila: a classe é abstrata.
- `Locale.ROOT` garante o ponto decimal; com a localidade `pt-BR`, `%.2f` escreveria `6,00`.

## 13

**Conceitos:** recursão, funções de ordem superior, ausência de efeitos colaterais (Aula14 p.10–20).

<!-- teste: saida-contem="10\n220" -->
```clojure
(defn soma-digitos [n]
  (if (< n 10)
    n                                            ; caso base: um só dígito
    (+ (mod n 10) (soma-digitos (quot n 10)))))  ; último dígito + soma do resto

(println (soma-digitos 1234))                    ; 10

(println (reduce + (map (fn [x] (* x x))
                        (filter even? (range 1 11)))))   ; 4 + 16 + 36 + 64 + 100 = 220
```

- **(a)** `(soma-digitos 1234)` = 4 + `(soma-digitos 123)` = 4 + 3 + 2 + 1 = **10**. A recursão substitui o laço: não há variável acumuladora sendo reatribuída.
- **(b)** `range` gera 1…10; `filter even?` mantém 2, 4, 6, 8, 10; `map` eleva ao quadrado; `reduce +` soma: **220**.
- **(c)** Cada função recebe uma coleção e devolve **outra**, nova; nenhuma altera a original nem uma variável externa. O resultado depende só da entrada, então a expressão pode ser avaliada em qualquer ordem e sempre dá 220 — é a **transparência referencial**.

## 14

**Conceitos:** fatos, regras, conjunção, negação por falha, recursão (Aula15 p.14–23).

<!-- teste: consulta="(pode_cursar(ana, compiladores) -> A = sim ; A = nao), (pode_cursar(bruno, plp) -> B = sim ; B = nao), (depende(compiladores, algoritmos) -> C = sim ; C = nao)." saida-contem="A = nao|B = sim|C = sim" -->
```prolog
prerequisito(plp, algoritmos).
prerequisito(compiladores, plp).
prerequisito(compiladores, automatos).
aprovado(ana, algoritmos).
aprovado(ana, plp).
aprovado(bruno, algoritmos).

% (a) não existe pré-requisito de D em que o aluno NÃO tenha sido aprovado
pode_cursar(Aluno, Disciplina) :-
    \+ ( prerequisito(Disciplina, P), \+ aprovado(Aluno, P) ).

% (c) dependência direta ou indireta
depende(D, P) :- prerequisito(D, P).
depende(D, P) :- prerequisito(D, X), depende(X, P).
```

- **(a)** "Aprovado em **todos**" é escrito como "não existe nenhum pré-requisito sem aprovação". `\+` é a **negação por falha**: `\+ G` é verdadeiro quando `G` não pode ser provado (mundo fechado). **[Complemento]** O `\+` não aparece nos slides; o SWI-Prolog também oferece `forall(prerequisito(D, P), aprovado(A, P))`. Use a regra com os dois argumentos instanciados: com `Aluno` livre, a negação não gera respostas.
- **(b)** `pode_cursar(ana, compiladores)` → **false**: Ana foi aprovada em `plp`, mas não em `automatos`. `pode_cursar(bruno, plp)` → **true**: o único pré-requisito é `algoritmos`, e Bruno foi aprovado.
- **(c)** `depende(compiladores, algoritmos)` → **true**. A primeira cláusula falha (não há fato direto); a segunda encontra `prerequisito(compiladores, plp)` e prova `depende(plp, algoritmos)` pela primeira cláusula. A cláusula não recursiva vem **antes**, para a busca terminar.

## 15

**Conceitos:** comparação de paradigmas (Aulas 12, 14 e 15; Aula15 p.3–5).

**Orientado a objetos (Java)** — o dado e o comportamento ficam juntos na classe; o programador escreve **como** percorrer a turma:

<!-- teste: saida-contem="Ana\nCarla" -->
```java
import java.util.ArrayList;
import java.util.List;

class Aluno {
    private final String nome;
    private final double media;
    Aluno(String nome, double media) { this.nome = nome; this.media = media; }
    public String getNome() { return nome; }
    public boolean aprovado() { return media >= 6; }   // a regra pertence ao objeto
}

public class Main {
    public static void main(String[] args) {
        List<Aluno> turma = List.of(new Aluno("Ana", 8.0), new Aluno("Bruno", 5.5), new Aluno("Carla", 6.0));
        List<String> aprovados = new ArrayList<>();
        for (Aluno a : turma) {                        // passo a passo: imperativo
            if (a.aprovado()) aprovados.add(a.getNome());
        }
        aprovados.forEach(System.out::println);
    }
}
```

**Funcional (Clojure)** — uma composição de funções sobre dados imutáveis:

<!-- teste: saida-contem="Ana|Carla" -->
```clojure
(def turma [{:nome "Ana" :media 8.0} {:nome "Bruno" :media 5.5} {:nome "Carla" :media 6.0}])

(println (map :nome (filter #(>= (:media %) 6) turma)))   ; (Ana Carla)
```

**Lógico (Prolog)** — fatos e uma regra; o programador declara **o que** é um aprovado e pede todas as soluções:

<!-- teste: consulta="findall(N, aprovado(N), L)." saida-contem="L = [ana,carla]" -->
```prolog
aluno(ana, 8.0).
aluno(bruno, 5.5).
aluno(carla, 6.0).

aprovado(Nome) :- aluno(Nome, Media), Media >= 6.
```

| Paradigma | Como o problema é expresso | "Como" ou "o quê"? |
| --- | --- | --- |
| **OO** | Objetos `Aluno` com a regra `aprovado()`; um laço percorre a turma | **Como** (o laço é imperativo); a OO organiza o código, mas o algoritmo é descrito passo a passo |
| **Funcional** | `filter` + `map` compostos, sem variáveis alteradas | Mais próximo do **o quê**: descreve a transformação, e o laço fica dentro de `filter` |
| **Lógico** | Uma regra que **define** aprovado; `findall` reúne as soluções | **O quê**: o mecanismo de busca do Prolog decide como encontrar as respostas |

> **[Atenção]** A Aula15 (p.3–5) classifica o funcional como **procedural**, junto com o imperativo e a OO, e reserva o termo **declarativo** para o lógico. Boa parte da literatura põe o funcional entre os declarativos (ver a errata 31). Na prova, use a classificação do professor e, se houver espaço, cite a divergência.
