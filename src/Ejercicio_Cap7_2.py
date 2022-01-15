# Ejercicio 2, Capítulo 7. Diccionarios.
# Del libro Aprendiendo Python desde 0. Jon Vadillo. 2020
# Autor. Gregorio Coronado Morón.
# Fecha. 12-2020

diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,
'Maite': 5}


lista = []

for key in diccionario:
    try:
        lista.index(diccionario[key])      
    except ValueError:
        lista.insert(0,diccionario[key])
        
print(lista)