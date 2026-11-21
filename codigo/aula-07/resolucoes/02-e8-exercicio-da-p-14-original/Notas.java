// Gerado automaticamente a partir de 01 - Aulas/Aula 07 - Tipos Compostos/04 - Resoluções/resolucoes-aula-07.md (linha 72).
// Seção: E8 — Exercício da p.14 (original)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-07/resolucoes/02-e8-exercicio-da-p-14-original/Notas.java
// Entrada de exemplo: 7 8 9 4 5 6 5 5 5 8 10 7 7 7 7 6 8 8 7 8 9 1 10 10
// A saída deve conter: Media do aluno 3 na disciplina 0: 8.33 | Media do aluno 1 na disciplina 1: 7.33 | Media do aluno 3 nas primeiras avaliacoes: 4.50

import java.util.Scanner;

public class Notas {
    static final int DISC = 2, ALUNOS = 4, AVAL = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        float[][][] notas = new float[DISC][ALUNOS][AVAL];   // uma única variável

        // Leitura: disciplina -> aluno -> avaliação
        for (int d = 0; d < DISC; d++) {
            System.out.println("*****Digite as notas da disciplina " + d + "*****");
            for (int a = 0; a < ALUNOS; a++) {
                for (int k = 0; k < AVAL; k++) {
                    System.out.print("Aluno " + a + ", avaliacao " + k + ": ");
                    notas[d][a][k] = in.nextFloat();
                }
            }
        }

        // (a) média final de cada aluno em cada disciplina
        for (int d = 0; d < DISC; d++) {
            for (int a = 0; a < ALUNOS; a++) {
                float soma = 0;
                for (int k = 0; k < AVAL; k++) soma += notas[d][a][k];
                System.out.printf("%nMedia do aluno %d na disciplina %d: %.2f", a, d, soma / AVAL);
            }
        }

        // (b) média na primeira avaliação (k = 0) de cada aluno em todas as disciplinas
        for (int a = 0; a < ALUNOS; a++) {
            float soma = 0;
            for (int d = 0; d < DISC; d++) soma += notas[d][a][0];
            System.out.printf("%nMedia do aluno %d nas primeiras avaliacoes: %.2f", a, soma / DISC);
        }
        System.out.println();
    }
}
