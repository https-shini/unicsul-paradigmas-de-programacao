;; Testes do projeto P4. Rode com:  python3 ferramentas/testar_projetos.py P4
;; A ferramenta junta o seu estatisticas.clj com este arquivo e executa no Clojure (ou no nbb).
(ns estatisticas-test
  (:require [clojure.test :refer [deftest is testing run-tests]]))

(def texto "O gato e o rato. O rato roeu a roupa do rei de Roma!")

(defn perto? [a b] (< (Math/abs (- a b)) 1e-9))

(deftest t1-palavras
  (is (= ["o" "gato" "e" "o" "rato" "o" "rato" "roeu" "a" "roupa" "do" "rei" "de" "roma"]
         (estatisticas/palavras texto)))
  (is (= ["programação" "é" "ótima"] (estatisticas/palavras "Programação é ÓTIMA!!!")))
  (is (= ["plp" "2026"] (estatisticas/palavras "  PLP, 2026.  ")))
  (is (empty? (estatisticas/palavras "")))
  (is (empty? (estatisticas/palavras "... ?!"))))

(deftest t2-contar-recursivo
  (is (= 14 (estatisticas/contar (estatisticas/palavras texto))))
  (is (= 0 (estatisticas/contar [])))
  (is (= 3 (estatisticas/contar ["a" "b" "c"]))))

(deftest t3-frequencias
  (let [f (estatisticas/frequencias (estatisticas/palavras texto))]
    (is (= 3 (get f "o")))
    (is (= 2 (get f "rato")))
    (is (= 1 (get f "roma")))
    (is (nil? (get f "cachorro")))
    (is (= 11 (count f))))
  (is (= {} (estatisticas/frequencias []))))

(deftest t4-stopwords
  (is (= ["gato" "rato" "rato" "roeu" "roupa" "rei" "roma"]
         (estatisticas/sem-stopwords (estatisticas/palavras texto)))))

(deftest t5-mais-frequentes
  (is (= [["b" 3] ["a" 2] ["c" 2]] (estatisticas/mais-frequentes 3 {"a" 2 "b" 3 "c" 2 "d" 1})))
  (is (= [["b" 3]] (estatisticas/mais-frequentes 1 {"a" 2 "b" 3})))
  (is (= [] (estatisticas/mais-frequentes 5 {}))))

(deftest t6-medidas
  (let [ps (estatisticas/palavras texto)]
    (is (perto? (/ 37.0 14) (estatisticas/comprimento-medio ps)))
    (is (= "roupa" (estatisticas/maior-palavra ps))))
  (is (perto? 0.0 (estatisticas/comprimento-medio [])))
  (is (nil? (estatisticas/maior-palavra [])))
  (is (= "abc" (estatisticas/maior-palavra ["ab" "abc" "xyz"]))))

(deftest t7-indice
  (is (= {"g" ["gato"] "r" ["rato" "roeu" "roupa"]}
         (estatisticas/indice-alfabetico ["rato" "gato" "roeu" "rato" "roupa"])))
  (is (= ["g" "r"] (keys (estatisticas/indice-alfabetico ["rato" "gato"])))))

(deftest t8-relatorio
  (let [r (estatisticas/relatorio texto)]
    (is (= 14 (:total r)))
    (is (= 11 (:distintas r)))
    (is (= "roupa" (:maior r)))
    (is (= [["rato" 2] ["gato" 1] ["rei" 1]] (:top3 r)))
    (is (perto? (/ 37.0 14) (:media r)))))

(deftest t9-sem-efeitos-colaterais
  (let [ps ["b" "a" "b"]
        antes (vec ps)]
    (estatisticas/frequencias ps)
    (estatisticas/sem-stopwords ps)
    (estatisticas/mais-frequentes 2 {"a" 1 "b" 2})
    (is (= antes ps))
    (is (= (estatisticas/relatorio texto) (estatisticas/relatorio texto)))))

(run-tests 'estatisticas-test)
