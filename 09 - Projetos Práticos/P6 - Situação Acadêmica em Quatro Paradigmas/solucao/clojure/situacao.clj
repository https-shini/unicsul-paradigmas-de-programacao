;; Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão FUNCIONAL.
;; O desempenho é um MAPA (dado imutável); a regra é uma função pura que devolve uma palavra-chave.
(ns situacao)

(defn nota-minima-af
  "Nota mínima na AF: 6 menos a maior entre A1 e A2."
  [a1 a2]
  (- 6 (max a1 a2)))

(defn situacao
  "Recebe {:a1 :a2 :af :freq} (:af nil = não fez) e devolve :aprovado, :reprovado,
  :reprovado-por-falta, :af, :aprovado-na-af ou :reprovado-na-af.
  cond avalia os testes em ordem e devolve o valor do primeiro verdadeiro: é uma EXPRESSÃO, não uma sequência de comandos."
  [{:keys [a1 a2 af freq]}]
  (cond
    (< freq 75)                 :reprovado-por-falta
    (>= (+ a1 a2) 6)            :aprovado
    (or (< a1 1) (< a2 1))      :reprovado
    (nil? af)                   :af
    (>= (+ af (max a1 a2)) 6)   :aprovado-na-af
    :else                       :reprovado-na-af))

(defn resumo-da-turma
  "Exemplo de uso com funções de ordem superior: quantos alunos em cada situação."
  [desempenhos]
  (frequencies (map situacao desempenhos)))
