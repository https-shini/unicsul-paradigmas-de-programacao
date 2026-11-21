% Testes do projeto P5. Rode com:  python3 ferramentas/testar_projetos.py P5
% A ferramenta junta base.pl + regras.pl + este arquivo e consulta executar_testes(Falhas).
% Falhas = [] significa que tudo passou; senão, a lista traz o nome dos testes que falharam.

teste(r1_aprovado_ana_alg,        aprovado(ana, alg)).
teste(r1_reprovado_ana_poo,       \+ aprovado(ana, poo)).
teste(r1_bruno_aprovado_2a_vez,   aprovado(bruno, alg)).
teste(r1_davi_nada,               \+ aprovado(davi, _)).

teste(r2_situacao_aprovado,       situacao(ana, ed, aprovado)).
teste(r2_situacao_reprovado,      situacao(ana, poo, reprovado)).
teste(r2_situacao_pendente,       situacao(ana, comp, pendente)).
teste(r2_situacao_unica,          (findall(S, situacao(bruno, alg, S), L), L == [aprovado])).

teste(r3_ana_pode_poo,            pode_cursar(ana, poo)).
teste(r3_ana_pode_ia,             pode_cursar(ana, ia)).
teste(r3_ana_nao_pode_plp,        \+ pode_cursar(ana, plp)).
teste(r3_ana_nao_repete_aprovada, \+ pode_cursar(ana, alg)).
teste(r3_bruno_pode_lp1,          pode_cursar(bruno, lp1)).
teste(r3_bruno_nao_pode_ed,       \+ pode_cursar(bruno, ed)).

teste(r4_disponiveis_ana,         disponiveis(ana, [ia, poo])).
teste(r4_disponiveis_bruno,       disponiveis(bruno, [aut, lp1])).
teste(r4_disponiveis_davi,        disponiveis(davi, [alg, mat])).
teste(r4_disponiveis_carla,       disponiveis(carla, [])).

teste(r5_depende_direto,          depende(plp, ed)).
teste(r5_depende_indireto,        depende(comp, alg)).
teste(r5_nao_depende,             \+ depende(aut, alg)).
teste(r5_todas_de_comp,           (findall(P, depende(comp, P), Ps), sort(Ps, S), S == [alg, aut, ed, lp1, mat, plp, poo])).

teste(r6_cadeia_primeira,         cadeia(comp, alg, [comp, plp, ed, lp1, alg])).
teste(r6_duas_cadeias,            (findall(C, cadeia(comp, alg, C), Cs), length(Cs, 2))).
teste(r6_cadeia_direta,           cadeia(lp1, alg, [lp1, alg])).

teste(r7_liberadas_lp1,           liberadas_por(lp1, [ed, poo])).
teste(r7_liberadas_mat,           liberadas_por(mat, [aut, ia])).
teste(r7_liberadas_nenhuma,       liberadas_por(comp, [])).

teste(r8_soma,                    (soma([1, 2, 3.5], S), S =:= 6.5)).
teste(r8_soma_vazia,              (soma([], S), S =:= 0)).
teste(r8_media_ana,               (media(ana, M), M > 7.166, M < 7.167)).
teste(r8_media_bruno,             (media(bruno, M), M > 5.833, M < 5.834)).
teste(r8_media_sem_notas,         \+ media(davi, _)).

teste(r9_reprovacoes_ana,         reprovacoes(ana, 1)).
teste(r9_reprovacoes_carla,       reprovacoes(carla, 0)).

teste(r10_carla_formada,          formado(carla)).
teste(r10_ana_nao_formada,        \+ formado(ana)).
teste(r10_quem_se_formou,         (findall(A, formado(A), As), As == [carla])).

executar_testes(Falhas) :-
    findall(Nome, (teste(Nome, Objetivo), \+ catch(Objetivo, _, fail)), Falhas).
