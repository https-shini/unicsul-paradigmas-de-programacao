// Gerado automaticamente a partir de 06 - Revisões e Sínteses/quadros-comparativos.md (linha 62).
// Seção: 2. Um mesmo problema nos quatro paradigmas
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/revisoes/quadros-comparativos/02-2-um-mesmo-problema-nos-quatro-paradigmas/Main.java
// A saída deve conter: 120

class Calculadora {
    private long ultimo;                          // estado encapsulado
    long fatorial(int n) {
        ultimo = 1;
        for (int i = 2; i <= n; i++) ultimo *= i;
        return ultimo;
    }
}
public class Main {
    public static void main(String[] args) {
        Calculadora c = new Calculadora();       // objeto
        System.out.println(c.fatorial(5));       // mensagem
    }
}
