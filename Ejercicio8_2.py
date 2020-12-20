# Ejercicio 2, Capítulo 8. Funciones.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

from random import randint, uniform, random

def acierta(num = 0):
    num_pensado=input("En que numero estoy pensando? ")
    while (int(num_pensado)!=num):
        if (int(num_pensado)>num): 
            print("El numero es más bajo")
        else: 
            print("El numero es más alto")
        num_pensado=input("En que numero estoy pensando? ")
        
    print("Acertaste!")


numero = randint(0,10)

acierta(numero)
