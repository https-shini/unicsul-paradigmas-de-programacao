% Gerado por gerar_testes.py a partir de casos.csv — não edite à mão.
% Cada caso exige UMA resposta só: findall(S, situacao(...), [Esperado]).
teste(caso_01, findall(S, situacao(3.5, 4.0, nenhuma, 80.0, S), [aprovado])).
teste(caso_02, findall(S, situacao(3.0, 3.0, nenhuma, 75.0, S), [aprovado])).
teste(caso_03, findall(S, situacao(2.1, 3.9, nenhuma, 80.0, S), [aprovado])).
teste(caso_04, findall(S, situacao(5.0, 5.0, nenhuma, 74.9, S), [reprovado_por_falta])).
teste(caso_05, findall(S, situacao(0.0, 0.0, nenhuma, 0.0, S), [reprovado_por_falta])).
teste(caso_06, findall(S, situacao(2.0, 3.0, 5.0, 70.0, S), [reprovado_por_falta])).
teste(caso_07, findall(S, situacao(0.5, 5.0, nenhuma, 100.0, S), [reprovado])).
teste(caso_08, findall(S, situacao(5.0, 0.9, nenhuma, 100.0, S), [reprovado])).
teste(caso_09, findall(S, situacao(0.5, 5.0, 5.0, 80.0, S), [reprovado])).
teste(caso_10, findall(S, situacao(2.0, 3.0, nenhuma, 90.0, S), [af])).
teste(caso_11, findall(S, situacao(1.0, 1.0, nenhuma, 80.0, S), [af])).
teste(caso_12, findall(S, situacao(2.0, 3.0, 3.5, 90.0, S), [aprovado_na_af])).
teste(caso_13, findall(S, situacao(1.0, 1.0, 5.0, 80.0, S), [aprovado_na_af])).
teste(caso_14, findall(S, situacao(2.9, 3.0, 3.0, 80.0, S), [aprovado_na_af])).
teste(caso_15, findall(S, situacao(4.5, 1.4, 2.0, 76.0, S), [aprovado_na_af])).
teste(caso_16, findall(S, situacao(2.0, 3.0, 2.5, 90.0, S), [reprovado_na_af])).
teste(caso_17, findall(S, situacao(4.0, 1.9, 1.9, 80.0, S), [reprovado_na_af])).
teste(caso_18, findall(S, situacao(4.0, 4.0, 3.0, 80.0, S), [aprovado])).
teste(minima_1, (nota_minima_af(2.0, 3.0, N), abs(N - 3.0) < 1.0e-9)).
teste(minima_2, (nota_minima_af(1.0, 1.0, N), abs(N - 5.0) < 1.0e-9)).
teste(minima_3, (nota_minima_af(4.5, 1.4, N), abs(N - 1.5) < 1.0e-9)).
teste(minima_4, (nota_minima_af(4.1, 1.0, N), abs(N - 1.9) < 1.0e-9)).

executar_testes(Falhas) :-
    findall(Nome, (teste(Nome, Objetivo), \+ catch(Objetivo, _, fail)), Falhas).
