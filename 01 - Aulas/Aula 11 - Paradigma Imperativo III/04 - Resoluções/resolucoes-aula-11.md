# Aula 11 — Paradigma Imperativo III · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-11.md`](../03%20-%20Exercícios/exercicios-aula-11.md). C++ e Java foram compilados e executados. O C# (E8) foi analisado sem execução, porque não há compilador C# no ambiente de validação; sua lógica é a mesma da versão C++ testada no E9.

## E1

| | Procedimento | Função |
| --- | --- | --- |
| Retorna valor? | Não | Sim |
| C++ | `void hipotenusaP(double c1, double c2)` | `double hipotenusaF(double c1, double c2)` |
| Pascal | `procedure hipotenusaP(c1, c2: real);` | `function hipotenusaF(c1, c2: real): real;` |

## E2

1. Um único ponto de entrada.
2. A unidade chamadora fica suspensa durante a execução.
3. O controle volta à chamadora quando o subprograma termina.
4. A chamada é a requisição de execução.

## E3

**Resposta: c.** Com `out`, o argumento não precisa estar inicializado, e o método **deve** atribuir. `ref` permite mas não obriga; `in` e `ref readonly` proíbem a atribuição.

## E4

- **Formal:** o que está na **declaração** — `x` e `y` em `int elevado(int x, int y = 2)`.
- **Real (argumento):** o que está na **chamada** — `base` e `expo` em `elevado(base, expo)`.
- A associação é **posicional**: `base` → `x`, `expo` → `y`. Em `elevado(base)`, `y` assume o padrão 2.

## E5

- **Padrões no fim:** a associação é por posição. Se um parâmetro com padrão viesse antes de um sem padrão, não daria para omitir o primeiro sem ambiguidade. Em `f(int a = 1, int b)`, a chamada `f(5)` não diz se 5 é `a` ou `b`.
- **Nomeados:** na assinatura da p.12, o `*` depois de `activation` torna todos os parâmetros seguintes **somente nomeados**: a própria biblioteca obriga a escrever `MLPClassifier(max_iter=500)`. Em funções sem esse `*`, a chamada posicional exigiria repetir todos os parâmetros anteriores ao que se quer mudar. Com nomes, basta `MLPClassifier(max_iter=500)`. Além disso, a chamada se autodocumenta.

## E6

| Modelo | Direção | Cópia? | Custo / risco |
| --- | --- | --- | --- |
| Valor | Entrada | Sim (real → formal) | Espaço e tempo da cópia; lento para matrizes |
| Resultado | Saída | Sim (formal → real, no fim) | Idem; o formal começa sem valor |
| Valor-resultado | Entrada e saída | Sim, duas cópias | Idem, em dobro |
| Referência | Entrada e saída | Não: passa o endereço | Acesso mais lento (indireção); alterações inadvertidas no real; *aliasing* |

## E7

Chamada `p(a, a)` com `a = 2`:

**(a) Por valor:** `x` e `y` são cópias. As alterações ficam nas cópias, e **a = 2**.

**(b) Por referência:** `x` e `y` são **o próprio** `a`.
- `x = x + 1` → a = 3.
- `y = y * 10` → a = 30.
- **a = 30**.

**(c) Valor-resultado, copiando x e depois y:**
- Entrada: x = 2, y = 2.
- Corpo: x = 3, y = 20.
- Saída: a ← x (3); depois a ← y (20). **a = 20**.

O caso (c) mostra que valor-resultado e referência, ambos "entrada e saída", dão resultados **diferentes** quando há *aliasing*.

<!-- teste: saida-contem="valor: 2|referencia: 30|valor-resultado: 20" -->
```cpp
#include <iostream>

void por_valor(int x, int y)       { x = x + 1; y = y * 10; }
void por_referencia(int &x, int &y) { x = x + 1; y = y * 10; }

// Valor-resultado simulado: copia na entrada, trabalha nas cópias e copia de volta no fim
void por_valor_resultado(int &rx, int &ry) {
    int x = rx, y = ry;          // entrada (cópias)
    x = x + 1; y = y * 10;       // corpo
    rx = x;                      // saída: primeiro x...
    ry = y;                      // ...depois y
}

int main() {
    int a = 2; por_valor(a, a);           std::cout << "valor: " << a << "\n";
    a = 2;     por_referencia(a, a);      std::cout << "referencia: " << a << "\n";
    a = 2;     por_valor_resultado(a, a); std::cout << "valor-resultado: " << a << "\n";
    return 0;
}
```

## E8 — Atividade 1 (original, p.21)

<!-- teste: entrada="3\n7" saida-contem="a = 3, b = 7|a = 7, b = 3" -->
```csharp
using System;

class Program {
    // out: o argumento não precisa estar inicializado e o método DEVE atribuir.
    //      Modelo semântico: SAÍDA (por resultado, implementado por referência).
    static void LerValores(out int a, out int b) {
        Console.Write("Primeiro numero: ");
        a = int.Parse(Console.ReadLine());
        Console.Write("Segundo numero: ");
        b = int.Parse(Console.ReadLine());
    }

    // ref: o argumento já tem valor, e o método o lê E o altera.
    //      Modelo semântico: ENTRADA E SAÍDA (por referência).
    static void Inverter(ref int a, ref int b) {
        int temp = a;
        a = b;
        b = temp;
    }

    // in: o argumento já tem valor, e o método só pode ler.
    //     Modelo semântico: ENTRADA (por referência somente leitura, sem cópia).
    static void Imprimir(in int a, in int b) {
        Console.WriteLine($"a = {a}, b = {b}");
    }

    static void Main() {
        int x, y;                  // não inicializados: permitido por causa do out
        LerValores(out x, out y);
        Imprimir(in x, in y);
        Inverter(ref x, ref y);
        Imprimir(in x, in y);
    }
}
```

**Descrição da passagem, por função:**

| Função | Modificador | Por quê |
| --- | --- | --- |
| `LerValores` | `out` | Só **produz** valores; dispensa inicializar `x` e `y` antes |
| `Inverter` | `ref` | Precisa **ler** os valores atuais e **alterá-los** no chamador |
| `Imprimir` | `in` | Só **lê**; o compilador impede alteração. `ref readonly` também atenderia |

**Erro comum:** usar `ref` em `LerValores`. Compilaria só se `x` e `y` fossem inicializados antes, e não expressaria a intenção de "saída".

## E9

<!-- teste: entrada="3 8" saida-contem="a = 3, b = 8|a = 8, b = 3" -->
```cpp
#include <iostream>

void lerValores(int &a, int &b) {             // ~ out: escreve no chamador
    std::cin >> a >> b;
}

void inverter(int &a, int &b) {               // ~ ref: lê e altera
    int temp = a;
    a = b;
    b = temp;
}

void imprimir(const int &a, const int &b) {   // ~ in / ref readonly: só lê, sem cópia
    std::cout << "a = " << a << ", b = " << b << "\n";
}

int main() {
    int x, y;
    lerValores(x, y);
    imprimir(x, y);
    inverter(x, y);
    imprimir(x, y);
    return 0;
}
```

| C++ | C# equivalente |
| --- | --- |
| `int&` usado só para escrever | `out` (C++ não obriga a escrever) |
| `int&` para ler e escrever | `ref` |
| `const int&` | `in` / `ref readonly` |

Em C++, a referência não aparece na **chamada** (`inverter(x, y)`). Em C#, `ref` aparece também na chamada — uma vantagem de legibilidade.

## E10

**Indireção** é acessar um dado em **dois passos**: primeiro ler o endereço guardado no parâmetro, depois ir àquele endereço buscar o valor. Na passagem **por valor**, o dado já está no próprio parâmetro, um passo só. Por isso:

- **passar** por referência é rápido: copia-se só um endereço, de tamanho fixo;
- **usar** o parâmetro dentro da função é um pouco mais lento: cada leitura ou escrita passa pelo endereço (p.17).

Para estruturas grandes, a economia na passagem compensa de longe o custo da indireção.

## E11

<!-- teste: saida-contem="soma dos pares = 30" -->
```java
public class Main {
    static int somaPares(int[] v) {
        int soma = 0;                         // VARIÁVEL + ATRIBUIÇÃO
        for (int i = 0; i < v.length; i++) { // REPETIÇÃO
            if (v[i] % 2 == 0) {              // DECISÃO
                soma = soma + v[i];           // ATRIBUIÇÃO (destino = expressão)
            }
        }
        return soma;
    }

    public static void main(String[] args) {
        System.out.println("soma dos pares = " + somaPares(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
    }
}
```

O método está dentro de uma classe (organização OO), mas o corpo é puramente imperativo: variáveis, atribuição, decisão e repetição. É o que a [Aula 14](../../Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) reforça: a OO muda a organização, não os comandos.
