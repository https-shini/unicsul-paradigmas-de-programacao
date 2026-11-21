% Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão LÓGICA.
% situacao(A1, A2, AF, Freq, S): AF = nenhuma quando o aluno não fez a avaliação final.
% S é um dos átomos: aprovado, reprovado, reprovado_por_falta, af, aprovado_na_af, reprovado_na_af.
% Os testes exigem UMA resposta só: escreva cláusulas com condições mutuamente exclusivas
% (ou use corte / if-then-else, e explique a escolha no README).

situacao(_A1, _A2, _AF, _Freq, _S) :- fail.     % TODO

% nota_minima_af(A1, A2, N): N é 6 menos a maior entre A1 e A2 (use is e max/2).
nota_minima_af(_A1, _A2, _N) :- fail.           % TODO
