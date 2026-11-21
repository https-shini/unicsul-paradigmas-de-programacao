# Gerado automaticamente a partir de 01 - Aulas/Aula 03 - Implementação das Linguagens/04 - Resoluções/resolucoes-aula-03.md (linha 115).
# Seção: Perl (Grupo 2, interpretada)
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-03/resolucoes/04-perl-grupo-2-interpretada.pl
# Entrada de exemplo: 5 ⏎ 3 ⏎ 9 ⏎ 1 ⏎ 7 ⏎ 2 ⏎ 8 ⏎ 6 ⏎ 4 ⏎ 10
# A saída deve conter: Media: 5.50 | Maior: 10.00 | Menor: 1.00

use strict;
use warnings;

my ($soma, $maior, $menor) = (0, undef, undef);
for my $i (1 .. 10) {
    my $x = <STDIN>;
    chomp $x;
    $maior = $x if !defined $maior || $x > $maior;
    $menor = $x if !defined $menor || $x < $menor;
    $soma += $x;
}
printf "Media: %.2f\nMaior: %.2f\nMenor: %.2f\n", $soma / 10, $maior, $menor;
