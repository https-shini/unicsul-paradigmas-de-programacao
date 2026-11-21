/** Item que pode sair da biblioteca. Herda de Item e implementa Emprestavel: herança + interface. */
public abstract class ItemCirculante extends Item implements Emprestavel {
    private String usuario;                       // null = disponível

    protected ItemCirculante(String codigo, String titulo, int ano) {
        super(codigo, titulo, ano);
    }

    @Override
    public boolean emprestar(String usuario) {
        if (!disponivel() || usuario == null || usuario.isBlank()) return false;
        this.usuario = usuario;
        return true;
    }

    @Override
    public void devolver() { this.usuario = null; }

    @Override
    public boolean disponivel() { return usuario == null; }

    @Override
    public String getUsuario() { return usuario; }
}
