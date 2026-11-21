# Guia de estudo para as avaliações

> **[Explicação elaborada]** Roteiro de revisão montado a partir do plano de ensino e das duas listas de revisão do professor. **Não antecipa o conteúdo das provas.** Confirme sempre com o professor o que será cobrado em cada avaliação. Legenda: [Convenções](../README.md#convenções-de-marcação).

## 1. O que as listas do professor revelam

As duas listas de revisão (`Aula16a` e `Aula16b`) são o único indicativo do **estilo** de questão no material:

| Característica | Lista 01 | Lista 02 |
| --- | --- | --- |
| Questões | 11 discursivas | 12 discursivas |
| Abrangência | Funcional e lógico (Aulas 09, 14, 15) | Disciplina inteira (Aulas 02–15) |
| Verbos mais usados | explique, diferencie, escreva | diferencie, compare, explique, conceitue |
| Código | Clojure (avaliar e escrever) e Prolog (consultas) | Nenhum código exigido |

**Conclusão prática:** treine **respostas discursivas comparativas**, com definição, diferença, exemplo e consequência. Saiba **ler e escrever** Clojure e Prolog em pequenos trechos.

## 2. Estrutura de uma boa resposta discursiva

Para "diferencie X e Y":

1. **Defina** X e Y em uma frase cada.
2. **Diferencie** pelo critério central (o *quando*, o *como*, o *onde*).
3. **Exemplifique** com uma linguagem ou um trecho de código das aulas.
4. **Conclua** com a consequência (vantagem/desvantagem, impacto em legibilidade, confiabilidade, desempenho).

> **Exemplo (escopo):** "No escopo **estático**, a variável não local é resolvida pela posição da declaração no texto; no **dinâmico**, pela sequência de chamadas em execução. Em C, que usa escopo estático, `f()` chamada por `g()` vê a global `n = 10`, mesmo que `g` tenha um `n = 20`; com escopo dinâmico, veria 20. Por isso o escopo dinâmico reduz a legibilidade: não basta ler a função para saber a que variável o nome se refere."

## 3. Plano de revisão em cinco sessões

| Sessão | Conteúdo | Material | Teste final |
| --- | --- | --- | --- |
| 1 | Fundamentos (02–05) | [Revisão da Unidade 1](Revisões%20por%20Unidade/unidade-1-fundamentos.md), quadros 1, 3–5 | Lista 02, Q1–Q4 |
| 2 | Tipos e memória (06–08) | [Revisão da Unidade 1](Revisões%20por%20Unidade/unidade-1-fundamentos.md), quadros 6–7 | Lista 02, Q5–Q6 |
| 3 | Imperativo (09–11) | [Revisão da Unidade 2](Revisões%20por%20Unidade/unidade-2-imperativo.md), quadros 8–10, artigo de Dijkstra | Lista 02, Q7–Q9 |
| 4 | OO (12–13) | [Revisão da Unidade 3](Revisões%20por%20Unidade/unidade-3-orientacao-a-objetos.md), quadros 11–12 | Lista 02, Q10–Q11 |
| 5 | Funcional e lógico (14–15) | [Revisão da Unidade 4](Revisões%20por%20Unidade/unidade-4-funcional-e-logico.md), quadro 13 | Lista 01 inteira; Lista 02, Q12 |
| Final | Tudo | [Simulado 01](../04%20-%20Provas%20e%20Avaliações/Simulados/simulado-01.md), [questões integradoras](questoes-integradoras.md) | Corrigir com as resoluções |

Os quadros estão em [quadros-comparativos.md](quadros-comparativos.md).

## 4. Os 20 pontos que mais aparecem

1. Os quatro paradigmas e a classificação procedural × declarativa.
2. Por que o imperativo é ligado à arquitetura de von Neumann.
3. Compilação × interpretação × híbrida; papel da JVM.
4. Lexema, token e padrão; erro léxico × sintático.
5. Os seis atributos da variável.
6. Escopo estático × dinâmico.
7. Tipagem estática × dinâmica; forte × fraca; coerção.
8. Alocação estática × dinâmica; pilha × heap; ponteiros.
9. Turing-completude.
10. `goto`, Dijkstra, Böhm e Jacopini, programação estruturada.
11. Abstração procedural; acoplamento e coesão.
12. TDA e encapsulamento.
13. Os quatro modelos de passagem de parâmetros; `ref`/`out`/`in`.
14. Classe, objeto, modificadores de acesso.
15. Destrutor × coleta de lixo.
16. Herança simples × múltipla; interfaces.
17. Sobrecarga × sobrescrita.
18. Características do funcional; puras × impuras.
19. Notação prefixa em Clojure; `Ratio`, `quot`, `rem`.
20. Fatos, regras, consultas e unificação em Prolog.

## 5. Armadilhas

- Repetir as **imprecisões dos slides** sem ressalva: ver [erratas](erratas-e-inconsistencias.md), em especial "baixa coesão" e "uso excessivo de `goto`".
- Confundir **eixos independentes**: estática/dinâmica × forte/fraca; escopo × tempo de vida.
- Em Clojure, esquecer que o **operador vem primeiro** e que `/` entre inteiros gera fração na JVM.
- Em Prolog, usar **maiúscula** em constantes (`Joao` é variável) ou `=` no lugar de `is` para calcular.
- Responder "sobrecarga" quando a pergunta é sobre **vinculação dinâmica**.

## 6. Na véspera

- [ ] Reler o [resumo geral](resumo-geral-da-disciplina.md).
- [ ] Refazer de memória os quadros 1, 6, 8 e 13.
- [ ] Revisar o [glossário](../07%20-%20Glossário/glossario.md).
- [ ] Conferir as regras de avaliação na [ementa](../00%20-%20Planejamento%20e%20Organização/ementa.md#avaliação).
