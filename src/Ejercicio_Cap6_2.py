# Ejercicio 2, Capítulo 6. Listas y tuplas.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

lista1=[]
lista2=[]
lista3=[]

print ("Escribe 5 números")

for num in range(0,5):
    num = input()
    lista1.insert(0,num)

print ("Escribe otros 5 numeros")

for num in range(0,5):
    num = input()
    lista2.insert(0,num)

for num in lista1:
    try:
        if lista2.index(num)!=0:
            lista3.insert(0,num)
    except ValueError:
        print(num)

print (lista1)
print (lista2)
print (lista3)