// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/04 - Resoluções/resolucoes-aula-13.md (linha 212).
// Seção: E10
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resolucoes/06-e10/Main.java
// A saída deve conter: Retangulo: 6.00 | Circulo: 3.14

import java.util.List;

abstract class Forma {
    abstract double area();                 // sem implementação: obriga as subclasses
    abstract String nome();
}

class Retangulo extends Forma {
    private final double largura, altura;
    Retangulo(double l, double a) { largura = l; altura = a; }
    double area() { return largura * altura; }
    String nome() { return "Retangulo"; }
}

class Circulo extends Forma {
    private final double raio;
    Circulo(double r) { raio = r; }
    double area() { return Math.PI * raio * raio; }
    String nome() { return "Circulo"; }
}

public class Main {
    public static void main(String[] args) {
        List<Forma> formas = List.of(new Retangulo(2, 3), new Circulo(1));
        for (Forma f : formas) {
            System.out.printf("%s: %.2f%n", f.nome(), f.area());   // <- LIGAÇÃO TARDIA aqui
        }
        // new Forma();  // não compila: Forma é abstrata
    }
}
