#Verifica si las palabras almacenadas en las variables no se encuentran en el texto
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

print("\nVerificamos si 'éxito' y 'tecnología' no se encuentran en el siguiente texto")
print(frase)
mi_bool = not (('éxito' in frase) and ('tecnología' in frase))
diccionario = {True:'Las palabras no se encuentran en el texto', False: 'Alguna de las palabras esta en el texto'}
print(diccionario[mi_bool])