// Gerado automaticamente a partir de 01 - Aulas/Aula 11 - Paradigma Imperativo III/04 - Resoluções/resolucoes-aula-11.md (linha 63).
// Seção: E7
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-11/resolucoes/01-e7.cpp
// A saída deve conter: valor: 2 | referencia: 30 | valor-resultado: 20

#include <iostream>

void por_valor(int x, int y)       { x = x + 1; y = y * 10; }
void por_referencia(int &x, int &y) { x = x + 1; y = y * 10; }

// Valor-resultado simulado: copia na entrada, trabalha nas cópias e copia de volta no fim
void por_valor_resultado(int &rx, int &ry) {
    int x = rx, y = ry;          // entrada (cópias)
    x = x + 1; y = y * 10;       // corpo
    rx = x;                      // saída: primeiro x...
    ry = y;                      // ...depois y
}

int main() {
    int a = 2; por_valor(a, a);           std::cout << "valor: " << a << "\n";
    a = 2;     por_referencia(a, a);      std::cout << "referencia: " << a << "\n";
    a = 2;     por_valor_resultado(a, a); std::cout << "valor-resultado: " << a << "\n";
    return 0;
}
