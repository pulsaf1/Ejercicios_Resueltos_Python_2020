lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]

diccionario = {}

for i in lista:
    try:
        diccionario[i] += 1        
    except KeyError:
        diccionario[i] = 1

#for i in lista:
#    diccionario[i] += 1
    
print(diccionario)

