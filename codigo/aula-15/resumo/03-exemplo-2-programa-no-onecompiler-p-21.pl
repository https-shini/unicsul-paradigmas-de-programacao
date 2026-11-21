% Gerado automaticamente a partir de 01 - Aulas/Aula 15 - Paradigma Lógico/02 - Resumo Teórico/resumo-aula-15.md (linha 196).
% Seção: Exemplo 2 — programa no OneCompiler (p.21)
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/aula-15/resumo/03-exemplo-2-programa-no-onecompiler-p-21.pl
% Consulta: ?- main.
% A saída deve conter: Joao eh homem? Sim | Pedro eh homem? Nao | Quem eh homem? [joao,jose] | Quem eh mulher? [maria] | Joao gosta de quem? [maria] | Jose gosta de quem? []

/*Fatos*/
homem(joao).
homem(jose).
mulher(maria).
gosta(joao,maria).

/* Inicialização do programa*/
:- initialization(main).

main :-
    /*Consultas*/
    write('Joao eh homem? '),
    (homem(joao) -> write('Sim') ; write('Nao')), nl,
    write('Pedro eh homem? '),
    (homem(pedro) -> write('Sim') ; write('Nao')), nl,
    findall(X, homem(X), ListaHomens),
    write('Quem eh homem? '), write(ListaHomens), nl,
    findall(X, mulher(X), ListaMulheres),
    write('Quem eh mulher? '), write(ListaMulheres), nl,
    findall(X, gosta(joao,X), ListaGostaJoao),
    write('Joao gosta de quem? '), write(ListaGostaJoao), nl,
    findall(X, gosta(jose,X), ListaGostaJose),
    write('Jose gosta de quem? '), write(ListaGostaJose), nl.
