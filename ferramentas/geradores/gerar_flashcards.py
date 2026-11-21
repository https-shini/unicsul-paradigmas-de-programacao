#!/usr/bin/env python3
"""Gera o baralho de flashcards (Anki) em 06 - Revisões e Sínteses/Flashcards/.

Saídas: plp-flashcards.apkg (importável no Anki/AnkiDroid/AnkiMobile), plp-flashcards.tsv e README.md.
Fontes: o glossário (lista E de gerar_glossario.py) + cartões de comparação e de leitura de código abaixo.
Uso: python3 ferramentas/geradores/gerar_flashcards.py   (requer: pip install genanki)
"""
import csv, html, os, re, sys
import genanki

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import gerar_glossario as G  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(AQUI))
SAIDA = os.path.join(RAIZ, "06 - Revisões e Sínteses", "Flashcards")

# (frente, verso, aulas)
COMPARACOES = [
 ("Diferencie compilação, interpretação pura e implementação híbrida.", "**Compilação:** traduz todo o programa para código de máquina antes da execução (rápido, preso à plataforma; C, C++). **Interpretação pura:** traduz e executa instrução a instrução (portável, lento; Python, PHP, JavaScript na classificação da disciplina). **Híbrida:** compila para código intermediário (bytecode/CIL) executado por uma máquina virtual (Java/JVM, C#/CLR).", [3]),
 ("Qual o papel do bytecode e da JVM na portabilidade de Java?", "O `javac` gera bytecode independente de plataforma (`.class`); a JVM, implementada para cada sistema, executa esse bytecode (interpretando ou compilando com JIT). O mesmo `.class` roda em qualquer sistema com JVM.", [3]),
 ("Diferencie lexema, token e padrão.", "**Lexema:** a sequência concreta de caracteres (`soma1`, `10`, `+`). **Token:** a categoria do lexema (identificador, constante, operador…). **Padrão:** a regra que descreve a forma dos lexemas de um token.", [4]),
 ("`x = (y + 10 * z;` tem erro léxico ou sintático? Por quê?", "**Sintático.** Todos os lexemas formam tokens válidos; o erro é a estrutura (parêntese sem fechar), que a gramática não aceita.", [4]),
 ("Diferencie sintaxe concreta e sintaxe abstrata.", "A **concreta** define como os tokens se combinam em comandos (descrita por BNF), incluindo pontuação e parênteses. A **abstrata** guarda só a estrutura essencial, como uma árvore, sem esses detalhes.", [4]),
 ("Quais são os seis atributos de uma variável?", "Nome, endereço, valor, tipo, tempo de vida e escopo.", [5]),
 ("Diferencie escopo estático e escopo dinâmico.", "**Estático (léxico):** o nome não local é resolvido pela posição no texto (ancestral textual), na compilação; C, Java. **Dinâmico:** resolvido pela sequência de chamadas em execução; APL, LISP antigo, `local` em Perl. O dinâmico prejudica a legibilidade.", [5]),
 ("Diferencie escopo e tempo de vida, com um exemplo.", "**Escopo:** onde o nome é visível no código. **Tempo de vida:** quando a variável existe na memória. Exemplo: uma local `static` em C tem escopo local, mas existe durante todo o programa.", [5, 8]),
 ("Diferencie semântica estática e semântica dinâmica.", "**Estática:** regras verificáveis na compilação (tipos, declarações). **Dinâmica:** o significado/comportamento do programa durante a execução.", [5]),
 ("Diferencie tipagem estática e dinâmica.", "**Estática:** o tipo é vinculado na compilação e não muda (C, Java). **Dinâmica:** o tipo é vinculado na execução, conforme o valor (Python, PHP).", [6]),
 ("Diferencie tipagem forte e fraca. A coerção torna a tipagem mais forte ou mais fraca?", "Força = quanto a linguagem recusa operações entre tipos diferentes. A **coerção** (conversão implícita) **enfraquece** a tipagem. Forte: Java, Python. Fraca: C, PHP. É um eixo independente de estática/dinâmica.", [6]),
 ("Classifique C, Java, Python e PHP quanto à tipagem (estática/dinâmica × forte/fraca).", "C: estática e fraca. Java: estática e forte. Python: dinâmica e forte. PHP: dinâmica e fraca.", [6]),
 ("Diferencie alocação estática e dinâmica.", "**Estática:** definida na compilação, tamanho fixo (globais e `static` no segmento estático). **Dinâmica:** em tempo de execução, no heap, com `new`/`malloc`, tamanho variável; liberada com `delete`/`free` ou pela coleta de lixo.", [8]),
 ("Quais são as regiões de memória de um programa e o que vai em cada uma?", "**Código:** instruções. **Estático:** globais e `static`. **Heap:** dados alocados dinamicamente. **Livre:** espaço entre heap e pilha. **Pilha:** locais, parâmetros e endereços de retorno.", [8]),
 ("Diferencie `new int(4)` e `new int[4]` em C++.", "`new int(4)` aloca **um** inteiro com valor 4 (liberar com `delete`). `new int[4]` aloca **quatro** inteiros (liberar com `delete[]`).", [8]),
 ("Quais são os requisitos de Turing-completude de uma linguagem imperativa (segundo a Aula 09)?", "Variáveis, números inteiros, operações aritméticas, atribuição, sequenciamento baseado em memória, condições e comandos de ramificação (desvio).", [9]),
 ("Por que as linguagens imperativas são chamadas de 'linguagens de von Neumann'?", "Porque abstraem essa arquitetura: variáveis = células de memória; atribuição = transferência de dados entre CPU e memória; repetição = execução eficiente de instruções armazenadas em sequência.", [9]),
 ("O que Dijkstra argumentou em 1968 e o que Böhm e Jacopini provaram em 1966?", "**Dijkstra:** o `goto` destrói a correspondência entre o texto do programa e sua execução (índices textuais e dinâmicos) e deveria ser **abolido** das linguagens de alto nível. **Böhm e Jacopini:** provaram que sequência, seleção e repetição bastam para qualquer fluxograma.", [9]),
 ("Diferencie abstração procedural e abstração de dados.", "**Procedural:** esconde **como** um cálculo é feito, expondo a assinatura da função (característica do imperativo). **De dados (TDA):** esconde **como** um tipo é representado, expondo só suas operações (base da OO).", [10, 12]),
 ("O que é acoplamento e o que é coesão? Qual é o desejável?", "**Acoplamento:** grau de dependência entre módulos — desejável **baixo**. **Coesão:** grau em que um módulo tem uma única responsabilidade — desejável **alta**.", [10]),
 ("Quais são os quatro modelos de passagem de parâmetros e sua semântica?", "**Por valor:** entrada (cópia). **Por resultado:** saída (cópia no retorno). **Por valor-resultado:** entrada e saída (cópia na ida e na volta). **Por referência:** entrada e saída (endereço; alteração imediata).", [11]),
 ("Diferencie passagem por valor-resultado e por referência.", "Ambas são de entrada e saída. Valor-resultado **copia** o valor e só atualiza o argumento **no retorno**; referência usa o **endereço**, e a alteração é imediata. Diferem quando há *aliasing*.", [11]),
 ("O que fazem `ref`, `out` e `in` em C#?", "`ref`: referência (entrada e saída; precisa estar inicializado). `out`: semântica de saída, implementada por referência (o método deve atribuir). `in` (e `ref readonly`): referência somente leitura.", [11]),
 ("O que é encapsulamento e qual o papel dos modificadores de acesso?", "Agrupar dados e operações numa unidade (classe) e ocultar os detalhes internos. `private` protege o estado, `public` expõe a interface e `protected` libera para as subclasses.", [12]),
 ("Diferencie destrutor (C++) e coleta de lixo (Java).", "Em C++, o programador libera objetos do heap com `delete`, que chama o destrutor `~Classe()` para liberar recursos. Em Java, não há destrutor: a coleta de lixo libera automaticamente objetos sem referência.", [12]),
 ("Diferencie herança simples, herança múltipla e interfaces em Java.", "**Simples:** uma superclasse (Java, C#). **Múltipla:** várias superclasses (C++, Python) — mais reuso, mais complexidade e ambiguidades. **Interfaces:** Java permite uma superclasse e várias interfaces, herdando contratos em vez de código.", [13]),
 ("Diferencie sobrecarga e sobrescrita.", "**Sobrecarga** (polimorfismo estático): mesmo nome, parâmetros diferentes; escolhida na compilação. **Sobrescrita** (polimorfismo dinâmico): a subclasse redefine o método herdado com a mesma assinatura; escolhida em execução pelo tipo real do objeto.", [13]),
 ("Diferencie classe abstrata e interface (modelo clássico de Java).", "Ambas não são instanciáveis. A classe abstrata pode ter atributos de instância e métodos com corpo, e a classe herda de só uma (`extends`). A interface clássica tem só assinaturas e constantes, e a classe pode implementar várias (desde o Java 8 há métodos `default`).", [13]),
 ("Quais são as características do paradigma funcional puro?", "Programa = composição de funções matemáticas; sem variáveis mutáveis, sem atribuição e sem laços; logo, sem efeitos colaterais. A repetição é feita por recursão.", [14]),
 ("Diferencie linguagens funcionais puras e impuras, com exemplos.", "**Puras:** não permitem efeitos colaterais nem estado mutável (Haskell, Miranda). **Impuras:** permitem alguns recursos imperativos (LISP, Scheme, Clojure, Elixir, Erlang).", [14]),
 ("Diferencie abordagem procedural e declarativa. Como o professor classifica os paradigmas?", "**Procedural:** o programador especifica os passos da solução. **Declarativa:** especifica o que se deseja, e um mecanismo encontra a resposta. Professor (Aula 15): imperativo, OO e funcional são procedurais; o lógico é declarativo.", [2, 15]),
 ("Diferencie fato, regra e consulta em Prolog.", "**Fato:** proposição assumida verdadeira (`pai(joao, ana).`). **Regra:** define uma relação a partir de outras (`avo(X,Z) :- pai(X,Y), pai(Y,Z).`). **Consulta:** pergunta à base (`?- pai(X, ana).`).", [15]),
 ("O que é unificação em Prolog?", "Tornar dois termos idênticos encontrando valores para as variáveis. `pai(X, ana)` unifica com `pai(joao, ana)` fazendo `X = joao`.", [15]),
 ("Em Prolog, qual a diferença entre `X = 2 + 3` e `X is 2 + 3`?", "`=` **unifica**: X fica ligado ao termo `2+3`. `is` **avalia** a expressão aritmética: X = 5.", [15]),
]

CODIGO = [
 ("Clojure (JVM): quanto vale `(/ 10 4)`?", "`5/2` — um `Ratio` (fração exata). Clojure não trunca a divisão de inteiros.", [14]),
 ("Clojure: quanto valem `(quot 10 4)` e `(rem 10 4)`?", "`2` e `2` — quociente inteiro e resto.", [14]),
 ("Clojure: quanto vale `(- 20 7 4)`?", "`9` — a subtração com vários argumentos é feita da esquerda para a direita: (20 − 7) − 4.", [14]),
 ("Clojure: avalie `(* (+ 2 3) (- 10 (quot 9 2)))`.", "`30` — (quot 9 2) = 4; 10 − 4 = 6; 2 + 3 = 5; 5 · 6 = 30.", [14]),
 ("Clojure: como escrever x + 2·y?", "`(+ x (* 2 y))` — notação prefixa: o operador vem primeiro.", [14]),
 ("Prolog: com `pai(joao, ana). pai(joao, maria).`, o que responde `?- pai(joao, X).`?", "`X = ana ;` `X = maria.` — o *backtracking* encontra todas as soluções.", [15]),
 ("Prolog: `Joao` é uma constante ou uma variável?", "**Variável** — começa com maiúscula. Constantes (átomos) começam com minúscula: `joao`.", [15]),
 ("C: o que acontece em `int r = 2.5 + 3;`?", "Compila; `r` vale `5` — a coerção implícita converte 5.5 para int (tipagem fraca). Em Java, o equivalente não compila sem *cast*.", [6]),
 ("PHP × Python: `10 + \"20\"`", "PHP: `30` (coerção — tipagem fraca). Python: `TypeError` (dinâmica, porém forte).", [6]),
 ("Java: o que imprime `System.out.println(1 + 2 + \"3\");`? E `\"1\" + 2 + 3`?", "`33` e `123` — o `+` é avaliado da esquerda para a direita; ao encontrar uma `String`, passa a concatenar (sobrecarga do operador).", [6, 13]),
 ("C: `int n = 10; void f(){ printf(\"%d\", n); } void g(){ int n = 20; f(); }` — o que `g()` imprime? E com escopo dinâmico?", "C (escopo estático): **10**. Com escopo dinâmico: **20** (o `n` mais recente na pilha de chamadas é o de `g`).", [5]),
 ("Matriz `int m[3][4]` em C (por linhas), base 1000, `int` de 4 bytes: endereço de `m[2][1]`?", "1000 + (2·4 + 1)·4 = **1036**.", [7]),
 ("`troca(a, b)` com x = 1, y = 2: o que imprime `x, y` após a chamada, por valor e por referência?", "Por valor: **1 2** (a troca é feita nas cópias). Por referência: **2 1**.", [11]),
 ("Java: `Conta c = new ContaEspecial(); c.tipo();` — qual versão de `tipo()` é chamada?", "A de `ContaEspecial`: vinculação dinâmica, pelo tipo **real** do objeto (polimorfismo dinâmico).", [13]),
]

MODELO = genanki.Model(
    1607392319, "PLP — Básico",
    fields=[{"name": "Frente"}, {"name": "Verso"}, {"name": "Fonte"}],
    templates=[{"name": "Cartão", "qfmt": "<div class='f'>{{Frente}}</div>",
                "afmt": "<div class='f'>{{Frente}}</div><hr id=answer><div class='v'>{{Verso}}</div><div class='s'>{{Fonte}}</div>"}],
    css=".card{font-family:system-ui,sans-serif;font-size:19px;text-align:left;line-height:1.45;padding:8px}"
        ".f{font-weight:600}.s{margin-top:14px;font-size:14px;color:#777}code{background:#f2f2f2;padding:1px 4px;border-radius:3px}")


def md_html(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", t)
    return t


def aulas_txt(aulas):
    return "Aulas: " + ", ".join(f"{a:02d}" if isinstance(a, int) else "artigo de Dijkstra" for a in aulas)


def main():
    cartas = []  # (baralho, frente, verso, fonte, tags)
    for termo, defin, ex, aulas, comp in G.E:
        verso = defin + ("  [Complemento]" if comp else "") + "\n\nExemplo: " + ex
        tags = ["glossario"] + [f"aula-{a:02d}" for a in aulas if isinstance(a, int)]
        cartas.append(("PLP::1 Glossário", termo, verso, aulas_txt(aulas), tags))
    for f, v, aulas in COMPARACOES:
        cartas.append(("PLP::2 Comparações", f, v, aulas_txt(aulas), ["comparacao"] + [f"aula-{a:02d}" for a in aulas]))
    for f, v, aulas in CODIGO:
        cartas.append(("PLP::3 Leitura de código", f, v, aulas_txt(aulas), ["codigo"] + [f"aula-{a:02d}" for a in aulas]))

    ids = {"PLP::1 Glossário": 2059400110, "PLP::2 Comparações": 2059400111, "PLP::3 Leitura de código": 2059400112}
    decks = {n: genanki.Deck(i, n) for n, i in ids.items()}
    for deck, f, v, fonte, tags in cartas:
        nota = genanki.Note(model=MODELO, fields=[md_html(f), md_html(v).replace("\n", "<br>"), fonte],
                            tags=tags, guid=genanki.guid_for("plp", f))
        decks[deck].add_note(nota)
    os.makedirs(SAIDA, exist_ok=True)
    pacote = genanki.Package(list(decks.values()))
    caminho = os.path.join(SAIDA, "plp-flashcards.apkg")
    pacote.write_to_file(caminho, timestamp=1763700000)
    with open(os.path.join(SAIDA, "plp-flashcards.tsv"), "w", encoding="utf-8", newline="") as fh:
        fh.write("#separator:tab\n#html:true\n#deck column:1\n#tags column:5\n")
        w = csv.writer(fh, delimiter="\t", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        for deck, f, v, fonte, tags in cartas:
            w.writerow([deck, md_html(f), md_html(v).replace("\n", "<br>"), fonte, " ".join(tags)])
    cont = {n: sum(1 for c in cartas if c[0] == n) for n in ids}
    escrever_readme(cont, len(cartas))
    print(f"{len(cartas)} cartões:", cont)


def escrever_readme(cont, total):
    L = ["# Flashcards (Anki)", "",
         "> **[Explicação elaborada]** Baralho de repetição espaçada gerado a partir do [glossário](../../07%20-%20Glossário/glossario.md) e dos [quadros comparativos](../quadros-comparativos.md). Não é material do professor.", "",
         "| Baralho | Cartões | Conteúdo |", "| --- | :-: | --- |",
         f"| PLP › 1 Glossário | {cont['PLP::1 Glossário']} | Um cartão por termo: definição, exemplo e aulas |",
         f"| PLP › 2 Comparações | {cont['PLP::2 Comparações']} | \"Diferencie X e Y\" — o formato mais cobrado nas listas |",
         f"| PLP › 3 Leitura de código | {cont['PLP::3 Leitura de código']} | \"O que este trecho imprime?\" em C, Java, PHP, Python, Clojure e Prolog |",
         f"| **Total** | **{total}** | |", "",
         "## Como usar", "",
         "1. Instale o [Anki](https://apps.ankiweb.net/) (computador), o AnkiDroid (Android) ou o AnkiMobile (iOS).",
         "2. Baixe [`plp-flashcards.apkg`](plp-flashcards.apkg) e abra o arquivo (no Anki: **Arquivo › Importar**).",
         "3. Estude um pouco por dia; o Anki mostra cada cartão de novo na hora certa para fixar o conteúdo.", "",
         "Cada cartão tem etiquetas `aula-NN`, `glossario`, `comparacao` ou `codigo`. No Anki, a busca `tag:aula-14` filtra os cartões de uma aula — útil na semana da prova.", "",
         "**Sem Anki?** O arquivo [`plp-flashcards.tsv`](plp-flashcards.tsv) pode ser importado em outros aplicativos de flashcards (Quizlet, RemNote, Mochi) ou aberto numa planilha.", "",
         "**Para atualizar:** edite os termos em `ferramentas/geradores/gerar_glossario.py` ou as listas `COMPARACOES` e `CODIGO` em `ferramentas/geradores/gerar_flashcards.py` e rode `python3 ferramentas/geradores/gerar_flashcards.py`. Reimportar o `.apkg` atualiza os cartões sem duplicar e sem perder o seu histórico."]
    open(os.path.join(SAIDA, "README.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
