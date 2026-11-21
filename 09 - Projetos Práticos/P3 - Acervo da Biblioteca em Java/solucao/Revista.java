public class Revista extends ItemCirculante {
    private final int edicao;

    public Revista(String codigo, String titulo, int ano, int edicao) {
        super(codigo, titulo, ano);
        this.edicao = edicao;
    }

    public int getEdicao() { return edicao; }

    @Override public String tipo() { return "Revista"; }
    @Override public int prazoDias() { return 7; }
    @Override public double multaPorDia() { return 0.50; }

    @Override
    public String descricao() { return super.descricao() + " — ed. " + edicao; }
}
