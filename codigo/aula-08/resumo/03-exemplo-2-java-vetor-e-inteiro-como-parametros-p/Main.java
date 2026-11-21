// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/02 - Resumo Teórico/resumo-aula-08.md (linha 106).
// Seção: Exemplo 2 — Java, vetor e inteiro como parâmetros (p.10)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resumo/03-exemplo-2-java-vetor-e-inteiro-como-parametros-p/Main.java
// A saída deve conter: Impressao 1 ⏎ Vetor[0] = 1 ⏎ Vetor[1] = 3 ⏎ Vetor[2] = 5 ⏎ Vetor[3] = 7 ⏎ Impressao 2 ⏎ Vetor[0] = 2 ⏎ Vetor[1] = 4 ⏎ Vetor[2] = 6 ⏎ Vetor[3] = 8

import java.util.*;

public class Main {
    public static void imprime(int vet[], int tam) {
        for (int i = 0; i < tam; i++) {
            System.out.println("Vetor[" + i + "] = " + vet[i]);
            vet[i]++;              // altera o vetor ORIGINAL
        }
        tam++;                     // altera só a cópia local
    }

    public static void main(String[] args) {
        int vetor[] = {1, 3, 5, 7, 9};
        int tamanho = 4;
        System.out.println("Impressao 1");
        imprime(vetor, tamanho);
        System.out.println("Impressao 2");
        imprime(vetor, tamanho);
    }
}
