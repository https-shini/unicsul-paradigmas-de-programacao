;; Gerado automaticamente a partir de 01 - Aulas/Aula 14 - Paradigma Funcional/04 - Resoluções/resolucoes-aula-14.md (linha 86).
;; Seção: E8 — Atividade 2 (original, p.20)
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/aula-14/resolucoes/03-e8-atividade-2-original-p-20.clj
;; Entrada de exemplo: 2 3
;; A saída deve conter: -5 ⏎ 8 ⏎ 12 ⏎ 3/25 ⏎ 76.0

(println "Digite os valores de x e y:")
(def x (read))
(def y (read))
(println (- (+ x y) 10))                        ; x + y - 10
(println (+ x (* 2 y)))                         ; x + 2*y
(println (* (+ x 2) y))                         ; (x + 2) * y
(println (/ (* (+ x 2) y) (* 10 (+ x 8))))      ; (x + 2) * y / [10 * (x + 8)]
(println (- (Math/pow (* 3 y) 2) (+ x y)))      ; (3*y)^2 - (x + y)
