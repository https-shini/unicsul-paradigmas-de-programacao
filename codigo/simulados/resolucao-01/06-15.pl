% Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-01.md (linha 144).
% Seção: 15
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-01/06-15.pl
% Consulta: ?- pode_acessar(Quem, s204).
% A saída deve conter: Quem = ana

cargo(ana, gerente).      andar_pessoa(ana, 2).
cargo(bruno, visitante).
sala(s204, 2).            sala(recepcao, 0).

pode_acessar(P, S) :- cargo(P, gerente), andar_pessoa(P, A), sala(S, A).
pode_acessar(P, recepcao) :- cargo(P, visitante).
