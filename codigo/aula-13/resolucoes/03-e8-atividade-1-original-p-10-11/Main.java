// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/04 - Resoluções/resolucoes-aula-13.md (linha 135).
// Seção: E8 — Atividade 1 (original, p.10–11)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resolucoes/03-e8-atividade-1-original-p-10-11/Main.java
// A saída deve conter: Estou imprimindo um documento. ⏎ Estou digitalizando um documento. ⏎ Estou copiando um documento

interface Impressora {
    default void imprimaDocumento() { System.out.println("Estou imprimindo um documento."); }
}

interface Scanner {
    default void digitalizeDocumento() { System.out.println("Estou digitalizando um documento."); }
}

class Multifuncional implements Impressora, Scanner {
    public void copieDocumento() {
        System.out.println("Estou copiando um documento");
        System.out.println("******");
        digitalizeDocumento();
        imprimaDocumento();
        System.out.println("******");
    }
}

public class Main {
    public static void main(String[] args) {
        Multifuncional hp3000 = new Multifuncional();
        hp3000.imprimaDocumento();
        hp3000.digitalizeDocumento();
        hp3000.copieDocumento();
    }
}
