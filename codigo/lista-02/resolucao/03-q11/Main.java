// Gerado automaticamente a partir de 02 - Listas de Exercícios/Lista 02 - Revisão II/02 - Resolução/resolucao-lista-02.md (linha 180).
// Seção: Q11
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/lista-02/resolucao/03-q11/Main.java
// A saída deve conter: sobrecarga int: 5 | sobrescrita: Especial

class Conta { String tipo() { return "Conta"; } }
class ContaEspecial extends Conta { @Override String tipo() { return "Especial"; } }

public class Main {
    static String soma(int a, int b)       { return "sobrecarga int: " + (a + b); }
    static String soma(double a, double b) { return "sobrecarga double: " + (a + b); }
    public static void main(String[] args) {
        System.out.println(soma(2, 3));                     // estático: escolhido na compilação
        Conta c = new ContaEspecial();                      // tipo base, objeto derivado
        System.out.println("sobrescrita: " + c.tipo());     // dinâmico: escolhido na execução
    }
}
