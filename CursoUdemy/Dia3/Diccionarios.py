#Ejemplos de diccionarios
print("\nCreamos un diccionario")
diccionario = {'c1':'valor1', 'c2': 'valor2'}
#print(type(diccionario))
print(diccionario)

print("\nConsultamos un elemento del diccionario")
resultado = diccionario['c1']
print(resultado)

print("\nDiccionario de un cliente")
cliente = {'nombre': 'Juan', 'apellido': 'Perez', 'peso':60, 'altura': 1.80}
consulApellido = cliente['apellido']
print(consulApellido)

#Los diccionarios pueden almacenar listas u otros diccionarios
print("\nAccedemos un elemento de una lista, que esta dentro de un diccionario")
dic = {'c1':88, 'c2':[20,9,57], 'c3':{'s1':100, 's2':200}}
#Si no agregamos un indice de la lista, nos muestra toda la lista
consulta = dic['c2'][2]
print(consulta)

print("\nAccedemos a un elemento del diccionario que esta dentro del diccionario")
#Si no se agrega una clave del otro diccionario, imprime todo el diccionario
consulta = dic['c3']['s1']
print(consulta)

print("\nImprimir la letra 'e' del diccionario en mayusculas")
dic2 = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic2['c2'][1].upper())

#Como agregar elementos a un diccionario ya antes creado
print("\nAgregamos elementos a un diccionario ya creado")
dic3 = {1:'a', 2:'b'}
dic3[3] = 'c'
print(dic3)

#Sobre escribir en un diccionario
print("\nSobre escribimos un valor dentro de un diccionario")
dic3[2] = 'B'
print(dic3)

#Obtener todas las claves del diccionario
print("\nImprimimos todas las claves de un diccionario")
claves = dic3.keys()
print(dic3.keys())
print("\nImprimimos solo los valores de las claves")
print(dic.values())
print("\nImprimimos todo el diccionario")
print(dic.items())

#Crea una función print que devuelva del segundo item de la lista llamada points2
print("\nImprimimos el segundo iteam de la lista points2")
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

