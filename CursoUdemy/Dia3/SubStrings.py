#Extraemos la primera palabra de la frase utilizando slicing
print("\nExtraemos palabras usando slicing")
frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase [:9]
print(fragmento)

print("\nToma cada tercer caracter empezando desde el noveno hasta el final de la frase")
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8: :3]
print(fragmento)

print("\nInvierte la posición de todos los caracteres")
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[ : :-1]
print(fragmento)