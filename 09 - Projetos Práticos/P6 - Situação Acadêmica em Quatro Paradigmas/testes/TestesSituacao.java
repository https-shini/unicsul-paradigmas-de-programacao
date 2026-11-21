// Gerado por gerar_testes.py a partir de casos.csv — não edite à mão.
public class TestesSituacao {
    static int total = 0, falhas = 0;

    static void caso(double a1, double a2, Double af, double freq, String esperado, String coment) {
        total++;
        String obtido;
        try { obtido = new Desempenho(a1, a2, af, freq).situacao(); }
        catch (RuntimeException e) { obtido = e.toString(); }
        if (!esperado.equals(obtido)) {
            falhas++;
            System.out.printf("  FALHOU Desempenho(%s, %s, %s, %s): esperado \"%s\", obtido \"%s\"  (%s)%n", a1, a2, af, freq, esperado, obtido, coment);
        }
    }

    static void minima(double a1, double a2, double esperado) {
        total++;
        try {
            double obtido = new Desempenho(a1, a2, null, 100).notaMinimaAF();
            if (Math.abs(obtido - esperado) > 1e-9) {
                falhas++; System.out.printf("  FALHOU notaMinimaAF(%s, %s): esperado %s, obtido %s%n", a1, a2, esperado, obtido);
            }
        } catch (RuntimeException e) { falhas++; System.out.println("  FALHOU notaMinimaAF: " + e); }
    }

    static void invalido(double a1, double a2, Double af, double freq) {
        total++;
        try {
            new Desempenho(a1, a2, af, freq);
            falhas++; System.out.printf("  FALHOU: Desempenho(%s, %s, %s, %s) deveria lançar IllegalArgumentException%n", a1, a2, af, freq);
        } catch (IllegalArgumentException e) { /* esperado */ }
        catch (RuntimeException e) { falhas++; System.out.println("  FALHOU: exceção errada: " + e); }
    }

    public static void main(String[] args) {
        caso(3.5, 4.0, null, 80.0, "APROVADO", "soma 7,5");
        caso(3.0, 3.0, null, 75.0, "APROVADO", "limites: soma 6,0 e frequência 75%");
        caso(2.1, 3.9, null, 80.0, "APROVADO", "soma 6,0 com decimais");
        caso(5.0, 5.0, null, 74.9, "REPROVADO POR FALTA", "nota máxima não salva a frequência");
        caso(0.0, 0.0, null, 0.0, "REPROVADO POR FALTA", "a frequência é verificada primeiro");
        caso(2.0, 3.0, 5.0, 70.0, "REPROVADO POR FALTA", "AF não salva a frequência");
        caso(0.5, 5.0, null, 100.0, "REPROVADO", "menos de 1 ponto na A1: sem direito à AF");
        caso(5.0, 0.9, null, 100.0, "REPROVADO", "menos de 1 ponto na A2: sem direito à AF");
        caso(0.5, 5.0, 5.0, 80.0, "REPROVADO", "a nota de AF é ignorada");
        caso(2.0, 3.0, null, 90.0, "AF", "soma 5,0: precisa de 3,0 na AF");
        caso(1.0, 1.0, null, 80.0, "AF", "exatamente 1 ponto: tem direito à AF");
        caso(2.0, 3.0, 3.5, 90.0, "APROVADO NA AF", "3,5 substitui o 2,0: 6,5");
        caso(1.0, 1.0, 5.0, 80.0, "APROVADO NA AF", "5,0 + 1,0 = 6,0");
        caso(2.9, 3.0, 3.0, 80.0, "APROVADO NA AF", "3,0 + 3,0 = 6,0");
        caso(4.5, 1.4, 2.0, 76.0, "APROVADO NA AF", "2,0 substitui o 1,4: 6,5");
        caso(2.0, 3.0, 2.5, 90.0, "REPROVADO NA AF", "2,5 + 3,0 = 5,5");
        caso(4.0, 1.9, 1.9, 80.0, "REPROVADO NA AF", "1,9 + 4,0 = 5,9");
        caso(4.0, 4.0, 3.0, 80.0, "APROVADO", "já aprovado: a AF não muda nada");
        minima(2.0, 3.0, 3.0);
        minima(1.0, 1.0, 5.0);
        minima(4.5, 1.4, 1.5);
        minima(4.1, 1.0, 1.9);
        invalido(5.5, 3.0, null, 80);   // A1 vale no máximo 5
        invalido(3.0, -1.0, null, 80);
        invalido(3.0, 2.0, 6.0, 80);    // AF vale no máximo 5
        invalido(3.0, 2.0, null, 101);
        System.out.println("\nRESULTADO: " + total + " testes, " + falhas + " falhas");
        System.exit(falhas == 0 ? 0 : 1);
    }
}
