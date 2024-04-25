animales = ["perro","gato","loro","cocodrilo"]
numeros = [1,2,3,4]

#Recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#Recorriendo la lista numeros y multiplicamos por 10    
for numero in numeros:
    resultado = numero * 10
    print(f'Ahora la variable numero es igual a: {numero} pero esos numeros multiplicados por 10 es igual a: {resultado}')
    
#Iterando 2 lista del mismo tamaño al mismo tiempo con zip()
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

#forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#Usando el for/else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')

#Todo lo anterior funciona exactamente igual para tuplas y conjuntos
