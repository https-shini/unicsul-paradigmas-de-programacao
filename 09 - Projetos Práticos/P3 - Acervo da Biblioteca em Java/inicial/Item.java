import java.util.Locale;

/**
 * Classe base ABSTRATA do acervo (Aula 13 p.13): não pode ser instanciada.
 * Atributos privados (encapsulamento, Aula 12).
 */
public abstract class Item {
    private final String codigo;
    private final String titulo;
    private final int ano;

    protected Item(String codigo, String titulo, int ano) {
        // TODO (R2): lançar IllegalArgumentException se código ou título forem nulos/vazios (isBlank) ou ano <= 0
        this.codigo = codigo;
        this.titulo = titulo;
        this.ano = ano;
    }

    public String getCodigo() { return codigo; }
    public String getTitulo() { return titulo; }
    public int getAno() { return ano; }

    /** Nome do tipo para relatórios: "Livro", "Revista", "Referência". */
    public abstract String tipo();

    /** Valor da multa por dia de atraso; cada subclasse define o seu. */
    public abstract double multaPorDia();

    /** TODO (R4): 0 se diasAtraso <= 0; senão, diasAtraso * multaPorDia(). */
    public double multa(int diasAtraso) {
        throw new UnsupportedOperationException("TODO: Item.multa");
    }

    /** TODO (R5): "[Tipo] Título (ano)" — use String.format(Locale.ROOT, ...). */
    public String descricao() {
        throw new UnsupportedOperationException("TODO: Item.descricao");
    }

    @Override
    public String toString() { return descricao(); }
}
