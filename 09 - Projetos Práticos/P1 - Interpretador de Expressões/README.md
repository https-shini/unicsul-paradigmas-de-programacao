# P1 — Interpretador de expressões

> **[Exercício autoral]** Projeto prático elaborado para este repositório. **Não é trabalho do professor** e não vale nota. A pasta `solucao/` é uma **[Resolução elaborada]**, não gabarito oficial.

| | |
| --- | --- |
| **Linguagem** | Python 3 (só a biblioteca padrão) |
| **Aulas** | 03 (implementação), 04 (sintaxe e BNF), 05 (semântica), 06 (tipos) |
| **Duração sugerida** | 4 etapas de 1 a 2 horas |
| **Testes** | 26, em `testes/test_calc.py` |

## Objetivo

Construir, fase por fase, a implementação de uma pequena linguagem — a **calc**. Você vai escrever o analisador léxico, o analisador sintático a partir de uma gramática BNF, um **interpretador** que percorre a árvore e, por fim, um **compilador** para um bytecode de máquina de pilha, executado por uma **máquina virtual**. São exatamente as fases que as Aulas 03 e 04 mostram em diagrama.

```text
x = 2 + 3 * 4        →  tokens  →  árvore  →  interpretador  →  14
print x - 1                                 →  bytecode + VM  →  13
```

## Conceitos da disciplina aplicados

| Conceito | Onde aparece no projeto | Resumo |
| --- | --- | --- |
| Fases do compilador; compilação × interpretação × híbrida | os quatro módulos; interpretador × VM | [Aula 03](../../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/02%20-%20Resumo%20Teórico/resumo-aula-03.md) |
| Lexema, token, palavra reservada | `lexico.py` | [Aula 04](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) |
| BNF, árvore de análise, precedência e associatividade | `sintatico.py` | [Aula 04](../../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md) |
| Vinculação nome → valor; erros semânticos dinâmicos | `interpretador.py` | [Aula 05](../../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md) |
| Inteiro × ponto flutuante | `Num`, divisão `/` | [Aula 06](../../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md) |

## A linguagem calc

Um programa é uma sequência de linhas. Cada linha tem no máximo um comando: uma **atribuição** ou um **print**. `#` inicia um comentário.

```text
# média das notas
a1 = 3.5
a2 = 2 + 1.5
print a1 + a2          # 7.0
print (a1 + a2) / 2    # 3.5
```

**Gramática (BNF):**

```text
<programa> ::= { <linha> } FIM
<linha>    ::= [ <comando> ] ( FIM_LINHA | FIM )
<comando>  ::= id "=" <expr> | "print" <expr>
<expr>     ::= <termo> { ( "+" | "-" ) <termo> }
<termo>    ::= <fator> { ( "*" | "/" ) <fator> }
<fator>    ::= "-" <fator> | num | id | "(" <expr> ")"
```

**Semântica:** números sem ponto são inteiros (`int`); com ponto, reais (`float`). `+`, `-` e `*` seguem as regras do Python; `/` é sempre a divisão real (`7 / 2` = `3.5`, `6 / 3` = `2.0`). Usar uma variável antes de atribuir e dividir por zero são **erros de execução**.

## Estrutura

```text
P1 - Interpretador de Expressões/
├── README.md            ← este enunciado
├── projeto.json         ← descrição dos testes (usada pela ferramenta)
├── exemplos/            ← programas .calc para experimentar
├── inicial/calc/        ← ESQUELETO: é aqui que você trabalha (procure os TODO)
├── solucao/calc/        ← resolução de referência — consulte só depois de tentar
└── testes/test_calc.py  ← testes automáticos, organizados por etapa
```

Os módulos `arvore.py`, `__init__.py` e `__main__.py` já vêm prontos. Você completa `lexico.py`, `sintatico.py`, `interpretador.py` e `compilador.py`.

## Etapas e requisitos

### Etapa 1 — Análise léxica (`lexico.py`)

- **R1.** `tokenizar(codigo)` devolve a lista de `Token(tipo, lexema, linha, coluna)`, terminada por `FIM`.
- **R2.** Tipos: `NUM`, `ID`, `PRINT` (palavra reservada), `OP` (`+ - * /`), `ATRIB` (`=`), `ABRE`, `FECHA`, `FIM_LINHA`, `FIM`.
- **R3.** Espaços e comentários são descartados; `2.5` é um único `NUM`.
- **R4.** Um caractere inválido lança `ErroLexico` com linha e coluna.

Teste mental: quantos tokens há em `soma = x + 10`? (A mesma pergunta da [Lista 02](../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md) e do [simulado 02](../../04%20-%20Provas%20e%20Avaliações/Simulados/simulado-02.md).)

### Etapa 2 — Análise sintática (`sintatico.py`)

- **R5.** Um método por regra da gramática (`expr`, `termo`, `fator`): é a **descida recursiva**.
- **R6.** `2 + 3 * 4` gera `Binario("+", 2, Binario("*", 3, 4))` — a precedência vem da gramática, não de `if`s.
- **R7.** `10 - 3 - 2` associa à esquerda: `(10 - 3) - 2`.
- **R8.** Erros de sintaxe (`print 2 +`, `x = (1`) lançam `ErroSintatico` com a posição.

### Etapa 3 — Interpretador (`interpretador.py`)

- **R9.** `avaliar(no)` calcula o valor de uma expressão; `executar(programa)` devolve a lista de valores impressos.
- **R10.** As variáveis ficam em `self.memoria` e **persistem** entre chamadas de `executar` (é o que permite o modo interativo).
- **R11.** Variável não definida e divisão por zero lançam `ErroExecucao`, **só quando o comando executa**.

### Etapa 4 — Compilador e máquina virtual (`compilador.py`)

- **R12.** `compilar(programa)` gera instruções de máquina de pilha em **pós-ordem**: `x = 2 + 3` → `PUSH 2`, `PUSH 3`, `ADD`, `STORE x`.
- **R13.** `MaquinaVirtual.executar(codigo)` produz **as mesmas saídas** que o interpretador e termina com a pilha vazia.

## Como testar e usar

```bash
python3 ferramentas/testar_projetos.py P1                  # roda os testes sobre inicial/
python3 ferramentas/testar_projetos.py P1 -v               # mostra cada teste
cd "09 - Projetos Práticos/P1 - Interpretador de Expressões/inicial"
python3 -m calc ../exemplos/media.calc                     # executa um programa
python3 -m calc --tokens ../exemplos/media.calc            # mostra cada fase:
python3 -m calc --arvore ../exemplos/precedencia.calc      #   tokens, árvore, bytecode
python3 -m calc --bytecode ../exemplos/media.calc
python3 -m calc --vm ../exemplos/media.calc                # executa pela máquina virtual
python3 -m calc                                            # modo interativo
```

Os testes estão em classes `Etapa1Lexico` … `Etapa4Compilador`: no início, foque nos erros da etapa em que você está.

## Critérios de autoavaliação

| Critério | Peso |
| --- | :-: |
| Os 26 testes passam | 40% |
| Cada método do analisador corresponde a uma regra da BNF (dá para ler a gramática no código) | 20% |
| Mensagens de erro com linha e coluna, e no tipo certo (léxico, sintático ou de execução) | 15% |
| Interpretador e VM compartilham a mesma semântica (por exemplo, a mesma função `aplicar`) | 15% |
| Você consegue explicar, com o seu código, a diferença entre interpretação pura e híbrida | 10% |

## Extensões

1. **Potência** `^` com precedência maior que `*` e associatividade **à direita** (`2 ^ 3 ^ 2` = 512). Como a gramática muda?
2. **Verificação estática:** antes de executar, percorra a árvore e acuse uso de variável nunca atribuída. O erro passa de dinâmico para estático — compare com a observação da Aula 05 (p.17) sobre linguagens interpretadas.
3. **Comparações e `while`:** acrescente `<`, `==` e um laço; na VM, isso exige instruções de salto (`JUMP`, `JUMP_IF_FALSE`) — é o `goto` da Aula 09 escondido no bytecode.
4. **Inteiros de tamanho fixo:** simule `int` de 32 bits (como em C ou Java) e trate o *overflow* da Aula 06.

## Para refletir

- Por que o interpretador detecta `print y` só quando a linha executa, e um compilador com tipagem estática poderia detectar antes?
- Na versão híbrida, o que equivale ao `.class` da JVM? E ao `java` que o executa?
- Onde a precedência de operadores está definida no seu código? E a associatividade?
