// Gerado automaticamente a partir de 01 - Aulas/Aula 11 - Paradigma Imperativo III/04 - Resoluções/resolucoes-aula-11.md (linha 88).
// Seção: E8 — Atividade 1 (original, p.21)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-11/resolucoes/02-e8-atividade-1-original-p-21/Programa.cs
// Entrada de exemplo: 3 ⏎ 7
// A saída deve conter: a = 3, b = 7 | a = 7, b = 3

using System;

class Program {
    // out: o argumento não precisa estar inicializado e o método DEVE atribuir.
    //      Modelo semântico: SAÍDA (por resultado, implementado por referência).
    static void LerValores(out int a, out int b) {
        Console.Write("Primeiro numero: ");
        a = int.Parse(Console.ReadLine());
        Console.Write("Segundo numero: ");
        b = int.Parse(Console.ReadLine());
    }

    // ref: o argumento já tem valor, e o método o lê E o altera.
    //      Modelo semântico: ENTRADA E SAÍDA (por referência).
    static void Inverter(ref int a, ref int b) {
        int temp = a;
        a = b;
        b = temp;
    }

    // in: o argumento já tem valor, e o método só pode ler.
    //     Modelo semântico: ENTRADA (por referência somente leitura, sem cópia).
    static void Imprimir(in int a, in int b) {
        Console.WriteLine($"a = {a}, b = {b}");
    }

    static void Main() {
        int x, y;                  // não inicializados: permitido por causa do out
        LerValores(out x, out y);
        Imprimir(in x, in y);
        Inverter(ref x, ref y);
        Imprimir(in x, in y);
    }
}
