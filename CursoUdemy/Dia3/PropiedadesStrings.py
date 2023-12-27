#Inmutabilidad: Los strings no pueden ser cambiados
'''
#esto no se puede hacer
nombre = "Carina"
nombre[0] = "K"
print(nombre)
'''
#Esta es la forma correcta
print("\nCambiamos el contenido de la variable, pero no del string")
nombre = "Carina"
nombre = "Karina"
print(nombre)

#Concatenacion
print("\nConcatenacion")
n1 = "Kari"
n2 = "na"
print(n1+n2)

#Multiplicidad
print("\nMultiplicidad")
n1 = "Kari"
n2 = "na"
print(n1*3)

#Multilineales
print("\nMultilinealidad")
texto = """Mil pequeños peces blancos
como si hierviera
el color del agua""" 
print(texto)

#Buscar subStrings
print("\nBuscamos una subcadena")
#Buscamos si existe la palabra agua en el texto y si existe regresa "True or False"
print("agua" in texto)
#Tambien podemos buscar si una palabra no esta en el strin y regresa "True or False"
print("agua" not in texto)

#Largo de una cadena
print("\nImprimimos la longitud de una cadena")
print(len(texto))

