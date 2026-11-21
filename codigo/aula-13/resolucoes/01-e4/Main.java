// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/04 - Resoluções/resolucoes-aula-13.md (linha 25).
// Seção: E4
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resolucoes/01-e4/Main.java
// A saída deve conter: int: 5 | double: 5.5 | Cachorro: au au

class Animal {
    String som() { return "..."; }
}

class Cachorro extends Animal {
    @Override
    String som() { return "au au"; }              // SOBRESCRITA (dinâmico)
}

public class Main {
    static String soma(int a, int b)       { return "int: " + (a + b); }       // SOBRECARGA (estático)
    static String soma(double a, double b) { return "double: " + (a + b); }

    public static void main(String[] args) {
        System.out.println(soma(2, 3));           // compilador escolhe soma(int,int)
        System.out.println(soma(2.5, 3.0));       // compilador escolhe soma(double,double)
        Animal a = new Cachorro();                // referência do tipo base
        System.out.println("Cachorro: " + a.som());   // execução escolhe Cachorro.som()
    }
}
