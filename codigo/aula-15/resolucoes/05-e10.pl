% Gerado automaticamente a partir de 01 - Aulas/Aula 15 - Paradigma Lógico/04 - Resoluções/resolucoes-aula-15.md (linha 160).
% Seção: E10
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/aula-15/resolucoes/05-e10.pl
% Consulta: ?- irmao(ana, Y).
% A saída deve conter: Y = maria ⏎ Y = carlos

pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).
irmao(X, Y) :- pai(P, X), pai(P, Y), X \== Y.
