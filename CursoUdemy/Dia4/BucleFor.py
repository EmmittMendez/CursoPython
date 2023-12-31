#Ejemplos del bucle for
print("\nImprimos uno por uno de los elementos de una lista")
lista = ['a', 'b', 'c', 'd']

for letra in lista:
    indice = lista.index(letra) + 1 #Obtenemos el indice de cada iteracion
    print(f"La letra en el indice {indice} es {letra}")
    
#Ejemplo con nombres
print("\nImprimimos los nombres de la lista que empiezan con 'l'")
nombres = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in nombres:
    if nombre.startswith('l'):
        print(f"{nombre} comienza con 'l'")
    else:
        print(f"{nombre} no comienza con 'l'")
        
#Ejemplo 3 
print("\nImprimimos la suma de los elementos del arreglo")
numeros = [1,2,3,4,5]
total = 0
for numero in numeros:
    total = total + numero
print("El valor total del arreglo es:", total)

#Recorremos un string
print("\nRecorremos un string con un for")
palabra = 'python'
for letra in palabra:
    print(letra)
    
#Tambien podemos recorrer las palabras, listas, diccionarios en el for 
print("\nRecorremos una palabra dentro del bucle")
for letra in 'python':
    print(letra)
    
#Imprimos las listas que estan dentro de una lista
print("\nImprimimos los elementos de una lista que contiene otras listas")
for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

#Imprimos los objetos de la lista por seprado
print("\nImprimimos los elementos por separado")
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)    #Imprime el primer elemento de cada lista
    print(b)    #Imprime el segundo elemento de cada lista
    
#Diccionarios con el bucle for
print("\nImprimimos las claves de un diccionario")
diccionario = {'c1': 'a', 'c2': 'b', 'c3':'c'}
for clave in diccionario:
    print(clave)

#Imprimos todo el contenido del diccionario
print("\nImprimimos todo el contenido del diccionario")
for iteam in diccionario.items():
    print(iteam)
    
#Imprimimos solo los valores del diccionario
print("\nImprimimos solo los valores del diccionario")
for valor in diccionario.values():
    print(valor)

#Imprimimos la clave y el valor
print("\nImprimimoa las claves y los valores del diccionario")
for a,b in diccionario.items():
    print("La clave del diccionario es:", a)    #Imprimimos las claves del diccionario
    print("El valor del diccionario es:", b)    #Imprimimos los valores del diccionario


#Realiza la suma de todos los números pares e impares por separado 
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
print("\nSumamos los numeros pares e impares por separado")
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    elif numero % 2 != 0:
        suma_impares = suma_impares + numero

print(f"La suma de los numeros pares es {suma_pares}")
print(f"La suma de los numeros impares es {suma_impares}")


