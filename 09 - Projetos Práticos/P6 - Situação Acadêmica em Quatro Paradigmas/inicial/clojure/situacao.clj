;; Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão FUNCIONAL.
;; O desempenho é um mapa {:a1 :a2 :af :freq} (:af nil = não fez); a regra é uma função pura.
(ns situacao)

(defn nota-minima-af
  "TODO: 6 menos a maior entre A1 e A2."
  [a1 a2]
  (throw (ex-info "TODO: nota-minima-af" {})))

(defn situacao
  "TODO: devolva :aprovado, :reprovado, :reprovado-por-falta, :af, :aprovado-na-af ou :reprovado-na-af.
  Dica: desestruture o mapa com [{:keys [a1 a2 af freq]}] e use cond (os testes são avaliados em ordem)."
  [desempenho]
  (throw (ex-info "TODO: situacao" {})))
