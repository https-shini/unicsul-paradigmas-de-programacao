// Gerado automaticamente a partir de 01 - Aulas/Aula 08 - Ponteiros/02 - Resumo Teórico/resumo-aula-08.md (linha 216).
// Seção: Exemplo 4 — C++, onde cada variável mora (p.14)
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/aula-08/resumo/05-exemplo-4-c-onde-cada-variavel-mora-p-14.cpp

#include <iostream>
using namespace std;

int n, res;                                   // globais -> segmento estático
int funcaoA(int x, int y){                     // parâmetros -> pilha (frame de funcaoA)
  int resultado;
  resultado = x + y;
  cout << "Endereco de x: " << &x <<"\n";
  cout << "Endereco de y: " << &y <<"\n";
  return resultado;
}

int main() {
  int a, b;                                    // locais -> pilha (frame de main)
  cout << "Digite um número inteiro: \n";
  cin >> a;
  cout << "Digite um número inteiro: \n";
  cin >> b;
  cout << "Endereco de a: " << &a <<"\n";
  cout << "Endereco de b: " << &b <<"\n";
  cout << "Endereco de n: " << &n <<"\n";
  cout << "Endereco de res: " << &res <<"\n";
  res = funcaoA(a,b);
  cout << "Digite a quantidade de elementos do vetor:\n";
  cin >> n;
  int* vetor = new int(4);                     // [Atenção] veja abaixo
  cout << "Endereco de vetor: " << vetor <<"\n";
  for (int i=0;i<n;i++) {
    cout << "Digite o elemento da posicao " << i << ": \n";
    cin >> vetor[i];
  }
  for (int i=0;i<n;i++) {
    cout << "Vetor[" << i <<"] = " << vetor[i]*res << endl;
  }
  delete vetor;
  return 0;
}
