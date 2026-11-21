# Lista 02 — Revisão II · Resolução comentada

> **[Resolução elaborada]** Resolução produzida para estudo. **Não é gabarito oficial do professor.** Enunciados: [README da lista](../README.md) · original: [`Aula16b_ExRevisao2.pdf`](../01%20-%20Enunciado%20Original/Aula16b_ExRevisao2.pdf).
> Cada questão traz: **assunto**, **conceitos necessários**, **resposta-modelo** com fonte (`AulaXX p.N`) e, quando pertinente, **erros comuns**. Os trechos de código foram compilados e executados.

---

## Q1

**Assunto:** os quatro paradigmas. **Conceitos:** abordagem procedural/declarativa, unidade de modelagem. **Fontes:** Aula02 p.8–13; Aula15 p.3–5.

**Resposta-modelo:**

| Paradigma | Como modela o problema | Como resolve | Abordagem |
| --- | --- | --- | --- |
| **Imperativo** | Variáveis (estado na memória) e procedimentos | Sequência de **comandos** que alteram o estado — atribuição, seleção, repetição — no modelo de von Neumann. Principal característica: **abstração procedural** | Procedural |
| **Orientado a objetos** | **Objetos** que reúnem estado e comportamento, definidos por **classes** | Objetos **ativos trocam mensagens** (chamam métodos uns dos outros), com encapsulamento, herança e polimorfismo | Procedural |
| **Funcional** | **Funções matemáticas**, cada uma com domínio de entrada e resultado | **Composição** e aplicação de funções; no modelo puro, sem estado nem efeitos colaterais | Procedural (classificação do professor) |
| **Lógico** | **Fatos e regras** em lógica de predicados | O programador descreve **o que** quer; um **algoritmo de inferência** busca a solução por unificação | **Declarativo** |

Os três primeiros **especificam os passos** que levam à solução; o lógico especifica o resultado (Aula15 p.3).

## Q2

**Assunto:** implementação de linguagens. **Conceitos:** tradução, código intermediário, máquina virtual. **Fonte:** Aula03 p.7–15.

**Resposta-modelo:**

- **Compilação:** traduz **todo** o programa-fonte, antes da execução, para **código de máquina de uma plataforma específica**, salvo num executável (Fortran, C, C++, Pascal). Passa pelas fases léxica, sintática, semântica/código intermediário, otimização e geração de código. Execução **rápida**, mas o executável fica **preso à plataforma**.
- **Interpretação pura:** um **interpretador** simula a máquina em software e **traduz e executa** cada instrução ao mesmo tempo (Lisp, JavaScript, PHP, Python). **Portável** — basta o interpretador —, mas mais **lento**, porque re-decodifica as instruções a cada execução, e sem verificação estática.
- **Híbrida:** um compilador traduz o fonte para um **código intermediário** (bytecode Java, CIL do .NET), que é executado por um **interpretador** (Java, C#, VB.NET).
- **Papel do código intermediário e da VM:** o código intermediário é **independente de plataforma** e mais simples de interpretar que o fonte. A **máquina virtual** (JVM, CLR) é o interpretador desse código, implementado para cada sistema. O mesmo `.class` roda em qualquer plataforma com JVM — **portabilidade** com desempenho melhor que a interpretação pura, ainda maior com compilação JIT **[Complemento]**. A VM é um dos "computadores virtuais" em camadas da Fig. 1.2 de Sebesta (Aula03 p.15).

## Q3

**Assunto:** níveis de sintaxe. **Fonte:** Aula04 p.6–10.

**Resposta-modelo:**

- **Sintaxe léxica:** regras dos **símbolos básicos** — identificadores, literais, operadores, pontuação. Define como caracteres se agrupam em elementos válidos.
  - **Lexema:** sequência concreta de caracteres do fonte (`soma1`, `10`, `+`).
  - **Token:** classificação dos lexemas que seguem um padrão (identificador, constante, operador…).
  - **Padrão:** descrição da forma dos lexemas. C tem seis grupos de token: identificador, palavra reservada, constante, string, símbolo especial e operador.
- **Sintaxe concreta:** a representação **real** do programa, usando os tokens como alfabeto. Define como os tokens formam **comandos válidos** (`soma = x + 10;`). Exemplo-chave: `x = (y + 10 * z;` é **lexicamente válido**, porque todos os tokens existem, mas **sintaticamente inválido**, porque o parêntese não fecha.
- **Sintaxe abstrata:** considera só a **informação essencial** — a estrutura da árvore —, sem pontuação e parênteses, já representados pela forma da árvore.
- **Estruturação formal:** a léxica é descrita por expressões regulares/autômatos finitos, e a concreta, por **gramáticas livres de contexto** (BNF). O analisador léxico produz tokens, e o sintático os organiza em árvores (Aula03 p.9).

## Q4

**Assunto:** escopo. **Fonte:** Aula05 p.9–12.

**Resposta-modelo:**

- **Escopo estático (léxico):** a variável não local é resolvida pela **posição da declaração no texto**. Procura-se no bloco local; se não houver, no **ancestral textual** (bloco ou função que o envolve), até o mais abrangente; se não houver em nenhum, é erro. A resolução é feita em **tempo de compilação**.
- **Escopo dinâmico:** a resolução segue a **ordem de chamada dos subprogramas** em execução — o nome se refere à declaração mais recente na pilha de chamadas. Usado em APL e nos primeiros LISP; Perl e Common LISP o permitem.
- **Por que reduz legibilidade e confiabilidade:** com escopo dinâmico, a mesma função pode acessar variáveis **diferentes** conforme **quem a chamou**, e isso pode mudar de uma execução para outra. Lendo o código da função, não se sabe a que variável o nome se refere — é preciso simular a execução. Uma função também pode alterar, sem querer, variáveis do chamador.

<!-- teste: saida-contem="10" -->
```c
#include <stdio.h>
int n = 10;                         /* global */
void f(void) { printf("%d\n", n); } /* n não é local de f */
void g(void) { int n = 20; f(); }   /* g tem um n local */
int main(void) { g(); return 0; }   /* estático: imprime 10. Com escopo dinâmico, seria 20 */
```

## Q5

**Assunto:** tipagem. **Fonte:** Aula06 p.9–21.

**Resposta-modelo:**

- **Tipagem estática:** o tipo é definido na **declaração**, em tempo de compilação, e **não muda** (C/C++, Java, Ada). Erros de tipo são detectados **antes** da execução; o programa executa mais rápido e é mais fácil de ler.
- **Tipagem dinâmica:** o tipo é definido em **tempo de execução**, conforme o valor atribuído, e a mesma variável pode mudar de tipo (Perl, Python, PHP, JavaScript). É mais simples de escrever, mas os erros aparecem só em execução.
- **Força da tipagem** é outro eixo, **independente** do anterior: quanto **mais exigente** a linguagem com operações entre tipos diferentes, **mais forte**. A **coerção** (conversão implícita) **enfraquece** a tipagem, porque operações que deveriam ser erros passam silenciosamente; a exposição de ponteiros como valores numéricos também.
- **Exemplos:** em C, `int res = 2.5 + 3;` converte implicitamente e dá 5; Java recusa a compilação e exige `(int)`. PHP calcula `10 + "20" + 10.2 = 40.2`; Python lança `TypeError`.
- **Conclusão:** C é estática e mais fraca; Java é estática e forte; PHP é dinâmica e fraca; Python é dinâmica e forte.

<!-- teste: saida-contem="res = 5" -->
```c
#include <stdio.h>
int main(void) {
    double x = 2.5; int y = 3;
    int res = x + y;              /* coerção implícita: 5.5 -> 5 (em Java: erro de compilação) */
    printf("res = %d\n", res);
    return 0;
}
```

## Q6

**Assunto:** alocação de memória. **Fonte:** Aula08 p.3, p.12–14.

**Resposta-modelo:**

| | Alocação estática | Alocação dinâmica |
| --- | --- | --- |
| **Momento** | Definido antes da execução: o segmento estático é reservado na compilação/carga; os frames da pilha são criados a cada chamada, com tamanho fixado na compilação | Em execução, quando o programa pede (`new`/`malloc`) |
| **Tamanho** | Fixo, não pode ser alterado | Pode ser alterado |
| **Região** | **Segmento estático** (globais e `static`); locais e parâmetros na **pilha**, de tamanho conhecido | **Heap** |
| **Liberação** | Fim do programa (estático); fim da função (pilha) | Explícita (`delete`/`free`) ou coleta de lixo |

O slide (Aula08 p.13) trata a pilha junto com a alocação estática porque o **tamanho** de cada frame é conhecido na compilação, embora o frame só exista durante a chamada.

- **Regiões (Aula08 p.13):** código, estático, heap, memória livre e pilha. Heap e pilha crescem em direção à memória livre.
- **Relação com ponteiros:** a memória do heap **não tem nome**: `new`/`malloc` devolvem um **endereço**, que precisa ser guardado num **ponteiro**. Por isso estruturas dinâmicas — listas, pilhas, filas, árvores — são construídas com ponteiros, como a pilha encadeada com `Nodo* proximo` (Aula12). No Exemplo 4 da Aula08: `n`/`res` no segmento estático; `a`, `b`, `x`, `y` na pilha; a área criada com `new` (apontada por `vetor`) no heap — no slide, `new int(4)` cria um único `int`; o correto seria `new int[n]`.

## Q7

**Assunto:** imperativo e programação estruturada. **Fontes:** Aula09 p.8–22; artigo de Dijkstra (Aula09a).

**Resposta-modelo:**

- **Completude de Turing:** uma linguagem é completa quanto a Turing se tem recursos mínimos para expressar **todos os algoritmos concebíveis**. Uma linguagem imperativa é Turing-completa se tem **variáveis, números inteiros, operações aritméticas, atribuição, sequenciamento baseado em memória, condições e comandos de ramificação (`goto`)**.
- **Programação não estruturada:** controla o fluxo com `goto`/`jump` para números de linha ou rótulos (Assembly, BASIC). Repetição e seleção são construídas com saltos.
- **Transição para a estruturada:** Dijkstra, em *Go To Statement Considered Harmful* (1968), argumentou que:
  - com sequência, condicionais, procedimentos e laços, o progresso do processo é descrito por **índices textuais e dinâmicos** — coordenadas independentes do programador que permitem interpretar o valor das variáveis;
  - o `goto` livre **destrói** essa correspondência entre o **texto estático** do programa e o **processo dinâmico**, e resta só um contador de passos inútil.
- Por isso defendeu **abolir** o `goto` das linguagens de alto nível. A prova de que ele é logicamente dispensável é de **Böhm e Jacopini** (1966), citada no artigo.
- **Programação estruturada:** sequência, **seleção** e **repetição** em blocos, mais **subprogramas**. Facilita leitura e confiabilidade; a linguagem pode até suportar `goto`, mas o dispensa.

> **[Atenção]** O slide (Aula09 p.18) diz que Dijkstra "mostrou" que todo programa com `goto` pode ser reescrito com laços. O artigo não traz essa prova: ele a atribui a **Böhm e Jacopini (1966)**. Na resposta, cite Dijkstra como quem defendeu **abolir** o `goto` e Böhm–Jacopini como autores da prova (ver a errata 17).

## Q8

**Assunto:** abstração. **Fontes:** Aula10 p.4–18; Aula12 p.17–22.

**Resposta-modelo:**

- **Abstração de processos (procedural):** o programador se preocupa com a **interface** da função — entrada, saída, o que calcula — e ignora **como** ela calcula. O problema é decomposto em funções cada vez mais primitivas, até os comandos da linguagem. É a característica do imperativo e traz organização, reuso e bibliotecas.
- **Abstração de dados:** agrupa a **representação** de um tipo e as **operações** sobre ele, ocultando a representação. É a base da OO.
- **Acoplamento:** grau de dependência entre módulos; o desejável é **baixo**. Variáveis globais o elevam.
- **Coesão:** responsabilidade única de cada função ou classe; o desejável é **alta**.
- A abstração procedural **não favorece** baixo acoplamento nem alta coesão. **[Atenção]** O slide (Aula10 p.16) escreve "baixa coesão"; o conceito correto é que ela não favorece a **alta** coesão.
- **Papel do TDA:** permite declarar variáveis do tipo, **oculta a representação** (encapsulamento) e expõe só operações. Assim, (1) os clientes não alteram o estado indevidamente; (2) a representação pode mudar sem afetar os clientes, o que é baixo acoplamento — na pilha da Aula12, trocar vetor por lista encadeada não mudou o `main`; (3) cada TDA reúne uma responsabilidade, o que é alta coesão. O resultado é software mais fácil de **organizar e manter**.

## Q9

**Assunto:** passagem de parâmetros. **Fontes:** Aula11 p.13–19; Aula08 p.8–11.

**Resposta-modelo:**

| Modelo | Semântica | Memória | Efeito no argumento real |
| --- | --- | --- | --- |
| **Por valor** | **Entrada**: o formal é uma local inicializada com o valor do real | **Cópia** (mais espaço; lento para matrizes) | **Nenhum**: alterações ficam na cópia |
| **Por resultado** | **Saída**: o formal é uma local **não inicializada**, copiada para o real no fim | Cópia | O real recebe o valor final; o valor inicial é ignorado |
| **Por valor-resultado** | **Entrada e saída** por cópia: inicializa com o real e copia de volta no fim | **Duas cópias** | O real é atualizado só no **retorno**; com *aliasing*, o resultado depende da ordem das cópias |
| **Por referência** | **Entrada e saída** por **caminho** (endereço) | **Sem memória extra**, passagem rápida; acesso mais lento (indireção) | **Imediato**: o formal **é** o real, e alterações inadvertidas afetam o chamador (efeitos colaterais, *aliasing*) |

**Exemplos:** em C#, `Metodo1(int x)` é por valor e não altera `numero`; `Metodo2(ref int x)` é por referência e altera. `out` corresponde à semântica de saída, implementada por referência; `in` e `ref readonly`, a referência só para leitura. Em Java, primitivos são passados por valor, e objetos, por cópia da referência.

## Q10

**Assunto:** encapsulamento e memória em OO. **Fonte:** Aula12 p.18–30.

**Resposta-modelo:**

- **Encapsulamento:** mecanismo que agrupa dados (atributos) e operações (métodos) logicamente relacionados numa entidade — a classe — e, por **controle de acesso**, **oculta** os detalhes internos dos clientes.
- **Modificadores de acesso:**
  - `public`: qualquer classe acessa — em geral, os **métodos** que formam a interface.
  - `private`: só a própria classe — em geral, os **atributos**.
  - `protected`: a classe e suas derivadas.
- **Proteção do estado:** com atributos privados, o estado só muda pelas operações da classe (`push`/`pop`, get/set), que podem **validar** as alterações. Os clientes não corrompem o objeto, nem de propósito nem por acidente — confiabilidade, legibilidade e menos conflitos de nome.
- **Gerenciamento de memória dinâmica:**
  - **C++:** o programador é responsável. Objetos criados com `new` devem ser liberados com `delete`, que chama o **destrutor** (`~Pilha()`), onde a classe libera os recursos que alocou (os `Nodo`). Esquecer o `delete` causa vazamento de memória.
  - **Java:** **coleta de lixo automática** — objetos sem referência são recolhidos pela JVM. O programador não libera memória, ao custo de menos controle sobre quando isso ocorre.

## Q11

**Assunto:** herança e polimorfismo. **Fonte:** Aula13 p.4–13.

**Resposta-modelo:**

- **Herança simples:** a classe tem **uma** superclasse (Java, C#).
- **Herança múltipla:** a classe tem **várias** (C++, Python). Aumenta a reutilização, mas traz **complexidade e perda de eficiência**. **[Complemento]** Há também ambiguidade quando duas bases têm membros de mesmo nome e o problema do diamante. Exemplo: `class Multifuncional : public Impressora, public Scanner` em C++.
- **Interfaces em Java:** como alternativa, Java permite **implementar várias interfaces** — `class Multifuncional implements Impressora, Scanner`. A classe herda o **contrato** (métodos a implementar), não o código, e deve **implementar** os métodos (desde o Java 8, há métodos `default`).
- **Polimorfismo estático (sobrecarga):** mesmo nome de método com **parâmetros diferentes**; o **compilador** escolhe a versão pela assinatura. Também vale para operadores, como `+` com `int` ou `double`.
- **Polimorfismo dinâmico (sobrescrita com vinculação tardia):** a subclasse **redefine** um método herdado. Uma referência do tipo base (`Conta c`) pode apontar para qualquer derivada, e a versão chamada é decidida **em tempo de execução** pelo tipo **real** do objeto. Um único comando da classe base chama métodos de diferentes derivadas.

<!-- teste: saida-contem="sobrecarga int: 5|sobrescrita: Especial" -->
```java
class Conta { String tipo() { return "Conta"; } }
class ContaEspecial extends Conta { @Override String tipo() { return "Especial"; } }

public class Main {
    static String soma(int a, int b)       { return "sobrecarga int: " + (a + b); }
    static String soma(double a, double b) { return "sobrecarga double: " + (a + b); }
    public static void main(String[] args) {
        System.out.println(soma(2, 3));                     // estático: escolhido na compilação
        Conta c = new ContaEspecial();                      // tipo base, objeto derivado
        System.out.println("sobrescrita: " + c.tipo());     // dinâmico: escolhido na execução
    }
}
```

## Q12

**Assunto:** funcional × lógico. **Fontes:** Aula14; Aula15.

**Resposta-modelo:**

| Aspecto | Funcional | Lógico |
| --- | --- | --- |
| Base teórica | Funções matemáticas | Cálculo de predicados de primeira ordem |
| Abordagem (professor) | Procedural: especifica a composição de funções que calcula o resultado | **Declarativa**: especifica o que se deseja, e a inferência encontra |
| Programa | Funções primitivas, aplicação e formas funcionais | **Fatos** (proposições assumidas verdadeiras) e regras |
| Execução | Avaliação de expressões, de dentro para fora | **Consultas** respondidas por **unificação** (e *backtracking*) |
| Estado | No modelo puro, **imutabilidade**: sem variáveis mutáveis nem atribuição, logo **sem efeitos colaterais** | Variáveis são incógnitas ligadas por unificação; uma vez ligadas, não mudam |
| Classificação interna | **Puras** (Haskell, Miranda) × **impuras** (LISP, Scheme, Clojure, Elixir, Erlang) | — |
| Linguagem da disciplina | Clojure | Prolog |

- **Ponto em comum:** ambos **fogem do modelo de von Neumann** e surgiram ligados à IA e à matemática ou lógica.
- **Diferença central:** o funcional calcula um **valor** aplicando funções. O lógico encontra **instanciações** que tornam uma consulta verdadeira — por exemplo, `pai(X, maria)` → `X = joao`. O mesmo fato `pai/2` responde a perguntas em várias direções.

> **[Complemento]** "Imutabilidade" e "funções puras" aparecem no enunciado, mas os slides falam em "sem variável, atribuição e laço" e "sem efeitos colaterais". Uma **função pura** é aquela cujo resultado depende só dos argumentos e que não produz efeitos colaterais; **imutabilidade** é a propriedade de os valores não serem alterados depois de criados.

---

## Padrões de cobrança observados nas duas listas

- **Formato:** 23 questões **discursivas**; 18 pedem **diferenciar, comparar ou relacionar** pares de conceitos. As tabelas de [`quadros-comparativos.md`](../../../06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md) são o material mais direto.
- **Código:** só em Clojure (avaliar e escrever) e Prolog (consultas). Nos outros paradigmas, os exemplos das aulas servem para **sustentar** as respostas.
- **Aulas mais presentes:** 14 e 15 (nas duas listas). Na Lista 02, as Aulas 02–06, 09–11 e 13 aparecem uma vez cada; a 08 e a 12, duas vezes (Q6/Q9 e Q8/Q10); a Aula 07 (tipos compostos) não é cobrada diretamente.
- **Termos que aparecem nos enunciados sem estar nos slides** — imutabilidade e função pura: prepare definições curtas (ver o [glossário](../../../07%20-%20Glossário/glossario.md)). Outros termos aparecem com outro nome: "segmento estático" é o "Estático" da Aula08 p.13, e "vinculação tardia" é a "ligação tardia" da Aula13 p.12.
