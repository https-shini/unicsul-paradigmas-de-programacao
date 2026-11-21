<!-- nav:topo -->
[Início](../../../README.md) › [01 - Aulas](../../README.md) › [Aula 10](../README.md) › [04 - Resoluções](README.md) · [Mapa](../../../MAPA.md)
<!-- /nav:topo -->

# Aula 10 — Paradigma Imperativo II · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-10.md`](../03%20-%20Exercícios/exercicios-aula-10.md). Os programas foram compilados e executados com gcc.

## E1

- **Abstração:** habilidade de concentrar-se nos aspectos essenciais de um contexto, ignorando os menos importantes, para simplificar a construção da solução ([p.4](../01%20-%20Slides%20Originais/README.md#página-4)).
- **Abstração procedural:** processo que permite ao programador se preocupar com a **interface** da função e com o **que** ela calcula, ignorando **como** o cálculo é feito ([p.6](../01%20-%20Slides%20Originais/README.md#página-6)).

## E2

1. Descrever sucintamente a função, com entrada e saída.
2. Dividi-la em funções mais primitivas, cada uma com entrada e saída.
3. Repetir até que tudo seja executável com os comandos e tipos primitivos da linguagem ([p.7](../01%20-%20Slides%20Originais/README.md#página-7)).

## E3

**Resposta: b.** Abstração de processos → imperativo; abstração de dados → orientado a objetos ([p.5](../01%20-%20Slides%20Originais/README.md#página-5)).

## E4

- **Acoplamento:** grau de dependência entre módulos. Desejável: **baixo**.
- **Coesão:** grau em que uma função ou classe tem uma única responsabilidade. Desejável: **alta**.
- **Globais:** qualquer função pode lê-las e alterá-las, então todas as funções que as usam ficam dependentes delas e umas das outras. Uma mudança na global afeta muitos pontos, e um valor errado pode ter sido gravado em qualquer lugar — difícil de depurar.

> **[Atenção]** O slide escreve "não favorece a baixa coesão"; o conceito correto é que a abstração procedural não favorece a **alta** coesão.

## E5

1. Permite declarar variáveis do tipo.
2. Oculta a representação interna.
3. Tem um conjunto de operações para manipular as variáveis.
4. Declara tipo e operações na mesma unidade sintática (a implementação pode estar em outra).
5. A representação só é acessível pelas operações.

## E6

Porque a troca precisa saber **onde** está o menor elemento para movê-lo para a posição `i`. Só com o valor, `ordenarVetor` não saberia qual posição trocar: precisaria procurar o valor de novo, e valores repetidos causariam ambiguidade. Por isso o código guarda `posMenor` e chama `trocarElementos(&vetor[i], &vetor[posMenor])`.

## E7 — Exercício da p.19 (original)

<!-- teste: entrada="10 20 30 40 50 60 70 80 90 100" saida-contem="Notas digitadas: 10 20 30 40 50 60 70 80 90 100|Notas invertidas: 100 90 80 70 60 50 40 30 20 10" -->
```c
#include <stdio.h>
#define TAM 10

/* Auxiliar: troca dois elementos via ponteiros */
void trocarElementos(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* Lê TAM notas entre 0 e 100 (repete a leitura se estiver fora da faixa) */
void lerVetor(int v[]) {
    for (int i = 0; i < TAM; i++) {
        do {
            scanf("%d", &v[i]);
        } while (v[i] < 0 || v[i] > 100);
    }
}

void mostrarVetor(const int v[], const char *titulo) {
    printf("%s:", titulo);
    for (int i = 0; i < TAM; i++) printf(" %d", v[i]);
    printf("\n");
}

/* Inverte no próprio vetor: troca o i-ésimo com o seu "espelho" */
void inverterVetor(int v[]) {
    for (int i = 0; i < TAM / 2; i++) {
        trocarElementos(&v[i], &v[TAM - 1 - i]);
    }
}

int main(void) {                 /* apenas orquestra */
    int notas[TAM];
    lerVetor(notas);
    mostrarVetor(notas, "Notas digitadas");
    inverterVetor(notas);
    mostrarVetor(notas, "Notas invertidas");
    return 0;
}
```

**Raciocínio:**

- Inverter = trocar o elemento `i` com o elemento `TAM−1−i` (seu espelho).
- O laço vai só até `TAM/2`: na metade, todos os pares já foram trocados. Se fosse até `TAM`, cada par seria trocado **duas vezes**, e o vetor voltaria ao original — erro clássico.
- Não há vetor auxiliar: só uma variável temporária dentro de `trocarElementos`.
- O `main` lê como a descrição do problema: ler, mostrar, inverter, mostrar.

## E8 — Atividade 1 da p.20 (original)

<!-- teste: entrada="5 2" saida-contem="Arranjos A(5,2) = 20|Combinacoes C(5,2) = 10" -->
```c
#include <stdio.h>

/* Nível 3: fatorial (long long suporta até 20!) */
long long fatorial(int k) {
    long long f = 1;
    for (int i = 2; i <= k; i++) f *= i;
    return f;
}

/* Nível 2: as duas fórmulas */
long long arranjo(int n, int p) {
    return fatorial(n) / fatorial(n - p);
}

long long combinacao(int n, int p) {
    return fatorial(n) / (fatorial(p) * fatorial(n - p));
}

/* Nível 2: entrada validada */
void lerDados(int *n, int *p) {
    do {
        scanf("%d %d", n, p);
    } while (*n < 0 || *p < 0 || *p > *n);
}

/* Nível 1 */
int main(void) {
    int n, p;
    lerDados(&n, &p);
    printf("Arranjos A(%d,%d) = %lld\n", n, p, arranjo(n, p));
    printf("Combinacoes C(%d,%d) = %lld\n", n, p, combinacao(n, p));
    return 0;
}
```

**Hierarquia:** `main` → `lerDados`, `arranjo`, `combinacao` → `fatorial`. A função `fatorial` é **reutilizada** pelas duas fórmulas — um dos benefícios citados na [p.15](../01%20-%20Slides%20Originais/README.md#página-15).

**Teste:** n = 5, p = 2 → A = 5!/3! = 120/6 = **20**; C = 5!/(2!·3!) = 120/12 = **10**.

**Por que `lerDados` recebe ponteiros:** precisa devolver dois valores ao `main`, e em C isso se faz com ponteiros (Aula 08). A Aula 11 chama isso de passagem para **saída**.

## E9

**Passo 1 — descrição:** entrada: notas e nomes dos alunos; saída: média da turma e lista dos alunos acima dela.

**Passo 2 — decomposição:**

```text
main
├── lerTurma(nomes[], notas[], n)           -> preenche os vetores
├── calcularMedia(notas[], n) -> media      -> soma / n
│     └── somar(notas[], n) -> soma
└── listarAcima(nomes[], notas[], n, media) -> imprime quem tem nota > media
```

**Passo 3 — parada:** `somar` e o laço de `listarAcima` já usam só comandos primitivos (laço, `+`, comparação, `printf`), então não é preciso decompor mais.

## E10

A abstração procedural organiza **ações**, mas os **dados** continuam soltos — vetores e variáveis, às vezes globais, que qualquer função pode alterar. Isso gera **alto acoplamento** e dificulta a **alta coesão**, porque nada impede uma função de mexer em dados que não são "dela".

A OO acrescenta o **TDA com encapsulamento**: os dados ficam **dentro** da classe, ocultos (`private`), e só as operações da própria classe os manipulam. Assim:

1. o acoplamento cai, porque os clientes dependem só da interface pública;
2. a coesão sobe, porque cada classe reúne os dados e as operações de **uma** responsabilidade;
3. a representação pode mudar sem afetar os clientes — é exatamente o que a [pilha da Aula 12](../../Aula%2012%20-%20Paradigma%20Orientado%20a%20Objetos%20I/02%20-%20Resumo%20Teórico/resumo-aula-12.md#3-o-exemplo-progressivo-da-pilha-p716) demonstra.

## E11

- 12! = 479.001.600 cabe num `int` de 32 bits (máximo 2.147.483.647), mas **13! = 6.227.020.800 estoura**. Com `long long` (64 bits), o limite é 20!.
- **Evitando fatoriais enormes:** calcular C(n, p) por produto incremental, que mantém sempre um inteiro exato:

<!-- teste: entrada="30 15" saida-contem="C(30,15) = 155117520" -->
```c
#include <stdio.h>

long long combinacao(int n, int p) {
    if (p > n - p) p = n - p;               /* C(n,p) = C(n,n-p): usa o menor */
    long long c = 1;
    for (int i = 1; i <= p; i++) {
        c = c * (n - p + i) / i;            /* a cada passo, c = C(n-p+i, i), sempre inteiro */
    }
    return c;
}

int main(void) {
    int n, p;
    scanf("%d %d", &n, &p);
    printf("C(%d,%d) = %lld\n", n, p, combinacao(n, p));   /* 30! não caberia em long long */
    return 0;
}
```

O valor intermediário nunca passa muito de C(n, p) × n, enquanto 30! ≈ 2,6 × 10³² não caberia nem em 64 bits. É o problema de estouro da [Aula 06](../../Aula%2006%20-%20Sistema%20de%20Tipos/02%20-%20Resumo%20Teórico/resumo-aula-06.md#4-tipos-básicos-e-seus-tamanhos-p68).


<!-- nav:rodape -->

---

**Aula 10:** [Visão geral](../README.md) · [Slides](../01%20-%20Slides%20Originais/README.md) · [Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [Exercícios](../03%20-%20Exercícios/exercicios-aula-10.md) · **Resoluções** · [Complementos](../05%20-%20Materiais%20Complementares/materiais-complementares.md)

← [Aula 09 · Resoluções](../../Aula%2009%20-%20Paradigma%20Imperativo%20I/04%20-%20Resoluções/resolucoes-aula-09.md) · [Aula 11 · Resoluções](../../Aula%2011%20-%20Paradigma%20Imperativo%20III/04%20-%20Resoluções/resolucoes-aula-11.md) →

**Links para esta página (5):** [Aula 10 · Resumo](../02%20-%20Resumo%20Teórico/resumo-aula-10.md) · [Aula 10 · Exercícios](../03%20-%20Exercícios/exercicios-aula-10.md) · [Aula 10 · visão geral](../README.md) · [03 — Trabalhos e Projetos](../../../03%20-%20Trabalhos%20e%20Projetos/README.md) · [Paradigmas de Linguagens de Programação — UNICSUL](../../../README.md)

<!-- /nav:rodape -->
