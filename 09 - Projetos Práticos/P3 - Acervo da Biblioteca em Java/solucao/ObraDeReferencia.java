/** Dicionários e enciclopédias: só consulta local. É um Item, mas NÃO é Emprestavel. */
public class ObraDeReferencia extends Item {
    public ObraDeReferencia(String codigo, String titulo, int ano) {
        super(codigo, titulo, ano);
    }

    @Override public String tipo() { return "Referência"; }
    @Override public double multaPorDia() { return 0.0; }
}
