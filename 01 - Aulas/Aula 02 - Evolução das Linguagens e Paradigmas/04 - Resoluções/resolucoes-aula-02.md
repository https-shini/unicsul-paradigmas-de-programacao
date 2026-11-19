# Aula 02 — Evolução das Linguagens e Paradigmas · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-02.md`](../03%20-%20Exercícios/exercicios-aula-02.md). Base: [`Aula02_Evolução_LinguagensDeProgramacao.pdf`](../01%20-%20Slides%20Originais/Aula02_Evolução_LinguagensDeProgramacao.pdf).

## E1

- **(a)** Conjunto de termos e regras sintáticas e semânticas que permitem a construção de instruções processáveis por um computador (p.3).
- **(b)** Modelo ou padrão que orienta uma determinada atividade (p.8).
- **(c)** Padrão para resolução de problemas e para a representação computacional dessa solução (p.8).

**Erro comum:** confundir "paradigma" com "linguagem". Uma linguagem pertence a (ou suporta) um ou mais paradigmas.

## E2

| Linguagem | Paradigma (slides) |
| --- | --- |
| Smalltalk | Orientado a objetos |
| Prolog | Lógico |
| Cobol | Imperativo |
| Haskell | Funcional |
| Ada | Imperativo |
| C# | Orientado a objetos |
| Scheme | Funcional |

## E3

**Resposta: b.** O slide (p.10) afirma que a abstração procedural é a principal característica do imperativo. As demais alternativas são, respectivamente, de OO (a), funcional (c) e lógico (d).

## E4

**Resposta-modelo:** no imperativo, a pilha é um vetor e uma variável `topo` manipulados por funções externas. Qualquer parte do programa pode alterar `topo` diretamente, ou seja, o dado é **passivo**. Na OO, a pilha é um objeto que encapsula vetor e topo e expõe só `push` e `pop`: o cliente **envia uma mensagem** (`pilha.push(5)`) e o próprio objeto decide como mudar seu estado. O dado se torna **ativo**, responsável pelo próprio comportamento.

**Relação:** é exatamente a evolução das versões 1a → 1c da pilha na [Aula 12](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md).

## E5

| Restrição | Explicação |
| --- | --- |
| Arquitetura | Linguagens são feitas para von Neumann; máquinas feitas para LISP/Prolog fracassaram. |
| Configuração técnica | Área de aplicação, sistema operacional, IDE, preferências da comunidade. |
| Padrões | Linguagens populares são padronizadas, o que favorece a portabilidade. |
| Sistemas legados | Novas versões precisam compilar código antigo e acumulam recursos obsoletos. |

**Por que Java é contraexemplo:** C++ manteve compatibilidade com C e herdou seus recursos antigos (exemplo do problema). Java, embora com sintaxe inspirada em C++, **não** se comprometeu a compilar código C/C++. Pôde, assim, eliminar ponteiros explícitos, gerência manual de memória e herança múltipla de classes, ficando mais enxuta.

## E6

**Fontes (p.8):** (1) a **sintaxe** de linguagens do mesmo paradigma e (2) as **características gerais** de paradigmas diferentes.

- **Sintaxe, mesmo paradigma (Pascal × Java):** atribuição `:=` × `=`; comparação `=` × `==`; blocos `begin/end` × `{ }`; `readln` × `Scanner`.
- **Paradigma diferente (Pascal/Java × Prolog):** o Prolog não tem declaração de variáveis nem atribuição — o programa é uma **regra** (`:-`) com objetivos em conjunção, e `Dobro is Num1 * 2` vincula, não atribui.

## E7

**[Atenção]** No slide, a linha 7 é `dobro := n1 * n2;`.

- **n1 = 3, n2 = 6:** dobro = 18; 6 ≠ 18 → imprime "...nao e igual...". **Errado**, pois 2 × 3 = 6.
- **n1 = 2, n2 = 4:** dobro = 8; 4 ≠ 8 → "...nao e igual...". **Errado** de novo.
- Só acerta por coincidência, quando n1 × n2 = n2 (por exemplo, n1 = 1) ou n2 = 0.

**Correção:** `dobro := 2 * n1;`. As versões em Java e Prolog já fazem isso.

**Lição:** um programa sintaticamente correto pode estar **semanticamente** errado — ele compila, mas não faz o que se pretende. Esse é o tema da Aula 05.

## E8

| Trecho | Leitura |
| --- | --- |
| `verifica_dobro :-` | "`verifica_dobro` é verdadeiro **se**…" |
| `write(...)`, `read(Num1)` | Escreve a mensagem **e** lê um termo, vinculando-o a `Num1`. |
| `,` | "E": todos os objetivos precisam ser satisfeitos, em ordem. |
| `Dobro is Num1 * 2` | Avalia `Num1 * 2` e vincula o resultado a `Dobro`. |
| `Dobro =:= Num2` | Testa igualdade **numérica** entre os valores. |
| `( C -> A ; B )` | Se C for verdadeiro, prova A; senão, prova B. |

**Complemento:** `=` em Prolog é **unificação**, não comparação aritmética. `X = 1+1` vincula X ao termo `1+1`, enquanto `X is 1+1` vincula X a 2.

## E9

**Por que divergem:** "geração" não é um conceito padronizado. Cada autor usa um critério diferente — época, nível de abstração, paradigma ou domínio de aplicação — e as figuras misturam esses critérios.

| Linguagem | Árvore (p.19) | "Generation…" (p.20) | Mapa mental (p.21) |
| --- | --- | --- | --- |
| LISP | Não é citada; por ser declarativa, ficaria na 5ª | 5ª | 3ª |
| Java | 4ª (OO) | 3ª | 3ª |
| SQL | Não é citada | 4ª | 4ª (aplicações específicas) |

## E10

**Resposta-modelo:** como as máquinas especializadas não vingaram, linguagens funcionais e lógicas precisam rodar sobre hardware de von Neumann. A forma natural é um **interpretador** (ou máquina virtual) que simula em software o modelo de execução da linguagem — avaliação de funções ou motor de inferência. É o "computador virtual" da Fig. 1.2 de Sebesta (Aula 03): cada interpretador cria uma camada que se comporta como uma máquina daquela linguagem. A Aula 14 confirma que linguagens funcionais são, em geral, interpretadas, embora possam ser compiladas; Clojure, por exemplo, roda sobre a JVM.

## E11

**[Resolução elaborada]** Exemplo de avaliação, justificada:

| Linguagem | Legibilidade | Facilidade de escrita | Confiabilidade |
| --- | --- | --- | --- |
| Pascal | Alta: palavras-chave em inglês (`begin`, `then`), tipos declarados | Média: verbosa | Alta: tipagem forte e estática |
| C | Média: operadores compactos (`++`, `&`, `*`) dificultam a leitura | Alta para quem domina | Menor: ponteiros, conversão implícita, sem verificação de limites de vetor |
| Python | Alta: indentação obrigatória, sintaxe enxuta | Muito alta | Média: tipagem dinâmica e forte; erros de tipo só aparecem em execução |

O importante é **ligar cada nota a um recurso da linguagem**, como faz Sebesta.
