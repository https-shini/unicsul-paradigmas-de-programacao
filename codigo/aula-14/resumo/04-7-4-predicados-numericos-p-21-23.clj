;; Gerado automaticamente a partir de 01 - Aulas/Aula 14 - Paradigma Funcional/02 - Resumo Teórico/resumo-aula-14.md (linha 186).
;; Seção: 7.4 Predicados numéricos (p.21, 23)
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/aula-14/resumo/04-7-4-predicados-numericos-p-21-23.clj
;; Entrada de exemplo: 4
;; A saída deve conter: Maior que zero:  true | Diferente de zero:  true | Par:  true

(println "Digite o valor de x: ")
(def x (read))
(println "Maior que zero: " (> x 0))
(println "Diferente de zero: " (not (= x 0)))
(println "Par: " (even? x))
