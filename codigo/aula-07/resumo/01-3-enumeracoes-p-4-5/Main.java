// Gerado automaticamente a partir de 01 - Aulas/Aula 07 - Tipos Compostos/02 - Resumo Teórico/resumo-aula-07.md (linha 32).
// Seção: 3. Enumerações (p.4–5)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-07/resumo/01-3-enumeracoes-p-4-5/Main.java
// Entrada de exemplo: Ciencia da Computacao ⏎ Direito
// A saída deve conter: Turno de oferta: MATUTINO | Turno de oferta: VESPERTINO

import java.util.Scanner;

class Main {
    public enum Turno { MATUTINO, VESPERTINO, NOTURNO }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String curso1, curso2;
        Turno turno1, turno2;
        System.out.print("Digite o nome do curso 1: ");
        curso1 = input.nextLine();
        System.out.print("Digite o nome do curso 2: ");
        curso2 = input.nextLine();

        turno1 = Turno.MATUTINO;
        System.out.println("Curso 1: " + curso1);
        System.out.println("Turno de oferta: " + turno1);

        turno2 = Turno.VESPERTINO;
        System.out.println("Curso 2: " + curso2);
        System.out.println("Turno de oferta: " + turno2);
    }
}
