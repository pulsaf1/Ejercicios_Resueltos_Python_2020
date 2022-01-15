# Ejercicio 1, Capítulo 8. Funciones.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

# Un numero es primo cuando solo es divisible por si mismo y por el 1.
# Versión con un UNICO RETURN en la función y que levanta una excepción si el
# parámetro no es un entero o es un número negativo. 

def esPrimo(x):
    if x < 0:
        raise TypeError("El numero no puede ser negativo") 

    divisores = 1 
    if x >= 2:
        divisores = 0
        num = 2
        while (num < x and divisores == 0):
            if (x % num == 0): divisores+=1
            num += 1
    return (divisores == 0)    

