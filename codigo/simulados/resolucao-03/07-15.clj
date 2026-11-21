;; Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 222).
;; Seção: 15
;; Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
;; Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/07-15.clj
;; A saída deve conter: Ana | Carla

(def turma [{:nome "Ana" :media 8.0} {:nome "Bruno" :media 5.5} {:nome "Carla" :media 6.0}])

(println (map :nome (filter #(>= (:media %) 6) turma)))   ; (Ana Carla)
