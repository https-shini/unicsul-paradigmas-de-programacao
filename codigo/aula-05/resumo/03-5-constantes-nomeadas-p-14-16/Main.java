// Gerado automaticamente a partir de 01 - Aulas/Aula 05 - Semântica/02 - Resumo Teórico/resumo-aula-05.md (linha 186).
// Seção: 5. Constantes nomeadas (p.14–16)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-05/resumo/03-5-constantes-nomeadas-p-14-16/Main.java
// Entrada de exemplo: 2
// A saída deve conter: Area: 12.5664 | Comprimento: 12.5664

import java.util.Scanner;

class Main {
    static final float pi = 3.1416f;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o raio de uma circunferência: ");
        float raio = Float.valueOf(input.nextLine());
        float area = pi * raio * raio;
        float comprimento = 2 * pi * raio;
        System.out.println("Area: " + area);
        System.out.println("Comprimento: " + comprimento);
    }
}
