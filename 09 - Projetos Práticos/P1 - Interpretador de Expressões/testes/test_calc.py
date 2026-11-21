"""Testes do projeto P1. Rode com:  python3 ferramentas/testar_projetos.py P1   (testa a pasta inicial/)"""
import unittest

from calc import executar
from calc.lexico import tokenizar, ErroLexico
from calc.sintatico import analisar, ErroSintatico
from calc.arvore import Num, Var, Unario, Binario, Atribuicao, Imprime
from calc.interpretador import Interpretador, ErroExecucao
from calc.compilador import compilar, desmontar, MaquinaVirtual


def tipos(codigo):
    return [(t.tipo, t.lexema) for t in tokenizar(codigo)]


class Etapa1Lexico(unittest.TestCase):
    def test_comando_simples(self):
        self.assertEqual(tipos("soma = x + 10"),
                         [("ID", "soma"), ("ATRIB", "="), ("ID", "x"), ("OP", "+"), ("NUM", "10"), ("FIM", "")])

    def test_espacos_nao_importam(self):
        self.assertEqual(tipos("soma=x+10"), tipos("soma   =  x +   10"))

    def test_palavra_reservada_e_parenteses(self):
        self.assertEqual(tipos("print (a1)"),
                         [("PRINT", "print"), ("ABRE", "("), ("ID", "a1"), ("FECHA", ")"), ("FIM", "")])

    def test_numero_real_e_operadores(self):
        self.assertEqual(tipos("2.5*3/4-1"),
                         [("NUM", "2.5"), ("OP", "*"), ("NUM", "3"), ("OP", "/"), ("NUM", "4"),
                          ("OP", "-"), ("NUM", "1"), ("FIM", "")])

    def test_linhas_e_comentarios(self):
        toks = tokenizar("x = 1  # comentário\nprint x")
        self.assertEqual([t.tipo for t in toks], ["ID", "ATRIB", "NUM", "FIM_LINHA", "PRINT", "ID", "FIM"])
        self.assertEqual((toks[4].linha, toks[4].coluna), (2, 1))

    def test_identificador_com_sublinhado(self):
        self.assertEqual(tipos("nota_final")[0], ("ID", "nota_final"))

    def test_caractere_invalido(self):
        with self.assertRaises(ErroLexico) as ctx:
            tokenizar("x = 3 @ 4")
        self.assertIn("coluna 7", str(ctx.exception))


class Etapa2Sintatico(unittest.TestCase):
    def arvore(self, codigo):
        return analisar(tokenizar(codigo)).comandos

    def test_atribuicao(self):
        cmd, = self.arvore("x = 2")
        self.assertIsInstance(cmd, Atribuicao)
        self.assertEqual((cmd.nome, cmd.expr.valor), ("x", 2))

    def test_precedencia(self):
        cmd, = self.arvore("print 2 + 3 * 4")
        self.assertIsInstance(cmd, Imprime)
        e = cmd.expr
        self.assertEqual(e.op, "+")                     # o + fica na raiz
        self.assertIsInstance(e.dir, Binario)
        self.assertEqual(e.dir.op, "*")

    def test_associatividade_a_esquerda(self):
        e = self.arvore("print 10 - 3 - 2")[0].expr
        self.assertEqual(e.op, "-")
        self.assertIsInstance(e.esq, Binario)           # (10 - 3) - 2
        self.assertIsInstance(e.dir, Num)

    def test_parenteses_e_unario(self):
        e = self.arvore("print -(a + 1)")[0].expr
        self.assertIsInstance(e, Unario)
        self.assertIsInstance(e.expr, Binario)
        self.assertIsInstance(e.expr.esq, Var)

    def test_linhas_vazias(self):
        self.assertEqual(len(self.arvore("\n\nx = 1\n\nprint x\n")), 2)

    def test_erros(self):
        for codigo in ["print 2 +", "x = (1 + 2", "= 3", "x 3", "print 2 3", "x = * 2"]:
            with self.subTest(codigo=codigo), self.assertRaises(ErroSintatico):
                analisar(tokenizar(codigo))


class Etapa3Interpretador(unittest.TestCase):
    def test_aritmetica(self):
        casos = {"print 2 + 3 * 4": ["14"], "print (2 + 3) * 4": ["20"], "print 10 - 3 - 2": ["5"],
                 "print 8 / 4 / 2": ["1.0"], "print 7 / 2": ["3.5"], "print -2 * -3": ["6"],
                 "print 2.5 * 2": ["5.0"], "print --4": ["4"]}
        for codigo, esperado in casos.items():
            with self.subTest(codigo=codigo):
                self.assertEqual(executar(codigo), esperado)

    def test_variaveis(self):
        self.assertEqual(executar("a1 = 3.5\na2 = 2 + 1.5\nprint a1 + a2\nprint (a1 + a2) / 2"), ["7.0", "3.5"])

    def test_reatribuicao(self):
        self.assertEqual(executar("x = 1\nx = x + 1\nx = x * 10\nprint x"), ["20"])

    def test_memoria_persiste_entre_execucoes(self):
        it = Interpretador()
        it.executar(analisar(tokenizar("x = 4")))
        self.assertEqual(it.executar(analisar(tokenizar("print x * x"))), [16])

    def test_variavel_nao_definida(self):
        with self.assertRaises(ErroExecucao) as ctx:
            executar("x = 1\nprint y + x")
        self.assertIn("y", str(ctx.exception))

    def test_divisao_por_zero(self):
        with self.assertRaises(ErroExecucao):
            executar("x = 10\nprint x / (x - 10)")

    def test_erro_dinamico_so_quando_executa(self):
        # o comando com erro está na linha 2; a linha 1 já foi executada
        it = Interpretador()
        with self.assertRaises(ErroExecucao):
            it.executar(analisar(tokenizar("a = 5\nprint a / 0")))
        self.assertEqual(it.memoria["a"], 5)


class Etapa4Compilador(unittest.TestCase):
    def bytecode(self, codigo):
        return desmontar(compilar(analisar(tokenizar(codigo))))

    def test_bytecode_atribuicao(self):
        self.assertEqual(self.bytecode("x = 2 + 3"), ["PUSH 2", "PUSH 3", "ADD", "STORE x"])

    def test_bytecode_posordem(self):
        self.assertEqual(self.bytecode("print a * (b - 1)"),
                         ["LOAD a", "LOAD b", "PUSH 1", "SUB", "MUL", "PRINT"])

    def test_bytecode_unario(self):
        self.assertEqual(self.bytecode("print -x"), ["LOAD x", "NEG", "PRINT"])

    def test_vm_igual_ao_interpretador(self):
        programas = ["print 2 + 3 * 4", "a = 7\nb = 2\nprint a / b\nprint a - b - 1",
                     "x = 1\nx = x + 1\nprint -x * (x + 10)", "print 1.5 * 4 - 0.5"]
        for p in programas:
            with self.subTest(programa=p):
                self.assertEqual(executar(p, modo="vm"), executar(p))

    def test_vm_pilha_vazia_no_fim(self):
        vm = MaquinaVirtual()
        vm.executar(compilar(analisar(tokenizar("x = 1 + 2 * 3\nprint x"))))
        self.assertEqual(vm.pilha, [])
        self.assertEqual(vm.memoria, {"x": 7})

    def test_vm_erros(self):
        for p in ["print z", "print 1 / 0"]:
            with self.subTest(programa=p), self.assertRaises(ErroExecucao):
                executar(p, modo="vm")


if __name__ == "__main__":
    unittest.main()
