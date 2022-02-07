import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_com_5_return_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_5_negativo_e_5_return_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (3, 4, 7),
            (1.7, 1.7, 3.4),
            (7, 7, 14),
            (1, 1, 2),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest():
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_nem_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_nem_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(11, '0')


unittest.main(verbosity=2)
