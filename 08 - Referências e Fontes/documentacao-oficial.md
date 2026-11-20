# Documentação oficial das linguagens

> **[Complemento]** Especificações e documentação oficial das linguagens usadas nos slides. Elas são a **fonte primária** para confirmar o comportamento de uma construção, especialmente quando o material didático simplifica ou diverge da norma (ver [erratas](../06%20-%20Revisões%20e%20Sínteses/erratas-e-inconsistencias.md)). Links conferidos em 19/11/2026. Marcações: [Convenções](../README.md#convenções-de-marcação).

**Como usar:** a coluna "Norma" indica o documento que **define** a linguagem; "Documentação" indica onde consultar no dia a dia; "Ponto da disciplina" mostra onde a consulta é útil.

| Linguagem | Aulas | Norma | Documentação | Ponto da disciplina |
| --- | --- | --- | --- | --- |
| C | 04, 06–10 | ISO/IEC 9899 (edição atual: C23, publicada em 2024) | [cppreference — C](https://en.cppreference.com/w/c) · [manuais do GCC](https://gcc.gnu.org/onlinedocs/) | Categorias de tokens (Aula 04); tamanhos mínimos de tipos e conversões implícitas (Aula 06); ponteiros e `malloc`/`free` (Aula 08) |
| C++ | 08, 12, 13 | ISO/IEC 14882 (edição atual: C++23, publicada em 2024) | [cppreference — C++](https://en.cppreference.com/w/cpp) · [`new`](https://en.cppreference.com/w/cpp/language/new) · [destrutores](https://en.cppreference.com/w/cpp/language/destructor) · [classes derivadas](https://en.cppreference.com/w/cpp/language/derived_class) | `new int(4)` × `new int[4]` (Aula 08); destrutor e `delete` (Aula 12); herança múltipla (Aula 13) |
| Java | 02, 03, 06, 07, 11–13 | *Java Language Specification* e *Java Virtual Machine Specification* | [JLS e JVMS](https://docs.oracle.com/javase/specs/) · [Java Tutorials](https://docs.oracle.com/javase/tutorial/java/javaOO/) · [Interfaces e herança](https://docs.oracle.com/javase/tutorial/java/IandI/) · [enum](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) · [arrays](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html) | Bytecode e JVM (Aula 03); conversões e tipagem forte (Aula 06); interfaces com métodos `default` desde o Java 8 (Aula 13) |
| C# | 03, 11 | ECMA-334 (*C# Language Specification*) | [Documentação do C# (Microsoft Learn)](https://learn.microsoft.com/pt-br/dotnet/csharp/) · [parâmetros de método](https://learn.microsoft.com/pt-br/dotnet/csharp/language-reference/keywords/method-parameters) | CLR e CIL (Aula 03); `ref`, `out`, `in` e `ref readonly` (Aula 11) |
| Python | 03, 06, 11 | Definida pela implementação de referência (CPython) e pela *Python Language Reference* | [Documentação do Python em português](https://docs.python.org/pt-br/3/) · [argumentos nomeados](https://docs.python.org/pt-br/3/tutorial/controlflow.html#keyword-arguments) | Bytecode `.pyc` (Aula 03); `TypeError` em `10 + "20"` (Aula 06); parâmetros nomeados e valores padrão (Aula 11) |
| PHP | 06 | Definida pela implementação oficial | [Manual do PHP em português](https://www.php.net/manual/pt_BR/) · [conversão automática de tipos](https://www.php.net/manual/pt_BR/language.types.type-juggling.php) | `10 + "20" + 10.2 = 40.2` e tipagem fraca (Aula 06) |
| Perl | 05, 06 | Definida pela implementação oficial | [perlsub](https://perldoc.perl.org/perlsub) · [perldoc](https://perldoc.perl.org/) | `my` (escopo estático) × `local` (escopo dinâmico) (Aula 05); coerção string ↔ número (Aula 06) |
| Pascal | 02, 09 | ISO 7185 (Pascal padrão) e ISO/IEC 10206 (Pascal estendido) | [Documentação do Free Pascal](https://www.freepascal.org/docs.html) | Programa do "dobro" (Aula 02); estruturas de controle (Aula 09) |
| Clojure | 14 | Definida pela implementação de referência (JVM) | [Referência — leitor e formas especiais](https://clojure.org/reference/reader) · [Learn Clojure](https://clojure.org/guides/learn/clojure) · [números e `Ratio`](https://clojure.org/reference/data_structures#Numbers) · [diferenças do ClojureScript](https://clojurescript.org/about/differences) | Notação prefixa, `quot`, `rem`, `Ratio`, `def`, `not=` (Aula 14) |
| Prolog | 02, 15 | ISO/IEC 13211-1:1995 (Prolog padrão) | [Manual do SWI-Prolog](https://www.swi-prolog.org/pldoc/) · [SWISH](https://swish.swi-prolog.org/) · [Tau-Prolog](http://tau-prolog.org/) | Fatos, regras, `findall/3`, `read/1`, `->` (Aula 15) |

## Observações

- **Normas ISO são pagas.** Para consulta, use o [cppreference](https://en.cppreference.com/), que acompanha as normas de C e C++ e indica em que versão cada recurso surgiu.
- **Os Java Tutorials da Oracle cobrem até o Java 8.** Para recursos mais novos (por exemplo, `record` e `sealed`), consulte a JLS da versão correspondente.
- **ClojureScript × Clojure.** O código Clojure deste repositório foi testado com ClojureScript ([nbb](https://github.com/babashka/nbb)), que não tem o tipo `Ratio`. A página de diferenças explica esse e outros casos.
- **Prolog.** As aulas usam SWI-Prolog (via SWISH e OneCompiler); este repositório validou o código com Tau-Prolog. Ambos seguem a norma ISO nos recursos usados na disciplina.
