;; Gerado por gerar_testes.py a partir de casos.csv — não edite à mão.
(ns situacao-test
  (:require [clojure.test :refer [deftest is run-tests]]))

(deftest casos-de-casos-csv
  (is (= :aprovado (situacao/situacao {:a1 3.5 :a2 4.0 :af nil :freq 80.0})) "soma 7,5")
  (is (= :aprovado (situacao/situacao {:a1 3.0 :a2 3.0 :af nil :freq 75.0})) "limites: soma 6,0 e frequência 75%")
  (is (= :aprovado (situacao/situacao {:a1 2.1 :a2 3.9 :af nil :freq 80.0})) "soma 6,0 com decimais")
  (is (= :reprovado-por-falta (situacao/situacao {:a1 5.0 :a2 5.0 :af nil :freq 74.9})) "nota máxima não salva a frequência")
  (is (= :reprovado-por-falta (situacao/situacao {:a1 0.0 :a2 0.0 :af nil :freq 0.0})) "a frequência é verificada primeiro")
  (is (= :reprovado-por-falta (situacao/situacao {:a1 2.0 :a2 3.0 :af 5.0 :freq 70.0})) "AF não salva a frequência")
  (is (= :reprovado (situacao/situacao {:a1 0.5 :a2 5.0 :af nil :freq 100.0})) "menos de 1 ponto na A1: sem direito à AF")
  (is (= :reprovado (situacao/situacao {:a1 5.0 :a2 0.9 :af nil :freq 100.0})) "menos de 1 ponto na A2: sem direito à AF")
  (is (= :reprovado (situacao/situacao {:a1 0.5 :a2 5.0 :af 5.0 :freq 80.0})) "a nota de AF é ignorada")
  (is (= :af (situacao/situacao {:a1 2.0 :a2 3.0 :af nil :freq 90.0})) "soma 5,0: precisa de 3,0 na AF")
  (is (= :af (situacao/situacao {:a1 1.0 :a2 1.0 :af nil :freq 80.0})) "exatamente 1 ponto: tem direito à AF")
  (is (= :aprovado-na-af (situacao/situacao {:a1 2.0 :a2 3.0 :af 3.5 :freq 90.0})) "3,5 substitui o 2,0: 6,5")
  (is (= :aprovado-na-af (situacao/situacao {:a1 1.0 :a2 1.0 :af 5.0 :freq 80.0})) "5,0 + 1,0 = 6,0")
  (is (= :aprovado-na-af (situacao/situacao {:a1 2.9 :a2 3.0 :af 3.0 :freq 80.0})) "3,0 + 3,0 = 6,0")
  (is (= :aprovado-na-af (situacao/situacao {:a1 4.5 :a2 1.4 :af 2.0 :freq 76.0})) "2,0 substitui o 1,4: 6,5")
  (is (= :reprovado-na-af (situacao/situacao {:a1 2.0 :a2 3.0 :af 2.5 :freq 90.0})) "2,5 + 3,0 = 5,5")
  (is (= :reprovado-na-af (situacao/situacao {:a1 4.0 :a2 1.9 :af 1.9 :freq 80.0})) "1,9 + 4,0 = 5,9")
  (is (= :aprovado (situacao/situacao {:a1 4.0 :a2 4.0 :af 3.0 :freq 80.0})) "já aprovado: a AF não muda nada"))

(deftest nota-minima
  (is (< (Math/abs (- 3.0 (situacao/nota-minima-af 2.0 3.0))) 1e-9))
  (is (< (Math/abs (- 5.0 (situacao/nota-minima-af 1.0 1.0))) 1e-9))
  (is (< (Math/abs (- 1.5 (situacao/nota-minima-af 4.5 1.4))) 1e-9))
  (is (< (Math/abs (- 1.9 (situacao/nota-minima-af 4.1 1.0))) 1e-9)))

(run-tests 'situacao-test)
