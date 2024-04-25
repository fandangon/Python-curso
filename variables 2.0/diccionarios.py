#Creando diccionarios con dict()
diccionario = dict(nombre="Jorge", apellido="Garofalo")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Jorge", "Garofalo"]):"jajaja"}

#Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])
#Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")



print(diccionario)