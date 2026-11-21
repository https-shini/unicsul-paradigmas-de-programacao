;; Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 146).
;; Seção: 13
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/04-13.clj
;; A saída deve conter: 10 ⏎ 220

(defn soma-digitos [n]
  (if (< n 10)
    n                                            ; caso base: um só dígito
    (+ (mod n 10) (soma-digitos (quot n 10)))))  ; último dígito + soma do resto

(println (soma-digitos 1234))                    ; 10

(println (reduce + (map (fn [x] (* x x))
                        (filter even? (range 1 11)))))   ; 4 + 16 + 36 + 64 + 100 = 220
