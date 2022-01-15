# Ejercicio 2, Capítulo 5. Estructuras de Control
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

num1 = input("Introduce un numero> ")
num2 = input("Introduce otro> ")

sum = 0
for num in range(int(num1),int(num2)+1):
    sum += num

print("El resultado es: ", sum)