#Cual es el funcionamiento de la funcion index
print("\nBusqueda de un caracter en base al indice positivo")
texto = "Esta es una prueba"
resultado = texto[5]
print(f'El caracter es: "{resultado}"')

print("\nBusqueda de un caracter en base al indice negativo")
resultado = texto[-5]
print(f'El caracter es: "{resultado}"')

print("\nBuscando el indice en el que se encuentra un caracter")
resultado = texto.index("p")
print(f'El indice es: "{resultado}"')

#Si buscamos una palabra, nos devuelve desde donde comienza esa palabra
print("\nBuscando el indice de donde comienza una palabra")
resultado = texto.index("prueba")
print(f'El primer indice de la palabra es: "{resultado}"')

#Buscamos las palabras desde un indice hasta otro
print("\nBuscamos un caracter desde el indice 5, hasta el 11")
resultado = texto.index("a",5,11)
print(f'El valor del indice es: "{resultado}"')

#Este metodo busca de derecha a izquierda y la regresa con el indice de izquierda a derecha (positivo)
print("\nBuscamos con el metodo rindex")
resultado = texto.rindex("a")
print(f'El valor del indice es: "{resultado}"')

#Encuentra y muestra en pantalla qué caracter ocupa la quinta posición
print("\nMuestra en pantalla que caracter ocupa la 5ta posicion")
palabra = "ordenador"
resultado = palabra[4]
print(resultado)

#Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica"
print("\nMuestra en pantalla el indice de la primera aparicion de la palabra práctica")
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)

#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica"
print("\nMuestra en pantalla el indice de la ultima aparicion de la palabra práctica")
resultado = frase.rindex("práctica")
print(resultado)
