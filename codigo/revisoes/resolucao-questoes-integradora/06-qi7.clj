;; Gerado automaticamente a partir de 06 - Revisões e Sínteses/resolucao-questoes-integradoras.md (linha 210).
;; Seção: QI7
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/revisoes/resolucao-questoes-integradora/06-qi7.clj
;; A saída deve conter: 30 | 30

(println (reduce + (map (fn [x] (* x x)) (range 1 5))))   ; formas funcionais

(defn soma-quadrados [n]                                   ; recursão
  (if (= n 0) 0 (+ (* n n) (soma-quadrados (- n 1)))))
(println (soma-quadrados 4))
