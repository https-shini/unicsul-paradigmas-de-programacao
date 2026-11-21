import java.util.Locale;

/**
 * Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão ORIENTADA A OBJETOS.
 * O desempenho é um objeto: o construtor garante que as notas são válidas (invariante),
 * e os atributos privados não mudam depois (objeto imutável).
 */
public final class Desempenho {
    private final double a1, a2;
    private final Double af;          // null = não fez a AF (tipo por referência admite "ausente")
    private final double freq;

    public Desempenho(double a1, double a2, Double af, double freq) {
        validar(a1, "A1");
        validar(a2, "A2");
        if (af != null) validar(af, "AF");
        if (freq < 0 || freq > 100) throw new IllegalArgumentException("frequência fora de 0–100: " + freq);
        this.a1 = a1;
        this.a2 = a2;
        this.af = af;
        this.freq = freq;
    }

    private static void validar(double nota, String nome) {
        if (nota < 0 || nota > 5) throw new IllegalArgumentException(nome + " fora de 0–5: " + nota);
    }

    public double notaFinal() { return a1 + a2; }

    public double maiorNota() { return Math.max(a1, a2); }

    public double notaMinimaAF() { return 6.0 - maiorNota(); }

    public boolean podeFazerAF() { return a1 >= 1 && a2 >= 1; }

    public String situacao() {
        if (freq < 75) return "REPROVADO POR FALTA";
        if (notaFinal() >= 6) return "APROVADO";
        if (!podeFazerAF()) return "REPROVADO";
        if (af == null) return "AF";
        return af + maiorNota() >= 6 ? "APROVADO NA AF" : "REPROVADO NA AF";
    }

    @Override
    public String toString() {
        return String.format(Locale.ROOT, "A1=%.1f A2=%.1f AF=%s freq=%.0f%% -> %s",
                a1, a2, af == null ? "-" : String.format(Locale.ROOT, "%.1f", af), freq, situacao());
    }
}
