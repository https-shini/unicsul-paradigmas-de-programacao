/** Item que pode sair da biblioteca: herda de Item e implementa Emprestavel. */
public abstract class ItemCirculante extends Item implements Emprestavel {
    private String usuario;                       // null = disponível

    protected ItemCirculante(String codigo, String titulo, int ano) {
        super(codigo, titulo, ano);
    }

    /** TODO (R6): false se já emprestado ou usuário vazio; senão guarda o usuário e devolve true. */
    @Override
    public boolean emprestar(String usuario) {
        throw new UnsupportedOperationException("TODO: emprestar");
    }

    @Override
    public void devolver() {
        throw new UnsupportedOperationException("TODO: devolver");
    }

    @Override
    public boolean disponivel() {
        throw new UnsupportedOperationException("TODO: disponivel");
    }

    @Override
    public String getUsuario() { return usuario; }
}
