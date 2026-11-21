[Início](../README.md) › **codigo** · [Mapa](../MAPA.md)

# Código dos exemplos

Todos os programas dos resumos, resoluções, listas, simulados e revisões, um por arquivo, prontos para executar.

> **Gerado automaticamente** por `ferramentas/gerar_codigo.py` a partir dos arquivos Markdown, que são a fonte. Para alterar um exemplo, edite o Markdown e gere de novo; os testes automáticos conferem se esta pasta está atualizada.

## Como executar

Abra o repositório no **Codespaces** (todas as linguagens já instaladas) ou instale o ambiente com `bash ferramentas/instalar-ambiente.sh`. Depois:

```bash
python3 ferramentas/rodar.py codigo/aula-14/resolucoes/04-e8-atividade-2-original-p-20.clj
```

O `rodar.py` compila quando preciso, usa automaticamente o arquivo `.entrada.txt` ao lado do programa (se existir) e, para Prolog, executa a consulta indicada no cabeçalho. Opções: `--entrada "2 3"` e `--consulta "pai(X, ana)."`.

Também é possível usar cada ferramenta diretamente:

| Linguagem | Comando |
| --- | --- |
| C | `gcc arquivo.c -o programa -lm && ./programa` |
| C++ | `g++ -std=c++17 arquivo.cpp -o programa && ./programa` |
| Java | `java Classe.java` (dentro da pasta do exemplo) |
| C# | `dotnet run` (dentro da pasta do exemplo) |
| Python / PHP / Perl | `python3 arquivo.py` · `php arquivo.php` · `perl arquivo.pl` |
| Clojure | `clojure -M arquivo.clj` |
| Prolog | `swipl arquivo.pl` e, no prompt, a consulta do cabeçalho |

## Totais

| Linguagem | Programas |
| --- | :-: |
| C | 45 |
| C++ | 12 |
| Java | 28 |
| C# | 2 |
| Python | 6 |
| PHP | 2 |
| Perl | 3 |
| Clojure | 11 |
| Prolog | 16 |
| **Total** | **125** |

## Índice

### aula-02

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-02/resumo/01-java-p-6/Main.java`](aula-02/resumo/01-java-p-6/Main.java) | Java | [resumo-aula-02.md — Java (p.6)](../01%20-%20Aulas/Aula%2002%20-%20Evolução%20das%20Linguagens%20e%20Paradigmas/02%20-%20Resumo%20Teórico/resumo-aula-02.md#java-p6) |

### aula-03

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-03/resolucoes/01-c-grupo-1-compilada.c`](aula-03/resolucoes/01-c-grupo-1-compilada.c) | C | [resolucoes-aula-03.md — C (Grupo 1, compilada)](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/04%20-%20Resoluções/resolucoes-aula-03.md#c-grupo-1-compilada) |
| [`aula-03/resolucoes/02-python-grupo-1-interpretada.py`](aula-03/resolucoes/02-python-grupo-1-interpretada.py) | Python | [resolucoes-aula-03.md — Python (Grupo 1, interpretada)](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/04%20-%20Resoluções/resolucoes-aula-03.md#python-grupo-1-interpretada) |
| [`aula-03/resolucoes/03-java-referencia-para-a-comparacao-hibrida/Main.java`](aula-03/resolucoes/03-java-referencia-para-a-comparacao-hibrida/Main.java) | Java | [resolucoes-aula-03.md — Java (referência para a comparação, híbrida)](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/04%20-%20Resoluções/resolucoes-aula-03.md#java-referência-para-a-comparação-híbrida) |
| [`aula-03/resolucoes/04-perl-grupo-2-interpretada.pl`](aula-03/resolucoes/04-perl-grupo-2-interpretada.pl) | Perl | [resolucoes-aula-03.md — Perl (Grupo 2, interpretada)](../01%20-%20Aulas/Aula%2003%20-%20Implementação%20das%20Linguagens/04%20-%20Resoluções/resolucoes-aula-03.md#perl-grupo-2-interpretada) |

### aula-04

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-04/resumo/03-10-exemplo-1-p-20.c`](aula-04/resumo/03-10-exemplo-1-p-20.c) | C | [resumo-aula-04.md — 10. Exemplo 1 (p.20)](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/02%20-%20Resumo%20Teórico/resumo-aula-04.md#10-exemplo-1-p20) |
| [`aula-04/resolucoes/01-e10.py`](aula-04/resolucoes/01-e10.py) | Python | [resolucoes-aula-04.md — E10](../01%20-%20Aulas/Aula%2004%20-%20Sintaxe/04%20-%20Resoluções/resolucoes-aula-04.md#e10) |

### aula-05

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-05/resumo/01-escopo-estatico-p-10-11.cpp`](aula-05/resumo/01-escopo-estatico-p-10-11.cpp) | C++ | [resumo-aula-05.md — Escopo estático (p.10–11)](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md#escopo-estático-p1011) |
| [`aula-05/resumo/02-4-6-tempo-de-vida-p-13.c`](aula-05/resumo/02-4-6-tempo-de-vida-p-13.c) | C | [resumo-aula-05.md — 4.6 Tempo de vida (p.13)](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md#46-tempo-de-vida-p13) |
| [`aula-05/resumo/03-5-constantes-nomeadas-p-14-16/Main.java`](aula-05/resumo/03-5-constantes-nomeadas-p-14-16/Main.java) | Java | [resumo-aula-05.md — 5. Constantes nomeadas (p.14–16)](../01%20-%20Aulas/Aula%2005%20-%20Semântica/02%20-%20Resumo%20Teórico/resumo-aula-05.md#5-constantes-nomeadas-p1416) |
| [`aula-05/exercicios/01-avancado.c`](aula-05/exercicios/01-avancado.c) | C | [exercicios-aula-05.md — Avançado](../01%20-%20Aulas/Aula%2005%20-%20Semântica/03%20-%20Exercícios/exercicios-aula-05.md#avançado) |
| [`aula-05/resolucoes/01-e7.c`](aula-05/resolucoes/01-e7.c) | C | [resolucoes-aula-05.md — E7](../01%20-%20Aulas/Aula%2005%20-%20Semântica/04%20-%20Resoluções/resolucoes-aula-05.md#e7) |
| [`aula-05/resolucoes/02-e10.pl`](aula-05/resolucoes/02-e10.pl) | Perl | [resolucoes-aula-05.md — E10](../01%20-%20Aulas/Aula%2005%20-%20Semântica/04%20-%20Resoluções/resolucoes-aula-05.md#e10) |

### aula-06

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-06/resumo/01-4-tipos-basicos-e-seus-tamanhos-p-6-8.c`](aula-06/resumo/01-4-tipos-basicos-e-seus-tamanhos-p-6-8.c) | C | [resumo-aula-06.md — 4. Tipos básicos e seus tamanhos (p.6–8)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#4-tipos-básicos-e-seus-tamanhos-p68) |
| [`aula-06/resumo/02-5-tipagem-estatica-dinamica-p-9-14.php`](aula-06/resumo/02-5-tipagem-estatica-dinamica-p-9-14.php) | PHP | [resumo-aula-06.md — 5. Tipagem estática × dinâmica (p.9–14)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#5-tipagem-estática--dinâmica-p914) |
| [`aula-06/resumo/03-5-tipagem-estatica-dinamica-p-9-14.py`](aula-06/resumo/03-5-tipagem-estatica-dinamica-p-9-14.py) | Python | [resumo-aula-06.md — 5. Tipagem estática × dinâmica (p.9–14)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#5-tipagem-estática--dinâmica-p914) |
| [`aula-06/resumo/04-6-1-java-ou-c-p-16.c`](aula-06/resumo/04-6-1-java-ou-c-p-16.c) | C | [resumo-aula-06.md — 6.1 Java ou C? (p.16)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#61-java-ou-c-p16) |
| [`aula-06/resumo/05-6-1-java-ou-c-p-16-nao-compila/Main.java`](aula-06/resumo/05-6-1-java-ou-c-p-16-nao-compila/Main.java) | Java | [resumo-aula-06.md — 6.1 Java ou C? (p.16)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#61-java-ou-c-p16) |
| [`aula-06/resumo/06-6-3-exemplo-php-e-atividade-p-19-20.php`](aula-06/resumo/06-6-3-exemplo-php-e-atividade-p-19-20.php) | PHP | [resumo-aula-06.md — 6.3 Exemplo PHP e atividade (p.19–20)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#63-exemplo-php-e-atividade-p1920) |
| [`aula-06/resolucoes/01-e8.py`](aula-06/resolucoes/01-e8.py) | Python | [resolucoes-aula-06.md — E8](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md#e8) |
| [`aula-06/resolucoes/02-c-tentativa-literal-nao-compila.c`](aula-06/resolucoes/02-c-tentativa-literal-nao-compila.c) | C | [resolucoes-aula-06.md — C — tentativa literal](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md#c--tentativa-literal) |
| [`aula-06/resolucoes/03-c-versao-que-funciona-conversao-explicita.c`](aula-06/resolucoes/03-c-versao-que-funciona-conversao-explicita.c) | C | [resolucoes-aula-06.md — C — versão que funciona (conversão explícita)](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md#c--versão-que-funciona-conversão-explícita) |
| [`aula-06/resolucoes/04-python.py`](aula-06/resolucoes/04-python.py) | Python | [resolucoes-aula-06.md — Python](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md#python) |
| [`aula-06/resolucoes/05-e11.pl`](aula-06/resolucoes/05-e11.pl) | Perl | [resolucoes-aula-06.md — E11](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md#e11) |
| [`aula-06/resolucoes/06-e12.c`](aula-06/resolucoes/06-e12.c) | C | [resolucoes-aula-06.md — E12](../01%20-%20Aulas/Aula%2006%20-%20Sistema%20de%20Tipos/04%20-%20Resoluções/resolucoes-aula-06.md#e12) |

### aula-07

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-07/resumo/01-3-enumeracoes-p-4-5/Main.java`](aula-07/resumo/01-3-enumeracoes-p-4-5/Main.java) | Java | [resumo-aula-07.md — 3. Enumerações (p.4–5)](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md#3-enumerações-p45) |
| [`aula-07/resumo/02-3-enumeracoes-p-4-5/Main.java`](aula-07/resumo/02-3-enumeracoes-p-4-5/Main.java) | Java | [resumo-aula-07.md — 3. Enumerações (p.4–5)](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md#3-enumerações-p45) |
| [`aula-07/resumo/03-4-estruturas-ou-registros-p-6-8.cpp`](aula-07/resumo/03-4-estruturas-ou-registros-p-6-8.cpp) | C++ | [resumo-aula-07.md — 4. Estruturas ou registros (p.6–8)](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/02%20-%20Resumo%20Teórico/resumo-aula-07.md#4-estruturas-ou-registros-p68) |
| [`aula-07/resolucoes/01-e6.cpp`](aula-07/resolucoes/01-e6.cpp) | C++ | [resolucoes-aula-07.md — E6](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/04%20-%20Resoluções/resolucoes-aula-07.md#e6) |
| [`aula-07/resolucoes/02-e8-exercicio-da-p-14-original/Notas.java`](aula-07/resolucoes/02-e8-exercicio-da-p-14-original/Notas.java) | Java | [resolucoes-aula-07.md — E8 — Exercício da p.14 (original)](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/04%20-%20Resoluções/resolucoes-aula-07.md#e8--exercício-da-p14-original) |
| [`aula-07/resolucoes/03-e9-desafio-da-p-16-original/NotasSemestres.java`](aula-07/resolucoes/03-e9-desafio-da-p-16-original/NotasSemestres.java) | Java | [resolucoes-aula-07.md — E9 — Desafio da p.16 (original)](../01%20-%20Aulas/Aula%2007%20-%20Tipos%20Compostos/04%20-%20Resoluções/resolucoes-aula-07.md#e9--desafio-da-p16-original) |

### aula-08

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-08/resumo/01-2-o-que-e-um-ponteiro-p-3.c`](aula-08/resumo/01-2-o-que-e-um-ponteiro-p-3.c) | C | [resumo-aula-08.md — 2. O que é um ponteiro (p.3)](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#2-o-que-é-um-ponteiro-p3) |
| [`aula-08/resumo/02-exemplo-1-c-ref-p-9/Programa.cs`](aula-08/resumo/02-exemplo-1-c-ref-p-9/Programa.cs) | C# | [resumo-aula-08.md — Exemplo 1 — C#, `ref` (p.9)](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-1--c-ref-p9) |
| [`aula-08/resumo/03-exemplo-2-java-vetor-e-inteiro-como-parametros-p/Main.java`](aula-08/resumo/03-exemplo-2-java-vetor-e-inteiro-como-parametros-p/Main.java) | Java | [resumo-aula-08.md — Exemplo 2 — Java, vetor e inteiro como parâmetros (p.10)](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-2--java-vetor-e-inteiro-como-parâmetros-p10) |
| [`aula-08/resumo/04-exemplo-3-referencias-a-objetos-em-java-p-11/Main.java`](aula-08/resumo/04-exemplo-3-referencias-a-objetos-em-java-p-11/Main.java) | Java | [resumo-aula-08.md — Exemplo 3 — Referências a objetos em Java (p.11)](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-3--referências-a-objetos-em-java-p11) |
| [`aula-08/resumo/05-exemplo-4-c-onde-cada-variavel-mora-p-14.cpp`](aula-08/resumo/05-exemplo-4-c-onde-cada-variavel-mora-p-14.cpp) | C++ | [resumo-aula-08.md — Exemplo 4 — C++, onde cada variável mora (p.14)](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-4--c-onde-cada-variável-mora-p14) |
| [`aula-08/resumo/06-exemplo-4-c-onde-cada-variavel-mora-p-14.cpp`](aula-08/resumo/06-exemplo-4-c-onde-cada-variavel-mora-p-14.cpp) | C++ | [resumo-aula-08.md — Exemplo 4 — C++, onde cada variável mora (p.14)](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-4--c-onde-cada-variável-mora-p14) |
| [`aula-08/exercicios/01-intermediario.c`](aula-08/exercicios/01-intermediario.c) | C | [exercicios-aula-08.md — Intermediário](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/03%20-%20Exercícios/exercicios-aula-08.md#intermediário) |
| [`aula-08/resolucoes/01-e4.c`](aula-08/resolucoes/01-e4.c) | C | [resolucoes-aula-08.md — E4](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/04%20-%20Resoluções/resolucoes-aula-08.md#e4) |
| [`aula-08/resolucoes/02-e8.c`](aula-08/resolucoes/02-e8.c) | C | [resolucoes-aula-08.md — E8](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/04%20-%20Resoluções/resolucoes-aula-08.md#e8) |
| [`aula-08/resolucoes/03-e10.c`](aula-08/resolucoes/03-e10.c) | C | [resolucoes-aula-08.md — E10](../01%20-%20Aulas/Aula%2008%20-%20Ponteiros/04%20-%20Resoluções/resolucoes-aula-08.md#e10) |

### aula-09

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-09/resumo/01-8-programas-com-goto-p-19-22.c`](aula-09/resumo/01-8-programas-com-goto-p-19-22.c) | C | [resumo-aula-09.md — 8. Programas com `goto` (p.19–22)](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md#8-programas-com-goto-p1922) |
| [`aula-09/resumo/02-8-programas-com-goto-p-19-22.c`](aula-09/resumo/02-8-programas-com-goto-p-19-22.c) | C | [resumo-aula-09.md — 8. Programas com `goto` (p.19–22)](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md#8-programas-com-goto-p1922) |
| [`aula-09/resumo/03-8-programas-com-goto-p-19-22.c`](aula-09/resumo/03-8-programas-com-goto-p-19-22.c) | C | [resumo-aula-09.md — 8. Programas com `goto` (p.19–22)](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/02%20-%20Resumo%20Teórico/resumo-aula-09.md#8-programas-com-goto-p1922) |
| [`aula-09/exercicios/01-avancado.c`](aula-09/exercicios/01-avancado.c) | C | [exercicios-aula-09.md — Avançado](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/03%20-%20Exercícios/exercicios-aula-09.md#avançado) |
| [`aula-09/resolucoes/01-e7-atividade-1-original-p-21-22.c`](aula-09/resolucoes/01-e7-atividade-1-original-p-21-22.c) | C | [resolucoes-aula-09.md — E7 — Atividade 1 (original, p.21–22)](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/04%20-%20Resoluções/resolucoes-aula-09.md#e7--atividade-1-original-p2122) |
| [`aula-09/resolucoes/02-e8-atividade-2-original-p-24.c`](aula-09/resolucoes/02-e8-atividade-2-original-p-24.c) | C | [resolucoes-aula-09.md — E8 — Atividade 2 (original, p.24)](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/04%20-%20Resoluções/resolucoes-aula-09.md#e8--atividade-2-original-p24) |
| [`aula-09/resolucoes/03-e9.c`](aula-09/resolucoes/03-e9.c) | C | [resolucoes-aula-09.md — E9](../01%20-%20Aulas/Aula%2009%20-%20Paradigma%20Imperativo%20I/04%20-%20Resoluções/resolucoes-aula-09.md#e9) |

### aula-10

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-10/resumo/01-4-exemplo-guiado-ordenar-dez-numeros-p-8-14.c`](aula-10/resumo/01-4-exemplo-guiado-ordenar-dez-numeros-p-8-14.c) | C | [resumo-aula-10.md — 4. Exemplo guiado: ordenar dez números (p.8–14)](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md#4-exemplo-guiado-ordenar-dez-números-p814) |
| [`aula-10/resolucoes/01-e7-exercicio-da-p-19-original.c`](aula-10/resolucoes/01-e7-exercicio-da-p-19-original.c) | C | [resolucoes-aula-10.md — E7 — Exercício da p.19 (original)](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/04%20-%20Resoluções/resolucoes-aula-10.md#e7--exercício-da-p19-original) |
| [`aula-10/resolucoes/02-e8-atividade-1-da-p-20-original.c`](aula-10/resolucoes/02-e8-atividade-1-da-p-20-original.c) | C | [resolucoes-aula-10.md — E8 — Atividade 1 da p.20 (original)](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/04%20-%20Resoluções/resolucoes-aula-10.md#e8--atividade-1-da-p20-original) |
| [`aula-10/resolucoes/03-e11.c`](aula-10/resolucoes/03-e11.c) | C | [resolucoes-aula-10.md — E11](../01%20-%20Aulas/Aula%2010%20-%20Paradigma%20Imperativo%20II/04%20-%20Resoluções/resolucoes-aula-10.md#e11) |

### aula-11

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-11/resumo/01-4-parametros-p-8-12.cpp`](aula-11/resumo/01-4-parametros-p-8-12.cpp) | C++ | [resumo-aula-11.md — 4. Parâmetros (p.8–12)](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md#4-parâmetros-p812) |
| [`aula-11/resumo/02-4-parametros-p-8-12.py`](aula-11/resumo/02-4-parametros-p-8-12.py) | Python | [resumo-aula-11.md — 4. Parâmetros (p.8–12)](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/02%20-%20Resumo%20Teórico/resumo-aula-11.md#4-parâmetros-p812) |
| [`aula-11/resolucoes/01-e7.cpp`](aula-11/resolucoes/01-e7.cpp) | C++ | [resolucoes-aula-11.md — E7](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md#e7) |
| [`aula-11/resolucoes/02-e8-atividade-1-original-p-21/Programa.cs`](aula-11/resolucoes/02-e8-atividade-1-original-p-21/Programa.cs) | C# | [resolucoes-aula-11.md — E8 — Atividade 1 (original, p.21)](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md#e8--atividade-1-original-p21) |
| [`aula-11/resolucoes/03-e9.cpp`](aula-11/resolucoes/03-e9.cpp) | C++ | [resolucoes-aula-11.md — E9](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md#e9) |
| [`aula-11/resolucoes/04-e11/Main.java`](aula-11/resolucoes/04-e11/Main.java) | Java | [resolucoes-aula-11.md — E11](../01%20-%20Aulas/Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md#e11) |

### aula-12

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-12/resumo/01-versao-1a-tudo-no-main-p-8-9/Main.java`](aula-12/resumo/01-versao-1a-tudo-no-main-p-8-9/Main.java) | Java | [resumo-aula-12.md — Versão 1a — tudo no `main` (p.8–9)](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#versão-1a--tudo-no-main-p89) |
| [`aula-12/resumo/02-versao-1b-metodos-push-e-pop-p-10-11/Main.java`](aula-12/resumo/02-versao-1b-metodos-push-e-pop-p-10-11/Main.java) | Java | [resumo-aula-12.md — Versão 1b — métodos `push` e `pop` (p.10–11)](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#versão-1b--métodos-push-e-pop-p1011) |
| [`aula-12/resumo/03-versao-1c-classe-pilha-com-atributos-privados-p/Main.java`](aula-12/resumo/03-versao-1c-classe-pilha-com-atributos-privados-p/Main.java) | Java | [resumo-aula-12.md — Versão 1c — classe `Pilha` com atributos privados (p.12–13)](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#versão-1c--classe-pilha-com-atributos-privados-p1213) |
| [`aula-12/resumo/04-versao-1d-lista-encadeada-p-14-16/Main.java`](aula-12/resumo/04-versao-1d-lista-encadeada-p-14-16/Main.java) | Java | [resumo-aula-12.md — Versão 1d — lista encadeada (p.14–16)](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#versão-1d--lista-encadeada-p1416) |
| [`aula-12/resumo/07-7-criacao-e-destruicao-de-objetos-p-28-30.cpp`](aula-12/resumo/07-7-criacao-e-destruicao-de-objetos-p-28-30.cpp) | C++ | [resumo-aula-12.md — 7. Criação e destruição de objetos (p.28–30)](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#7-criação-e-destruição-de-objetos-p2830) |
| [`aula-12/resolucoes/02-e8/Main.java`](aula-12/resolucoes/02-e8/Main.java) | Java | [resolucoes-aula-12.md — E8](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/04%20-%20Resoluções/resolucoes-aula-12.md#e8) |
| [`aula-12/resolucoes/03-e10/Main.java`](aula-12/resolucoes/03-e10/Main.java) | Java | [resolucoes-aula-12.md — E10](../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/04%20-%20Resoluções/resolucoes-aula-12.md#e10) |

### aula-13

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-13/resumo/01-3-exemplo-impressora-multifuncional-p-7-9.cpp`](aula-13/resumo/01-3-exemplo-impressora-multifuncional-p-7-9.cpp) | C++ | [resumo-aula-13.md — 3. Exemplo: impressora multifuncional (p.7–9)](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md#3-exemplo-impressora-multifuncional-p79) |
| [`aula-13/resumo/03-7-hierarquia-de-contas-p-14/Main.java`](aula-13/resumo/03-7-hierarquia-de-contas-p-14/Main.java) | Java | [resumo-aula-13.md — 7. Hierarquia de contas (p.14)](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md#7-hierarquia-de-contas-p14) |
| [`aula-13/resolucoes/01-e4/Main.java`](aula-13/resolucoes/01-e4/Main.java) | Java | [resolucoes-aula-13.md — E4](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md#e4) |
| [`aula-13/resolucoes/02-e8-atividade-1-original-p-10-11/Main.java`](aula-13/resolucoes/02-e8-atividade-1-original-p-10-11/Main.java) | Java | [resolucoes-aula-13.md — E8 — Atividade 1 (original, p.10–11)](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md#e8--atividade-1-original-p1011) |
| [`aula-13/resolucoes/03-e8-atividade-1-original-p-10-11/Main.java`](aula-13/resolucoes/03-e8-atividade-1-original-p-10-11/Main.java) | Java | [resolucoes-aula-13.md — E8 — Atividade 1 (original, p.10–11)](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md#e8--atividade-1-original-p1011) |
| [`aula-13/resolucoes/04-e9-nao-compila.cpp`](aula-13/resolucoes/04-e9-nao-compila.cpp) | C++ | [resolucoes-aula-13.md — E9](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md#e9) |
| [`aula-13/resolucoes/05-e9.cpp`](aula-13/resolucoes/05-e9.cpp) | C++ | [resolucoes-aula-13.md — E9](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md#e9) |
| [`aula-13/resolucoes/06-e10/Main.java`](aula-13/resolucoes/06-e10/Main.java) | Java | [resolucoes-aula-13.md — E10](../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/04%20-%20Resoluções/resolucoes-aula-13.md#e10) |

### aula-14

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-14/resumo/01-3-origem-e-ideia-central-p-7-8.clj`](aula-14/resumo/01-3-origem-e-ideia-central-p-7-8.clj) | Clojure | [resumo-aula-14.md — 3. Origem e ideia central (p.7–8)](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#3-origem-e-ideia-central-p78) |
| [`aula-14/resumo/04-7-4-predicados-numericos-p-21-23.clj`](aula-14/resumo/04-7-4-predicados-numericos-p-21-23.clj) | Clojure | [resumo-aula-14.md — 7.4 Predicados numéricos (p.21, 23)](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md#74-predicados-numéricos-p21-23) |
| [`aula-14/resolucoes/01-e6.c`](aula-14/resolucoes/01-e6.c) | C | [resolucoes-aula-14.md — E6](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/04%20-%20Resoluções/resolucoes-aula-14.md#e6) |
| [`aula-14/resolucoes/02-e7-atividade-1-original-p-17.clj`](aula-14/resolucoes/02-e7-atividade-1-original-p-17.clj) | Clojure | [resolucoes-aula-14.md — E7 — Atividade 1 (original, p.17)](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/04%20-%20Resoluções/resolucoes-aula-14.md#e7--atividade-1-original-p17) |
| [`aula-14/resolucoes/03-e8-atividade-2-original-p-20.clj`](aula-14/resolucoes/03-e8-atividade-2-original-p-20.clj) | Clojure | [resolucoes-aula-14.md — E8 — Atividade 2 (original, p.20)](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/04%20-%20Resoluções/resolucoes-aula-14.md#e8--atividade-2-original-p20) |
| [`aula-14/resolucoes/04-e10.clj`](aula-14/resolucoes/04-e10.clj) | Clojure | [resolucoes-aula-14.md — E10](../01%20-%20Aulas/Aula%2014%20-%20Paradigma%20Funcional/04%20-%20Resoluções/resolucoes-aula-14.md#e10) |

### aula-15

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`aula-15/resumo/01-exemplo-1-consultas-no-swi-prolog-online-p-19.pl`](aula-15/resumo/01-exemplo-1-consultas-no-swi-prolog-online-p-19.pl) | Prolog | [resumo-aula-15.md — Exemplo 1 — consultas no SWI-Prolog online (p.19)](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#exemplo-1--consultas-no-swi-prolog-online-p19) |
| [`aula-15/resumo/02-atividade-1-p-20.pl`](aula-15/resumo/02-atividade-1-p-20.pl) | Prolog | [resumo-aula-15.md — Atividade 1 (p.20)](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#atividade-1-p20) |
| [`aula-15/resumo/03-exemplo-2-programa-no-onecompiler-p-21.pl`](aula-15/resumo/03-exemplo-2-programa-no-onecompiler-p-21.pl) | Prolog | [resumo-aula-15.md — Exemplo 2 — programa no OneCompiler (p.21)](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/02%20-%20Resumo%20Teórico/resumo-aula-15.md#exemplo-2--programa-no-onecompiler-p21) |
| [`aula-15/resolucoes/01-e7-atividade-1-original-p-20.pl`](aula-15/resolucoes/01-e7-atividade-1-original-p-20.pl) | Prolog | [resolucoes-aula-15.md — E7 — Atividade 1 (original, p.20)](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/04%20-%20Resoluções/resolucoes-aula-15.md#e7--atividade-1-original-p20) |
| [`aula-15/resolucoes/02-e8-atividade-2-original-p-23.pl`](aula-15/resolucoes/02-e8-atividade-2-original-p-23.pl) | Prolog | [resolucoes-aula-15.md — E8 — Atividade 2 (original, p.23)](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/04%20-%20Resoluções/resolucoes-aula-15.md#e8--atividade-2-original-p23) |
| [`aula-15/resolucoes/03-e9.pl`](aula-15/resolucoes/03-e9.pl) | Prolog | [resolucoes-aula-15.md — E9](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/04%20-%20Resoluções/resolucoes-aula-15.md#e9) |
| [`aula-15/resolucoes/04-e10.pl`](aula-15/resolucoes/04-e10.pl) | Prolog | [resolucoes-aula-15.md — E10](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/04%20-%20Resoluções/resolucoes-aula-15.md#e10) |
| [`aula-15/resolucoes/05-e10.pl`](aula-15/resolucoes/05-e10.pl) | Prolog | [resolucoes-aula-15.md — E10](../01%20-%20Aulas/Aula%2015%20-%20Paradigma%20Lógico/04%20-%20Resoluções/resolucoes-aula-15.md#e10) |

### lista-01

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`lista-01/resolucao/01-q7.clj`](lista-01/resolucao/01-q7.clj) | Clojure | [resolucao-lista-01.md — Q7](../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/02%20-%20Resolução/resolucao-lista-01.md#q7) |
| [`lista-01/resolucao/02-q11.pl`](lista-01/resolucao/02-q11.pl) | Prolog | [resolucao-lista-01.md — Q11](../02%20-%20Listas%20de%20Exercícios/Lista%2001%20-%20Revisão%20I/02%20-%20Resolução/resolucao-lista-01.md#q11) |

### lista-02

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`lista-02/resolucao/01-q4.c`](lista-02/resolucao/01-q4.c) | C | [resolucao-lista-02.md — Q4](../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q4) |
| [`lista-02/resolucao/02-q5.c`](lista-02/resolucao/02-q5.c) | C | [resolucao-lista-02.md — Q5](../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q5) |
| [`lista-02/resolucao/03-q11/Main.java`](lista-02/resolucao/03-q11/Main.java) | Java | [resolucao-lista-02.md — Q11](../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/02%20-%20Resolução/resolucao-lista-02.md#q11) |

### simulados

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`simulados/resolucao-01/01-parte-a-comentarios.c`](simulados/resolucao-01/01-parte-a-comentarios.c) | C | [resolucao-simulado-01.md — Parte A — comentários](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md#parte-a--comentários) |
| [`simulados/resolucao-01/02-parte-a-comentarios.c`](simulados/resolucao-01/02-parte-a-comentarios.c) | C | [resolucao-simulado-01.md — Parte A — comentários](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md#parte-a--comentários) |
| [`simulados/resolucao-01/03-parte-a-comentarios.pl`](simulados/resolucao-01/03-parte-a-comentarios.pl) | Prolog | [resolucao-simulado-01.md — Parte A — comentários](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md#parte-a--comentários) |
| [`simulados/resolucao-01/04-13.c`](simulados/resolucao-01/04-13.c) | C | [resolucao-simulado-01.md — 13](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md#13) |
| [`simulados/resolucao-01/05-14.clj`](simulados/resolucao-01/05-14.clj) | Clojure | [resolucao-simulado-01.md — 14](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md#14) |
| [`simulados/resolucao-01/06-15.pl`](simulados/resolucao-01/06-15.pl) | Prolog | [resolucao-simulado-01.md — 15](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md#15) |
| [`simulados/resolucao-02/01-parte-a-comentarios.c`](simulados/resolucao-02/01-parte-a-comentarios.c) | C | [resolucao-simulado-02.md — Parte A — comentários](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-02.md#parte-a--comentários) |
| [`simulados/resolucao-02/02-12.c`](simulados/resolucao-02/02-12.c) | C | [resolucao-simulado-02.md — 12](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-02.md#12) |
| [`simulados/resolucao-02/03-13.c`](simulados/resolucao-02/03-13.c) | C | [resolucao-simulado-02.md — 13](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-02.md#13) |
| [`simulados/resolucao-02/04-14.c`](simulados/resolucao-02/04-14.c) | C | [resolucao-simulado-02.md — 14](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-02.md#14) |
| [`simulados/resolucao-02/05-15.c`](simulados/resolucao-02/05-15.c) | C | [resolucao-simulado-02.md — 15](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-02.md#15) |
| [`simulados/resolucao-03/01-parte-a-comentarios.pl`](simulados/resolucao-03/01-parte-a-comentarios.pl) | Prolog | [resolucao-simulado-03.md — Parte A — comentários](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#parte-a--comentários) |
| [`simulados/resolucao-03/02-11/Main.java`](simulados/resolucao-03/02-11/Main.java) | Java | [resolucao-simulado-03.md — 11](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#11) |
| [`simulados/resolucao-03/03-12/Main.java`](simulados/resolucao-03/03-12/Main.java) | Java | [resolucao-simulado-03.md — 12](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#12) |
| [`simulados/resolucao-03/04-13.clj`](simulados/resolucao-03/04-13.clj) | Clojure | [resolucao-simulado-03.md — 13](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#13) |
| [`simulados/resolucao-03/05-14.pl`](simulados/resolucao-03/05-14.pl) | Prolog | [resolucao-simulado-03.md — 14](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#14) |
| [`simulados/resolucao-03/06-15/Main.java`](simulados/resolucao-03/06-15/Main.java) | Java | [resolucao-simulado-03.md — 15](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#15) |
| [`simulados/resolucao-03/07-15.clj`](simulados/resolucao-03/07-15.clj) | Clojure | [resolucao-simulado-03.md — 15](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#15) |
| [`simulados/resolucao-03/08-15.pl`](simulados/resolucao-03/08-15.pl) | Prolog | [resolucao-simulado-03.md — 15](../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-03.md#15) |
| [`simulados/simulado-01/01-parte-a-questoes-objetivas-1-ponto-cada.c`](simulados/simulado-01/01-parte-a-questoes-objetivas-1-ponto-cada.c) | C | [simulado-01.md — Parte A — Questões objetivas (1 ponto cada)](../04%20-%20Provas%20e%20Avaliações/Simulados/simulado-01.md#parte-a--questões-objetivas-1-ponto-cada) |
| [`simulados/simulado-02/01-parte-b-questoes-discursivas-e-de-programacao-2.c`](simulados/simulado-02/01-parte-b-questoes-discursivas-e-de-programacao-2.c) | C | [simulado-02.md — Parte B — Questões discursivas e de programação (2 pontos cada)](../04%20-%20Provas%20e%20Avaliações/Simulados/simulado-02.md#parte-b--questões-discursivas-e-de-programação-2-pontos-cada) |

### revisoes

| Programa | Linguagem | Origem |
| --- | --- | --- |
| [`revisoes/quadros-comparativos/01-2-um-mesmo-problema-nos-quatro-paradigmas.c`](revisoes/quadros-comparativos/01-2-um-mesmo-problema-nos-quatro-paradigmas.c) | C | [quadros-comparativos.md — 2. Um mesmo problema nos quatro paradigmas](../06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md#2-um-mesmo-problema-nos-quatro-paradigmas) |
| [`revisoes/quadros-comparativos/02-2-um-mesmo-problema-nos-quatro-paradigmas/Main.java`](revisoes/quadros-comparativos/02-2-um-mesmo-problema-nos-quatro-paradigmas/Main.java) | Java | [quadros-comparativos.md — 2. Um mesmo problema nos quatro paradigmas](../06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md#2-um-mesmo-problema-nos-quatro-paradigmas) |
| [`revisoes/quadros-comparativos/03-2-um-mesmo-problema-nos-quatro-paradigmas.clj`](revisoes/quadros-comparativos/03-2-um-mesmo-problema-nos-quatro-paradigmas.clj) | Clojure | [quadros-comparativos.md — 2. Um mesmo problema nos quatro paradigmas](../06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md#2-um-mesmo-problema-nos-quatro-paradigmas) |
| [`revisoes/quadros-comparativos/04-2-um-mesmo-problema-nos-quatro-paradigmas.pl`](revisoes/quadros-comparativos/04-2-um-mesmo-problema-nos-quatro-paradigmas.pl) | Prolog | [quadros-comparativos.md — 2. Um mesmo problema nos quatro paradigmas](../06%20-%20Revisões%20e%20Sínteses/quadros-comparativos.md#2-um-mesmo-problema-nos-quatro-paradigmas) |
| [`revisoes/questoes-integradoras/01-questoes-integradoras.c`](revisoes/questoes-integradoras/01-questoes-integradoras.c) | C | [questoes-integradoras.md — Questões integradoras](../06%20-%20Revisões%20e%20Sínteses/questoes-integradoras.md#questões-integradoras) |
| [`revisoes/resolucao-questoes-integradora/01-qi2.c`](revisoes/resolucao-questoes-integradora/01-qi2.c) | C | [resolucao-questoes-integradoras.md — QI2](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi2) |
| [`revisoes/resolucao-questoes-integradora/02-qi3.c`](revisoes/resolucao-questoes-integradora/02-qi3.c) | C | [resolucao-questoes-integradoras.md — QI3](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi3) |
| [`revisoes/resolucao-questoes-integradora/03-qi4.c`](revisoes/resolucao-questoes-integradora/03-qi4.c) | C | [resolucao-questoes-integradoras.md — QI4](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi4) |
| [`revisoes/resolucao-questoes-integradora/04-qi5/Main.java`](revisoes/resolucao-questoes-integradora/04-qi5/Main.java) | Java | [resolucao-questoes-integradoras.md — QI5](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi5) |
| [`revisoes/resolucao-questoes-integradora/05-qi7.c`](revisoes/resolucao-questoes-integradora/05-qi7.c) | C | [resolucao-questoes-integradoras.md — QI7](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi7) |
| [`revisoes/resolucao-questoes-integradora/06-qi7.clj`](revisoes/resolucao-questoes-integradora/06-qi7.clj) | Clojure | [resolucao-questoes-integradoras.md — QI7](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi7) |
| [`revisoes/resolucao-questoes-integradora/07-qi7.pl`](revisoes/resolucao-questoes-integradora/07-qi7.pl) | Prolog | [resolucao-questoes-integradoras.md — QI7](../06%20-%20Revisões%20e%20Sínteses/resolucao-questoes-integradoras.md#qi7) |
