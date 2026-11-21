<?php
// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/02 - Resumo Teórico/resumo-aula-06.md (linha 88).
// Seção: 5. Tipagem estática × dinâmica (p.9–14)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resumo/02-5-tipagem-estatica-dinamica-p-9-14.php
// A saída deve conter: x eh integer | x eh double | x eh string | z eh string
$x = 10;
echo "x eh " . gettype($x) . PHP_EOL;     // integer
$x = 10.2;
echo "x eh " . gettype($x) . PHP_EOL;     // double
$x = "Universidade Cruzeiro Do Sul";
echo "x eh " . gettype($x) . PHP_EOL;     // string
$z = $x;
echo "Resultado: $z" . PHP_EOL;
echo "z eh " . gettype($z) . PHP_EOL;     // string
?>
