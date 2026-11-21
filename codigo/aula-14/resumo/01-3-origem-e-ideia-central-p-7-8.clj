;; Gerado automaticamente a partir de 01 - Aulas/Aula 14 - Paradigma Funcional/02 - Resumo Teórico/resumo-aula-14.md (linha 53).
;; Seção: 3. Origem e ideia central (p.7–8)
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/aula-14/resumo/01-3-origem-e-ideia-central-p-7-8.clj
;; A saída deve conter: 55

;; Soma de 1 a 10 sem variável mutável nem laço:
;; range gera (1 2 ... 10), e reduce aplica + acumulando.
(println (reduce + (range 1 11)))   ; 55
