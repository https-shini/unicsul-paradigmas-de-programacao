// Gerado automaticamente a partir de 01 - Aulas/Aula 11 - Paradigma Imperativo III/02 - Resumo Teórico/resumo-aula-11.md (linha 63).
// Seção: 4. Parâmetros (p.8–12)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-11/resumo/01-4-parametros-p-8-12.cpp
// Entrada de exemplo: 2 5
// A saída deve conter: 2 elevado a 5: 32 | 2 elevado ao quadrado: 4

#include <iostream>

int elevado(int x, int y = 2) {        // y tem valor padrão 2
    int t = 1;
    for (int i = 0; i < y; i++) {
        t = t * x;
    }
    return t;
}

int main() {
    int base, expo, res1, res2;
    std::cout << "Digite o valor da base: ";
    std::cin >> base;
    std::cout << "Digite o valor do expoente: ";
    std::cin >> expo;
    res1 = elevado(base, expo);        // usa o expoente informado
    res2 = elevado(base);              // omite y: usa o padrão 2
    std::cout << base << " elevado a " << expo << ": " << res1 << "\n";
    std::cout << base << " elevado ao quadrado: " << res2 << "\n";
    return 0;
}
