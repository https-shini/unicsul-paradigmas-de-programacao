// Gerado automaticamente a partir de 01 - Aulas/Aula 11 - Paradigma Imperativo III/04 - Resoluções/resolucoes-aula-11.md (linha 185).
// Seção: E11
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-11/resolucoes/04-e11/Main.java
// A saída deve conter: soma dos pares = 30

public class Main {
    static int somaPares(int[] v) {
        int soma = 0;                         // VARIÁVEL + ATRIBUIÇÃO
        for (int i = 0; i < v.length; i++) { // REPETIÇÃO
            if (v[i] % 2 == 0) {              // DECISÃO
                soma = soma + v[i];           // ATRIBUIÇÃO (destino = expressão)
            }
        }
        return soma;
    }

    public static void main(String[] args) {
        System.out.println("soma dos pares = " + somaPares(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
    }
}
