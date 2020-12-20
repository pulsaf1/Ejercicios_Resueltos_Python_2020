# Ejercicio 2, Capítulo 4. Operadores y Expresiones.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

num1 = input("Introduce un número> ")
num2 = input("Introduce otro> ")

num1 = int(num1)
num2 = int(num2)

suma = num1 + num2
print("La suma es {}", suma)
print(f"La resta es {int(num1 - num2)}")
print(f"La multiplicacion es {num1 * num2}")
print(f"La división es {num1 / num2}")
