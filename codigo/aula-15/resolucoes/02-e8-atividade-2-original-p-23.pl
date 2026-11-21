% Gerado automaticamente a partir de 01 - Aulas/Aula 15 - Paradigma Lógico/04 - Resoluções/resolucoes-aula-15.md (linha 70).
% Seção: E8 — Atividade 2 (original, p.23)
% Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
% Como executar:  python3 ferramentas/rodar.py codigo/aula-15/resolucoes/02-e8-atividade-2-original-p-23.pl
% Consulta: ?- mostra(ana, joao).
% A saída deve conter: Pai de ana: joao | Filhos de joao: [ana,maria,carlos]

/* Fatos */
pai(joao,ana).
pai(joao,maria).
pai(joao,carlos).
pai(carlos,renata).

:- initialization(main).

main :-
    write('Digite o primeiro nome (termine com ponto): '), read(Nome1),
    write('Digite o segundo nome (termine com ponto): '),  read(Nome2),
    mostra(Nome1, Nome2).

/* Separado do main para poder ser testado sem leitura do teclado */
mostra(Nome1, Nome2) :-
    (   pai(Pai, Nome1)                       % cada pessoa tem um único pai
    ->  write('Pai de '), write(Nome1), write(': '), write(Pai)
    ;   write(Nome1), write(' nao tem pai cadastrado')
    ), nl,
    findall(Filho, pai(Nome2, Filho), Filhos), % reúne TODOS os filhos
    write('Filhos de '), write(Nome2), write(': '), write(Filhos), nl.
