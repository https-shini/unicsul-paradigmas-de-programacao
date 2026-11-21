// Gerado automaticamente a partir de 01 - Aulas/Aula 07 - Tipos Compostos/04 - Resoluções/resolucoes-aula-07.md (linha 138).
// Seção: E9 — Desafio da p.16 (original)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-07/resolucoes/03-e9-desafio-da-p-16-original/NotasSemestres.java
// Entrada de exemplo: 7 8 9 4 5 6 5 5 5 8 10 7 7 7 7 6 8 8 7 8 9 1 10 10 10 10 10 9 9 9 8 8 8 7 7 7 6 6 6 5 5 5 4 4 4 3 3 3
// A saída deve conter: Semestre 0 - media do aluno 3 na disciplina 0: 8.33 | Semestre 1 - media do aluno 0 na disciplina 0: 10.00 | Semestre 1 - media do aluno 3 nas primeiras avaliacoes: 5.00

import java.util.Scanner;

public class NotasSemestres {
    static final int SEM = 2, DISC = 2, ALUNOS = 4, AVAL = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        float[][][][] notas = new float[SEM][DISC][ALUNOS][AVAL];   // 4 dimensões, 48 notas

        for (int s = 0; s < SEM; s++)
            for (int d = 0; d < DISC; d++)
                for (int a = 0; a < ALUNOS; a++)
                    for (int k = 0; k < AVAL; k++)
                        notas[s][d][a][k] = in.nextFloat();

        for (int s = 0; s < SEM; s++) {
            for (int d = 0; d < DISC; d++)
                for (int a = 0; a < ALUNOS; a++) {
                    float soma = 0;
                    for (int k = 0; k < AVAL; k++) soma += notas[s][d][a][k];
                    System.out.printf("Semestre %d - media do aluno %d na disciplina %d: %.2f%n", s, a, d, soma / AVAL);
                }
            for (int a = 0; a < ALUNOS; a++) {
                float soma = 0;
                for (int d = 0; d < DISC; d++) soma += notas[s][d][a][0];
                System.out.printf("Semestre %d - media do aluno %d nas primeiras avaliacoes: %.2f%n", s, a, soma / DISC);
            }
        }
    }
}
