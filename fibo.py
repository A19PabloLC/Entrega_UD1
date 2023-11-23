## La escala de Fibonacci es: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc

def fibona(n):
#Se creara una funcion para definir la escala de Fibonacci

    if n < 0:
        print("Valor incorrecto")
#No se admitiran valores menores que 0
    elif n == 0 or n == 1:
        return 0
#La posicion 0 y 1 son iguales, son 0
    elif n == 2 or n == 3:
        return 1
#La posicion 2 y 3 son iguales, son 1
    else:
        return fibona(n - 1) + fibona(n - 2)
#Utilizando la formula matematica, se podra averiguar el numero de cada posicion en la secuencia a partir de la posicion 4

print(fibona(5))
#Poniendo un numero 5 que se corresponde con la posicion 5 de Fibonacci, nos indicara el numero 3