# Aula 08 — Ponteiros · Resoluções comentadas

> **[Resolução elaborada]** Não é gabarito oficial. Enunciados: [`exercicios-aula-08.md`](../03%20-%20Exercícios/exercicios-aula-08.md). Os programas C e Java foram compilados e executados; o C# foi analisado sem execução (não há compilador C# no ambiente de validação).

## E1

Ponteiro é um valor que representa um endereço de memória (p.3). **Explícitos:** C, C++, Pascal, Ada (e Perl). **Implícitos:** Java e C# — referências a objetos gerenciadas pela máquina virtual.

## E2

| | Estática | Dinâmica |
| --- | --- | --- |
| Quando ocorre | Globais e `static`: antes da execução. Locais: a cada chamada, com tamanho fixado em compilação | Em execução, quando o programa pede (`new`/`malloc`) |
| Tamanho | Fixo, não pode ser alterado | Pode ser alterado |
| Onde (usual) | Segmento estático (globais); pilha (locais, de tamanho conhecido) | Heap, acessado por ponteiro |

## E3

**Resposta: d.** Objetos criados com `new` ficam no heap; a variável que guarda a referência pode estar na pilha.

## E4

<!-- teste: saida-contem="11 6" -->
```c
#include <stdio.h>
int main(void) {
    int a = 1, b = 2;
    int *p = &a;        /* p -> a */
    *p = *p + 10;       /* a = 1 + 10 = 11 */
    p = &b;             /* p agora -> b */
    *p = *p * 3;        /* b = 2 * 3 = 6 */
    printf("%d %d\n", a, b);
    return 0;
}
```

**Saída:** `11 6`. O mesmo ponteiro altera duas variáveis diferentes, conforme o endereço que guarda no momento.

## E5

Com os dois métodos por referência:

| Comando | Imprime |
| --- | --- |
| `Console.WriteLine(numero)` | 0 |
| `Metodo1(ref numero)` | 1 (e `numero` passa a 1) |
| `Console.WriteLine(numero)` | **1** |
| `Metodo2(ref numero)` | **2** |
| `Console.WriteLine(numero)` | **2** |

**Saída:** `0, 1, 1, 2, 2`.

## E6

- `vet` recebe uma cópia da **referência** ao mesmo array de `main`, então `vet[i]++` altera o array original e as mudanças aparecem na segunda impressão.
- `tam` recebe uma cópia do **valor** 4, então `tam++` só altera a cópia, e `tamanho` em `main` continua 4.
- **Se `imprime` fizesse `vet = new int[]{0,0,0,0,0};`:** a variável local `vet` passaria a apontar para um **novo** array, e o de `main` ficaria intocado. As duas impressões mostrariam `0 0 0 0`, e o vetor de `main` continuaria `{1,3,5,7,9}`.

Isso mostra que Java passa a **referência por valor**: dá para alterar o objeto apontado, mas não a variável do chamador.

## E7

**Erro:** `new int(4)` aloca **um** `int` com valor 4. O laço `for (i = 0; i < n; i++) cin >> vetor[i];` grava além dessa única posição quando `n > 1` — acesso fora da área alocada, com comportamento indefinido. Além disso, um vetor deve ser liberado com `delete[]`.

**Correção:** `int* vetor = new int[n];` … `delete[] vetor;` (versão completa e testada no [resumo](../02%20-%20Resumo%20Teórico/resumo-aula-08.md#exemplo-4--c-onde-cada-variável-mora-p14)).

| Variável | Região |
| --- | --- |
| `n`, `res` (globais) | Segmento estático |
| `a`, `b` (locais de `main`) | Pilha — frame de `main` |
| `x`, `y` (parâmetros de `funcaoA`) | Pilha — frame de `funcaoA` |
| `vetor` (o ponteiro) | Pilha — frame de `main` |
| `*vetor` (os inteiros alocados) | Heap |

## E8

<!-- teste: saida-contem="antes: x=1 y=2|depois: x=2 y=1|sem ponteiro: x=2 y=1" -->
```c
#include <stdio.h>

void troca(int *a, int *b) {     /* recebe ENDEREÇOS */
    int temp = *a;               /* guarda o valor apontado por a */
    *a = *b;                     /* escreve no x do chamador */
    *b = temp;                   /* escreve no y do chamador */
}

void troca_errada(int a, int b) {   /* recebe CÓPIAS */
    int temp = a; a = b; b = temp;  /* troca só as cópias locais */
}

int main(void) {
    int x = 1, y = 2;
    printf("antes: x=%d y=%d\n", x, y);
    troca(&x, &y);
    printf("depois: x=%d y=%d\n", x, y);
    troca_errada(x, y);
    printf("sem ponteiro: x=%d y=%d\n", x, y);   /* não mudou */
    return 0;
}
```

`troca_errada` recebe **cópias** (passagem por valor) e troca só as variáveis locais, que somem no retorno. Com ponteiros, a função recebe os **endereços** de `x` e `y` e escreve diretamente nelas. É assim que C, que só tem passagem por valor, simula a passagem por referência. É também a função `trocarElementos` da [Aula 10](../../Aula%2010%20-%20Paradigma%20Imperativo%20II/02%20-%20Resumo%20Teórico/resumo-aula-10.md).

## E9

**Não é possível** terminar com nomes diferentes usando um único objeto. Com um único `new`, existe um único objeto: se `p1` e `p2` o referenciam, `p1.nome` e `p2.nome` são **o mesmo campo** e só podem valer a mesma coisa. Para ter "Ana" e "Bia" ao mesmo tempo, são necessários **dois objetos**, ou seja, dois `new` (ou uma cópia explícita). Se `p2` ficar `null`, `p2.nome` lança `NullPointerException`.

## E10

<!-- teste: entrada="4 10 20 30 40 50 60" saida-contem="v[0] = 10|v[3] = 40|v[5] = 60|novo tamanho: 6" -->
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int *v = malloc(n * sizeof(int));           /* heap, tamanho decidido em execução */
    if (v == NULL) return 1;
    for (int i = 0; i < n; i++) scanf("%d", &v[i]);

    int novo = n + n / 2;                       /* +50% */
    int *tmp = realloc(v, novo * sizeof(int));  /* aumenta o bloco (pode mudar de endereço) */
    if (tmp == NULL) { free(v); return 1; }
    v = tmp;
    for (int i = n; i < novo; i++) scanf("%d", &v[i]);

    printf("novo tamanho: %d\n", novo);
    for (int i = 0; i < novo; i++) printf("v[%d] = %d\n", i, v[i]);
    free(v);                                    /* devolve a memória */
    return 0;
}
```

**Relação com o slide:** o tamanho foi decidido e **alterado** em tempo de execução, o que só é possível com alocação dinâmica, via ponteiro. Um `int v[4]` declarado no código teria tamanho fixo. **Detalhe:** `realloc` pode **mover** o bloco para outro endereço, por isso o resultado é atribuído a um ponteiro temporário antes de substituir `v`.

## E11

Passar uma estrutura grande **por valor** copia todos os seus bytes a cada chamada — gasta tempo e espaço na pilha. Passar um **ponteiro** copia só o endereço (8 bytes num sistema de 64 bits), qualquer que seja o tamanho da estrutura.

Exemplo: `struct Imagem { unsigned char pixels[1920*1080*3]; }` tem cerca de 6 MB. `processa(struct Imagem img)` copiaria 6 MB por chamada e provavelmente estouraria a pilha; `processa(struct Imagem *img)` copia 8 bytes. A Aula 11 retoma esse custo: a passagem por valor é "rápida para parâmetros pequenos, mas pode ser lenta em dados como matrizes".
