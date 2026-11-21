/** Capacidade de ser emprestado. Uma interface é um contrato: quem a implementa promete estes métodos (Aula 13). */
public interface Emprestavel {
    /** Empresta ao usuário; devolve false se o item já está emprestado. */
    boolean emprestar(String usuario);

    void devolver();

    boolean disponivel();

    /** Usuário com o item, ou null se disponível. */
    String getUsuario();

    int prazoDias();
}
