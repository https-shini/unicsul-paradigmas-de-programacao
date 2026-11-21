;; P4 — Estatísticas de texto no paradigma funcional (Aula 14).
;; Regras do jogo: só funções puras; nada de def dentro de funções, atom ou variável reatribuída.
;; O código deve rodar no Clojure (JVM) e no nbb (ClojureScript): evite Character, format e slurp.
(ns estatisticas
  (:require [clojure.string :as str]))

(def stopwords
  "Palavras muito comuns, ignoradas no ranking."
  #{"a" "o" "e" "é" "de" "da" "do" "que" "em" "um" "uma" "os" "as" "para" "com" "no" "na" "se"})

(defn palavras
  "R1. Vetor com as palavras do texto, em minúsculas, sem pontuação.
  Dica: str/lower-case e re-seq com #\"[a-z0-9áàâãéêíóôõúüç]+\"; vec garante [] quando não há palavras."
  [texto]
  (throw (ex-info "TODO: palavras" {})))

(defn contar
  "R2. Quantidade de palavras usando RECURSÃO — sem count, sem loop/recur."
  [ps]
  (throw (ex-info "TODO: contar" {})))

(defn frequencias
  "R3. Mapa palavra → ocorrências usando reduce (não vale chamar frequencies)."
  [ps]
  (throw (ex-info "TODO: frequencias" {})))

(defn sem-stopwords
  "R4. Vetor sem as stopwords. Dica: um conjunto também é uma função — (stopwords \"de\") devolve \"de\"."
  [ps]
  (throw (ex-info "TODO: sem-stopwords" {})))

(defn mais-frequentes
  "R5. Os n pares [palavra quantidade] mais frequentes; empate → ordem alfabética. Devolva um vetor de vetores."
  [n freq]
  (throw (ex-info "TODO: mais-frequentes" {})))

(defn comprimento-medio
  "R6. Média do número de letras, como double; 0.0 para lista vazia."
  [ps]
  (throw (ex-info "TODO: comprimento-medio" {})))

(defn maior-palavra
  "R6. A primeira palavra de maior comprimento; nil para lista vazia. Dica: reduce."
  [ps]
  (throw (ex-info "TODO: maior-palavra" {})))

(defn indice-alfabetico
  "R7. Mapa ORDENADO (sorted-map): letra inicial → palavras distintas, na ordem em que aparecem.
  Use (subs p 0 1) para a letra — (first p) dá um caractere na JVM e uma string no ClojureScript."
  [ps]
  (throw (ex-info "TODO: indice-alfabetico" {})))

(defn relatorio
  "R8. Mapa com :total :distintas :media :maior :top3 (as 3 mais frequentes, sem stopwords)."
  [texto]
  (throw (ex-info "TODO: relatorio" {})))
