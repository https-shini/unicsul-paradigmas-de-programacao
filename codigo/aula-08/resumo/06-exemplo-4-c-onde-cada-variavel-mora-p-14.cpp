// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/02 - Resumo Teórico/resumo-aula-08.md (linha 261).
// Seção: Exemplo 4 — C++, onde cada variável mora (p.14)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resumo/06-exemplo-4-c-onde-cada-variavel-mora-p-14.cpp
// Entrada de exemplo: 2 3 3 1 2 3
// A saída deve conter: Vetor[0] = 5 | Vetor[1] = 10 | Vetor[2] = 15

#include <iostream>
using namespace std;

int n, res;                                   // segmento estático

int funcaoA(int x, int y) {
    cout << "Endereco de x: " << &x << "\n";  // pilha (frame de funcaoA)
    cout << "Endereco de y: " << &y << "\n";
    return x + y;
}

int main() {
    int a, b;                                 // pilha (frame de main)
    cin >> a >> b;
    cout << "Endereco de a: " << &a << "\n";
    cout << "Endereco de b: " << &b << "\n";
    cout << "Endereco de n: " << &n << "\n";
    cout << "Endereco de res: " << &res << "\n";
    res = funcaoA(a, b);
    cin >> n;
    int* vetor = new int[n];                  // heap: vetor de n inteiros
    cout << "Endereco de vetor: " << vetor << "\n";
    for (int i = 0; i < n; i++) cin >> vetor[i];
    for (int i = 0; i < n; i++)
        cout << "Vetor[" << i << "] = " << vetor[i] * res << endl;
    delete[] vetor;                           // libera o vetor inteiro
    return 0;
}
