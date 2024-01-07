#Ejemplo de funciones dinamicas
print("\nFuncion que verifica si tenemos un numero de 3 cifras")
def verificar(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = verificar([50, 89, 800])
print(resultado)

print("\nFuncion que almacena todos los numeros de 3 cifras")
def verificarCifras(lista):
    arreglo = []
    for numero in lista:
        if numero in range(100,1000):
            arreglo.append(numero)
        else:
            pass
    
    return arreglo

resultado = verificarCifras([598, 89, 800])
print(resultado)

#Ejemplo 2
print("\nFuncion que suma los numeros de una lista que esten entre 0 y 1000")
lista_numeros = [34, 6450, 87, -10, 9, -67]
def suma_menores(lista):
    suma = 0
    for elemento in lista:
        if elemento in range(0, 1000):
            suma = suma + elemento
    return suma

resultado = suma_menores(lista_numeros)
print(resultado)

#Ejemplo 3
lista_numeros = [23, 4, 56, 7, 17, 8]
print("\nFuncion que imprime la cantidad de numeros pares de una lista")
def cantidad_pares(lista):
    pares = 0
    for elemento in lista:
        if elemento%2 == 0:
            pares += 1
    return pares
resultado = cantidad_pares(lista_numeros)
print(f"La cantidad de numeros pares en la lista es de {resultado}")





