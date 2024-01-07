#Programa que eliminar elementos de una lista y calcular su promedio

#Funcion que elimina elementos duplicados y el valor maximo de una lista
def reducir_lista(lista):
    lista_numeros = []
    mayor = max(lista)
    for elemento in lista:
        if elemento not in lista_numeros and elemento < mayor:
            lista_numeros.append(elemento)
        else:
            pass
    return lista_numeros

#Funcion que realiza el promedio de una lista
def promedio(lista):
    tamano = len(lista)
    sumatoria = 0
    
    for elemento in lista:
        sumatoria += elemento
        
    promedio = sumatoria / tamano
    return promedio

print("\nEliminamos los elementos repetidos y el valor maximo de la lista")            
lista_numeros = [1,2,1,15,7,2]
lista = reducir_lista(lista_numeros)
print(lista)
promedioF = round(promedio(lista), 1)
print(f"El promedio de la lista es {promedioF}")





