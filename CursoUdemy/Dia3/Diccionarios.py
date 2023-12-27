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
print("\nHacemos un diccionario con difereentes tipos de datos")
dic = {'c1':88, 'c2':[20,9,57], 'c3':{'s1':100, 's2':200}}
consulta = dic['c1']