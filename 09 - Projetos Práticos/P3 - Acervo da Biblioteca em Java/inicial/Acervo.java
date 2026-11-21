import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/** Coleção de itens. Trabalhe só com os tipos Item e Emprestavel: é aí que aparece o polimorfismo. */
public class Acervo {
    private final Map<String, Item> itens = new LinkedHashMap<>();   // mantém a ordem de inserção

    /** TODO (R7): código repetido → IllegalArgumentException. */
    public void adicionar(Item item) {
        throw new UnsupportedOperationException("TODO: adicionar");
    }

    public int tamanho() { return itens.size(); }

    /** Busca pelo código; null se não existir. */
    public Item buscar(String codigo) {
        throw new UnsupportedOperationException("TODO: buscar(String)");
    }

    /** TODO (R8): SOBRECARGA — mesmo nome, parâmetro int: itens do ano, na ordem de inserção. */
    public List<Item> buscar(int ano) {
        throw new UnsupportedOperationException("TODO: buscar(int)");
    }

    /** TODO (R8): títulos que contêm o trecho, sem diferenciar maiúsculas (toLowerCase(Locale.ROOT)). */
    public List<Item> buscarPorTitulo(String trecho) {
        throw new UnsupportedOperationException("TODO: buscarPorTitulo");
    }

    /** TODO (R9): só empresta se o item existir e for Emprestavel (instanceof). */
    public boolean emprestar(String codigo, String usuario) {
        throw new UnsupportedOperationException("TODO: emprestar");
    }

    /** TODO (R9): true se o item estava emprestado e foi devolvido. */
    public boolean devolver(String codigo) {
        throw new UnsupportedOperationException("TODO: devolver");
    }

    public List<Item> emprestados() {
        throw new UnsupportedOperationException("TODO: emprestados");
    }

    /** TODO (R10): multa do item (0 se não existir) — sem if por tipo: deixe a vinculação dinâmica trabalhar. */
    public double multa(String codigo, int diasAtraso) {
        throw new UnsupportedOperationException("TODO: multa");
    }

    /** TODO (R10): uma linha por item: descricao() + " · " + "disponível" | "emprestado a X" | "consulta local". */
    public List<String> relatorio() {
        throw new UnsupportedOperationException("TODO: relatorio");
    }
}
