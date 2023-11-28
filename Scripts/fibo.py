## La escala de Fibonacci es: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc

def fibonacci(n):
#Se creara una funcion para definir la escala de Fibonacci
    if n < 0:
        print("Valor incorrecto")
#No se admitiran valores menores que 0
    elif n == 0 or n == 1:
        return 0
#Si se pone la posicion 0 o 1, devuelve 0
    elif n == 2 or n == 3:
        return 1
#Si se pone la posicion 2 o 3, devuelve 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#Utilizando la formula matematica de la escala de Fibonacci, se podra averiguar el numero de cada posicion en la secuencia a partir de la posicion 4

print(fibonacci(5))
#Poniendo un numero 5 que se corresponde con la posicion 5 de Fibonacci, nos indicara el numero 3