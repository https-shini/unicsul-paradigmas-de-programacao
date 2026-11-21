% Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão LÓGICA.
% situacao(A1, A2, AF, Freq, S): cada cláusula DECLARA em que condições S vale.
% AF = nenhuma quando o aluno não fez a avaliação final.
% As condições são mutuamente exclusivas (cada cláusula nega as anteriores), então há uma resposta só.

situacao(_, _, _, Freq, reprovado_por_falta) :-
    Freq < 75.
situacao(A1, A2, _, Freq, aprovado) :-
    Freq >= 75,
    A1 + A2 >= 6.
situacao(A1, A2, _, Freq, reprovado) :-
    Freq >= 75,
    A1 + A2 < 6,
    sem_direito_a_af(A1, A2).
situacao(A1, A2, nenhuma, Freq, af) :-
    Freq >= 75,
    A1 + A2 < 6,
    \+ sem_direito_a_af(A1, A2).
situacao(A1, A2, AF, Freq, Resultado) :-
    number(AF),
    Freq >= 75,
    A1 + A2 < 6,
    \+ sem_direito_a_af(A1, A2),
    Maior is max(A1, A2),
    (   AF + Maior >= 6
    ->  Resultado = aprovado_na_af
    ;   Resultado = reprovado_na_af
    ).

sem_direito_a_af(A1, _) :- A1 < 1.
sem_direito_a_af(_, A2) :- A2 < 1.

nota_minima_af(A1, A2, N) :-
    N is 6 - max(A1, A2).
