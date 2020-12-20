# Ejercicio 1, Capítulo 7. Diccionarios.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64,23]
diccionario = {}

for num in range(0,len(lista)):
    diccionario[lista[num]]=0

for num in range(0,len(lista)):
    diccionario[lista[num]]+=1

print(diccionario)   