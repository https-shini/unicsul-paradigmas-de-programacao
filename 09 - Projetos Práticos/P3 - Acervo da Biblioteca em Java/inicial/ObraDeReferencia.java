/**
 * Dicionários e enciclopédias: só consulta local. É um Item, mas NÃO deve implementar Emprestavel.
 * TODO (R3): tipo "Referência" e multa por dia 0.
 */
public class ObraDeReferencia extends Item {
    public ObraDeReferencia(String codigo, String titulo, int ano) {
        super(codigo, titulo, ano);
    }

    @Override public String tipo() { throw new UnsupportedOperationException("TODO: ObraDeReferencia.tipo"); }
    @Override public double multaPorDia() { throw new UnsupportedOperationException("TODO: ObraDeReferencia.multaPorDia"); }
}
