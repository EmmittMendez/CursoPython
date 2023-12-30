#Proyecto que recibe un texto y busca caracteres
print("\nPrograma que recibe un texto")
texto = input("Ingrese un texto:\n")
mTexto = texto.lower()  #Convertimos todo a minusculas

#letras a analizar
let1= input("Ingrese la primera letra a analizar\n")
mLet1 = let1.lower()
let2 = input("Ingrese la segunda letra a analizar\n")
mLet2 = let2.lower()
let3 = input("Ingrese la tercera letra a analizar\n")
mLet3 = let3.lower()

#Mostramos cuantas veces aparecen las letras en el texto
print("La letra", mLet1, "aparece",mTexto.count(mLet1))
print("La letra", mLet2, "aparece",mTexto.count(mLet2))
print("La letra", mLet3, "aparece",mTexto.count(mLet3))

#Mostramos cuantas palabras hay en el texto
lTexto = mTexto.split() #Convertimos el texto en una lista
cPalabras = len(lTexto)
print("\nLa cantidad de palabras totales en el texto es de:", cPalabras)

#Buscamos cual es la primera y la ultima letra del texto
char1 = texto[0]
char2 = texto[-1]
print("\nEl primer caracter del texto es:", char1)
print("El ultimo caracter del texto es:", char2)

#Invertimos el texto ingresado
print("\nInvertimos las palabras de nuestro texto")
listTexto = texto.split()
listTexto.reverse()
rTexto = " ".join(listTexto)
print(rTexto)

#Verificamos si existe la palabra Python en el texto
print('\nVerificamos si la palabra "Python" se encuentra en el texto')
valor = str("Python" in texto)
diccionario = {'True': 'La palabra Python se encuentra en el texto', 'False': 'La palabra Python no se encuentra en el texto'}
resultado = diccionario[valor]
print(resultado)


