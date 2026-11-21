public class Livro extends ItemCirculante {
    private final String autor;

    public Livro(String codigo, String titulo, int ano, String autor) {
        super(codigo, titulo, ano);
        this.autor = autor;
    }

    public String getAutor() { return autor; }

    // Exemplo pronto de sobrescrita; faça o mesmo em Revista e ObraDeReferencia.
    @Override public String tipo() { return "Livro"; }
    @Override public int prazoDias() { return 14; }
    @Override public double multaPorDia() { return 1.00; }

    /** TODO (R5): super.descricao() + " — " + autor */
    @Override
    public String descricao() {
        throw new UnsupportedOperationException("TODO: Livro.descricao");
    }
}
