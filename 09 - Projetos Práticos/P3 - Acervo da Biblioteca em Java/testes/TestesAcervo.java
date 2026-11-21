import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.List;

/** Testes do projeto P3. Rode com:  python3 ferramentas/testar_projetos.py P3 */
public class TestesAcervo {
    static int total = 0, falhas = 0;

    static void checa(boolean cond, String descricao) {
        total++;
        if (!cond) { falhas++; System.out.println("  FALHOU: " + descricao); }
    }

    static boolean perto(double a, double b) { return Math.abs(a - b) < 1e-9; }

    interface Corpo { void run() throws Exception; }

    static void teste(String nome, Corpo corpo) {
        System.out.println(nome);
        try { corpo.run(); }
        catch (Throwable e) { total++; falhas++; System.out.println("  FALHOU: exceção inesperada: " + e); }
    }

    static boolean lanca(Class<? extends Throwable> tipo, Corpo corpo) {
        try { corpo.run(); } catch (Throwable e) { return tipo.isInstance(e); }
        return false;
    }

    static Livro sebesta() { return new Livro("L1", "Conceitos de Linguagens de Programação", 2011, "Robert W. Sebesta"); }
    static Revista cacm() { return new Revista("R1", "Communications of the ACM", 1968, 3); }
    static ObraDeReferencia dicionario() { return new ObraDeReferencia("D1", "Dicionário de Computação", 2005); }

    public static void main(String[] args) {
        System.out.println("== Hierarquia e encapsulamento ==");
        teste("Item é abstrata; Livro e Revista herdam de Item", () -> {
            checa(Modifier.isAbstract(Item.class.getModifiers()), "Item deve ser abstract");
            checa(Item.class.isAssignableFrom(Livro.class), "Livro deve herdar de Item");
            checa(Item.class.isAssignableFrom(Revista.class), "Revista deve herdar de Item");
            checa(Item.class.isAssignableFrom(ObraDeReferencia.class), "ObraDeReferencia deve herdar de Item");
        });
        teste("só Livro e Revista são Emprestavel", () -> {
            checa(sebesta() instanceof Emprestavel, "Livro deve implementar Emprestavel");
            checa(cacm() instanceof Emprestavel, "Revista deve implementar Emprestavel");
            checa(!(((Object) dicionario()) instanceof Emprestavel), "ObraDeReferencia NÃO deve implementar Emprestavel");
        });
        teste("todos os atributos de instância são private", () -> {
            for (Class<?> c : new Class<?>[]{Item.class, ItemCirculante.class, Livro.class, Revista.class, Acervo.class})
                for (Field f : c.getDeclaredFields())
                    if (!Modifier.isStatic(f.getModifiers()))
                        checa(Modifier.isPrivate(f.getModifiers()), c.getSimpleName() + "." + f.getName() + " deveria ser private");
        });
        teste("construtor valida os dados", () -> {
            checa(lanca(IllegalArgumentException.class, () -> new Livro("L9", "", 2000, "X")), "título vazio");
            checa(lanca(IllegalArgumentException.class, () -> new Revista("R9", "Revista", 0, 1)), "ano 0");
            checa(lanca(IllegalArgumentException.class, () -> new ObraDeReferencia(" ", "Atlas", 1999)), "código vazio");
        });

        System.out.println("== Métodos sobrescritos ==");
        teste("tipo, prazo e multa por dia de cada classe", () -> {
            Livro l = sebesta(); Revista r = cacm(); ObraDeReferencia d = dicionario();
            checa(l.tipo().equals("Livro") && r.tipo().equals("Revista") && d.tipo().equals("Referência"), "tipo()");
            checa(l.prazoDias() == 14, "prazo do livro = 14");
            checa(r.prazoDias() == 7, "prazo da revista = 7");
            checa(perto(l.multaPorDia(), 1.0) && perto(r.multaPorDia(), 0.5) && perto(d.multaPorDia(), 0.0), "multaPorDia()");
        });
        teste("multa(dias) usa a multaPorDia() de cada tipo (vinculação dinâmica)", () -> {
            Item[] itens = {sebesta(), cacm(), dicionario()};
            double soma = 0;
            for (Item i : itens) soma += i.multa(4);
            checa(perto(soma, 4 * 1.0 + 4 * 0.5), "soma das multas de 4 dias = 6.0, obtido " + soma);
            checa(perto(sebesta().multa(0), 0) && perto(sebesta().multa(-3), 0), "sem atraso, sem multa");
        });
        teste("descricao() sobrescrita reaproveita super.descricao()", () -> {
            checa(sebesta().descricao().equals("[Livro] Conceitos de Linguagens de Programação (2011) — Robert W. Sebesta"),
                  "livro: " + sebesta().descricao());
            checa(cacm().descricao().equals("[Revista] Communications of the ACM (1968) — ed. 3"), "revista: " + cacm().descricao());
            checa(dicionario().descricao().equals("[Referência] Dicionário de Computação (2005)"), "referência: " + dicionario().descricao());
            checa(sebesta().toString().equals(sebesta().descricao()), "toString() = descricao()");
        });

        System.out.println("== Empréstimo ==");
        teste("emprestar e devolver", () -> {
            Livro l = sebesta();
            checa(l.disponivel() && l.getUsuario() == null, "novo livro disponível");
            checa(l.emprestar("ana"), "primeiro empréstimo");
            checa(!l.disponivel() && "ana".equals(l.getUsuario()), "emprestado a ana");
            checa(!l.emprestar("bruno"), "não empresta duas vezes");
            checa("ana".equals(l.getUsuario()), "continua com ana");
            l.devolver();
            checa(l.disponivel() && l.getUsuario() == null, "devolvido");
            checa(!l.emprestar(""), "usuário vazio não pode pegar emprestado");
        });

        System.out.println("== Acervo ==");
        teste("adicionar e buscar por código", () -> {
            Acervo a = new Acervo();
            a.adicionar(sebesta()); a.adicionar(cacm()); a.adicionar(dicionario());
            checa(a.tamanho() == 3, "tamanho 3");
            checa(a.buscar("R1") != null && a.buscar("R1").getTitulo().equals("Communications of the ACM"), "buscar(\"R1\")");
            checa(a.buscar("X9") == null, "código inexistente → null");
            checa(lanca(IllegalArgumentException.class, () -> a.adicionar(new Livro("L1", "Outro", 2020, "Y"))), "código repetido");
        });
        teste("sobrecarga: buscar(int ano) e buscarPorTitulo", () -> {
            Acervo a = new Acervo();
            a.adicionar(sebesta()); a.adicionar(cacm()); a.adicionar(dicionario());
            a.adicionar(new Livro("L2", "Programming in Prolog", 1968, "Clocksin"));
            List<Item> de1968 = a.buscar(1968);
            checa(de1968.size() == 2 && de1968.get(0).getCodigo().equals("R1") && de1968.get(1).getCodigo().equals("L2"),
                  "buscar(1968) devolve R1 e L2, na ordem de inserção");
            checa(a.buscar(1500).isEmpty(), "ano sem itens → lista vazia");
            checa(a.buscarPorTitulo("acm").size() == 1, "busca por título ignora maiúsculas");
            checa(a.buscarPorTitulo("PRO").size() == 2, "\"PRO\" está em dois títulos");
        });
        teste("empréstimo pelo acervo respeita a interface", () -> {
            Acervo a = new Acervo();
            a.adicionar(sebesta()); a.adicionar(cacm()); a.adicionar(dicionario());
            checa(a.emprestar("L1", "ana"), "empresta o livro");
            checa(!a.emprestar("L1", "bruno"), "livro já emprestado");
            checa(!a.emprestar("D1", "carla"), "obra de referência não é emprestável");
            checa(!a.emprestar("X9", "ana"), "código inexistente");
            checa(a.emprestar("R1", "bruno"), "empresta a revista");
            checa(a.emprestados().size() == 2, "dois emprestados");
            checa(a.devolver("L1") && !a.devolver("L1"), "devolve uma vez só");
            checa(a.emprestados().size() == 1 && a.emprestados().get(0).getCodigo().equals("R1"), "sobra a revista");
        });
        teste("multa e relatório", () -> {
            Acervo a = new Acervo();
            a.adicionar(sebesta()); a.adicionar(cacm()); a.adicionar(dicionario());
            a.emprestar("L1", "ana");
            checa(perto(a.multa("L1", 3), 3.0) && perto(a.multa("R1", 3), 1.5), "multas de 3 dias");
            checa(perto(a.multa("X9", 3), 0.0), "item inexistente → 0");
            List<String> rel = a.relatorio();
            checa(rel.size() == 3, "três linhas");
            checa(rel.get(0).equals("[Livro] Conceitos de Linguagens de Programação (2011) — Robert W. Sebesta · emprestado a ana"), rel.get(0));
            checa(rel.get(1).equals("[Revista] Communications of the ACM (1968) — ed. 3 · disponível"), rel.get(1));
            checa(rel.get(2).equals("[Referência] Dicionário de Computação (2005) · consulta local"), rel.get(2));
        });

        System.out.println("\nRESULTADO: " + total + " testes, " + falhas + " falhas");
        System.exit(falhas == 0 ? 0 : 1);
    }
}
