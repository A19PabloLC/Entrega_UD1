import unittest
#Se importa la libreria unittest

from fibo import fibonacci
#Se importa del archivo fibo.py la funcion fibonacci

class TestMain(unittest.TestCase):
    def comprobar_fibo(self):
        self.assertEqual(fibonacci(5),3)
#Se pone en fibonacci la posicion 5 y se indica que su resultado debe ser igual a 3

if __name__== '__main__':
    unittest.main()

#Es necesario name = main puesto que si no, no ejecutara el test para compararlos