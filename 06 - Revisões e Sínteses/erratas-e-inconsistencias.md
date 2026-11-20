# Erratas e inconsistências do material

> **[Atenção]** Consolidação dos pontos em que os slides têm erro de digitação, código incorreto ou afirmação divergente da literatura. Cada item foi conferido no PDF original (`AulaXX p.N`) e é discutido no resumo da aula. **Os originais não foram alterados.**
> **Orientação para prova:** quando a divergência é **conceitual**, responda com a forma do professor e, se houver espaço, acrescente a ressalva. Quando é **erro de código**, use a versão corrigida.

**Legenda do impacto:** 🔴 código não funciona ou conceito invertido · 🟡 imprecisão que pode confundir · ⚪ forma (digitação, paginação).

| # | Local | O que diz o material | Problema | Forma correta | Impacto |
| --- | --- | --- | --- | --- | :-: |
| 1 | Aula01 p.3 | "doaradigma" | Digitação | "do paradigma" | ⚪ |
| 2 | Aula01 p.6 | Horários 08h30–11h10 sob o rótulo "Noite" | Horário matutino | Confirmar o horário da turma | ⚪ |
| 3 | Aula02 p.5 | Pascal: `dobro := n1 * n2;` | Calcula o **produto**; as versões em Java e Prolog usam `2 * n1` | `dobro := 2 * n1;` | 🔴 |
| 4 | Aula02 p.19–21 | Três figuras classificam a 4ª e 5ª gerações | As figuras **não concordam** entre si | Citar a figura usada na pergunta; o consenso é só até a 3ª geração | 🟡 |
| 5 | Aula03 p.10 | Python classificado como interpretado | Simplificação: CPython compila para bytecode (`.pyc`) | Aceitar "interpretado" na disciplina; citar o bytecode como complemento | 🟡 |
| 6 | Aula04 p.9 | `-5` listado como constante | Na análise léxica, são dois tokens: `-` e `5` | Tratar `-5` como operador unário + constante | 🟡 |
| 7 | Aula04 p.9 | `=` entre símbolos especiais; `==` entre operadores | Classificação própria do slide | Seguir o slide nas questões da disciplina | ⚪ |
| 8 | Aula06 p.6–7 | Tamanhos de tipos (`byte` em C/C++; `boolean` = 1 em Java) | C/C++ não têm `byte`; o tamanho de `boolean` não é fixado pela especificação | `char` em C/C++; `boolean` com representação dependente da JVM | 🟡 |
| 9 | Aula06 p.8 | Slide de overflow sem nomear o problema; "103" | O sobrescrito se perdeu | *Overflow*; 1,432 × 10³ | ⚪ |
| 10 | Aula06 p.13 | `print("z eh", type(x))` | Testa `x` em vez de `z` | `type(z)` | 🟡 |
| 11 | Aula06 p.17 | Perl entre as linguagens fortemente tipadas | Perl faz coerção string ↔ número, o que pela p.21 a tornaria mais fraca | Mencionar a falta de consenso que o próprio slide reconhece | 🟡 |
| 12 | Aula07 p.14–16 | Exercício cita o **8º** semestre; desafio cita **4º e 5º** | Enunciados inconsistentes | Não afeta a lógica | ⚪ |
| 13 | Aula07 p.15 | Saída de exemplo do exercício em Java | Gerada com `make` (C/C++) e com médias **truncadas** | Exibir médias `float` com casas decimais | 🟡 |
| 14 | Aula08 p.14 | `int* vetor = new int(4);` | Aloca **um** `int` com valor 4; o laço escreve fora da área alocada | `new int[n]` + `delete[] vetor;` | 🔴 |
| 15 | Aula09–Aula15, p.1 | Arquivos `Aula09`–`Aula15` com títulos "Aula 10"–"Aula 16" | Numeração deslocada em +1 | Este repositório usa o nome do arquivo | ⚪ |
| 16 | Aula09 p.11 | `int x = x + 20;` | Usa `x` antes de inicializar | `int x = 10; x = x + 20;` | 🔴 |
| 17 | Aula09 p.18 | Dijkstra mostrou que o "uso excessivo" de `goto` é prejudicial e que qualquer programa com `goto` pode ser reescrito com laços | O artigo pede **abolir** o `goto`; a prova de dispensabilidade é de **Böhm e Jacopini (1966)** | Ver [resumo do artigo](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-artigo-dijkstra-1968.md) | 🟡 |
| 18 | Aula09 p.23–24 | Bibliografia (p.23) antes da Atividade 2 (p.24) | Ordem dos slides | — | ⚪ |
| 19 | Aula09 p.22 | Programa sem `#include <stdio.h>` | Não compila sem aviso em C moderno | Incluir o cabeçalho | ⚪ |
| 20 | Aula10 p.13 | "atualizar a variável **menor** com este **valor**" | O código guarda a **posição** (`posMenor = j`) | O código está certo: a posição é necessária para a troca | 🟡 |
| 21 | Aula10 p.16 | "não favorece a **baixa** coesão" | Inverte o conceito: o desejável é **alta** coesão | "não favorece a **alta** coesão" | 🔴 |
| 22 | Aula12 p.8 | "empilhar **três** números" | Os laços Java vão de 0 a 4 (**cinco** números) | Só a versão C++ (p.30) usa 3 | ⚪ |
| 23 | Aula12 p.27 | `if (topo == tamanho-1)` | `tamanho` não está declarado em `pilha.h` | Declarar `const int tamanho = …;` | 🔴 |
| 24 | Aula12 p.30 | Corpo de `Pilha::pop()` | **Cortado** na borda do slide | Versão completada no [resumo da Aula 12](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) | 🟡 |
| 25 | Aula13 p.7 e p.9 | Atributos Resolução, Colorido, Modelo | Não aparecem no código C++ | — | ⚪ |
| 26 | Aula13 p.13 | Interfaces só têm assinaturas e constantes | Definição clássica, anterior ao Java 8 (`default`, `static`) e ao Java 9 (`private`) | Usar a definição do slide e citar a evolução | 🟡 |
| 27 | Aula14 p.8 | Prêmio "pelo seu trabalho como Fortran" | Redação truncada | "pelo trabalho com o Fortran" (e a BNF) | ⚪ |
| 28 | Aula14 p.18 | `(- (+ x y) 10))` | Parêntese **a mais** | `(- (+ x y) 10)` | 🔴 |
| 29 | Aula14 p.21, p.23 | Teste de diferente com `(not (= x 0))` | Clojure tem `not=` | Ambas as formas funcionam | ⚪ |
| 30 | Aula14 p.20 | "(3 * y)2" | Sobrescrito perdido | (3y)² | ⚪ |
| 31 | Aula15 p.3–5 | Funcional classificado como **procedural** | Boa parte da literatura classifica o funcional como **declarativo** | Seguir o professor; mencionar a divergência | 🟡 |
| 32 | Aula15 p.25 | Repete o slide de objetivos | Página solta após a bibliografia | — | ⚪ |

## Por que isso importa

- Os itens 🔴 aparecem em **código que você pode copiar** para uma atividade: use sempre a versão corrigida dos resumos, que foi compilada e testada.
- Os itens 🟡 são os que mais rendem em questões discursivas: mostrar que você conhece a nuance (por exemplo, Böhm e Jacopini × Dijkstra) demonstra domínio.
- Encontrou outro problema? Registre-o aqui com arquivo, página e a forma correta.
