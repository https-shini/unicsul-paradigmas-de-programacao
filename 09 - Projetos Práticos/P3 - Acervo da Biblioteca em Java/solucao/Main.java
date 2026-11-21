/** Demonstração: javac *.java && java Main */
public class Main {
    public static void main(String[] args) {
        Acervo acervo = new Acervo();
        acervo.adicionar(new Livro("L1", "Conceitos de Linguagens de Programação", 2011, "Robert W. Sebesta"));
        acervo.adicionar(new Livro("L2", "Structure and Interpretation of Computer Programs", 1996, "Abelson e Sussman"));
        acervo.adicionar(new Revista("R1", "Communications of the ACM", 1968, 3));
        acervo.adicionar(new ObraDeReferencia("D1", "Dicionário de Computação", 2005));

        acervo.emprestar("L1", "ana");
        acervo.emprestar("R1", "bruno");
        System.out.println(acervo.emprestar("D1", "carla") ? "emprestou" : "D1: só consulta local");

        for (String linha : acervo.relatorio()) System.out.println(linha);
        System.out.printf(java.util.Locale.ROOT, "Multa de L1 com 3 dias de atraso: R$ %.2f%n", acervo.multa("L1", 3));
        System.out.printf(java.util.Locale.ROOT, "Multa de R1 com 3 dias de atraso: R$ %.2f%n", acervo.multa("R1", 3));
    }
}
