<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 09](../README.md) › [02 - Resumo Teórico](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 09a — "Go To Statement Considered Harmful" (Dijkstra, 1968) · Resumo e análise

> **Fonte:** [`Aula09a_ArtigoDijkstra68.pdf`](../01%20-%20Slides%20Originais/Aula09a_ArtigoDijkstra68.pdf) (2 páginas). Edsger W. Dijkstra, Technological University Eindhoven. Publicado como carta ao editor em *Communications of the ACM*, v. 11, n. 3, p. 147–148, mar. 1968.
> **Sobre o arquivo:** o corpo do artigo é uma **digitalização (imagem) sem texto pesquisável**; só o cabeçalho, o rodapé e a linha de fonte acrescentados ao PDF são texto. Para este resumo, o texto foi extraído por OCR e conferido visualmente na imagem; a digitalização está legível, sem trechos perdidos.
>
> **[Atenção]** O cabeçalho do PDF e a bibliografia da Aula 01 ([p.9](../../Aula%2001%20-%20Apresentação%20da%20Disciplina/01%20-%20Slides%20Originais/README.md#página-9)) escrevem "Edgar Dijkstra"; o nome correto é **Edsger** W. Dijkstra, como na assinatura do artigo.
> **Legenda:** ver [Convenções](../../../README.md#convenções-de-marcação). O artigo está em inglês; as passagens abaixo são **paráfrases** em português. Os termos técnicos originais aparecem entre parênteses.

---

## 1. Em uma frase

**[Explicação elaborada]** Dijkstra argumenta que o `go to` deve ser **abolido** das linguagens de alto nível porque destrói a correspondência entre o **texto estático** do programa e o **processo dinâmico** que ele produz, tornando quase impossível raciocinar sobre o que o programa está fazendo em cada instante.

## 2. Contexto

**[Material original]** Dijkstra conta que, havia anos, percebia que "a qualidade dos programadores é uma função decrescente da densidade de comandos `go to` nos programas que produzem". Mais recentemente, descobriu **por que** o `go to` tem efeitos tão desastrosos e se convenceu de que ele deveria ser abolido de todas as linguagens de "alto nível" — tudo, exceto talvez o código de máquina puro. Publicou a carta porque foi incentivado a fazê-lo em discussões recentes.

Palavras-chave do artigo: *go to statement, jump instruction, branch instruction, conditional clause, alternative clause, repetitive clause, program intelligibility, program sequencing*.

## 3. O argumento, passo a passo

### 3.1 Primeira observação: o que importa é o processo

**[Material original]** A atividade do programador termina quando ele constrói um programa correto, mas o **verdadeiro objeto** dessa atividade é o **processo** que ocorre sob o controle do programa. É o processo, em seu comportamento dinâmico, que precisa satisfazer a especificação. E, depois que o programa está pronto, a "fabricação" do processo é delegada à máquina.

### 3.2 Segunda observação: somos bons com o estático e ruins com o dinâmico

**[Material original]** Nossas capacidades intelectuais dominam bem **relações estáticas** e são relativamente pobres para **visualizar processos que evoluem no tempo**. Por isso devemos, como programadores conscientes das próprias limitações, **encurtar ao máximo a distância conceitual** entre o programa estático (espalhado no espaço do texto) e o processo dinâmico (espalhado no tempo), tornando a correspondência entre os dois **a mais trivial possível**.

### 3.3 Como caracterizar o "ponto" em que um processo está?

**[Material original]** Dijkstra propõe um teste mental: se o processo for interrompido após uma ação qualquer, que dados precisamos guardar para refazê-lo até exatamente o mesmo ponto? A resposta depende das construções da linguagem:

| Construções presentes | Como descrever o progresso | Nome dado no artigo |
| --- | --- | --- |
| Só atribuições em sequência | Um ponteiro para um lugar no texto, entre duas ações | **Índice textual** (*textual index*) |
| + `if B then A`, `if B then A1 else A2`, `case` (Hoare), expressões condicionais (McCarthy) | Continua bastando **um** índice textual | — |
| + **procedimentos** | Uma **sequência** de índices textuais, do tamanho da profundidade dinâmica das chamadas | — |
| + **repetição** (`while B repeat A`, `repeat A until B`) | Índices textuais **e**, para cada laço ativo, um contador da iteração atual | **Índice dinâmico** (*dynamic index*) |

**[Material original] — sobre a repetição:** logicamente, as cláusulas de repetição seriam supérfluas, porque a recursão poderia expressá-las. Dijkstra as mantém "por realismo": são fáceis de implementar no hardware da época, e o raciocínio por **indução** nos permite dominar intelectualmente os processos que elas geram.

**[Material original] — jogo de palavras:** sem `go to`, Dijkstra se permite uma ambiguidade sintática na expressão "*successive action descriptions*": lida como "sucessivas (descrições de ações)", significa sucessivas no **texto**; lida como "descrições de (ações sucessivas)", sucessivas no **tempo**. Sem saltos, as duas leituras coincidem — e esse é o ponto.

### 3.4 O ponto principal: coordenadas independentes do programador

**[Material original]** Os valores desses índices **estão fora do controle do programador**. São gerados pela escrita do programa ou pela evolução dinâmica do processo, quer ele queira, quer não. Funcionam como **coordenadas independentes** para descrever o progresso do processo.

### 3.5 Por que precisamos dessas coordenadas — o exemplo da sala

**[Material original]** Só conseguimos interpretar o **valor de uma variável** em relação ao **progresso do processo**. Exemplo: para contar quantas pessoas, `n`, há numa sala inicialmente vazia, incrementamos `n` sempre que alguém entra. No instante entre ver alguém entrar e fazer o incremento, `n` vale **o número de pessoas na sala menos um**.

**[Explicação elaborada]** O significado de `n` ("número de pessoas" ou "número de pessoas − 1") depende de **onde** o processo está. Com índices textuais e dinâmicos, sabemos onde estamos e, portanto, o que `n` significa naquele ponto. É a ideia que, mais tarde, se formalizou como **invariante** de laço.

### 3.6 O problema do `go to`

**[Material original]**

- O uso desenfreado do `go to` torna "terrivelmente difícil" encontrar um conjunto significativo de coordenadas para descrever o progresso.
- Usar os valores de variáveis escolhidas como coordenadas está fora de questão, porque é **em relação ao progresso** que o significado desses valores deve ser entendido — seria um raciocínio circular.
- Com `go to`, ainda é possível descrever o progresso de forma única por um **contador do número de ações** executadas desde o início do programa — uma espécie de "relógio normalizado". Essa coordenada é única, mas **totalmente inútil**: nela, definir todos os pontos em que, por exemplo, `n` é igual ao número de pessoas menos um vira algo extremamente complicado.

### 3.7 Conclusão

**[Material original]** O `go to` como está é **primitivo demais**: é "um convite a fazer uma bagunça" no programa. As cláusulas estruturadas podem ser vistas como **freios** ao seu uso. Dijkstra não afirma que elas sejam exaustivas, mas qualquer cláusula nova proposta (por exemplo, cláusulas de aborto, *abortion clauses*) deve preservar um **sistema de coordenadas independente do programador**, útil e gerenciável.

## 4. Créditos e histórico (p.2)

**[Material original]**

- Dijkstra reconhece influência de **Peter Landin** e **Christopher Strachey**.
- Registra que **Heinz Zemanek**, na reunião pré-ALGOL do início de 1959 em Copenhague, já duvidava explicitamente que o `go to` merecesse o mesmo status sintático da atribuição. Dijkstra se culpa, "em modesta medida", por não ter tirado as consequências daquela observação.
- A recomendação de restringir o `go to` a **saídas de alarme** (*alarm exits*) não é nova; ele presume que tenha sido feita por **C. A. R. Hoare**.
- **Wirth e Hoare**, ao motivar o comando `case`, dizem que ele, como o condicional, reflete a estrutura dinâmica do programa com mais clareza que `go to` e *switches*, e dispensa muitos rótulos.
- **Giuseppe Jacopini** (com Böhm) parece ter provado a **superfluidade lógica** do `go to`. Mas Dijkstra **não recomenda** traduzir mecanicamente um fluxograma qualquer num fluxograma sem saltos: o resultado não seria mais transparente que o original.

**Referências do artigo:**

1. Wirth, N.; Hoare, C. A. R. *A contribution to the development of ALGOL*. Comm. ACM 9 (jun. 1966), 413–432.
2. Böhm, C.; Jacopini, G. *Flow diagrams, Turing machines and languages with only two formation rules*. Comm. ACM 9 (maio 1966), 366–371.

## 5. Análise e relevância

**[Explicação elaborada]**

1. **Tese:** não é uma questão de gosto. O `go to` impede raciocinar sobre programas, porque apaga a relação entre "onde está no texto" e "o que já aconteceu".
2. **Solução:** usar só construções cujo progresso é descritível por coordenadas automáticas — sequência, seleção (`if`/`case`), repetição (`while`/`repeat`) e procedimentos. São as **estruturas de controle** da programação estruturada ([Aula 09, p.10 e p.17](resumo-aula-09.md#7-não-estruturado--estruturado-p1618)).
3. **Teoria × prática:** Böhm e Jacopini provaram que o `go to` é dispensável; Dijkstra explicou **por que** dispensá-lo, um argumento cognitivo e de legibilidade.
4. **Legado:** o artigo é considerado o marco da **programação estruturada**. As linguagens projetadas depois (Pascal, 1970; C, 1972) mantêm o `goto` só como exceção, e Java nem o implementa (`goto` é palavra reservada sem uso). O título — com o padrão "*X considered harmful*" — virou expressão idiomática na computação.
5. **Ponte para as próximas aulas:** a ideia de aproximar o texto do processo combina com a **abstração procedural** (Aula 10) e com os subprogramas, que têm um **único ponto de entrada** e devolvem o controle ao chamador ao terminar (Aula 11, [p.4](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/01%20-%20Slides%20Originais/README.md#página-4)). O encapsulamento de dados leva à OO (Aula 12).

> **[Complemento]** Segundo relatos posteriores do próprio Dijkstra, o título original da carta era "A case against the GO TO statement"; o título publicado foi escolhido pelo editor, Niklaus Wirth. Essa informação **não consta** no PDF da disciplina.

## 6. Comparação com o slide da Aula 09 (p.18)

| Slide (Aula 09, [p.18](../01%20-%20Slides%20Originais/README.md#página-18)) | Artigo |
| --- | --- |
| "O uso **excessivo** de `goto` era prejudicial" | Defende a **abolição** do `go to` nas linguagens de alto nível |
| "Qualquer sequência com `goto` poderia ser escrita com laços condicionais" — atribuído a Dijkstra | Essa prova é atribuída a **Jacopini** (Böhm & Jacopini, 1966) |
| — | A tradução **mecânica** de `goto` em laços **não é recomendada** |

## 7. Perguntas para fixação

1. O que é um índice textual? E um índice dinâmico?
2. Por que, segundo Dijkstra, não podemos usar os valores das variáveis como coordenadas do progresso?
3. O que o exemplo da contagem de pessoas na sala demonstra?
4. Qual é a diferença entre a contribuição de Böhm e Jacopini e a de Dijkstra?

Respostas em [resolucoes-aula-09.md](../04%20-%20Resoluções/resolucoes-aula-09.md#e10--perguntas-sobre-o-artigo-de-dijkstra).


<!-- nav:rodape -->

---

**Aula 09:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](resumo-aula-09.md) · **Artigo** · [Exercícios](../03%20-%20Exercícios/exercicios-aula-09.md) · [Resoluções](../04%20-%20Resoluções/resolucoes-aula-09.md) · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

**Links para esta página (13):** [Aula 09 · Resumo](resumo-aula-09.md) · [Aula 09 · Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md) · [Aula 09 · visão geral](../README.md) · [Aula 14 · Resumo](../../Aula%2014%20-%20Paradigma%20Funcional/02%20-%20Resumo%20Teórico/resumo-aula-14.md) · [Lista 02](../../../02%20-%20Listas%20de%20Exercícios/Lista%2002%20-%20Revisão%20II/README.md) · [03 — Trabalhos e Projetos](../../../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Simulado 01 · Resolução comentada](../../../04%20-%20Provas%20e%20Avaliações/Simulados/resolucao-simulado-01.md) · [Revisão da Unidade 2 — Paradigma imperativo (Aulas 09–11)](../../../06%20-%20Revisões%20e%20Sínteses/Revisões%20por%20Unidade/unidade-2-imperativo.md) · [Erratas e inconsistências do material](../../../06%20-%20Revisões%20e%20Sínteses/erratas-e-inconsistencias.md) · [Resumo geral da disciplina](../../../06%20-%20Revisões%20e%20Sínteses/resumo-geral-da-disciplina.md) · [Glossário](../../../07%20-%20Glossário/glossario.md) · [Artigos clássicos](../../../08%20-%20Referências%20e%20Fontes/artigos.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
