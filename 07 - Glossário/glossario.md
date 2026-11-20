# Glossário

> Termos da disciplina em ordem alfabética, com definição, exemplo e as aulas onde aparecem (links para os resumos). Termos marcados com **[Complemento]** não são definidos nos slides, mas aparecem nos enunciados das listas ou ajudam a entendê-los. Legenda: [Convenções](../README.md#convenções-de-marcação).

**Índice:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [L](#l) · [M](#m) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v)

**Total:** 95 termos.

## A

### Abstração

Processo de destacar o que é essencial e ocultar detalhes para lidar com a complexidade.

- **Exemplo:** Uma função `ordenarVetor` esconde **como** a ordenação é feita; uma classe `Pilha` esconde **como** os dados são guardados.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Abstração de dados

Agrupamento da representação de um tipo com as operações sobre ele, com a representação oculta dos clientes.

- **Exemplo:** Base do tipo abstrato de dados e da orientação a objetos. Ver **TDA**.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Abstração procedural (de processos)

Decomposição do problema em subprogramas, de modo que quem usa uma função conhece sua interface (entrada, saída, efeito), mas não sua implementação.

- **Exemplo:** Característica principal do paradigma imperativo; obtida por refinamento sucessivo.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

### Acoplamento

Grau de dependência entre módulos de um programa. O desejável é **baixo** acoplamento.

- **Exemplo:** Funções que leem e alteram as mesmas variáveis globais estão fortemente acopladas.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md)

### Alocação dinâmica

Reserva de memória em **tempo de execução**, no heap, com tamanho que pode variar.

- **Exemplo:** `int *v = new int[n];` em C++; liberação com `delete[] v;`.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)

### Alocação estática

Reserva de memória definida em **tempo de compilação**, com tamanho fixo.

- **Exemplo:** Variáveis globais e locais `static` ficam no segmento estático.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)

### Análise léxica

Fase da compilação que lê os caracteres do fonte e os agrupa em **tokens**.

- **Exemplo:** `soma = x + 10;` → identificador, símbolo `=`, identificador, operador `+`, constante, `;`.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) · [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Análise sintática

Fase da compilação que verifica se a sequência de tokens forma construções válidas da gramática, produzindo a árvore sintática.

- **Exemplo:** `x = (y + 10 * z;` passa pela análise léxica e falha na sintática.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) · [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Arquitetura de von Neumann

Arquitetura em que dados e instruções ficam na **mesma memória**, separada da CPU, com execução sequencial de instruções.

- **Exemplo:** O paradigma imperativo é uma abstração dela: variáveis = células de memória; atribuição = transferência entre CPU e memória.
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Atribuição

Comando que avalia uma expressão e grava o resultado em uma variável (`destino = expressão`).

- **Exemplo:** Central no imperativo; ausente no modelo funcional puro.
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

## B

### Backtracking

Mecanismo pelo qual o Prolog, ao falhar um objetivo, volta à última escolha e tenta a próxima alternativa. **[Complemento]**

- **Exemplo:** Permite que `pai(joao, X)` devolva `X = ana`, depois `X = maria`…
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

### BNF (Backus-Naur Form)

Notação formal para descrever a sintaxe concreta de linguagens por meio de regras de produção (gramáticas livres de contexto).

- **Exemplo:** `<atrib> ::= <id> = <expr>`.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Bytecode

Código intermediário, independente de plataforma, gerado pelo compilador Java (`.class`) e executado pela JVM.

- **Exemplo:** Chave da implementação híbrida e da portabilidade de Java.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

## C

### Classe

Definição de um tipo que agrupa atributos (estado) e métodos (comportamento); molde a partir do qual objetos são criados.

- **Exemplo:** `class Pilha { private int topo; void push(int x) {…} }`.
- **Aulas:** [07](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Classe abstrata

Classe que não pode ser instanciada e pode conter métodos sem implementação, a serem definidos pelas subclasses.

- **Exemplo:** `abstract class Conta { abstract double saldo(); }`.
- **Aulas:** [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Clojure

Linguagem funcional impura, dialeto de LISP, executada sobre a JVM; usada na disciplina.

- **Exemplo:** `(+ 1 2)` vale 3; `(/ 10 4)` vale `5/2`.
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Coerção

Conversão de tipo **implícita**, feita automaticamente pela linguagem. Enfraquece a tipagem.

- **Exemplo:** Em C, `int r = 2.5 + 3;` dá 5; em PHP, `10 + "20"` dá 30.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)

### Coesão

Grau em que os elementos de um módulo contribuem para uma única responsabilidade. O desejável é **alta** coesão.

- **Exemplo:** Uma classe `Aluno` só com dados e operações de aluno tem alta coesão.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md)

### Coleta de lixo (garbage collection)

Liberação automática da memória de objetos que não são mais referenciados.

- **Exemplo:** Java usa coleta de lixo; C++ exige `delete`.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Compilação

Tradução de todo o programa-fonte, antes da execução, para código de máquina de uma plataforma.

- **Exemplo:** C, C++, Fortran, Pascal. Execução rápida, executável preso à plataforma.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

### Constante nomeada

Identificador associado a um valor que não pode ser alterado depois da vinculação.

- **Exemplo:** `const int MAX = 10;` em C; `final int MAX = 10;` em Java.
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)

### Construtor

Método especial executado na criação de um objeto, para inicializar seu estado.

- **Exemplo:** `Pilha() { topo = -1; }`.
- **Aulas:** [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Consulta (Prolog)

Pergunta feita à base de fatos e regras; o Prolog responde com `true`/`false` ou com valores para as variáveis.

- **Exemplo:** `?- pai(X, ana).` → `X = joao.`
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

## D

### Declarativa (abordagem)

Abordagem em que o programador especifica **o que** deseja obter, e não os passos para obtê-lo.

- **Exemplo:** Paradigma lógico; SQL e HTML são linguagens declarativas que não são de programação.
- **Aulas:** [02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md) · [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

### Destrutor

Método especial executado quando um objeto é destruído, usado para liberar recursos.

- **Exemplo:** `~Pilha()` em C++, que libera os nós alocados com `new`.
- **Aulas:** [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

## E

### Efeito colateral

Alteração de estado observável fora da função (variável global, parâmetro, E/S) além do valor retornado.

- **Exemplo:** Ausente nas funções puras do paradigma funcional.
- **Aulas:** [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md) · [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Encapsulamento

Agrupamento de dados e operações relacionados em uma unidade, com controle de acesso que oculta os detalhes internos.

- **Exemplo:** Atributos `private` e métodos `public` em uma classe.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Enumeração

Tipo composto cujos valores são uma lista finita de constantes nomeadas.

- **Exemplo:** `enum Dia {SEG, TER, QUA};`.
- **Aulas:** [07](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)

### Escopo

Trecho do programa em que um nome é **visível** (pode ser referenciado).

- **Exemplo:** Variável local é visível só no bloco onde foi declarada.
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)

### Escopo dinâmico

Regra que resolve nomes não locais pela **sequência de chamadas** em execução.

- **Exemplo:** APL, LISP antigo; Perl com `local`. Prejudica a legibilidade.
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)

### Escopo estático (léxico)

Regra que resolve nomes não locais pela **posição no texto** do programa (ancestral textual), em tempo de compilação.

- **Exemplo:** C, Java, Pascal.
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)

## F

### Fato (Prolog)

Proposição assumida como verdadeira na base de conhecimento.

- **Exemplo:** `pai(joao, ana).`
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

### Forma funcional

Função que recebe funções como argumento e/ou devolve uma função, permitindo construir funções complexas.

- **Exemplo:** `map`, `reduce`, `comp` em Clojure.
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Função pura

Função cujo resultado depende apenas dos argumentos e que não produz efeitos colaterais. **[Complemento]**

- **Exemplo:** `(defn dobro [x] (* 2 x))`.
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

## G

### Goto

Comando de desvio incondicional para um rótulo. Base da programação não estruturada.

- **Exemplo:** Criticado por Dijkstra (1968) por destruir a correspondência entre texto e execução.
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [artigo de Dijkstra](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)

## H

### Heap

Região de memória para dados alocados dinamicamente, sem nome, acessados por ponteiros.

- **Exemplo:** Objetos Java e dados criados com `new`/`malloc`.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)

### Herança

Mecanismo pelo qual uma classe (subclasse) reaproveita atributos e métodos de outra (superclasse) e pode estendê-los.

- **Exemplo:** `class ContaEspecial extends Conta`.
- **Aulas:** [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Herança múltipla

Herança de mais de uma superclasse. Aumenta o reuso, mas traz complexidade e ambiguidades.

- **Exemplo:** Permitida em C++ (`class Multifuncional : public Impressora, public Scanner`); não em Java.
- **Aulas:** [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

## I

### Identificador

Nome usado para designar variáveis, funções, tipos etc., formado segundo as regras léxicas da linguagem.

- **Exemplo:** Em C, começa com letra ou `_`; diferencia maiúsculas de minúsculas.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Implementação híbrida

Compilação do fonte para um código intermediário, que é então interpretado (ou compilado com JIT) por uma máquina virtual.

- **Exemplo:** Java (JVM), C# (CLR).
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

### Imutabilidade

Propriedade de um valor que não pode ser alterado depois de criado. **[Complemento]**

- **Exemplo:** No funcional puro, "alterar" um valor significa criar outro.
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Índices textual e dinâmico

Coordenadas que, segundo Dijkstra, descrevem o progresso de um processo: posição no texto e contagem de repetições/chamadas.

- **Exemplo:** O `goto` livre impede definir essas coordenadas.
- **Aulas:** [artigo de Dijkstra](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) · [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md)

### Interface (Java)

Tipo que define um contrato (assinaturas de métodos e constantes) que as classes implementam com `implements`.

- **Exemplo:** `class Multifuncional implements Impressora, Scanner`.
- **Aulas:** [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Interpretação pura

Execução do programa por um interpretador, que traduz e executa cada instrução durante a execução.

- **Exemplo:** Python, JavaScript, PHP (classificação da disciplina). Portável, mais lenta.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

## J

### JIT (Just-In-Time)

Compilação, durante a execução, de trechos do código intermediário para código de máquina. **[Complemento]**

- **Exemplo:** Usada pela JVM e pela CLR para melhorar o desempenho.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

## L

### Lexema

Sequência concreta de caracteres do fonte que corresponde a um token.

- **Exemplo:** `soma1`, `10`, `+`.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Linguagem multiparadigma

Linguagem que suporta construções de mais de um paradigma. **[Complemento]**

- **Exemplo:** C++ (imperativo e OO), Python, Scala.
- **Aulas:** [02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md)

## M

### Máquina virtual

Software que executa um código intermediário, simulando uma máquina; é implementado para cada plataforma.

- **Exemplo:** JVM, CLR.
- **Aulas:** [03](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)

### Matriz (array)

Tipo composto homogêneo, cujos elementos são acessados por índices.

- **Exemplo:** `float notas[2][4][3];`. Em C, armazenada por linhas (*row-major*).
- **Aulas:** [07](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)

### Método

Operação definida em uma classe, que atua sobre o estado do objeto.

- **Exemplo:** `pilha.push(5)`.
- **Aulas:** [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Modificadores de acesso

Palavras que controlam a visibilidade de membros de uma classe: `public`, `private`, `protected`.

- **Exemplo:** Atributos `private`; interface `public`.
- **Aulas:** [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Mundo fechado (hipótese)

Suposição de que tudo o que não pode ser provado a partir da base é falso. **[Complemento]**

- **Exemplo:** Se não há fato `homem(pedro)`, a consulta `homem(pedro).` responde `false`.
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

## O

### Objeto

Instância de uma classe, com estado próprio, criada em tempo de execução.

- **Exemplo:** `Pilha p = new Pilha();`.
- **Aulas:** [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Overflow (estouro)

Resultado de uma operação que excede a faixa de valores representável pelo tipo.

- **Exemplo:** `INT_MAX + 1` em C resulta em valor negativo.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)

## P

### Palavra reservada

Palavra da linguagem que **não pode** ser usada como identificador.

- **Exemplo:** `int`, `while`, `class` em C/Java.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Paradigma de programação

Modelo ou estilo de pensamento sobre como estruturar e resolver problemas com computador.

- **Exemplo:** Imperativo, orientado a objetos, funcional, lógico.
- **Aulas:** [02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md)

### Paradigma funcional

Paradigma baseado em funções matemáticas, em que o programa é uma composição de funções, sem estado mutável no modelo puro.

- **Exemplo:** Haskell (pura); LISP, Clojure (impuras).
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Paradigma imperativo

Paradigma em que o programa é uma sequência de comandos que alteram o estado da memória.

- **Exemplo:** C, Pascal, Fortran.
- **Aulas:** [02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md) · [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md)

### Paradigma lógico

Paradigma declarativo baseado em lógica de predicados: o programa é um conjunto de fatos e regras, e a execução responde a consultas.

- **Exemplo:** Prolog.
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

### Paradigma orientado a objetos

Paradigma em que o programa é um conjunto de objetos que encapsulam estado e comportamento e trocam mensagens.

- **Exemplo:** Java, C++, C#, Smalltalk.
- **Aulas:** [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) · [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Parâmetro formal / real

Formal: o declarado no cabeçalho do subprograma. Real (argumento): o valor ou variável passado na chamada.

- **Exemplo:** Em `void f(int x)` e `f(5)`, `x` é formal e `5` é real.
- **Aulas:** [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

### Passagem por referência

O subprograma recebe o **endereço** do argumento; alterações no formal afetam o real imediatamente.

- **Exemplo:** C++ `&`, C# `ref`, C com ponteiros.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) · [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

### Passagem por resultado

O formal é uma variável local não inicializada, cujo valor é copiado para o real no retorno (semântica de saída).

- **Exemplo:** Semântica do `out` do C#.
- **Aulas:** [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

### Passagem por valor

O formal recebe uma **cópia** do valor do real (semântica de entrada); alterações não afetam o real.

- **Exemplo:** Padrão em C e para primitivos em Java.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md) · [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

### Passagem por valor-resultado

O formal recebe uma cópia do real na entrada e seu valor final é copiado de volta no retorno.

- **Exemplo:** Entrada e saída por cópia.
- **Aulas:** [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

### Pilha (região de memória)

Região onde ficam variáveis locais, parâmetros e endereços de retorno; cresce e diminui com as chamadas.

- **Exemplo:** As locais de `main` e de cada função chamada.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)

### Polimorfismo dinâmico

Escolha, em tempo de execução, da versão de um método sobrescrito, de acordo com o tipo real do objeto (vinculação tardia).

- **Exemplo:** `Conta c = new ContaEspecial(); c.tipo();` chama a versão de `ContaEspecial`.
- **Aulas:** [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Polimorfismo estático

Escolha, em tempo de compilação, entre versões de um método ou operador com o mesmo nome e parâmetros diferentes (sobrecarga).

- **Exemplo:** `soma(int, int)` e `soma(double, double)`.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) · [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Ponteiro

Variável que armazena um **endereço de memória**.

- **Exemplo:** `int *p = &x; *p = 10;` altera `x`.
- **Aulas:** [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)

### Procedural (abordagem)

Abordagem em que o programador especifica os **passos** que levam à solução.

- **Exemplo:** Na classificação do professor: imperativo, OO e funcional.
- **Aulas:** [02](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md) · [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

### Programação estruturada

Programação que usa apenas sequência, seleção e repetição em blocos, além de subprogramas, dispensando o `goto`.

- **Exemplo:** Fundamentada por Böhm e Jacopini (1966) e Dijkstra (1968).
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) · [artigo de Dijkstra](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md)

### Prolog

Principal linguagem do paradigma lógico, baseada em cláusulas de Horn e unificação.

- **Exemplo:** `avo(X, Z) :- pai(X, Y), pai(Y, Z).`
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

## R

### Ratio

Tipo numérico de Clojure (na JVM) que representa frações exatas.

- **Exemplo:** `(/ 7 2)` → `7/2`; `(quot 7 2)` → 3.
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md)

### Recursão

Definição de uma função em termos dela mesma; substitui os laços no funcional e no lógico.

- **Exemplo:** `(defn fat [n] (if (<= n 1) 1 (* n (fat (- n 1)))))`.
- **Aulas:** [14](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) · [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

### Registro (struct)

Tipo composto heterogêneo, com campos nomeados de tipos possivelmente diferentes.

- **Exemplo:** `struct Aluno { char nome[50]; float nota; };`.
- **Aulas:** [07](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)

### Regra (Prolog)

Cláusula que define uma relação a partir de outras: a cabeça é verdadeira se o corpo for.

- **Exemplo:** `avo(X, Z) :- pai(X, Y), pai(Y, Z).`
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

## S

### Semântica

Significado dos construtos de uma linguagem.

- **Exemplo:** `x = x + 1` significa: ler `x`, somar 1, gravar em `x`.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) · [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)

### Semântica estática / dinâmica

Estática: regras verificáveis na compilação (tipos, declarações). Dinâmica: comportamento durante a execução.

- **Exemplo:** Declarar `int` e atribuir string é erro de semântica estática em Java.
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md)

### Sintaxe

Forma (estrutura) dos programas de uma linguagem.

- **Exemplo:** Três níveis: léxica, concreta e abstrata.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Sintaxe abstrata

Representação da estrutura essencial do programa, sem detalhes como pontuação.

- **Exemplo:** Árvore sintática abstrata de `x + 10 * z`.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Sintaxe concreta

Regras que definem como os tokens se combinam em comandos válidos.

- **Exemplo:** Descrita por BNF.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Sobrecarga

Definição de vários métodos ou operadores com o mesmo nome e parâmetros diferentes.

- **Exemplo:** `+` em Java soma números e concatena strings.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) · [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Sobrescrita

Redefinição, na subclasse, de um método herdado com a mesma assinatura.

- **Exemplo:** `@Override String tipo()` em `ContaEspecial`.
- **Aulas:** [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)

### Subprograma

Unidade de código com nome, parâmetros e corpo, chamada a partir de outros pontos: procedimento (sem retorno) ou função (com retorno).

- **Exemplo:** Mecanismo da abstração procedural.
- **Aulas:** [11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md)

## T

### TDA (tipo abstrato de dados)

Tipo definido pelo programador cuja representação é oculta e que só é manipulado por suas operações.

- **Exemplo:** Pilha com `push`, `pop`, `vazia`, independente de vetor ou lista.
- **Aulas:** [10](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md)

### Tempo de vida

Período da execução em que uma variável está vinculada a uma célula de memória.

- **Exemplo:** Uma local `static` em C tem escopo local e tempo de vida do programa inteiro.
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) · [08](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md)

### Tipagem estática / dinâmica

Estática: o tipo é vinculado na compilação e não muda. Dinâmica: o tipo é vinculado na execução, conforme o valor.

- **Exemplo:** Estática: C, Java. Dinâmica: Python, PHP.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)

### Tipagem forte / fraca

Força da tipagem: quanto a linguagem recusa operações entre tipos diferentes. A coerção a enfraquece.

- **Exemplo:** Forte: Java, Python. Fraca: C, PHP.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)

### Tipo

Conjunto de valores e de operações aplicáveis a eles.

- **Exemplo:** `int`: inteiros e operações aritméticas.
- **Aulas:** [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md)

### Tipo composto

Tipo construído a partir de outros tipos.

- **Exemplo:** Enumerações, registros, matrizes, strings, classes.
- **Aulas:** [07](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md)

### Token

Categoria de lexemas que seguem um mesmo padrão.

- **Exemplo:** Identificador, palavra reservada, constante, string, símbolo especial, operador (os seis grupos de C).
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md)

### Turing-completude

Capacidade de uma linguagem de expressar todos os algoritmos computáveis.

- **Exemplo:** Imperativo: basta ter variáveis, inteiros, aritmética, atribuição, sequência, condição e desvio.
- **Aulas:** [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md)

## U

### Unificação

Processo de tornar dois termos idênticos, encontrando valores para as variáveis.

- **Exemplo:** `pai(X, ana)` unifica com `pai(joao, ana)` com `X = joao`.
- **Aulas:** [15](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md)

## V

### Variável

Abstração de uma célula de memória, caracterizada por seis atributos: nome, endereço, valor, tipo, tempo de vida e escopo.

- **Exemplo:** `int x = 10;`.
- **Aulas:** [04](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) · [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) · [09](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md)

### Vinculação (binding)

Associação entre uma entidade e um atributo (nome–endereço, variável–tipo, chamada–método), em um momento determinado.

- **Exemplo:** Em tempo de compilação (estática) ou de execução (dinâmica).
- **Aulas:** [05](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) · [06](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) · [13](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md)
