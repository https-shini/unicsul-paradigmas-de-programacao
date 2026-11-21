<!-- nav:topo -->
[Início](../README.md) › [00 - Planejamento e Organização](README.md) · [Mapa](../MAPA.md)
<!-- /nav:topo -->

# Guia da base de conhecimento

Este repositório funciona como um **caderno digital navegável no próprio GitHub**, no estilo do Notion ou do Obsidian: todo o conteúdo está em Markdown, toda pasta tem uma página de índice e as notas se ligam umas às outras por links. Nada depende de ferramenta externa para ser lido; ferramentas externas (Obsidian, VS Code, Codespaces) são opcionais.

> **Requisito do projeto.** Esta premissa vale para todo o planejamento, desenvolvimento e organização do repositório. Qualquer conteúdo novo deve seguir os princípios abaixo.

## Princípios

1. **Markdown primeiro.** Documentação, anotações, explicações, resumos e exercícios são arquivos `.md`, legíveis por inteiro no navegador.
2. **Toda pasta tem um `README.md`.** O GitHub exibe o `README.md` logo abaixo da lista de arquivos ao abrir uma pasta: ele é a página de índice, como uma página-mãe do Notion.
3. **Tudo é interligado.** As notas usam links relativos (`[texto](../pasta/nota.md#secao)`), que funcionam no GitHub, no Obsidian e no VS Code. Cada nota mostra também quem aponta para ela.
4. **PDFs também são navegáveis.** O PDF original fica intacto e ganha uma **galeria**: cada página vira uma imagem dentro de uma nota, com o texto da página logo abaixo, que a busca encontra.
5. **Imagens dentro das notas.** Figuras dos slides e fotos aparecem no meio do texto, onde são discutidas.
6. **Código executável.** Os exemplos ficam em blocos de código com linguagem e são testados automaticamente. Os mesmos programas estão em arquivos separados em [`codigo/`](../codigo/README.md).
7. **Diagramas como texto.** Fluxos, hierarquias e mapas são escritos em [Mermaid](https://mermaid.js.org/), que o GitHub e o Obsidian desenham sozinhos.
8. **Origem sempre indicada.** `[Material original]`, `[Explicação elaborada]`, `[Complemento]`, `[Atenção]`, `[Exercício autoral]` e `[Resolução elaborada]` mostram de onde vem cada trecho.

## Como navegar

| Recurso | Onde aparece | Para quê |
| --- | --- | --- |
| **Trilha** (*breadcrumb*) | primeira linha de cada nota: `Início › 01 - Aulas › Aula 12 › …` | Subir para qualquer nível |
| **Barra da aula** | rodapé das notas de uma aula: `Aula 12: Visão geral · Slides · Resumo · …` | Pular entre as partes da mesma aula |
| **Anterior / próxima** | rodapé: `← Aula 11 · Resumo · Aula 13 · Resumo →` | Ler em sequência, como um livro |
| **Links para esta página** | rodapé | Ver todas as notas que citam a atual (os *backlinks* do Obsidian) |
| **Citações de página** | `p.12`, `Aula08 p.13` no texto | Abrir a página exata do slide citado |
| **[Mapa do repositório](../MAPA.md)** | raiz | Todas as notas numa só página, em árvore |
| **[Índice das aulas](../01%20-%20Aulas/README.md)** | `01 - Aulas` | Tabela com slides, resumo, exercícios e resoluções de cada aula |
| **Busca do GitHub** | tecla `/` no repositório | Procurar uma palavra em todas as notas, inclusive no texto dos slides |
| **Localizador de arquivos** | tecla `t` | Abrir um arquivo pelo nome |
| **Editor no navegador** | tecla `.` (abre o github.dev) | Ler e editar com a pré-visualização de Markdown do VS Code |

## Tipos de recurso

| Recurso | Onde guardar | Como aparece no GitHub |
| --- | --- | --- |
| Notas e explicações | `.md` na pasta do assunto | Renderizado, com títulos, tabelas, listas, fórmulas e blocos de código |
| Links internos | `[texto](caminho/relativo.md#secao)` | Clicáveis; `#secao` leva ao título |
| Links externos | `[texto](https://...)` ou `<https://...>` | Clicáveis; referências completas em [08 - Referências e Fontes](../08%20-%20Referências%20e%20Fontes/README.md) |
| PDF | ao lado da nota | Visualizador de PDF do GitHub + galeria em Markdown gerada automaticamente |
| Imagens e fotos | `imagens/` ao lado da nota (`.webp`, `.png`, `.jpg`) | Dentro do texto: `![descrição](imagens/foto.jpg)` ou `<img src="imagens/foto.jpg" width="600">` |
| Código | bloco ` ```java ` na nota; arquivo em `codigo/` | Com destaque de sintaxe; executável pelas [ferramentas](../ferramentas/README.md) |
| Diagramas | bloco ` ```mermaid ` | Desenhado pelo GitHub |
| Fórmulas | `$x^2$` ou bloco ` ```math ` | Renderizadas pelo GitHub |
| Avisos | `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]` | Caixas coloridas do GitHub (e *callouts* do Obsidian) |
| Conteúdo recolhível | `<details><summary>Título</summary> … </details>` | Seção que abre ao clicar (usado nas resoluções e no texto dos slides) |

## Como acrescentar conteúdo

**Pelo navegador (sem instalar nada):**

1. Abra a pasta no GitHub e use **Add file › Create new file** (nota) ou **Upload files** (imagem, foto, PDF).
2. Para uma nota, copie o [modelo de nota](Modelos/modelo-de-nota.md). Para uma foto, envie-a para a pasta `imagens/` mais próxima e cite-a na nota.
3. Faça o *commit* na `main`. Um workflow do GitHub atualiza sozinho a navegação: trilhas, índices, *backlinks*, `MAPA.md`, `codigo/` e a galeria de um PDF novo.

**No computador ou no Codespaces:** edite os arquivos e rode os geradores, na ordem indicada em [ferramentas](../ferramentas/README.md#para-manter-o-repositório). Antes de enviar, confira com `python3 ferramentas/verificar_links.py`.

O espaço para as suas próprias anotações e fotos é o [10 - Caderno de Anotações](../10%20-%20Caderno%20de%20Anotações/README.md).

## Usar no Obsidian (opcional)

1. Clone o repositório (ou baixe o ZIP) e, no Obsidian, use **Open folder as vault** na pasta clonada.
2. Em *Settings › Files and links*: desative **Use [[Wikilinks]]** e escolha **New link format: Relative path to file**. Assim, as notas novas usam o mesmo formato de link que o GitHub.
3. Links, imagens, Mermaid, *callouts* (`> [!NOTE]`) e o painel de *backlinks* funcionam como no GitHub. A pasta `ferramentas/node_modules` pode ser excluída da busca em *Settings › Files and links › Excluded files*.

## Convenções de nomes

- Pastas de primeiro nível numeradas (`00 -` a `10 -`), na ordem de estudo.
- Arquivos em minúsculas, com hífen e sem acento (`resumo-aula-12.md`); pastas com nomes legíveis (`02 - Resumo Teórico`).
- Imagens das páginas de um PDF: `paginas/<prefixo>-pNN.webp`, geradas automaticamente. Imagens próprias: `imagens/aaaa-mm-dd-descricao.jpg`.
- Os blocos entre `` (e `nav:rodape`) são gerados: escreva fora deles.


<!-- nav:rodape -->

---

**Links para esta página (3):** [Modelo de nota](Modelos/modelo-de-nota.md) · [00 — Planejamento e Organização](README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../README.md)

<!-- /nav:rodape -->
