import java.util.Locale;

/**
 * Classe base ABSTRATA do acervo (Aula 13 p.13): não pode ser instanciada.
 * Atributos privados (encapsulamento, Aula 12): só são lidos pelos getters e só mudam pelo construtor.
 */
public abstract class Item {
    private final String codigo;
    private final String titulo;
    private final int ano;

    protected Item(String codigo, String titulo, int ano) {
        if (codigo == null || codigo.isBlank()) throw new IllegalArgumentException("código vazio");
        if (titulo == null || titulo.isBlank()) throw new IllegalArgumentException("título vazio");
        if (ano <= 0) throw new IllegalArgumentException("ano inválido: " + ano);
        this.codigo = codigo;
        this.titulo = titulo;
        this.ano = ano;
    }

    public String getCodigo() { return codigo; }
    public String getTitulo() { return titulo; }
    public int getAno() { return ano; }

    /** Nome do tipo para relatórios: "Livro", "Revista"... */
    public abstract String tipo();

    /** Valor da multa por dia de atraso; cada subclasse define o seu. */
    public abstract double multaPorDia();

    /** Método concreto que usa um método abstrato: qual multaPorDia() executa é decidido em execução. */
    public double multa(int diasAtraso) {
        return diasAtraso <= 0 ? 0.0 : diasAtraso * multaPorDia();
    }

    public String descricao() {
        return String.format(Locale.ROOT, "[%s] %s (%d)", tipo(), titulo, ano);
    }

    @Override
    public String toString() { return descricao(); }
}
