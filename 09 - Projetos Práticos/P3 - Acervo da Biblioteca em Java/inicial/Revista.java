/** TODO (R3): prazo de 7 dias, multa de 0,50 por dia; descrição termina com " — ed. N". */
public class Revista extends ItemCirculante {
    private final int edicao;

    public Revista(String codigo, String titulo, int ano, int edicao) {
        super(codigo, titulo, ano);
        this.edicao = edicao;
    }

    public int getEdicao() { return edicao; }

    @Override public String tipo() { throw new UnsupportedOperationException("TODO: Revista.tipo"); }
    @Override public int prazoDias() { throw new UnsupportedOperationException("TODO: Revista.prazoDias"); }
    @Override public double multaPorDia() { throw new UnsupportedOperationException("TODO: Revista.multaPorDia"); }
}
