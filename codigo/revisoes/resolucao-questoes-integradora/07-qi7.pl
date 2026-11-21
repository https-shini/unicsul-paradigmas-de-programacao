% Gerado automaticamente a partir de 06 - Revisões e Sínteses/resolucao-questoes-integradoras.md (linha 217).
% Seção: QI7
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/revisoes/resolucao-questoes-integradora/07-qi7.pl
% Consulta: ?- soma_quadrados(4, S).
% A saída deve conter: S = 30

soma_quadrados(0, 0).
soma_quadrados(N, S) :- N > 0, N1 is N - 1, soma_quadrados(N1, S1), S is S1 + N * N.
