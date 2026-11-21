// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 105).
// Seção: 12
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/03-12/Main.java
// A saída deve conter: Retangulo: area 6.00 ⏎ Circulo: area 3.14

import java.util.Locale;

abstract class Forma {
    private final String nome;
    protected Forma(String nome) { this.nome = nome; }

    public abstract double area();                    // sem corpo: cada subclasse define

    public String descricao() {                       // método concreto, herdado
        return String.format(Locale.ROOT, "%s: area %.2f", nome, area());
    }
}

class Retangulo extends Forma {
    private final double base, altura;
    Retangulo(double base, double altura) { super("Retangulo"); this.base = base; this.altura = altura; }
    @Override public double area() { return base * altura; }
}

class Circulo extends Forma {
    private final double raio;
    Circulo(double raio) { super("Circulo"); this.raio = raio; }
    @Override public double area() { return Math.PI * raio * raio; }
}

public class Main {
    public static void main(String[] args) {
        Forma[] formas = { new Retangulo(2, 3), new Circulo(1) };
        for (Forma f : formas) {
            System.out.println(f.descricao());        // polimorfismo dinâmico
        }
    }
}
