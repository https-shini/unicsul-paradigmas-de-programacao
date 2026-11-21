% Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 235).
% Seção: 15
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/08-15.pl
% Consulta: ?- findall(N, aprovado(N), L).
% A saída deve conter: L = [ana,carla]

aluno(ana, 8.0).
aluno(bruno, 5.5).
aluno(carla, 6.0).

aprovado(Nome) :- aluno(Nome, Media), Media >= 6.
