# Gerado automaticamente a partir de 01 - Aulas/Aula 05 - Semântica/04 - Resoluções/resolucoes-aula-05.md (linha 104).
# Seção: E10
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-05/resolucoes/02-e10.pl
# A saída deve conter: dinamico (local): do chamador | estatico (my): global

use strict;
use warnings;

our $x = "global";            # variável de pacote (global)

sub mostra { print "$x\n"; }  # $x não é local de mostra

sub com_local {
    local $x = "do chamador"; # escopo DINÂMICO: vale para quem for chamado daqui
    print "dinamico (local): ";
    mostra();
}

sub com_my {
    my $x = "do chamador";    # escopo ESTÁTICO (léxico): só existe neste bloco
    print "estatico (my): ";
    mostra();
}

com_local();   # imprime: do chamador
com_my();      # imprime: global
