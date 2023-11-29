import unittest
#Se importa la libreria unittest

from fibo import fibonacci
#Se importa del archivo fibo.py la funcion fibonacci

class CompruebaFibonacci(unittest.TestCase):
#Se crea una clase nueva y se utiliza TestCase para comprobar si se cumple el resultado esperado de la funcion de Fibonacci
    def test_fibonacci(self):
#Se crea una funcion nueva y debe ponerse obligatoriamente al principio 'test' en el nombre de la funcion, porque si no, no realizara ningun test
        self.assertEqual(fibonacci(5), 3)
#Se pone en la funcion fibonacci la posicion 5 y se indica que su resultado debe ser igual a 3

if __name__== '__main__':
    unittest.main()
#Es necesario name = main ya que si no se pone, no ejecutara el test para compararlos