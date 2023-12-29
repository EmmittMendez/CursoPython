#Ejemplos de Tuples, pueden escribirse con o sin parentesis
print("\nImprimimos un tuple")
tuple = (1,2,(10,20),4) #Tuple con otro tuple dentro
print(type(tuple))
print(tuple)

#Podemos agregar elementos y los tuples pueden contener todo tipo de datos
print("\nConsultando los elementos de nustro tuple")
print("Elemento en la posicion 0 es:",tuple[0])
print("Segundo elemento dentro de otro tuple:", tuple[2][1])

#Podemos castear a los tuples
print("\nConvirtiendo nuestro tuple en una lista")
listaT = list (tuple)
print(type(listaT))
print("Imprimimos la lista")
print(listaT)

#Podemos asignar los elementos de un tuple a variables
print("\nAsignamos el contenido de un tuple a variables")
t = (1,2,3)
x,y,z = t
print(x,y,z)

#El metodo count sirve para contar la cantidad de veces que aparece un elemento
print("\nImprimos la cantidad de veces que aparece un elemento en nuestro tuple")
t = (1,2,3,1)
print("El 1 aparece",t.count(1),"veces")
print("El largo de el tuple es", len(t))


#Consultamos en que indice se encuentra algun elemento
print("\nImprimimos en que indice se encuentra el elemento 2")
print("El indice donde se encuentra el 2 es", t.index(2))

