// Gerado automaticamente a partir de 06 - Revisões e Sínteses/resolucao-questoes-integradoras.md (linha 131).
// Seção: QI5
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/resolucao-questoes-integradora/04-qi5/Main.java
// A saída deve conter: Ana: média 8.0 | Nota inválida

import java.util.ArrayList;
import java.util.List;

class Aluno {
    private final String nome;                 // dados reunidos e ocultos
    private final List<Double> notas = new ArrayList<>();
    private int faltas;

    Aluno(String nome) { this.nome = nome; }

    void registrarNota(double n) {             // a classe valida o próprio estado
        if (n < 0 || n > 10) throw new IllegalArgumentException("Nota inválida: " + n);
        notas.add(n);
    }
    void registrarFalta() { faltas++; }
    double media() { return notas.stream().mapToDouble(Double::doubleValue).average().orElse(0); }
    String getNome() { return nome; }
}

class Turma {
    private final List<Aluno> alunos = new ArrayList<>();
    void matricular(Aluno a) { alunos.add(a); }
    void relatorio() {
        for (Aluno a : alunos) System.out.printf("%s: média %.1f%n", a.getNome(), a.media());
    }
}

public class Main {
    public static void main(String[] args) {
        Aluno ana = new Aluno("Ana");
        ana.registrarNota(7); ana.registrarNota(9);
        Turma t = new Turma(); t.matricular(ana); t.relatorio();
        try { ana.registrarNota(11); } catch (IllegalArgumentException e) { System.out.println(e.getMessage()); }
    }
}
