;; Gerado automaticamente a partir de 02 - Listas de Exercícios/Lista 01 - Revisão I/02 - Resolução/resolucao-lista-01.md (linha 96).
;; Seção: Q7
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/lista-01/resolucao/01-q7.clj
;; Entrada de exemplo: 2 3
;; A saída deve conter: 3/25 ⏎ 76.0

(println "Digite os valores de x e y:")
(def x (read))                                 ; vincula o 1º valor lido ao símbolo x
(def y (read))                                 ; vincula o 2º valor lido ao símbolo y
(println (/ (* (+ x 2) y) (* 10 (+ x 8))))     ; ((x + 2) * y) / (10 * (x + 8))
(println (- (Math/pow (* 3 y) 2) (+ x y)))     ; (3 * y)^2 - (x + y)
