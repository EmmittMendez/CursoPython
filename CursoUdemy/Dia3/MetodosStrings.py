#Metodo upper
print("\nMetodo para pasar todo en mayusculas")
texto = "Ejemplo de texto para practicar"
resultado = texto.upper()
print(resultado)

print("\nImprimimos solo un caracter en mayusculas")
resultado = texto[2].upper()
print(resultado)

#Metodo lower
print("\nMetodo para pasar todo en minusculas")
texto = "EJEMPLO METODO LOWER"
resultado = texto.lower()
print(resultado)

#Metodo split
print("\nMetodo para separar en una lista")
texto = "Separamos en una lista"
#Si dentro de los parentesis podemos un caracter, toma a ese caracter como separacion
resultado = texto.split() 
print(resultado)

#Metodo join
print("\nMetodo para juntar palabras en un texto")
#El metodo join recibe una lista y esa lista la convierte en un texto, separada por el caracter de text
a = "Estoy"
b = "aprendiendo"
c = "Python"
text= " ".join([a,b,c])
print(text)

#Metodo find
print("\nMetodo para buscar un caracter y mostrar su indice")
#A diferencia del index, este metodo nos regresa un -1 si no encuentra el caracter que se ingreso
texto = "Buscamos algun caracter"
resultado = texto.find("a")
print(resultado)

#Metodo replace
print("\nMetodo para reemplazar caracteres")
#Este metodo puede reemplazar caracteres o palabras completas
resultado = texto.replace("a","x")
print(resultado)

#Ejemplo de replace
print("\nReemplazamos 2 palabras de un texto")
texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = texto.replace("difícil", "fácil")
resultado = resultado.replace("mala", "buena")
print(resultado)



