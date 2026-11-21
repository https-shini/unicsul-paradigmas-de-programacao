// Gerado automaticamente a partir de 01 - Aulas/Aula 03 - Implementação das Linguagens/04 - Resoluções/resolucoes-aula-03.md (linha 97).
// Seção: Java (referência para a comparação, híbrida)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-03/resolucoes/03-java-referencia-para-a-comparacao-hibrida/Main.java
// Entrada de exemplo: 5 3 9 1 7 2 8 6 4 10
// A saída deve conter: Media: 5.50 | Maior: 10.00 | Menor: 1.00

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double soma = 0, maior = 0, menor = 0;
        for (int i = 0; i < 10; i++) {
            double x = in.nextDouble();
            if (i == 0) { maior = x; menor = x; }
            maior = Math.max(maior, x);
            menor = Math.min(menor, x);
            soma += x;
        }
        System.out.printf("Media: %.2f%nMaior: %.2f%nMenor: %.2f%n", soma / 10, maior, menor);
    }
}
