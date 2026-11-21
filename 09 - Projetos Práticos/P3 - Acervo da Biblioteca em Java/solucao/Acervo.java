import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/** Coleção de itens. Trabalha só com os tipos abstratos Item e Emprestavel: polimorfismo. */
public class Acervo {
    private final Map<String, Item> itens = new LinkedHashMap<>();   // mantém a ordem de inserção

    public void adicionar(Item item) {
        if (itens.containsKey(item.getCodigo()))
            throw new IllegalArgumentException("código repetido: " + item.getCodigo());
        itens.put(item.getCodigo(), item);
    }

    public int tamanho() { return itens.size(); }

    /** Busca pelo código; null se não existir. */
    public Item buscar(String codigo) { return itens.get(codigo); }

    /** SOBRECARGA: mesmo nome, parâmetro de outro tipo — escolhida em tempo de compilação. */
    public List<Item> buscar(int ano) {
        List<Item> r = new ArrayList<>();
        for (Item i : itens.values()) if (i.getAno() == ano) r.add(i);
        return r;
    }

    public List<Item> buscarPorTitulo(String trecho) {
        String t = trecho.toLowerCase(Locale.ROOT);
        List<Item> r = new ArrayList<>();
        for (Item i : itens.values()) if (i.getTitulo().toLowerCase(Locale.ROOT).contains(t)) r.add(i);
        return r;
    }

    public boolean emprestar(String codigo, String usuario) {
        Item i = itens.get(codigo);
        if (i instanceof Emprestavel e) return e.emprestar(usuario);   // obra de referência: não entra aqui
        return false;
    }

    public boolean devolver(String codigo) {
        Item i = itens.get(codigo);
        if (i instanceof Emprestavel e && !e.disponivel()) {
            e.devolver();
            return true;
        }
        return false;
    }

    public List<Item> emprestados() {
        List<Item> r = new ArrayList<>();
        for (Item i : itens.values())
            if (i instanceof Emprestavel e && !e.disponivel()) r.add(i);
        return r;
    }

    public double multa(String codigo, int diasAtraso) {
        Item i = itens.get(codigo);
        return i == null ? 0.0 : i.multa(diasAtraso);    // vinculação dinâmica: multaPorDia() de cada tipo
    }

    public List<String> relatorio() {
        List<String> linhas = new ArrayList<>();
        for (Item i : itens.values()) {
            String situacao;
            if (i instanceof Emprestavel e)
                situacao = e.disponivel() ? "disponível" : "emprestado a " + e.getUsuario();
            else
                situacao = "consulta local";
            linhas.add(i.descricao() + " · " + situacao);
        }
        return linhas;
    }
}
