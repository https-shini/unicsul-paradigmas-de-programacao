<!-- nav:topo -->
[Início](../../README.md) › [06 - Revisões e Sínteses](../README.md) › [Revisões por Unidade](README.md) · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Revisão da Unidade 3 — Paradigma orientado a objetos (Aulas 12–13)

> **[Explicação elaborada]** Agrupamento organizacional deste repositório, **não** uma divisão oficial do professor. Legenda: [Convenções](../../README.md#convenções-de-marcação).

| Aula | Tema | Resumo | Exercícios |
| --- | --- | --- | --- |
| 12 | Classes, objetos, encapsulamento, pilha em Java e C++ | [resumo](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md) | [exercícios](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/03%20-%20Exercícios/exercicios-aula-12.md) |
| 13 | Herança, interfaces, polimorfismo | [resumo](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md) | [exercícios](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/03%20-%20Exercícios/exercicios-aula-13.md) |

## Conceitos que você precisa dominar

- [ ] Motivação histórica da OO (12)
- [ ] A evolução da **pilha** do `main` até a classe com lista encadeada, e o que cada passo melhora (12)
- [ ] **Abstração**, **TDA**, **encapsulamento** e **ocultação de informação** (12)
- [ ] **Classe × objeto**; atributos e métodos; **modificadores de acesso** (12)
- [ ] **Construtor**, **destrutor**, `new`/`delete` em C++ × **coleta de lixo** em Java (12)
- [ ] **Herança**: superclasse, subclasse, reuso (13)
- [ ] **Herança múltipla** em C++ e seus problemas; **interfaces** em Java como alternativa (13)
- [ ] **Polimorfismo estático** (sobrecarga) × **dinâmico** (sobrescrita + vinculação tardia) (13)
- [ ] **Classe abstrata × interface** (13)

## Confusões frequentes

| Confusão | Esclarecimento |
| --- | --- |
| Sobrecarga × sobrescrita | Sobre**carga**: mesmo nome, parâmetros **diferentes**, escolha na compilação. Sobre**scrita**: mesma assinatura redefinida na subclasse, escolha em execução. |
| Encapsulamento = deixar tudo `private` | Encapsular é **agrupar** dados e operações e **controlar o acesso**. A interface pública é parte do encapsulamento. |
| Java tem destrutor | Java não tem destrutor; a coleta de lixo libera objetos sem referência. |
| Interface Java não pode ter código | No modelo clássico (slide), não. Desde o Java 8, pode ter métodos `default` e `static`. |
| Herança múltipla é proibida em OO | É permitida em C++ e Python; Java e C# a evitam por complexidade. |

## Autoteste

1. Que problema da Versão 1a da pilha a Versão 1c resolve? → [Aula 12, §3](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#3-o-exemplo-progressivo-da-pilha-p716)
2. Explique a função do destrutor `~Pilha()` na versão com lista encadeada. → [Aula 12, §7](../../01%20-%20Aulas/Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#7-criação-e-destruição-de-objetos-p2830)
3. Como reescrever a impressora multifuncional em Java? → [Aula 13, §4](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md#4-atividade-o-mesmo-em-java-p1011)
4. Na hierarquia de contas, qual versão de um método é chamada quando `Conta c = new ContaEspecial();`? → [Aula 13, §7](../../01%20-%20Aulas/Aula%2013%20-%20Paradigma%20Orientado%20a%20Objetos%20II/02%20-%20Resumo%20Teórico/resumo-aula-13.md#7-hierarquia-de-contas-p14)

**Questões do professor sobre esta unidade:** [Lista 02, Q10–Q11](../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md).

**Anterior:** [Unidade 2](unidade-2-imperativo.md) · **Próxima:** [Unidade 4 — Funcional e lógico](unidade-4-funcional-e-logico.md).


<!-- nav:rodape -->

---

← [Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)](unidade-2-imperativo.md) · [Revisão da Unidade 4 — Paradigmas funcional e lógico (Aulas…](unidade-4-funcional-e-logico.md) →

**Links para esta página (5):** [Cronograma](../../00%20-%20Planejamento%20e%20Organização/cronograma.md) · [06 — Revisões e Sínteses](../README.md) · [Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)](unidade-2-imperativo.md) · [Revisão da Unidade 4 — Paradigmas funcional e lógico (Aulas…](unidade-4-funcional-e-logico.md) · [Guia de estudo para as avaliações](../guia-de-estudo-para-provas.md)

<!-- /nav:rodape -->
