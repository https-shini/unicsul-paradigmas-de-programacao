# Aula 13 — Paradigma Orientado a Objetos II · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-13.md`](../03%20-%20Exercícios/exercicios-aula-13.md). Os programas C++ e Java foram compilados e executados; o erro de ambiguidade do E9 foi reproduzido.

## E1

Herança é o mecanismo pelo qual uma classe (subclasse) é declarada a partir de outra (superclasse) e **herda suas variáveis e métodos**, possibilitando a reutilização de código. Normalmente representa uma associação **"é-um/é-uma"** (p.4).

## E2

1. Não tem acesso aos membros **privados** da superclasse.
2. Pode **adicionar** membros.
3. Pode **modificar o comportamento** de métodos herdados (p.5).

## E3

**Resposta: c.** Java e C# têm herança simples; C++ e Python, múltipla (p.6).

## E4

- **Estático (sobrecarga):** mesmo nome, parâmetros diferentes; o **compilador** escolhe pela assinatura.
- **Dinâmico (sobrescrita):** a subclasse redefine o método; a escolha ocorre **em execução**, pelo tipo real do objeto (ligação tardia).

<!-- teste: saida-contem="int: 5|double: 5.5|Cachorro: au au" -->
```java
class Animal {
    String som() { return "..."; }
}

class Cachorro extends Animal {
    @Override
    String som() { return "au au"; }              // SOBRESCRITA (dinâmico)
}

public class Main {
    static String soma(int a, int b)       { return "int: " + (a + b); }       // SOBRECARGA (estático)
    static String soma(double a, double b) { return "double: " + (a + b); }

    public static void main(String[] args) {
        System.out.println(soma(2, 3));           // compilador escolhe soma(int,int)
        System.out.println(soma(2.5, 3.0));       // compilador escolhe soma(double,double)
        Animal a = new Cachorro();                // referência do tipo base
        System.out.println("Cachorro: " + a.som());   // execução escolhe Cachorro.som()
    }
}
```

## E5

| | Classe abstrata | Interface Java |
| --- | --- | --- |
| Definição (slide) | Tem um ou mais métodos abstratos; não pode ser instanciada; as derivadas implementam os abstratos | Extensão do conceito: sem variáveis, construtores ou métodos não abstratos |
| Atributos | Sim | Só constantes (`public static final`) |
| Construtor | Sim | Não |
| Métodos com corpo | Sim | Desde o Java 8: `default` e `static` |
| Uma classe pode ter… | Uma superclasse | Várias interfaces |

**Quando usar:** classe abstrata quando há **estado e código comuns** a compartilhar (como a `Conta`); interface quando se quer só um **contrato** que classes não relacionadas podem cumprir (`Impressora`, `Scanner`).

## E6

| Par | Relação | Teste |
| --- | --- | --- |
| a) Gerente e Funcionário | **Herança** | Gerente **é um** funcionário |
| b) Carro e Roda | **Composição** | Carro **tem** rodas; carro não é roda |
| c) ContaEspecial e Conta | **Herança** | Conta especial **é uma** conta |
| d) Pilha e Nodo | **Composição** | Pilha **tem** nós (`Nodo topo`) |

## E7

```text
Estou imprimindo um documento.
Estou digitalizando um documento.
Estou copiando um documento
******
Estou digitalizando um documento.
Estou imprimindo um documento.
******
```

As duas primeiras linhas vêm das chamadas diretas aos métodos herdados. O bloco seguinte vem de `copieDocumento()`, que imprime sua mensagem e os asteriscos e chama os dois métodos herdados — primeiro digitalizar, depois imprimir. Repare que só a mensagem de cópia não tem ponto final.

## E8 — Atividade 1 (original, p.10–11)

**Alterações estruturais:**

1. Java não permite herança múltipla de **classes**. `Impressora` e `Scanner` viram **interfaces**.
2. `Multifuncional` passa a `implements Impressora, Scanner` em vez de herdar de duas classes.
3. Como as interfaces só declaram os métodos, `Multifuncional` precisa **implementá-los**.
4. **[Complemento]** Não importe `java.util.Scanner` explicitamente no mesmo arquivo, porque é erro de compilação. Renomear a interface evita a confusão.

<!-- teste: saida-contem="Estou imprimindo um documento.\nEstou digitalizando um documento.\nEstou copiando um documento\n******\nEstou digitalizando um documento.\nEstou imprimindo um documento.\n******" -->
```java
interface Impressora {
    void imprimaDocumento();
}

interface Scanner {
    void digitalizeDocumento();
}

class Multifuncional implements Impressora, Scanner {
    @Override
    public void imprimaDocumento() {                     // implementação obrigatória
        System.out.println("Estou imprimindo um documento.");
    }

    @Override
    public void digitalizeDocumento() {                  // implementação obrigatória
        System.out.println("Estou digitalizando um documento.");
    }

    public void copieDocumento() {
        System.out.println("Estou copiando um documento");
        System.out.println("******");
        digitalizeDocumento();
        imprimaDocumento();
        System.out.println("******");
    }
}

public class Main {
    public static void main(String[] args) {
        Multifuncional hp3000 = new Multifuncional();
        hp3000.imprimaDocumento();
        hp3000.digitalizeDocumento();
        hp3000.copieDocumento();
    }
}
```

**Variante com métodos `default` (Java 8+) [Complemento]** — recupera o reuso, porque o código fica na interface:

<!-- teste: saida-contem="Estou imprimindo um documento.\nEstou digitalizando um documento.\nEstou copiando um documento" -->
```java
interface Impressora {
    default void imprimaDocumento() { System.out.println("Estou imprimindo um documento."); }
}

interface Scanner {
    default void digitalizeDocumento() { System.out.println("Estou digitalizando um documento."); }
}

class Multifuncional implements Impressora, Scanner {
    public void copieDocumento() {
        System.out.println("Estou copiando um documento");
        System.out.println("******");
        digitalizeDocumento();
        imprimaDocumento();
        System.out.println("******");
    }
}

public class Main {
    public static void main(String[] args) {
        Multifuncional hp3000 = new Multifuncional();
        hp3000.imprimaDocumento();
        hp3000.digitalizeDocumento();
        hp3000.copieDocumento();
    }
}
```

## E9

Se as duas bases tiverem um método com o mesmo nome, a chamada pela classe derivada é **ambígua**:

<!-- teste: compilacao-falha="sim" erro-contem="ambiguous" -->
```cpp
#include <iostream>
class Impressora { public: void ligar() { std::cout << "Impressora ligada\n"; } };
class Scanner    { public: void ligar() { std::cout << "Scanner ligado\n"; } };
class Multifuncional : public Impressora, public Scanner { };

int main() {
    Multifuncional m;
    m.ligar();          // ERRO: request for member 'ligar' is ambiguous
    return 0;
}
```

**Solução:** qualificar com o operador de escopo `::`, ou redefinir `ligar()` em `Multifuncional` para decidir o que fazer:

<!-- teste: saida-contem="Impressora ligada\nScanner ligado" -->
```cpp
#include <iostream>
class Impressora { public: void ligar() { std::cout << "Impressora ligada\n"; } };
class Scanner    { public: void ligar() { std::cout << "Scanner ligado\n"; } };

class Multifuncional : public Impressora, public Scanner {
public:
    void ligar() {               // resolve o conflito explicitamente
        Impressora::ligar();
        Scanner::ligar();
    }
};

int main() {
    Multifuncional m;
    m.ligar();                   // agora não é ambíguo
    return 0;
}
```

## E10

<!-- teste: saida-contem="Retangulo: 6.00|Circulo: 3.14" -->
```java
import java.util.List;

abstract class Forma {
    abstract double area();                 // sem implementação: obriga as subclasses
    abstract String nome();
}

class Retangulo extends Forma {
    private final double largura, altura;
    Retangulo(double l, double a) { largura = l; altura = a; }
    double area() { return largura * altura; }
    String nome() { return "Retangulo"; }
}

class Circulo extends Forma {
    private final double raio;
    Circulo(double r) { raio = r; }
    double area() { return Math.PI * raio * raio; }
    String nome() { return "Circulo"; }
}

public class Main {
    public static void main(String[] args) {
        List<Forma> formas = List.of(new Retangulo(2, 3), new Circulo(1));
        for (Forma f : formas) {
            System.out.printf("%s: %.2f%n", f.nome(), f.area());   // <- LIGAÇÃO TARDIA aqui
        }
        // new Forma();  // não compila: Forma é abstrata
    }
}
```

**Ligação tardia:** em `f.area()`, o compilador só sabe que `f` é uma `Forma`. **Em execução**, a JVM verifica o objeto real (`Retangulo` ou `Circulo`) e chama a versão correspondente. Para acrescentar um `Triangulo`, basta criar a subclasse — o laço não muda. É a **extensibilidade** prometida pela OO.

## E11

- **Menos responsabilidades = alta coesão.** Cada classe faz uma coisa só, como no princípio da responsabilidade única da Aula 10. Uma classe coesa é mais fácil de **reutilizar** (não traz funções inúteis junto), de **estender** (a subclasse especializa um comportamento bem definido) e de **manter** (mudar uma responsabilidade mexe em um só lugar).
- **Classes "fracamente acopladas" = baixo acoplamento.** Os clientes dependem da interface, não da representação (pilha 1c/1d), então mudar a implementação não propaga alterações.

A OO oferece mecanismos — encapsulamento, interfaces, herança, polimorfismo — que **favorecem** essas duas propriedades, que a abstração procedural sozinha não favorecia (Aula 10, p.16).
