// Gerado automaticamente a partir de 01 - Aulas/Aula 11 - Paradigma Imperativo III/04 - Resoluções/resolucoes-aula-11.md (linha 138).
// Seção: E9
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-11/resolucoes/03-e9.cpp
// Entrada de exemplo: 3 8
// A saída deve conter: a = 3, b = 8 | a = 8, b = 3

#include <iostream>

void lerValores(int &a, int &b) {             // ~ out: escreve no chamador
    std::cin >> a >> b;
}

void inverter(int &a, int &b) {               // ~ ref: lê e altera
    int temp = a;
    a = b;
    b = temp;
}

void imprimir(const int &a, const int &b) {   // ~ in / ref readonly: só lê, sem cópia
    std::cout << "a = " << a << ", b = " << b << "\n";
}

int main() {
    int x, y;
    lerValores(x, y);
    imprimir(x, y);
    inverter(x, y);
    imprimir(x, y);
    return 0;
}
