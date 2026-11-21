// Gerado automaticamente a partir de 01 - Aulas/Aula 07 - Tipos Compostos/02 - Resumo Teórico/resumo-aula-07.md (linha 65).
// Seção: 3. Enumerações (p.4–5)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-07/resumo/02-3-enumeracoes-p-4-5/Main.java
// A saída deve conter: DOMINGO | SEGUNDA | SABADO

class Main {
    public enum Dia { DOMINGO, SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA, SABADO }

    public static void main(String[] args) {
        for (Dia d : Dia.values()) {   // values() devolve os valores na ordem declarada
            System.out.println(d);
        }
    }
}
