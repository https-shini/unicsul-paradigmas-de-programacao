% P5 — Regras sobre a grade curricular (Aula 15). Os fatos estão em base.pl (não altere).
% Cada regra abaixo é um esqueleto que sempre falha (":- fail."). Substitua o corpo pela sua solução.

% R1. aprovado(Aluno, Disciplina): cursou com nota >= 6 (basta uma vez).
aprovado(_A, _D) :- fail.          % TODO

% R2. situacao(Aluno, Disciplina, S): S = aprovado, reprovado (cursou e nunca passou) ou pendente.
%     Deve dar UMA resposta só. Dica: corte (!) depois de cada caso, ou if-then-else ( -> ; ).
situacao(_A, _D, _S) :- fail.      % TODO

% R3. pode_cursar(Aluno, Disciplina): o aluno ainda não foi aprovado na disciplina e foi aprovado
%     em TODOS os pré-requisitos. "Todos" = "não existe pré-requisito sem aprovação":
%     \+ ( prerequisito(D, P), \+ aprovado(A, P) )
%     Gere Aluno e Disciplina com aluno/1 e disciplina/3 antes de usar \+.
pode_cursar(_A, _D) :- fail.       % TODO

% R4. disponiveis(Aluno, Lista): disciplinas que pode cursar, em ordem alfabética (findall + sort).
disponiveis(_A, _Lista) :- fail.   % TODO

% R5. depende(D, P): D depende de P direta ou indiretamente. Duas cláusulas; a recursiva por último.
depende(_D, _P) :- fail.           % TODO

% R6. cadeia(D, P, Caminho): Caminho = [D, ..., P] seguindo pré-requisitos.
cadeia(_D, _P, _C) :- fail.        % TODO

% R7. liberadas_por(D, Lista): disciplinas que têm D como pré-requisito DIRETO, em ordem alfabética.
liberadas_por(_D, _Lista) :- fail. % TODO

% R8. soma(Lista, S) RECURSIVA (sem sum_list) e media(Aluno, M) de todas as notas do aluno.
%     Aluno sem notas: media/2 deve falhar.
soma(_Lista, _S) :- fail.          % TODO
media(_A, _M) :- fail.             % TODO

% R9. reprovacoes(Aluno, Qtd): quantas vezes cursou com nota < 6.
reprovacoes(_A, _Qtd) :- fail.     % TODO

% R10. formado(Aluno): não existe disciplina em que não tenha sido aprovado.
formado(_A) :- fail.               % TODO
