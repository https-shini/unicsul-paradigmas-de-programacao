;; Gerado automaticamente a partir de 06 - Revisões e Sínteses/quadros-comparativos.md (linha 82).
;; Seção: 2. Um mesmo problema nos quatro paradigmas
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/revisoes/quadros-comparativos/03-2-um-mesmo-problema-nos-quatro-paradigmas.clj
;; A saída deve conter: 120

(defn fatorial [n]
  (if (<= n 1)
    1
    (* n (fatorial (- n 1)))))
(println (fatorial 5))
