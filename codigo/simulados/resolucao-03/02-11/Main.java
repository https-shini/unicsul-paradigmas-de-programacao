// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-03.md (linha 53).
// Seção: 11
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-03/02-11/Main.java
// A saída deve conter: 10 ⏎ 20 ⏎ 30 ⏎ 40

class Fila {
    private final int[] itens = new int[4];   // representação OCULTA
    private int inicio = 0, fim = 0, tamanho = 0;

    public boolean vazia() { return tamanho == 0; }

    public void enfileirar(int x) {
        if (tamanho == itens.length) {
            System.out.println("Erro - fila cheia");
            return;
        }
        itens[fim] = x;
        fim = (fim + 1) % itens.length;       // volta ao início: vetor circular
        tamanho++;
    }

    public int desenfileirar() {
        if (vazia()) {
            System.out.println("Erro - fila vazia");
            return -1;
        }
        int x = itens[inicio];
        inicio = (inicio + 1) % itens.length;
        tamanho--;
        return x;
    }
}

public class Main {
    public static void main(String[] args) {
        Fila f = new Fila();
        f.enfileirar(10);
        f.enfileirar(20);
        f.enfileirar(30);
        System.out.println(f.desenfileirar());   // 10
        f.enfileirar(40);
        while (!f.vazia()) {
            System.out.println(f.desenfileirar());   // 20, 30, 40
        }
    }
}
