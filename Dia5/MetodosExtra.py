#Metodo lstrip() 
'''Retorna una copia de la cadena, eliminado determinados caracteres 
si se encuentren al principio'''

print('\nUsamos la lstrip para quitar los simbolos de la izquierda de nuestro texto')
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:_#%')
print(texto)

#Metodo insert
'Inserta un nuevo elemento en el arreglo, en la posicion que nosotros designemos'

print("\nInsertamos un elemento en la posicion 4 de nuestro arreglo")
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)

#Metodo isdisjoint
''' Verifica si dos conjuntos(listas) no tienen ningun elemento en comun'''
print("\nVerificamos si 2 listas tienen algun elemento en comun")
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)







