animales = {"perro","gato","loro","cocodrilo"}
numeros = {1,2,3,4}

#Recorriendo la conjunto animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#Recorriendo la conjunto numeros y multiplicamos por 10    
for numero in numeros:
    resultado = numero * 10
    print(f'Ahora la variable numero es igual a: {numero} pero esos numeros multiplicados por 10 es igual a: {resultado}')
    
#Iterando 2 conjunto del mismo tamaño al mismo tiempo con zip()
for numero,animal in zip(animales,numeros):
    print(f'recorriendo conjunto 1: {numero}')
    print(f'recorriendo conjunto 2: {animal}')
    
#Forma correcta de recorrer una conjunto con su indeica
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#Usando el for/else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')

#Todo lo anterior funciona exactamente igual para tuplas y listas
