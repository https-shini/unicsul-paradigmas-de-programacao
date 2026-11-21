// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 199).
// Seção: 15
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/06-15/Main.java
// A saída deve conter: Ana ⏎ Carla

import java.util.ArrayList;
import java.util.List;

class Aluno {
    private final String nome;
    private final double media;
    Aluno(String nome, double media) { this.nome = nome; this.media = media; }
    public String getNome() { return nome; }
    public boolean aprovado() { return media >= 6; }   // a regra pertence ao objeto
}

public class Main {
    public static void main(String[] args) {
        List<Aluno> turma = List.of(new Aluno("Ana", 8.0), new Aluno("Bruno", 5.5), new Aluno("Carla", 6.0));
        List<String> aprovados = new ArrayList<>();
        for (Aluno a : turma) {                        // passo a passo: imperativo
            if (a.aprovado()) aprovados.add(a.getNome());
        }
        aprovados.forEach(System.out::println);
    }
}
