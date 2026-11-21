#!/usr/bin/env python3
"""Gera 07 - Glossário/glossario.md. Os termos ficam na lista E abaixo (também usada pelos flashcards)."""
import os, urllib.parse, unicodedata, re
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = {1:"Aula 01 - Apresentação da Disciplina",2:"Aula 02 - Evolução das Linguagens e Paradigmas",3:"Aula 03 - Implementação das Linguagens",4:"Aula 04 - Sintaxe",5:"Aula 05 - Semântica",6:"Aula 06 - Sistema de Tipos",7:"Aula 07 - Tipos Compostos",8:"Aula 08 - Ponteiros",9:"Aula 09 - Paradigma Imperativo I",10:"Aula 10 - Paradigma Imperativo II",11:"Aula 11 - Paradigma Imperativo III",12:"Aula 12 - Paradigma Orientado a Objetos I",13:"Aula 13 - Paradigma Orientado a Objetos II",14:"Aula 14 - Paradigma Funcional",15:"Aula 15 - Paradigma Lógico"}
def link(n):
    if n == "D":
        p = "../01 - Aulas/Aula 09 - Paradigma Imperativo I/02 - Resumo Teórico/resumo-artigo-dijkstra-1968.md"
        return f"[artigo de Dijkstra]({p.replace(' ', '%20')})"
    p = f"../01 - Aulas/{A[n]}/02 - Resumo Teórico/resumo-aula-{n:02d}.md"
    return f"[{n:02d}]({p.replace(' ', '%20')})"
# (termo, definição, exemplo/explicação, aulas, complemento?)
E = [
("Abstração","Processo de destacar o que é essencial e ocultar detalhes para lidar com a complexidade.","Uma função `ordenarVetor` esconde **como** a ordenação é feita; uma classe `Pilha` esconde **como** os dados são guardados.",[10,12],False),
("Abstração de dados","Agrupamento da representação de um tipo com as operações sobre ele, com a representação oculta dos clientes.","Base do tipo abstrato de dados e da orientação a objetos. Ver **TDA**.",[10,12],False),
("Abstração procedural (de processos)","Decomposição do problema em subprogramas, de modo que quem usa uma função conhece sua interface (entrada, saída, efeito), mas não sua implementação.","Característica principal do paradigma imperativo; obtida por refinamento sucessivo.",[10,11],False),
("Acoplamento","Grau de dependência entre módulos de um programa. O desejável é **baixo** acoplamento.","Funções que leem e alteram as mesmas variáveis globais estão fortemente acopladas.",[10],False),
("Alocação dinâmica","Reserva de memória em **tempo de execução**, no heap, com tamanho que pode variar.","`int *v = new int[n];` em C++; liberação com `delete[] v;`.",[8],False),
("Alocação estática","Reserva de memória definida em **tempo de compilação**, com tamanho fixo.","Variáveis globais e locais `static` ficam no segmento estático.",[8],False),
("Análise léxica","Fase da compilação que lê os caracteres do fonte e os agrupa em **tokens**.","`soma = x + 10;` → identificador, símbolo `=`, identificador, operador `+`, constante, `;`.",[3,4],False),
("Análise sintática","Fase da compilação que verifica se a sequência de tokens forma construções válidas da gramática, produzindo a árvore sintática.","`x = (y + 10 * z;` passa pela análise léxica e falha na sintática.",[3,4],False),
("Arquitetura de von Neumann","Arquitetura em que dados e instruções ficam na **mesma memória**, separada da CPU, com execução sequencial de instruções.","O paradigma imperativo é uma abstração dela: variáveis = células de memória; atribuição = transferência entre CPU e memória.",[9,14],False),
("Atribuição","Comando que avalia uma expressão e grava o resultado em uma variável (`destino = expressão`).","Central no imperativo; ausente no modelo funcional puro.",[9,14],False),
("Backtracking","Mecanismo pelo qual o Prolog, ao falhar um objetivo, volta à última escolha e tenta a próxima alternativa.","Permite que `pai(joao, X)` devolva `X = ana`, depois `X = maria`…",[15],True),
("BNF (Backus-Naur Form)","Notação formal para descrever a sintaxe concreta de linguagens por meio de regras de produção (gramáticas livres de contexto).","`<atrib> ::= <id> = <expr>`.",[4],False),
("Bytecode","Código intermediário, independente de plataforma, gerado pelo compilador Java (`.class`) e executado pela JVM.","Chave da implementação híbrida e da portabilidade de Java.",[3],True),
("Classe","Definição de um tipo que agrupa atributos (estado) e métodos (comportamento); molde a partir do qual objetos são criados.","`class Pilha { private int topo; void push(int x) {…} }`.",[7,12],False),
("Classe abstrata","Classe que não pode ser instanciada e pode conter métodos sem implementação, a serem definidos pelas subclasses.","`abstract class Conta { abstract double saldo(); }`.",[13],False),
("Clojure","Linguagem funcional impura, dialeto de LISP, executada sobre a JVM; usada na disciplina.","`(+ 1 2)` vale 3; `(/ 10 4)` vale `5/2`.",[14],False),
("Coerção","Conversão de tipo **implícita**, feita automaticamente pela linguagem. Enfraquece a tipagem.","Em C, `int r = 2.5 + 3;` dá 5; em PHP, `10 + \"20\"` dá 30.",[6],False),
("Coesão","Grau em que os elementos de um módulo contribuem para uma única responsabilidade. O desejável é **alta** coesão.","Uma classe `Aluno` só com dados e operações de aluno tem alta coesão.",[10],False),
("Coleta de lixo (garbage collection)","Liberação automática da memória de objetos que não são mais referenciados.","Java usa coleta de lixo; C++ exige `delete`.",[8,12],False),
("Compilação","Tradução de todo o programa-fonte, antes da execução, para código de máquina de uma plataforma.","C, C++, Fortran, Pascal. Execução rápida, executável preso à plataforma.",[3],False),
("Constante nomeada","Identificador associado a um valor que não pode ser alterado depois da vinculação.","`const int MAX = 10;` em C; `final int MAX = 10;` em Java.",[5],False),
("Construtor","Método especial executado na criação de um objeto, para inicializar seu estado.","`Pilha() { topo = -1; }`.",[12],False),
("Consulta (Prolog)","Pergunta feita à base de fatos e regras; o Prolog responde com `true`/`false` ou com valores para as variáveis.","`?- pai(X, ana).` → `X = joao.`",[15],False),
("Declarativa (abordagem)","Abordagem em que o programador especifica **o que** deseja obter, e não os passos para obtê-lo.","Paradigma lógico; SQL e HTML são linguagens declarativas que, segundo a Aula15 p.5, não são linguagens de programação.",[2,15],False),
("Destrutor","Método especial executado quando um objeto é destruído, usado para liberar recursos.","`~Pilha()` em C++, que libera os nós alocados com `new`.",[12],False),
("Efeito colateral","Alteração de estado observável fora da função (variável global, parâmetro, E/S) além do valor retornado.","Ausente nas funções puras do paradigma funcional.",[11,14],False),
("Encapsulamento","Agrupamento de dados e operações relacionados em uma unidade, com controle de acesso que oculta os detalhes internos.","Atributos `private` e métodos `public` em uma classe.",[10,12],False),
("Enumeração","Tipo composto cujos valores são uma lista finita de constantes nomeadas.","`enum Dia {SEG, TER, QUA};`.",[7],False),
("Escopo","Trecho do programa em que um nome é **visível** (pode ser referenciado).","Variável local é visível só no bloco onde foi declarada.",[5],False),
("Escopo dinâmico","Regra que resolve nomes não locais pela **sequência de chamadas** em execução.","APL, LISP antigo; Perl com `local`. Prejudica a legibilidade.",[5],False),
("Escopo estático (léxico)","Regra que resolve nomes não locais pela **posição no texto** do programa (ancestral textual), em tempo de compilação.","C, Java, Pascal.",[5],False),
("Fato (Prolog)","Proposição assumida como verdadeira na base de conhecimento.","`pai(joao, ana).`",[15],False),
("Forma funcional","Função que recebe funções como argumento e/ou devolve uma função, permitindo construir funções complexas.","`map`, `reduce`, `comp` em Clojure.",[14],False),
("Função pura","Função cujo resultado depende apenas dos argumentos e que não produz efeitos colaterais.","`(defn dobro [x] (* 2 x))`.",[14],True),
("Goto","Comando de desvio incondicional para um rótulo. Base da programação não estruturada.","Criticado por Dijkstra (1968) por destruir a correspondência entre texto e execução.",[9,"D"],False),
("Heap","Região de memória para dados alocados dinamicamente, sem nome, acessados por ponteiros.","Objetos Java e dados criados com `new`/`malloc`.",[8],False),
("Herança","Mecanismo pelo qual uma classe (subclasse) reaproveita atributos e métodos de outra (superclasse) e pode estendê-los.","`class ContaEspecial extends Conta`.",[13],False),
("Herança múltipla","Herança de mais de uma superclasse. Aumenta o reuso, mas traz complexidade e ambiguidades.","Permitida em C++ (`class Multifuncional : public Impressora, public Scanner`); não em Java.",[13],False),
("Identificador","Nome usado para designar variáveis, funções, tipos etc., formado segundo as regras léxicas da linguagem.","Em C, começa com letra ou `_`; diferencia maiúsculas de minúsculas.",[4],False),
("Imutabilidade","Propriedade de um valor que não pode ser alterado depois de criado.","No funcional puro, \"alterar\" um valor significa criar outro.",[14],True),
("Índices textual e dinâmico","Coordenadas que, segundo Dijkstra, descrevem o progresso de um processo: posição no texto e contagem de repetições/chamadas.","O `goto` livre impede definir essas coordenadas.",["D"],False),
("Interface (Java)","Tipo que define um contrato (assinaturas de métodos e constantes) que as classes implementam com `implements`.","`class Multifuncional implements Impressora, Scanner`.",[13],False),
("Interpretação pura","Execução do programa por um interpretador, que traduz e executa cada instrução durante a execução.","Python, JavaScript, PHP (classificação da disciplina). Portável, mais lenta.",[3],False),
("Implementação híbrida","Compilação do fonte para um código intermediário, que é então interpretado (ou compilado com JIT) por uma máquina virtual.","Java (JVM), C# (CLR).",[3],False),
("JIT (Just-In-Time)","Compilação, durante a execução, de trechos do código intermediário para código de máquina.","Usada pela JVM e pela CLR para melhorar o desempenho.",[3],True),
("Lexema","Sequência concreta de caracteres do fonte que corresponde a um token.","`soma1`, `10`, `+`.",[4],False),
("Linguagem multiparadigma","Linguagem que suporta construções de mais de um paradigma.","C++ (imperativo e OO), Python, Scala.",[2],True),
("Máquina virtual","Software que executa um código intermediário, simulando uma máquina; é implementado para cada plataforma.","JVM, CLR.",[3],False),
("Matriz (array)","Tipo composto homogêneo, cujos elementos são acessados por índices.","`float notas[2][4][3];`. Em C, armazenada por linhas (*row-major*).",[7],False),
("Método","Operação definida em uma classe, que atua sobre o estado do objeto.","`pilha.push(5)`.",[12],False),
("Modificadores de acesso","Palavras que controlam a visibilidade de membros de uma classe: `public`, `private`, `protected`.","Atributos `private`; interface `public`.",[12],False),
("Mundo fechado (hipótese)","Suposição de que tudo o que não pode ser provado a partir da base é falso.","Se não há fato `homem(pedro)`, a consulta `homem(pedro).` responde `false`.",[15],True),
("Objeto","Instância de uma classe, com estado próprio, criada em tempo de execução.","`Pilha p = new Pilha();`.",[12],False),
("Overflow (estouro)","Resultado de uma operação que excede a faixa de valores representável pelo tipo.","Em Java, `Integer.MAX_VALUE + 1` dá a volta para `-2147483648`. Em C, `INT_MAX + 1` com `int` é comportamento indefinido; na prática, costuma dar a volta para um valor negativo.",[6],False),
("Palavra reservada","Palavra da linguagem que **não pode** ser usada como identificador.","`int`, `while`, `return` em C e em Java; `class` é reservada em Java e C++, mas não em C.",[4],False),
("Paradigma de programação","Modelo ou estilo de pensamento sobre como estruturar e resolver problemas com computador.","Imperativo, orientado a objetos, funcional, lógico.",[2],False),
("Paradigma funcional","Paradigma baseado em funções matemáticas, em que o programa é uma composição de funções, sem estado mutável no modelo puro.","Haskell (pura); LISP, Clojure (impuras).",[14],False),
("Paradigma imperativo","Paradigma em que o programa é uma sequência de comandos que alteram o estado da memória.","C, Pascal, Fortran.",[2,9],False),
("Paradigma lógico","Paradigma declarativo baseado em lógica de predicados: o programa é um conjunto de fatos e regras, e a execução responde a consultas.","Prolog.",[15],False),
("Paradigma orientado a objetos","Paradigma em que o programa é um conjunto de objetos que encapsulam estado e comportamento e trocam mensagens.","Java, C++, C#, Smalltalk.",[12,13],False),
("Parâmetro formal / real","Formal: o declarado no cabeçalho do subprograma. Real (argumento): o valor ou variável passado na chamada.","Em `void f(int x)` e `f(5)`, `x` é formal e `5` é real.",[11],False),
("Passagem por referência","O subprograma recebe o **endereço** do argumento; alterações no formal afetam o real imediatamente.","C++ `&`, C# `ref`, C com ponteiros.",[8,11],False),
("Passagem por resultado","O formal é uma variável local não inicializada, cujo valor é copiado para o real no retorno (semântica de saída).","Semântica do `out` do C#.",[11],False),
("Passagem por valor","O formal recebe uma **cópia** do valor do real (semântica de entrada); alterações não afetam o real.","Padrão em C e em Java. Em Java, toda passagem é por valor; para objetos, o valor copiado é a referência.",[8,11],False),
("Passagem por valor-resultado","O formal recebe uma cópia do real na entrada e seu valor final é copiado de volta no retorno.","Entrada e saída por cópia.",[11],False),
("Pilha (região de memória)","Região onde ficam variáveis locais, parâmetros e endereços de retorno; cresce e diminui com as chamadas.","As locais de `main` e de cada função chamada.",[8],False),
("Polimorfismo dinâmico","Escolha, em tempo de execução, da versão de um método sobrescrito, de acordo com o tipo real do objeto (vinculação tardia).","`Conta c = new ContaEspecial(); c.tipo();` chama a versão de `ContaEspecial`.",[13],False),
("Polimorfismo estático","Escolha, em tempo de compilação, entre versões de um método ou operador com o mesmo nome e parâmetros diferentes (sobrecarga).","`soma(int, int)` e `soma(double, double)`.",[6,13],False),
("Ponteiro","Variável que armazena um **endereço de memória**.","`int *p = &x; *p = 10;` altera `x`.",[8],False),
("Procedural (abordagem)","Abordagem em que o programador especifica os **passos** que levam à solução.","Na classificação do professor: imperativo, OO e funcional.",[2,15],False),
("Programação estruturada","Programação que usa apenas sequência, seleção e repetição em blocos, além de subprogramas, dispensando o `goto`.","Fundamentada por Böhm e Jacopini (1966) e Dijkstra (1968).",[9,"D"],False),
("Prolog","Principal linguagem do paradigma lógico, baseada em cláusulas de Horn e unificação.","`avo(X, Z) :- pai(X, Y), pai(Y, Z).`",[15],False),
("Ratio","Tipo numérico de Clojure (na JVM) que representa frações exatas.","`(/ 7 2)` → `7/2`; `(quot 7 2)` → 3.",[14],True),
("Recursão","Definição de uma função em termos dela mesma; substitui os laços no funcional e no lógico.","`(defn fat [n] (if (<= n 1) 1 (* n (fat (- n 1)))))`.",[14],True),
("Registro (struct)","Tipo composto heterogêneo, com campos nomeados de tipos possivelmente diferentes.","`struct Aluno { char nome[50]; float nota; };`.",[7],False),
("Regra (Prolog)","Cláusula que define uma relação a partir de outras: a cabeça é verdadeira se o corpo for.","`avo(X, Z) :- pai(X, Y), pai(Y, Z).`",[15],False),
("Semântica","Significado dos construtos de uma linguagem.","`x = x + 1` significa: ler `x`, somar 1, gravar em `x`.",[4,5],False),
("Semântica estática / dinâmica","Estática: regras verificáveis na compilação (tipos, declarações). Dinâmica: comportamento durante a execução.","Declarar `int` e atribuir string é erro de semântica estática em Java.",[5],False),
("Sintaxe","Forma (estrutura) dos programas de uma linguagem.","Três níveis: léxica, concreta e abstrata.",[4],False),
("Sintaxe abstrata","Representação da estrutura essencial do programa, sem detalhes como pontuação.","Árvore sintática abstrata de `x + 10 * z`.",[4],False),
("Sintaxe concreta","Regras que definem como os tokens se combinam em comandos válidos.","Descrita por BNF.",[4],False),
("Sobrecarga","Definição de vários métodos ou operadores com o mesmo nome e parâmetros diferentes.","`+` em Java soma números e concatena strings.",[6,13],False),
("Sobrescrita","Redefinição, na subclasse, de um método herdado com a mesma assinatura.","`@Override String tipo()` em `ContaEspecial`.",[13],False),
("Subprograma","Unidade de código com nome, parâmetros e corpo, chamada a partir de outros pontos: procedimento (sem retorno) ou função (com retorno).","Mecanismo da abstração procedural.",[11],False),
("TDA (tipo abstrato de dados)","Tipo definido pelo programador cuja representação é oculta e que só é manipulado por suas operações.","Pilha com `push`, `pop`, `vazia`, independente de vetor ou lista.",[10,12],False),
("Tempo de vida","Período da execução em que uma variável está vinculada a uma célula de memória.","Uma local `static` em C tem escopo local e tempo de vida do programa inteiro.",[5,8],False),
("Tipagem estática / dinâmica","Estática: o tipo é vinculado na compilação e não muda. Dinâmica: o tipo é vinculado na execução, conforme o valor.","Estática: C, Java. Dinâmica: Python, PHP.",[6],False),
("Tipagem forte / fraca","Força da tipagem: quanto a linguagem recusa operações entre tipos diferentes. A coerção a enfraquece.","Forte: Java, Python. Fraca: C, PHP.",[6],False),
("Tipo","Conjunto de valores e de operações aplicáveis a eles.","`int`: inteiros e operações aritméticas.",[6],False),
("Tipo composto","Tipo construído a partir de outros tipos.","Enumerações, registros, matrizes, strings, classes.",[7],False),
("Token","Categoria de lexemas que seguem um mesmo padrão.","Identificador, palavra reservada, constante, string, símbolo especial, operador (os seis grupos de C).",[4],False),
("Turing-completude","Capacidade de uma linguagem de expressar todos os algoritmos computáveis.","Imperativo: basta ter variáveis, inteiros, aritmética, atribuição, sequência, condição e desvio.",[9],False),
("Unificação","Processo de tornar dois termos idênticos, encontrando valores para as variáveis.","`pai(X, ana)` unifica com `pai(joao, ana)` com `X = joao`.",[15],False),
("Variável","Abstração de uma célula de memória, caracterizada por seis atributos: nome, endereço, valor, tipo, tempo de vida e escopo.","`int x = 10;`.",[4,5,9],False),
("Vinculação (binding)","Associação entre uma entidade e um atributo (nome–endereço, variável–tipo, chamada–método), em um momento determinado.","Em tempo de compilação (estática) ou de execução (dinâmica).",[5,13],False),
]
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
E.sort(key=lambda e: strip(e[0]).lower())
def slug(h):
    s = h.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s, flags=re.UNICODE)
    return s.replace(' ', '-')

def gerar():
    letters = []
    out = ["# Glossário", "",
    "> Termos da disciplina em ordem alfabética, com definição, exemplo e as aulas onde aparecem (links para os resumos). Termos marcados com **[Complemento]** não são definidos nos slides, mas aparecem nos enunciados das listas ou ajudam a entendê-los. Legenda: [Convenções](../README.md#convenções-de-marcação).",
    "", "__INDEX__", ""]
    cur = None
    for t, d, ex, aulas, comp in E:
        L = strip(t)[0].upper()
        if L != cur:
            cur = L; letters.append(L); out += ["", f"## {L}", ""]
        tag = " **[Complemento]**" if comp else ""
        out.append(f"### {t}")
        out.append("")
        out.append(f"{d}{tag}")
        out.append("")
        out.append(f"- **Exemplo:** {ex}")
        out.append(f"- **Aulas:** " + " · ".join(link(a) for a in aulas))
        out.append("")
    idx = "**Índice:** " + " · ".join(f"[{L}](#{L.lower()})" for L in letters) + f"\n\n**Total:** {len(E)} termos."
    md = "\n".join(out).replace("__INDEX__", idx)
    md = re.sub(r'\n{3,}', '\n\n', md)
    open(os.path.join(RAIZ, "07 - Glossário", "glossario.md"),"w").write(md.rstrip()+"\n")
    print(len(E), letters)


if __name__ == "__main__":
    gerar()
