#Ejemplos de While
print("\nContador de monedas")
monedas = int (input("Ingrese la cantidad de monedas: "))

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("Ya no tengo mas monedas")
    
#Ejemplo 2
print("\nSegundo ejemplo")
letra = 's'
while letra == 's':
    #pass
    letra = input("Ingrese 's' para continuar:  ")
else:
    print("El programa finalizo")
#Palabra reservada pass, sirve para que si no sabemos que poner en un bucle, reserva el espacio y continua

#Ejemplo de la palabra reservada break
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'a':
        break
    print(letra)
#Break corta la ejecucion del bucle

#Ejemplo de la palabra reservada continue
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'a':
        continue
    print(letra)
#Continue interrumple la iteracion actual y regresa al inicio del bucle para continuar con la siguiente

#Imprime los numeros que son multiplos de 5 
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1


