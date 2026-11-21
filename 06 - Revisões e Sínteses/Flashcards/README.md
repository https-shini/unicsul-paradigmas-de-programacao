<!-- nav:topo -->
[Início](../../README.md) › [06 - Revisões e Sínteses](../README.md) › **Flashcards** · [Mapa](../../MAPA.md)
<!-- /nav:topo -->

# Flashcards (Anki)

> **[Explicação elaborada]** Baralho de repetição espaçada gerado a partir do [glossário](../../07%20-%20Glossário/glossario.md) e dos [quadros comparativos](../quadros-comparativos.md). Não é material do professor.

| Baralho | Cartões | Conteúdo |
| --- | :-: | --- |
| PLP › 1 Glossário | 95 | Um cartão por termo: definição, exemplo e aulas |
| PLP › 2 Comparações | 34 | "Diferencie X e Y" — o formato mais cobrado nas listas |
| PLP › 3 Leitura de código | 14 | "O que este trecho imprime?" em C, Java, PHP, Python, Clojure e Prolog |
| **Total** | **143** | |

## Como usar

1. Instale o [Anki](https://apps.ankiweb.net/) (computador), o AnkiDroid (Android) ou o AnkiMobile (iOS).
2. Baixe [`plp-flashcards.apkg`](plp-flashcards.apkg) e abra o arquivo (no Anki: **Arquivo › Importar**).
3. Estude um pouco por dia; o Anki mostra cada cartão de novo na hora certa para fixar o conteúdo.

Cada cartão tem etiquetas `aula-NN`, `glossario`, `comparacao` ou `codigo`. No Anki, a busca `tag:aula-14` filtra os cartões de uma aula — útil na semana da prova.

**Sem Anki?** O arquivo [`plp-flashcards.tsv`](plp-flashcards.tsv) pode ser importado em outros aplicativos de flashcards (Quizlet, RemNote, Mochi) ou aberto numa planilha.

**Para atualizar:** edite os termos em `ferramentas/geradores/gerar_glossario.py` ou as listas `COMPARACOES` e `CODIGO` em `ferramentas/geradores/gerar_flashcards.py` e rode `python3 ferramentas/geradores/gerar_flashcards.py`. Reimportar o `.apkg` atualiza os cartões sem duplicar e sem perder o seu histórico.


<!-- nav:rodape -->

---

**Links para esta página (3):** [04 — Provas e Avaliações](../../04%20-%20Provas%20e%20Avaliações/README.md) · [06 — Revisões e Sínteses](../README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../README.md)

<!-- /nav:rodape -->
