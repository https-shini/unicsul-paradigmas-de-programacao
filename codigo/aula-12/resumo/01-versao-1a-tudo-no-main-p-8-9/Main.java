// Gerado automaticamente a partir de 01 - Aulas/Aula 12 - Paradigma Orientado a Objetos I/02 - Resumo Teórico/resumo-aula-12.md (linha 60).
// Seção: Versão 1a — tudo no `main` (p.8–9)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-12/resumo/01-versao-1a-tudo-no-main-p-8-9/Main.java
// Entrada de exemplo: 1 ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 5
// A saída deve conter: 5 ⏎ 4 ⏎ 3 ⏎ 2 ⏎ 1

import java.util.*;

public class Main {
    static int[] pilha = new int[5];
    static int topo = 0;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int elemento;
        for (int i = 0; i < 5; i++) {                 // empilha
            System.out.println("Digite um número: ");
            elemento = Integer.parseInt(input.nextLine());
            if (topo == 5) {
                System.out.println("Erro - pilha cheia");
            } else {
                pilha[topo] = elemento;
                topo++;
            }
        }
        for (int i = 0; i < 5; i++) {                 // desempilha
            if (topo == 0) {
                System.out.println("Erro - pilha vazia");
            } else {
                topo--;
                elemento = pilha[topo];
                System.out.println(elemento);
            }
        }
    }
}
