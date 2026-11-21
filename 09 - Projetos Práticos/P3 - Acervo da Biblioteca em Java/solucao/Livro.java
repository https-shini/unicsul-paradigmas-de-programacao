public class Livro extends ItemCirculante {
    private final String autor;

    public Livro(String codigo, String titulo, int ano, String autor) {
        super(codigo, titulo, ano);
        this.autor = autor;
    }

    public String getAutor() { return autor; }

    @Override public String tipo() { return "Livro"; }
    @Override public int prazoDias() { return 14; }
    @Override public double multaPorDia() { return 1.00; }

    @Override                                     // sobrescrita que reaproveita a versão da superclasse
    public String descricao() { return super.descricao() + " — " + autor; }
}
