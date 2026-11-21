% Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 171).
% Seção: 14
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/05-14.pl
% Consulta: ?- (pode_cursar(ana, compiladores) -> A = sim ; A = nao), (pode_cursar(bruno, plp) -> B = sim ; B = nao), (depende(compiladores, algoritmos) -> C = sim ; C = nao).
% A saída deve conter: A = nao | B = sim | C = sim

prerequisito(plp, algoritmos).
prerequisito(compiladores, plp).
prerequisito(compiladores, automatos).
aprovado(ana, algoritmos).
aprovado(ana, plp).
aprovado(bruno, algoritmos).

% (a) não existe pré-requisito de D em que o aluno NÃO tenha sido aprovado
pode_cursar(Aluno, Disciplina) :-
    \+ ( prerequisito(Disciplina, P), \+ aprovado(Aluno, P) ).

% (c) dependência direta ou indireta
depende(D, P) :- prerequisito(D, P).
depende(D, P) :- prerequisito(D, X), depende(X, P).
