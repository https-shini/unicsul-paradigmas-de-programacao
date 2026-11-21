<!-- nav:topo -->
[Início](../../../../README.md) › [09 - Projetos Práticos](../../../README.md) › [P1](../../README.md) › [solucao](../README.md) › **calc** · [Mapa](../../../../MAPA.md)
<!-- /nav:topo -->

<!-- indice gerado por ferramentas/geradores/gerar_navegacao.py -->

# P1 · solucao/calc

Pacote Python do interpretador.

| Conteúdo | Tipo | Descrição |
| --- | --- | --- |
| [`__init__.py`](__init__.py) | Python | calc — interpretador e compilador de uma pequena linguagem de expressões. |
| [`__main__.py`](__main__.py) | Python | Linha de comando: python3 -m calc [arquivo.calc] [--tokens | --arvore | --bytecode | --vm] |
| [`arvore.py`](arvore.py) | Python | Nós da árvore sintática abstrata (AST). Cada classe corresponde a uma regra da gramática. |
| [`compilador.py`](compilador.py) | Python | Implementação híbrida (Aula 03 p.12–14): a árvore é traduzida para um código intermediário |
| [`interpretador.py`](interpretador.py) | Python | Interpretação pura (Aula 03 p.10–11): percorre a árvore e executa cada comando diretamente. |
| [`lexico.py`](lexico.py) | Python | Análise léxica (Aula 03 p.9; Aula 04 p.8–9): agrupa caracteres em lexemas e classifica cada um como token. |
| [`sintatico.py`](sintatico.py) | Python | Análise sintática descendente recursiva (Aula 04): um método para cada regra da gramática em BNF. |
