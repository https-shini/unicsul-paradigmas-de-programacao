// Gerado automaticamente a partir de 01 - Aulas/Aula 10 - Paradigma Imperativo II/04 - Resoluções/resolucoes-aula-10.md (linha 47).
// Seção: E7 — Exercício da p.19 (original)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-10/resolucoes/01-e7-exercicio-da-p-19-original.c
// Entrada de exemplo: 10 20 30 40 50 60 70 80 90 100
// A saída deve conter: Notas digitadas: 10 20 30 40 50 60 70 80 90 100 | Notas invertidas: 100 90 80 70 60 50 40 30 20 10

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
