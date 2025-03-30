import unittest
from ohce import Ohce

class TestOhce(unittest.TestCase):
    def test_invierte_palabra(self):
        ohce = Ohce("Cristobal")
        resultado = ohce.procesar("Hola")
        self.assertEqual(resultado, "aloH")

if __name__ == '__main__':
    unittest.main()

    def test_mensaje_si_palindromo(self):
        ohce = Ohce("Cristobal")
        resultado = ohce.procesar("reconocer")  # Es un palíndromo
        self.assertIn("¡Bonita palabra!", resultado)
    def test_saludo_según_la_hora(self):
        def hora_falsa():
            return 9  # 9 AM

        ohce = Ohce("Cristobal", hora_actual=hora_falsa)
        saludo = ohce.saludo()
        self.assertEqual(saludo, "¡Buenos días, Cristobal!")
