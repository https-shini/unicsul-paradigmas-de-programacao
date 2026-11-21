// Gerado automaticamente a partir de 01 - Aulas/Aula 02 - Evolução das Linguagens e Paradigmas/02 - Resumo Teórico/resumo-aula-02.md (linha 53).
// Seção: Java (p.6)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-02/resumo/01-java-p-6/Main.java

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n1, n2, dobro;
        n1 = Integer.valueOf(input.nextLine());
        dobro = 2 * n1;
        n2 = Integer.valueOf(input.nextLine());
        if (dobro == n2) {
            System.out.println("O dobro do primeiro valor é igual ao segundo valor.");
        } else {
            System.out.println("O dobro do primeiro valor não é igual ao segundo valor.");
        }
    }
}
