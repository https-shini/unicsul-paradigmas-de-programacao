// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/02 - Resumo Teórico/resumo-aula-08.md (linha 140).
// Seção: Exemplo 3 — Referências a objetos em Java (p.11)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resumo/04-exemplo-3-referencias-a-objetos-em-java-p-11/Main.java
// A saída deve conter: Joao ⏎ Joao ⏎ Jose ⏎ Jose ⏎ Jose ⏎ Maria ⏎ Joao ⏎ Maria

class Main {
    public static void main(String[] args) {
        Pessoa p1, p2;
        p1 = new Pessoa("Joao");
        p2 = p1;                       // p2 aponta para o MESMO objeto
        System.out.println(p1.nome);   // Joao
        System.out.println(p2.nome);   // Joao
        p1.nome = "Jose";
        System.out.println(p1.nome);   // Jose
        System.out.println(p2.nome);   // Jose  (mesmo objeto!)
        p2 = new Pessoa("Maria");      // p2 passa a apontar para OUTRO objeto
        System.out.println(p1.nome);   // Jose
        System.out.println(p2.nome);   // Maria
        p1.nome = "Joao";
        System.out.println(p1.nome);   // Joao
        System.out.println(p2.nome);   // Maria
    }
}

class Pessoa {
    public String nome;
    public Pessoa(String nome) {
        this.nome = nome;
    }
}
