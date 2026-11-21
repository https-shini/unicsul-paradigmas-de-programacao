// Gerado automaticamente a partir de 01 - Aulas/Aula 07 - Tipos Compostos/02 - Resumo Teórico/resumo-aula-07.md (linha 90).
// Seção: 4. Estruturas ou registros (p.6–8)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-07/resumo/03-4-estruturas-ou-registros-p-6-8.cpp
// Entrada de exemplo: Ana ⏎ 20 ⏎ F
// A saída deve conter: Ana tem 20 anos e é do sexo F

#include <iostream>
using namespace std;

int main() {
    struct Pessoa {
        char nome[30];
        int idade;
        char sexo;
    };
    struct Pessoa p1, p2;

    std::cout << "Digite o nome da pessoa: ";
    std::cin >> p1.nome;
    std::cout << "Digite a idade da pessoa: ";
    std::cin >> p1.idade;
    std::cout << "Digite o sexo da pessoa: ";
    std::cin >> p1.sexo;
    p2 = p1;                                    // copia TODOS os campos
    std::cout << p2.nome << " tem " << p2.idade << " anos e é do sexo " << p2.sexo << endl;
    return 0;
}
