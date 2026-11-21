// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/02 - Resumo Teórico/resumo-aula-12.md (linha 213).
// Seção: Versão 1d — lista encadeada (p.14–16)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resumo/04-versao-1d-lista-encadeada-p-14-16/Main.java
// Entrada de exemplo: 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5
// A saída deve conter: 5 ⏎ 4 ⏎ 3 ⏎ 2 ⏎ 1

import java.util.*;

class Nodo {
    private int valor;
    private Nodo proximo;

    public Nodo(int x, Nodo prox) {
        this.valor = x;
        this.proximo = prox;
    }
    public int getValor()     { return this.valor; }
    public Nodo getProximo()  { return this.proximo; }
}

class Pilha {
    private Nodo topo;                 // a representação mudou...

    public Pilha() {                   // no slide: "public void Pilha()" (ver [Atenção] da 1c)
        this.topo = null;
    }

    public void push(int n) {          // ...mas a interface é a mesma
        Nodo x = new Nodo(n, this.topo);
        topo = x;
    }

    public int pop() {
        if (topo != null) {
            int x = topo.getValor();
            topo = topo.getProximo();
            return x;
        } else {
            System.out.println("Erro - pilha vazia");
            return -1;
        }
    }
}

public class Main {                     // main IDÊNTICO ao da versão com vetor (p.16)
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
