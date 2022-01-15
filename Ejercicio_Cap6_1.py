# Ejercicio 1, Capítulo 6. Listas y tuplas.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

lista = [12, 23, 5, 29, 92, 64]

#Elimina el último número y añádelo al principio.
lastNum = lista[len(lista)-1]
lista.pop(len(lista)-1)
lista.insert(0, lastNum)
print(lista)

#Mueve el segundo elemento a la última posición.
lista.append(lista[1])
lista.pop(1)
print(lista)

#Añade el número 14 al comienzo de la lista.
lista.insert(0, 14)
print(lista)

#Suma todos los números de la lista y añade el resultado al final de la lista.
sum = 0
for i in lista:
    sum = sum + i
lista.append(sum)
print(lista)

#Fusiona la lista actual con la siguiente: [4, 11, 32]
lista.extend([4, 11, 32])
print(lista)

#Elimina todos los números impares de la lista.

lista2 = lista.copy()
for i in lista2:
    if i % 2 != 0:
        lista.remove(i)
print(lista)

#Ordena los números de la lista de forma ascendente.
lista.sort()
print(lista)

#Vacía la lista.
lista.clear()
print(lista)