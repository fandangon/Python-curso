#Creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","mandarina","durazno"]
cadena = "Hola Mundo"
numeros = [2,5,8,10]

#saltearse un elemento con continue(Recorre el bucle, cuando llega a pera no lo muestra y continua)
for fruta in frutas:
    if fruta == 'pera':
        continue
    print(f'Me voy a comer una {fruta}')

#Evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'ciruela':
        break
#Esto no se ejecutará nunca
else:
    print('Terminado')
#--------- Aqui el codigo se vuelve a ejecutar ya que no esta en la misma sentencia -------------------   
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
