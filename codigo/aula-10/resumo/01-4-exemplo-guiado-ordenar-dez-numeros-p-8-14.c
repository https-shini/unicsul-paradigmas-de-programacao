// Gerado automaticamente a partir de 01 - Aulas/Aula 10 - Paradigma Imperativo II/02 - Resumo Teórico/resumo-aula-10.md (linha 73).
// Seção: 4. Exemplo guiado: ordenar dez números (p.8–14)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-10/resumo/01-4-exemplo-guiado-ordenar-dez-numeros-p-8-14.c
// Entrada de exemplo: 9 3 7 1 8 2 10 5 4 6
// A saída deve conter: 9 3 7 1 8 2 10 5 4 6 | 1 2 3 4 5 6 7 8 9 10

#include <stdio.h>
#define TAM 10

/* ---- Abstração 3 ---- */
int encontrarMenor(int *vetor, int inicio) {          /* devolve a POSIÇÃO do menor a partir de inicio */
    int posMenor = inicio;
    for (int j = inicio + 1; j < TAM; j++) {
        if (vetor[j] < vetor[posMenor]) {
            posMenor = j;
        }
    }
    return posMenor;
}

void trocarElementos(int *a, int *b) {                 /* código do slide (p.14) */
    int temp = *a;     /* 1. salva um dos valores numa temporária   */
    *a = *b;           /* 2. substitui pelo outro valor              */
    *b = temp;         /* 3. copia o valor salvo                     */
}

/* ---- Abstração 2 ---- */
void ordenarVetor(int *vetor) {                        /* selection sort */
    int posMenor;
    for (int i = 0; i < TAM; i++) {
        posMenor = encontrarMenor(vetor, i);
        trocarElementos(&vetor[i], &vetor[posMenor]);
    }
}

/* ---- Leitura e impressão: simples, codificadas diretamente ---- */
void lerVetor(int *vetor) {
    for (int i = 0; i < TAM; i++) scanf("%d", &vetor[i]);
}

void mostrarVetor(int *vetor) {
    /* simplificado: o slide (p.11) imprime "Elemento da posição %d: %d\n" */
    for (int i = 0; i < TAM; i++) printf("%d ", vetor[i]);
    printf("\n");
}

/* ---- Abstração 1 ---- */
int main() {
    int vetor[TAM];
    lerVetor(vetor);
    mostrarVetor(vetor);
    ordenarVetor(vetor);
    mostrarVetor(vetor);
    return 0;
}
