// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/02 - Resumo Teórico/resumo-aula-08.md (linha 84).
// Seção: Exemplo 1 — C#, `ref` (p.9)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resumo/02-exemplo-1-c-ref-p-9/Programa.cs
// A saída deve conter: 0 ⏎ 1 ⏎ 0 ⏎ 1 ⏎ 1

using System;

class Program {
    static void Metodo1(int x) {        // por valor
        x = x + 1;
        Console.WriteLine(x);
    }

    static void Metodo2(ref int x) {    // por referência
        x = x + 1;
        Console.WriteLine(x);
    }

    public static void Main(string[] args) {
        int numero = 0;
        Console.WriteLine(numero);   // 0
        Metodo1(numero);             // 1 (a cópia foi incrementada)
        Console.WriteLine(numero);   // 0 (o original não mudou)
        Metodo2(ref numero);         // 1
        Console.WriteLine(numero);   // 1 (o original mudou)
    }
}
