;; P4 — Estatísticas de texto no paradigma funcional (Aula 14).
;; Só funções puras: cada uma recebe dados e devolve dados NOVOS; nenhuma altera variável.
;; Roda no Clojure (JVM) e no nbb (ClojureScript): por isso não usamos Character, format nem slurp.
(ns estatisticas
  (:require [clojure.string :as str]))

(def stopwords
  "Palavras muito comuns, ignoradas no ranking."
  #{"a" "o" "e" "é" "de" "da" "do" "que" "em" "um" "uma" "os" "as" "para" "com" "no" "na" "se"})

(defn palavras
  "Vetor com as palavras do texto, em minúsculas, sem pontuação."
  [texto]
  (vec (re-seq #"[a-z0-9áàâãéêíóôõúüç]+" (str/lower-case texto))))

(defn contar
  "Quantidade de palavras, por RECURSÃO (sem laço e sem count): o funcional substitui a repetição pela recursão."
  [ps]
  (if (empty? ps)
    0
    (inc (contar (rest ps)))))

(defn frequencias
  "Mapa palavra → ocorrências, construído com reduce (o mesmo que a função frequencies do Clojure)."
  [ps]
  (reduce (fn [m p] (update m p (fnil inc 0))) {} ps))

(defn sem-stopwords
  "Remove as stopwords: filter/remove recebem uma FUNÇÃO como argumento (o conjunto é usado como função)."
  [ps]
  (vec (remove stopwords ps)))

(defn mais-frequentes
  "Os n pares [palavra quantidade] mais frequentes; empate → ordem alfabética."
  [n freq]
  (->> freq
       (sort-by (fn [[p c]] [(- c) p]))
       (take n)
       (mapv vec)))

(defn comprimento-medio
  "Média do número de letras; 0.0 para lista vazia."
  [ps]
  (if (empty? ps)
    0.0
    (double (/ (reduce + (map count ps)) (count ps)))))

(defn maior-palavra
  "A primeira palavra de maior comprimento; nil para lista vazia."
  [ps]
  (when (seq ps)
    (reduce (fn [a b] (if (> (count b) (count a)) b a)) ps)))

(defn indice-alfabetico
  "Mapa ordenado: letra inicial → palavras distintas, na ordem em que aparecem."
  [ps]
  (into (sorted-map)
        (map (fn [[letra lista]] [letra (vec (distinct lista))])
             (group-by #(subs % 0 1) ps))))

(defn relatorio
  "Combina as funções acima: composição de funções puras."
  [texto]
  (let [ps (palavras texto)]
    {:total     (contar ps)
     :distintas (count (set ps))
     :media     (comprimento-medio ps)
     :maior     (maior-palavra ps)
     :top3      (mais-frequentes 3 (frequencias (sem-stopwords ps)))}))
