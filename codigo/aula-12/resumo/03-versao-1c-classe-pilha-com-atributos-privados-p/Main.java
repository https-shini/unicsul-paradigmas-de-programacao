// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/02 - Resumo Teórico/resumo-aula-12.md (linha 152).
// Seção: Versão 1c — classe `Pilha` com atributos privados (p.12–13)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resumo/03-versao-1c-classe-pilha-com-atributos-privados-p/Main.java
// Entrada de exemplo: 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5
// A saída deve conter: 5 ⏎ 4 ⏎ 3 ⏎ 2 ⏎ 1

import java.util.*;

class Pilha {
    private int[] vetPilha = new int[5];   // representação OCULTA
    private int topo;

    public Pilha() {                       // construtor (no slide: "public void Pilha()", ver [Atenção])
        topo = 0;
    }

    public void push(int n) {
        if (this.topo == 5) {
            System.out.println("Erro - pilha cheia");
        } else {
            this.vetPilha[this.topo] = n;
            this.topo++;
        }
    }

    public int pop() {
        if (this.topo == 0) {
            System.out.println("Erro - pilha vazia");
            return -1;
        } else {
            this.topo--;
            int n = this.vetPilha[this.topo];
            return n;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        Pilha pilha = new Pilha();
        for (int i = 0; i < 5; i++) {
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            pilha.push(elemento);
        }
        for (int i = 0; i < 5; i++) {
            elemento = pilha.pop();
            if (elemento != -1) {
                System.out.println(elemento);
            }
        }
    }
}
