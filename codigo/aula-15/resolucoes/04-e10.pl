% Gerado automaticamente a partir de 01 - Aulas/Aula 15 - Paradigma Lógico/04 - Resoluções/resolucoes-aula-15.md (linha 135).
% Seção: E10
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/aula-15/resolucoes/04-e10.pl
% Consulta: ?- avo(joao, N).
% A saída deve conter: N = renata

pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).

% A é avô de N se A é pai de alguém (P) que é pai de N.
avo(A, N) :- pai(A, P), pai(P, N).

% X e Y são irmãos se têm o mesmo pai e são pessoas diferentes.
irmao(X, Y) :- pai(P, X), pai(P, Y), X \== Y.
