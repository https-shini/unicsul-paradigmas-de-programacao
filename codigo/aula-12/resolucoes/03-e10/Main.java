// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/04 - Resoluções/resolucoes-aula-12.md (linha 126).
// Seção: E10
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resolucoes/03-e10/Main.java
// Entrada de exemplo: -1 ⏎ 2 ⏎ 3
// A saída deve conter: 3 ⏎ 2 ⏎ -1 ⏎ Pilha vazia: Pilha vazia

import java.util.Scanner;

class Pilha {
    private int[] vetPilha = new int[5];
    private int topo = 0;

    public void push(int n) {
        if (topo == vetPilha.length) throw new IllegalStateException("Pilha cheia");
        vetPilha[topo++] = n;
    }

    public int pop() {
        if (topo == 0) throw new IllegalStateException("Pilha vazia");
        return vetPilha[--topo];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Pilha pilha = new Pilha();
        for (int i = 0; i < 3; i++) pilha.push(Integer.parseInt(input.nextLine()));
        try {
            for (int i = 0; i < 4; i++) {          // uma vez a mais, de propósito
                System.out.println(pilha.pop());   // -1 agora é um valor como outro qualquer
            }
        } catch (IllegalStateException e) {
            System.out.println("Pilha vazia: " + e.getMessage());
        }
    }
}
