/* Regra de aprovação da UNICSUL (Aula 01 p.6–7) — versão IMPERATIVA em C. */
#ifndef SITUACAO_H
#define SITUACAO_H

#define SEM_AF (-1.0)   /* C não tem "valor ausente" para double: usamos um valor impossível (sentinela) */

/* Devolve "APROVADO", "REPROVADO", "REPROVADO POR FALTA", "AF", "APROVADO NA AF" ou "REPROVADO NA AF".
   a1, a2 e af valem de 0 a 5; af = SEM_AF se o aluno não fez a AF; freq em %. */
const char *situacao(double a1, double a2, double af, double freq);

/* Nota mínima na AF para ser aprovado: 6 menos a maior entre A1 e A2. */
double nota_minima_af(double a1, double a2);

#endif
