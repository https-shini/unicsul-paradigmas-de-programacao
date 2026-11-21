% P5 — Base de fatos da grade curricular (fictícia). Igual em inicial/ e solucao/: NÃO é preciso alterar.
:- use_module(library(lists)).

% disciplina(Codigo, Nome, Semestre).
disciplina(alg,  'Algoritmos', 1).
disciplina(mat,  'Matemática Discreta', 1).
disciplina(lp1,  'Linguagem de Programação I', 2).
disciplina(ed,   'Estruturas de Dados', 3).
disciplina(aut,  'Autômatos', 3).
disciplina(poo,  'Programação Orientada a Objetos', 3).
disciplina(plp,  'Paradigmas de Linguagens de Programação', 4).
disciplina(comp, 'Compiladores', 5).
disciplina(ia,   'Inteligência Artificial', 5).

% prerequisito(Disciplina, PreRequisito): para cursar Disciplina, é preciso ter sido aprovado em PreRequisito.
prerequisito(lp1,  alg).
prerequisito(ed,   lp1).
prerequisito(poo,  lp1).
prerequisito(aut,  mat).
prerequisito(plp,  ed).
prerequisito(plp,  poo).
prerequisito(comp, plp).
prerequisito(comp, aut).
prerequisito(ia,   ed).
prerequisito(ia,   mat).

aluno(ana).
aluno(bruno).
aluno(carla).
aluno(davi).

% cursou(Aluno, Disciplina, Nota): cada vez que o aluno cursou a disciplina.
cursou(ana, alg, 8.0).
cursou(ana, mat, 7.5).
cursou(ana, lp1, 9.0).
cursou(ana, ed, 6.0).
cursou(ana, poo, 5.5).
cursou(ana, aut, 7.0).
cursou(bruno, alg, 4.0).
cursou(bruno, alg, 7.0).
cursou(bruno, mat, 6.5).
cursou(carla, alg, 10.0).
cursou(carla, mat, 9.0).
cursou(carla, lp1, 8.5).
cursou(carla, ed, 7.0).
cursou(carla, aut, 6.0).
cursou(carla, poo, 9.5).
cursou(carla, plp, 10.0).
cursou(carla, comp, 8.0).
cursou(carla, ia, 7.5).
