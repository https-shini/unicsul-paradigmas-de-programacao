;; Gerado automaticamente a partir de 01 - Aulas/Aula 14 - Paradigma Funcional/04 - Resoluções/resolucoes-aula-14.md (linha 130).
;; Seção: E10
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/aula-14/resolucoes/04-e10.clj
;; A saída deve conter: 120 ⏎ 120 ⏎ 3628800

;; Versão recursiva: a repetição vem da própria definição matemática
;;   n! = 1           se n <= 1
;;   n! = n * (n-1)!  caso contrário
(defn fatorial [n]
  (if (<= n 1)
    1
    (* n (fatorial (dec n)))))

;; Versão com forma funcional: reduce aplica * sobre a sequência 1..n
(defn fatorial-reduce [n]
  (reduce * 1 (range 1 (inc n))))

(println (fatorial 5))          ; 120
(println (fatorial-reduce 5))   ; 120
(println (fatorial 10))         ; 3628800
