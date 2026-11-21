// Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/02 - Resumo Teórico/resumo-aula-06.md (linha 166).
// Seção: 6.1 Java ou C? (p.16)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resumo/05-6-1-java-ou-c-p-16-nao-compila/Main.java
// ATENÇÃO: este exemplo NÃO compila de propósito (ilustra um erro).

public class Main {
    public static void main(String[] args) {
        double x = 2.5;
        int y = 3;
        int res = x + y;      // erro: incompatible types: possible lossy conversion from double to int
        System.out.println(res);
    }
}
