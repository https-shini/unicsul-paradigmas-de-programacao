// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/04 - Resoluções/resolucoes-aula-12.md (linha 57).
// Seção: E8
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resolucoes/02-e8/Main.java
// Entrada de exemplo: 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5
// A saída deve conter: 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5

import java.util.Scanner;

class Fila {
    private int[] dados = new int[5];
    private int inicio = 0;      // posição do primeiro elemento
    private int fim = 0;         // próxima posição livre
    private int quantidade = 0;

    public void enfileirar(int n) {
        if (quantidade == dados.length) {
            System.out.println("Erro - fila cheia");
            return;
        }
        dados[fim] = n;
        fim = (fim + 1) % dados.length;          // circular: volta ao 0 depois do último
        quantidade++;
    }

    public int desenfileirar() {
        if (quantidade == 0) {
            System.out.println("Erro - fila vazia");
            return -1;
        }
        int n = dados[inicio];
        inicio = (inicio + 1) % dados.length;
        quantidade--;
        return n;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Fila fila = new Fila();
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            fila.enfileirar(Integer.parseInt(input.nextLine()));
        }
        for (int i = 0; i < 5; i++) {
            int elemento = fila.desenfileirar();
            if (elemento != -1) System.out.println(elemento);
        }
    }
}
