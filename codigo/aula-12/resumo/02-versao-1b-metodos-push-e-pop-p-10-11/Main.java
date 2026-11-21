// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/02 - Resumo Teórico/resumo-aula-12.md (linha 93).
// Seção: Versão 1b — métodos `push` e `pop` (p.10–11)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resumo/02-versao-1b-metodos-push-e-pop-p-10-11/Main.java
// Entrada de exemplo: 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5
// A saída deve conter: 5 ⏎ 4 ⏎ 3 ⏎ 2 ⏎ 1

import java.util.*;

public class Main {
    static int[] pilha = new int[5];
    static int topo = 0;

    static void push(int n) {
        if (topo == 5) {
            System.out.println("Erro - pilha cheia");
        } else {
            pilha[topo] = n;
            topo++;
        }
    }

    static int pop() {
        if (topo == 0) {
            System.out.println("Erro - pilha vazia");
            return -1;
        } else {
            topo--;
            int n = pilha[topo];
            return n;
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            push(elemento);
        }
        for (int i = 0; i < 5; i++) {
            elemento = pop();
            if (elemento != -1) {
                System.out.println(elemento);
            }
        }
    }
}
