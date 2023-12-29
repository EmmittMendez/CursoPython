#Los sets solo admiten elementos unicos y no tienen un orden
print("\nEjemplo de set con un solo parametro")
sett = set([1,2,3,4,5])
print(type(sett))
print(sett)
print("El largo del set es: ", len(sett))

print("\nEjemplo de set con todos sus elementos")
sett2 = {1,2,3}
print(type(sett2))
print(sett2)
print("El largo del set es: ", len(sett2))

#Podemos hacer consultas dentro de nuestros sets
print("\nVerificamos si el 2 se encuentra dentro de nuestro set")
print("El 2 se encuentra en el set? ", 2 in sett)
print("\nVerificamos si el 2 no se encuentra dentro de nuestro set")
print("El 2 no se encuentra en el set? ", 2 not in sett)

#Podemos unir diferentes sets
print("\nUnimos diferentes sets en uno nuevo")
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#Podemos agregar elementos a nuestros sets
print("\nAgregamos un elemento a nuestro set")
s1.add(4)
print(s1)

#Podemos eliminar elementos de nuestros sets
print("\nEliminamos un elemento de nuestro set")
#Tambien podemos usar el discard en lugar del remove
s1.remove(4)
print(s1)

#Podemos sacar un elemento de nuestro set
print("\nSacamos un elemento de nuestro set")
#Por lo general saca el primer elemento
s1.pop()
print(s1)

#Podemos vacia nuestro set
print("\nVaciando todo nuestro set")
s1.clear()
print(s1)


