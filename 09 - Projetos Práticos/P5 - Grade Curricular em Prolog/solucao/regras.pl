% P5 — Regras sobre a grade curricular (Aula 15). Os fatos estão em base.pl.

% R1. Aprovado: cursou com nota >= 6 (basta uma vez).
aprovado(A, D) :-
    cursou(A, D, N),
    N >= 6.

% R2. Situação de um aluno numa disciplina: aprovado, reprovado (cursou e não passou) ou pendente.
situacao(A, D, aprovado)  :- aprovado(A, D), !.
situacao(A, D, reprovado) :- cursou(A, D, _), !.
situacao(_, _, pendente).

% R3. Pode cursar: ainda não foi aprovado e NÃO existe pré-requisito em que não tenha sido aprovado.
%     \+ é a negação por falha (mundo fechado): \+ G é verdadeiro quando G não pode ser provado.
pode_cursar(A, D) :-
    aluno(A),
    disciplina(D, _, _),
    \+ aprovado(A, D),
    \+ ( prerequisito(D, P), \+ aprovado(A, P) ).

% R4. Disciplinas que o aluno pode cursar, em ordem alfabética e sem repetição.
disponiveis(A, Lista) :-
    findall(D, pode_cursar(A, D), Ds),
    sort(Ds, Lista).

% R5. Dependência direta ou indireta (fecho transitivo). A cláusula não recursiva vem primeiro.
depende(D, P) :- prerequisito(D, P).
depende(D, P) :- prerequisito(D, X), depende(X, P).

% R6. Caminho de pré-requisitos de D até P: [D, ..., P].
cadeia(D, P, [D, P]) :- prerequisito(D, P).
cadeia(D, P, [D | Resto]) :- prerequisito(D, X), cadeia(X, P, Resto).

% R7. Disciplinas que têm D como pré-requisito direto.
liberadas_por(D, Lista) :-
    findall(X, prerequisito(X, D), Xs),
    sort(Xs, Lista).

% R8. Soma recursiva de uma lista e média das notas do aluno (todas as vezes que cursou).
soma([], 0).
soma([X | R], S) :-
    soma(R, S1),
    S is S1 + X.

media(A, M) :-
    findall(N, cursou(A, _, N), Notas),
    Notas \== [],
    soma(Notas, S),
    length(Notas, Qtd),
    M is S / Qtd.

% R9. Quantidade de reprovações (cada vez que cursou com nota < 6).
reprovacoes(A, Qtd) :-
    aluno(A),
    findall(D, (cursou(A, D, N), N < 6), Ds),
    length(Ds, Qtd).

% R10. Formado: não existe disciplina em que não tenha sido aprovado.
formado(A) :-
    aluno(A),
    \+ ( disciplina(D, _, _), \+ aprovado(A, D) ).
