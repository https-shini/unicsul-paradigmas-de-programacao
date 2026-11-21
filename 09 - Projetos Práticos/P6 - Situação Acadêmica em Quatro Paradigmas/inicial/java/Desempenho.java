/**
 * Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão ORIENTADA A OBJETOS.
 * TODO: complete os métodos. O construtor deve garantir notas válidas (invariante do objeto).
 */
public final class Desempenho {
    private final double a1, a2;
    private final Double af;          // null = não fez a AF
    private final double freq;

    public Desempenho(double a1, double a2, Double af, double freq) {
        // TODO: IllegalArgumentException se A1, A2 ou AF estiverem fora de 0–5, ou freq fora de 0–100
        this.a1 = a1;
        this.a2 = a2;
        this.af = af;
        this.freq = freq;
    }

    public double notaFinal() { return a1 + a2; }

    public double maiorNota() { return Math.max(a1, a2); }

    /** TODO: 6 menos a maior nota. */
    public double notaMinimaAF() {
        throw new UnsupportedOperationException("TODO: notaMinimaAF");
    }

    /** TODO: true se tirou pelo menos 1 ponto na A1 e na A2. */
    public boolean podeFazerAF() {
        throw new UnsupportedOperationException("TODO: podeFazerAF");
    }

    /** TODO: "APROVADO", "REPROVADO", "REPROVADO POR FALTA", "AF", "APROVADO NA AF" ou "REPROVADO NA AF". */
    public String situacao() {
        throw new UnsupportedOperationException("TODO: situacao");
    }

    @Override
    public String toString() {
        return "A1=" + a1 + " A2=" + a2 + " AF=" + (af == null ? "-" : af) + " freq=" + freq + "% -> " + situacao();
    }
}
