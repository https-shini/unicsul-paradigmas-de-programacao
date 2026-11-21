// Gerado automaticamente a partir de 01 - Aulas/Aula 13 - Paradigma Orientado a Objetos II/02 - Resumo Teórico/resumo-aula-13.md (linha 188).
// Seção: 7. Hierarquia de contas (p.14)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-13/resumo/03-7-hierarquia-de-contas-p-14/Main.java
// A saída deve conter: Simples: saque negado | Especial: saque de 150.0 realizado | Saldos: 100.0  |  -50.0  |  102.0

import java.util.List;

abstract class Conta {
    protected int numero;
    protected String cliente;
    protected double saldo;

    Conta(int numero, String cliente, double saldo) {
        this.numero = numero; this.cliente = cliente; this.saldo = saldo;
    }

    void efetueDeposito(double valor) { saldo += valor; }

    boolean efetueSaque(double valor) {           // regra padrão: não pode ficar negativo
        if (valor > saldo) return false;
        saldo -= valor;
        return true;
    }

    abstract String tipo();                       // cada subclasse DEVE implementar
}

class ContaSimples extends Conta {
    ContaSimples(int n, String c, double s) { super(n, c, s); }
    String tipo() { return "Simples"; }
}

class ContaPoupanca extends Conta {
    ContaPoupanca(int n, String c, double s) { super(n, c, s); }
    void acrescenteRendimentos(double taxa) { saldo += saldo * taxa; }   // membro ADICIONADO
    String tipo() { return "Poupanca"; }
}

class ContaEspecial extends Conta {
    private double limite;                                              // atributo ADICIONADO
    ContaEspecial(int n, String c, double s, double limite) { super(n, c, s); this.limite = limite; }

    @Override
    boolean efetueSaque(double valor) {           // comportamento MODIFICADO (sobrescrita)
        if (valor > saldo + limite) return false;
        saldo -= valor;
        return true;
    }
    String tipo() { return "Especial"; }
}

public class Main {
    public static void main(String[] args) {
        ContaPoupanca poup = new ContaPoupanca(3, "Caio", 100);
        List<Conta> contas = List.of(new ContaSimples(1, "Ana", 100),
                                     new ContaEspecial(2, "Bia", 100, 200),
                                     poup);
        for (Conta c : contas) {                  // referência do tipo BASE
            if (c instanceof ContaPoupanca) continue;
            boolean ok = c.efetueSaque(150);       // LIGAÇÃO TARDIA: qual efetueSaque roda?
            System.out.println(c.tipo() + ": " + (ok ? "saque de 150.0 realizado" : "saque negado"));
        }
        poup.acrescenteRendimentos(0.02);
        System.out.println("Saldos: " + contas.get(0).saldo + " | " + contas.get(1).saldo + " | " + poup.saldo);
    }
}
