// Gerado automaticamente a partir de 04 - Provas e Avaliações/Simulados/resolucao-simulado-02.md (linha 144).
// Seção: 15
// Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
// Como executar:  python3 ferramentas/rodar.py codigo/simulados/resolucao-02/05-15.c
// Entrada de exemplo: 7 8 9
// A saída deve conter: 8.0 | Aprovado

#include <stdio.h>

float media(float n1, float n2, float n3) {          /* uma responsabilidade: calcular */
    return (n1 + n2 + n3) / 3;
}

const char *situacao(float m) {                      /* uma responsabilidade: classificar */
    if (m >= 6) return "Aprovado";
    if (m >= 4) return "Exame";
    return "Reprovado";
}

int main(void) {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    float m = media(a, b, c);
    printf("Media: %.1f\nSituacao: %s\n", m, situacao(m));
    return 0;
}
