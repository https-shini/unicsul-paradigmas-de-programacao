<!-- nav:topo -->
[Início](../README.md) › **ferramentas** · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# Ferramentas

Scripts que mantêm a base de conhecimento funcionando: executam o código das notas, corrigem exercícios, testam os projetos e **geram** as partes derivadas (galerias, navegação, `codigo/`, glossário, flashcards, apostila) a partir dos arquivos Markdown, que são sempre a fonte.

## Para estudar

| Comando | Para quê |
| --- | --- |
| `python3 ferramentas/verificar.py --listar` | Lista os exercícios com correção automática |
| `python3 ferramentas/verificar.py 14 E8 minha.clj` | Corrige a sua solução de um exercício (aula, questão, arquivo) |
| `python3 ferramentas/testar_projetos.py P1` | Testa um projeto prático (pasta `inicial/` por padrão) |
| `python3 ferramentas/rodar.py codigo/aula-14/...` | Executa qualquer programa de `codigo/` |

## Para manter o repositório

Depois de editar notas, rode os geradores **nesta ordem** e confira com as verificações:

```bash
python3 ferramentas/geradores/gerar_glossario.py      # só se mudou o glossário (dados no próprio script)
python3 ferramentas/geradores/gerar_galerias.py       # só se entrou um PDF novo
python3 ferramentas/gerar_codigo.py                   # código das notas → codigo/
python3 ferramentas/geradores/gerar_navegacao.py      # trilhas, índices, backlinks, links de página, MAPA.md
python3 ferramentas/verificar_links.py                # links e âncoras internos
```

| Script | O que gera ou confere |
| --- | --- |
| [`geradores/gerar_navegacao.py`](geradores/gerar_navegacao.py) | Trilha no topo e rodapé (aula, anterior/próxima, *links para esta página*) de cada nota; índice `README.md` nas pastas sem um; links das citações `p.N` para a página do slide; [`MAPA.md`](../MAPA.md) |
| [`geradores/gerar_galerias.py`](geradores/gerar_galerias.py) | Páginas dos PDFs originais em imagem (WebP) e a galeria `README.md` de cada pasta de slides, com o texto pesquisável de cada página |
| [`gerar_codigo.py`](gerar_codigo.py) | A pasta [`codigo/`](../codigo/README.md), com um arquivo por programa e um `README.md` por pasta |
| [`geradores/gerar_glossario.py`](geradores/gerar_glossario.py) · [`gerar_flashcards.py`](geradores/gerar_flashcards.py) · [`gerar_referencias.py`](geradores/gerar_referencias.py) · [`gerar_readmes_aulas.py`](geradores/gerar_readmes_aulas.py) | Glossário, baralho do Anki, catálogo de referências e páginas de visão geral das aulas |
| [`geradores/gerar_apostila.py`](geradores/gerar_apostila.py) | Os PDFs da apostila (requer pandoc e Chrome) |
| [`testar_codigo.py`](testar_codigo.py) | Executa todos os blocos de código das notas e confere a saída |
| [`verificar_links.py`](verificar_links.py) · [`verificar_mermaid.mjs`](verificar_mermaid.mjs) · [`verificar_bib.py`](verificar_bib.py) | Links e âncoras, sintaxe dos diagramas, BibTeX |
| [`instalar-ambiente.sh`](instalar-ambiente.sh) | Instala as linguagens (usado pelo CI e pelo Codespaces) |
| [`motores.py`](motores.py) · [`blocos.py`](blocos.py) · [`tau.js`](tau.js) | Bibliotecas internas: como executar cada linguagem e como ler os blocos das notas |

O [CI](../.github/workflows/validacao.yml) roda as verificações a cada envio e falha se algum arquivo gerado estiver desatualizado.


<!-- nav:rodape -->

---

**Links para esta página (1):** [Guia da base de conhecimento](../00%20-%20Planejamento%20e%20Organização/guia-da-base-de-conhecimento.md)

<!-- /nav:rodape -->
