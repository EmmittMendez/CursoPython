#Ejemplos de listas
print("\nTipos de listas")
listaStr = ["a", "b", "c"]
lista = ["a", 6, 9.8]

print(type(listaStr))
print(type(lista))

print("\nLongitud de listas")
resultado = len(lista)
print(resultado)

#Para acceder a los elemetos de una lista, funciona similar a los strings
print("\n Accedemos a un elemeto de la lista")
resultado = lista[0]
print(resultado)
print("\nAccedemos a 2 elementos de la lista")
resultado = lista[0:2]
print(resultado)

#Concatenacion de las listas
print("\n Concatenacion de las listas")
listaStr = ["a", "b", "c"]
lista = ["d", "e", "f"]

#Union de listas en una nueva lista
lista2 = listaStr + lista
print(listaStr + lista)
print("\nUnimos las 2 listas en una lista nueva")
print(lista2)

#Agregar elementos a una lista
print("\nAgregamos un nuevo elemento a una lista")
lista2.append("g")
print(lista2)

#Usamos pop, para sacar el ultimo elemento de la lista a menos que se le asigne un valor
print("\nSacamos el ultimo elemento de la lista")
lista2.pop()
#lista2.pop(3)
print(lista2)

#Se pueden guardar los elementos sacados con el pop
print("\nSacamos un elemento y guadamos ese elemnto")
elemento = lista2.pop()
print(lista2)
print(elemento)

#Ordenamos listas con el metodo sort
print("\nImprimimos una nueva lista ordenada, no importa si son numeros o letras")
lista3 = ['a', 'f', 'z', 'b', 'g']
lista3.sort()
print(lista3)

#Cambiamos el orden de la lista (la pone al reves)
print("\nPonemos la lista al reves")
#lista3 = ['a', 'f', 'z', 'b', 'g']
lista3.reverse()
print(lista3)