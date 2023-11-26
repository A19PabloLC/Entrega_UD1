import unittest
#Se importa la libreria unittest

from fibo import fibonacci
#Se importa del archivo fibo.py la funcion fibona

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(fibonacci(5),3)
#Se pone en fibona la posicion 5 y se indica que su resultado debe ser igual a 3

if __name__== '__main__':
    unittest.main()

#Una vez hecho