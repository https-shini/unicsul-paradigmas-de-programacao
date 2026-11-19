# Aula 02 — Evolução das Linguagens e Paradigmas · Resumo teórico

> **Fonte:** [`Aula02_Evolução_LinguagensDeProgramacao.pdf`](../01%20-%20Slides%20Originais/Aula02_Evolução_LinguagensDeProgramacao.pdf) (23 páginas). Apoio indicado: Tucker & Noonan, seções 1.2 e 1.4; Sebesta (9ª ed.), seções 1.3, 1.4 e 1.5 (p.23).
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). `p.N` = página do PDF.

---

## 1. Objetivos da aula (p.2)

**[Material original]** Reconhecer os quatro principais paradigmas e algumas de suas linguagens; conhecer as restrições consideradas no projeto de uma linguagem; aplicar critérios de avaliação de linguagens; descrever a evolução das linguagens.

## 2. O que é uma linguagem de programação (p.3)

**[Material original]** "Pode-se definir uma linguagem de programação como um conjunto de termos e regras **sintáticas** e **semânticas** que permitem a construção de instruções processáveis por um computador."

**[Explicação elaborada]** A definição tem três partes, e cada uma vira um assunto do curso:

- **Termos** → o vocabulário: identificadores, palavras reservadas, operadores (Aula 04, sintaxe léxica).
- **Regras sintáticas** → como os termos se combinam (Aula 04, sintaxe concreta).
- **Regras semânticas** → o que cada combinação significa (Aula 05).

A expressão "processáveis por um computador" lembra que toda linguagem precisa ser traduzida para a máquina (Aula 03).

## 3. Um problema, três linguagens (p.4–8)

**[Material original]** O professor resolve o mesmo problema em três linguagens: ler dois inteiros `n1` e `n2` e informar se o dobro de `n1` é igual a `n2`.

### Pascal (p.5)

```pascal
program exemplo1;
var
  n1, n2, dobro: integer;
begin
  readln(n1);
  readln(n2);
  dobro := n1 * n2;          { veja a observação abaixo }
  if n2 = dobro then
    writeln('O dobro do primeiro valor e igual ao segundo valor.')
  else
    writeln('O dobro do primeiro valor nao e igual ao segundo valor.');
end.
```

> **[Atenção]** No slide, a linha 7 é `dobro := n1 * n2;`, que calcula o **produto**, não o dobro. As versões em Java e Prolog usam `2 * n1`. O correto seria `dobro := 2 * n1;`. Com a linha como está, o programa responde errado, por exemplo, para n1 = 3 e n2 = 6 (calcula 18, não 6).

### Java (p.6)

```java
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n1, n2, dobro;
        n1 = Integer.valueOf(input.nextLine());
        dobro = 2 * n1;
        n2 = Integer.valueOf(input.nextLine());
        if (dobro == n2) {
            System.out.println("O dobro do primeiro valor é igual ao segundo valor.");
        } else {
            System.out.println("O dobro do primeiro valor não é igual ao segundo valor.");
        }
    }
}
```

### Prolog (p.7)

```prolog
verifica_dobro :-
    write('Digite o primeiro numero inteiro: '), read(Num1),
    write('Digite o segundo numero inteiro: '),  read(Num2),
    Dobro is Num1 * 2,
    (   Dobro =:= Num2
    ->  write('O dobro do primeiro numero é igual ao segundo.')
    ;   write('O dobro do primeiro numero NAO é igual ao segundo.')
    ).
```

**[Explicação elaborada] — lendo o Prolog:**

| Símbolo | Significado |
| --- | --- |
| `verifica_dobro :- ...` | Uma **regra**: "`verifica_dobro` é verdadeiro **se** o corpo for verdadeiro". |
| `,` | Conjunção ("e"): os objetivos são provados da esquerda para a direita. |
| `is` | Avalia a expressão aritmética da direita e unifica o resultado com a variável da esquerda. |
| `=:=` | Compara dois valores numéricos (igualdade aritmética). |
| `( C -> A ; B )` | Se C, então A; senão, B. |
| `Num1`, `Dobro` | Variáveis começam com **maiúscula** em Prolog. |

**[Material original] — conclusão do professor (p.8):** as diferenças entre os códigos vêm da **sintaxe** de linguagens do mesmo paradigma (Pascal × Java) e/ou das **características gerais de paradigmas diferentes** (Pascal/Java × Prolog).

**[Explicação elaborada]** Compare:

- Pascal e Java são **imperativos**: declaram variáveis, atribuem (`:=` × `=`), testam (`=` × `==`) e escrevem. A estrutura é a mesma; mudam os símbolos. O Java exige uma classe (`class Main`) porque a linguagem é OO, mas a lógica dentro do `main` é imperativa.
- No Prolog, o programa é uma **regra** cujo corpo é uma conjunção de objetivos. Em vez de "atribuir", `Dobro is Num1 * 2` **vincula** a variável a um valor.

> **[Complemento]** Este exemplo de Prolog ainda é bem "procedural" (lê, calcula, decide, escreve). O estilo declarativo típico do paradigma lógico, baseado em fatos e consultas, aparece na [Aula 15](../../Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md).

## 4. Paradigma e paradigma de programação (p.8)

**[Material original]**

- **Paradigma:** modelo ou padrão que orienta uma determinada atividade.
- **Paradigma de programação:** padrão para resolução de problemas e para a representação computacional dessa solução.

## 5. Os quatro paradigmas (p.9–13)

**[Material original]**

| Paradigma | Caracterização | Exemplos |
| --- | --- | --- |
| **Imperativo** | Primeiro paradigma, baseado no modelo clássico de **von Neumann**. Atribuições, sequências de comandos, laços e condicionais. **A abstração procedural é sua principal característica.** | C, Cobol, Fortran, Pascal, Ada |
| **Orientado a objetos** | Programa = vários **objetos que trocam mensagens**. Objetos de dados são **ativos** (no imperativo, passivos). Caracterizado por classes, herança e passagem de mensagens. | C++, C#, Java, Smalltalk |
| **Funcional** | Problema modelado por **funções matemáticas**, cada uma com espaço de entrada e resultado. As funções interagem por **composição funcional**. | LISP, Haskell, Scheme, ML, Java 8 |
| **Lógico** | **Declarativo**: descreve o problema e *o que* se deseja, não *como* fazer. Um **algoritmo de inferência** busca a solução. Conhecido como baseado em regras. | Prolog |

**[Explicação elaborada] — "objetos ativos × passivos":** no imperativo, um dado (por exemplo, um vetor) é passivo — funções externas o leem e alteram. Na OO, o objeto carrega o próprio comportamento: você **pede** ao objeto que faça algo (`pilha.push(5)`), e ele decide como alterar seu estado. Essa ideia é desenvolvida na [Aula 12](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md).

**[Explicação elaborada] — "Java 8" na lista funcional:** o Java 8 introduziu expressões lambda e *streams*, recursos de estilo funcional. Isso não torna Java uma linguagem funcional; mostra que linguagens modernas são **multiparadigma** (Aula 14, p.10).

## 6. Restrições de projeto de uma linguagem (p.14–16)

**[Material original]** "O que se deve considerar no projeto de uma linguagem?"

| Restrição | Explicação do slide |
| --- | --- |
| **Arquitetura** | As linguagens são projetadas para uma arquitetura (von Neumann). Tentativas inversas — máquinas feitas para a linguagem, como as de LISP e Prolog — não deram certo. |
| **Configuração técnica** | Área de aplicação, sistema operacional, IDE e outras preferências da comunidade de usuários. |
| **Padrões** | Linguagens muito usadas tendem a ser padronizadas, o que facilita a portabilidade. |
| **Sistemas legados** | Novas versões devem compilar programas antigos, então tendem a ficar sobrecarregadas de comandos obsoletos. **Exemplo:** C++ em relação a C. **Contraexemplo:** Java em relação a C++. |

**[Explicação elaborada]** C++ manteve compatibilidade com C (ponteiros, `struct`, `printf`, macros), acumulando duas formas de fazer muitas coisas. Java rompeu com isso: removeu ponteiros explícitos, herança múltipla de classes e gerência manual de memória, ganhando simplicidade.

## 7. Critérios de avaliação (p.17)

**[Material original]** O slide apenas pergunta: "Quais critérios podem ser usados para avaliar uma linguagem?" — sem resposta escrita.

**[Complemento]** A resposta clássica está em Sebesta, seção 1.3, indicada na bibliografia da aula:

| Critério | Pergunta que responde | Características que influenciam |
| --- | --- | --- |
| Legibilidade | É fácil **ler e entender** programas? | Simplicidade, ortogonalidade, tipos de dados, sintaxe clara, estruturas de controle |
| Facilidade de escrita (*writability*) | É fácil **escrever** programas? | Simplicidade, suporte à abstração, expressividade |
| Confiabilidade | O programa se comporta conforme a especificação? | Verificação de tipos, tratamento de exceções, ausência de *aliasing* perigoso |
| Custo | Quanto custa usar a linguagem? | Treinamento, escrita, compilação, execução, manutenção |

Esses critérios reaparecem ao longo do curso: o escopo dinâmico prejudica a **legibilidade** e a **confiabilidade** (Aula 05); a tipagem estática melhora a **confiabilidade** (Aula 06); o `goto` prejudica a **legibilidade** (Aula 09).

## 8. Evolução das linguagens (p.18–22)

**[Material original]** A p.18 pergunta como foram construídos os primeiros programas e a primeira linguagem, com uma foto do ENIAC. As p.19–22 trazem quatro figuras.

**Figura 1 — árvore de gerações (p.19):**

| Nível | Geração | Conteúdo |
| --- | --- | --- |
| Baixo nível | 1ª | Linguagem de máquina |
| Baixo nível | 2ª | Linguagem Assembly |
| Alto nível | 3ª | Linguagens imperativas |
| Alto nível | 4ª | Linguagens OO ou aplicativas |
| Alto nível | 5ª | Linguagens declarativas |

**Figura 2 — "Generation of programming languages examples" (p.20):** 1ª máquina; 2ª Assembly; 3ª C, C#, C++, Fortran, Pascal, COBOL, Visual Basic, Java, JavaScript; 4ª SQL, Python, Perl, Ruby, MatLab; 5ª Prolog, Mercury, LISP, OPS5.

**Figura 3 — mapa mental "15 – Gerações das linguagens" (p.21):**

- 1ª: 0 e 1, década de 1940, linguagem de máquina.
- 2ª: Assembly, linguagem simbólica/montagem, 1ª metade dos anos 1950.
- 3ª: alto nível, procedimentais, 2ª metade dos anos 1950 (Fortran, Cobol, Lisp, C, C++, C#, Java).
- 4ª: aplicações específicas (NOMAD, SQL, Postscript), para relatórios, bancos de dados e formatação de texto.
- 5ª: lógica com restrição (Prolog, OPS5).

**Figura 4 — linha do tempo 1950–2000 (p.22):** colunas *Imperative*, *Object Oriented*, *Functional* e *Logical*. Vai de A-0, FORTRAN, COBOL, ALGOL, LISP e PROLOG (anos 1950–70) até Java, Python, Haskell 98 e Visual Basic (anos 1990).

> **[Atenção] — as classificações divergem.** As três primeiras figuras **não concordam** sobre a 4ª e a 5ª gerações. A árvore põe a OO na 4ª; a Figura 2 põe Java e C# na 3ª e LISP na 5ª; o mapa mental põe na 4ª linguagens de propósito específico (SQL), e não a OO. O ponto de consenso: 1ª = máquina, 2ª = Assembly, 3ª = alto nível procedimental, 5ª = lógica/declarativa. Numa prova, **diga qual classificação está usando**.

**[Explicação elaborada] — a lógica da evolução:**

1. **Máquina (anos 1940):** instruções em binário, específicas de cada computador.
2. **Assembly:** mnemônicos (`ADD`, `MOV`) traduzidos 1:1 para binário por um montador.
3. **Alto nível (Fortran, 1957):** uma instrução da linguagem vira várias de máquina; surge o compilador.
4. **Estruturação e abstração:** Algol, Pascal e C (estruturas de controle e procedimentos); depois Simula, Smalltalk, C++ e Java (objetos).
5. **Ramos não von Neumann:** LISP (1958) dá origem aos funcionais; Prolog (1972), aos lógicos.

## 9. Conexões

- A definição de linguagem (sintaxe + semântica) é retomada na [Aula 04](../../Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md).
- As figuras de gerações voltam nas Aulas 03 e 09.
- Von Neumann é detalhado na [Aula 09](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md) e na Aula 14.
- O caráter declarativo do lógico é aprofundado na [Aula 15](../../Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md).

## 10. Pontos para a prova

- Saber **as definições** de linguagem, paradigma e paradigma de programação.
- Saber caracterizar os **quatro paradigmas** com exemplos de linguagens.
- Saber as **quatro restrições de projeto**, incluindo o exemplo e o contraexemplo dos sistemas legados.
- Saber que as classificações de gerações **divergem**.

---

**Anterior:** [Aula 01](../../Aula%2001%20-%20Apresentação%20da%20Disciplina/02%20-%20Resumo%20Teórico/resumo-aula-01.md) · **Próxima:** [Aula 03 — Implementação das Linguagens](../../Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md)
