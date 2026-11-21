<?php
// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/02 - Resumo Teórico/resumo-aula-06.md (linha 193).
// Seção: 6.3 Exemplo PHP e atividade (p.19–20)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resumo/06-6-3-exemplo-php-e-atividade-p-19-20.php
// A saída deve conter: x eh integer | y eh string | w eh double | Resultado(x+y+w): 40.2
$x = 10;
$y = "20";
$w = 10.2;
echo "x eh " . gettype($x) . PHP_EOL;     // integer
echo "y eh " . gettype($y) . PHP_EOL;     // string
echo "w eh " . gettype($w) . PHP_EOL;     // double
$z = $x + $y + $w;                         // "20" vira 20 automaticamente
echo "Resultado(x+y+w): $z" . PHP_EOL;     // 40.2
?>
