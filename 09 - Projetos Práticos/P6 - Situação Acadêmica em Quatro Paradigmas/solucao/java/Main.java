/** Demonstração: javac *.java && java Main */
public class Main {
    public static void main(String[] args) {
        Desempenho[] turma = {
            new Desempenho(3.5, 4.0, null, 80),
            new Desempenho(2.0, 3.0, null, 90),
            new Desempenho(2.0, 3.0, 3.5, 90),
            new Desempenho(0.5, 5.0, null, 100),
            new Desempenho(5.0, 5.0, null, 70),
        };
        for (Desempenho d : turma) System.out.println(d);
    }
}
