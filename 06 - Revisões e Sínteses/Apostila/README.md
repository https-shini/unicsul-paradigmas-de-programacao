# Apostila em PDF

> **[Explicação elaborada]** Versões em PDF do conteúdo deste repositório, para ler offline, imprimir ou anotar no tablet. **Não são material oficial do professor** e não substituem os slides originais.

| Arquivo | Páginas | Conteúdo |
| --- | :-: | --- |
| [`apostila-plp.pdf`](apostila-plp.pdf) | ~150 | Resumo geral, resumos das 15 aulas (e do artigo de Dijkstra), quadros comparativos, mapas conceituais, erratas e glossário |
| [`caderno-de-exercicios-plp.pdf`](caderno-de-exercicios-plp.pdf) | ~155 | Exercícios das aulas, Listas 01 e 02, simulados 01–03 e questões integradoras; **resoluções comentadas numa parte separada, no fim** |

## Como usar

- O sumário e os links internos são clicáveis, e o leitor de PDF mostra os marcadores (*bookmarks*) por parte e capítulo.
- Cada capítulo começa com o caminho do arquivo de origem no repositório, em cinza.
- Links para arquivos que não estão no PDF (slides originais, código, listas) apontam para o GitHub.
- Os diagramas Mermaid saem desenhados; os blocos de código, com destaque de sintaxe.
- No caderno, tente resolver tudo antes de abrir a última parte. As questões de programação também podem ser conferidas com `python3 ferramentas/verificar.py` (ver o [README principal](../../README.md)).

## Como gerar de novo

Os PDFs são gerados dos arquivos Markdown, que são a fonte. Depois de alterar um resumo ou uma resolução:

```bash
bash ferramentas/instalar-ambiente.sh --geradores   # pandoc e dependências Node (uma vez)
python3 ferramentas/geradores/gerar_apostila.py     # gera os dois PDFs
```

Requer **pandoc** e **Google Chrome ou Chromium** (usado em modo *headless* para imprimir o PDF). Opções: `--so teoria` ou `--so exercicios` gera um volume só; `--html` guarda também o HTML intermediário.
