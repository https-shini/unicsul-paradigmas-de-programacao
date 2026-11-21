% Gerado automaticamente a partir de 06 - Revisões e Sínteses/quadros-comparativos.md (linha 97).
% Seção: 2. Um mesmo problema nos quatro paradigmas
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/revisoes/quadros-comparativos/04-2-um-mesmo-problema-nos-quatro-paradigmas.pl
% Consulta: ?- fatorial(5, F).
% A saída deve conter: F = 120

fatorial(0, 1).
fatorial(N, F) :- N > 0, N1 is N - 1, fatorial(N1, F1), F is N * F1.
