#Adivinador de numero
from random import *

intentos = 0
numero = 0
usuario = input("\nIngrese su nombre: ")

print(f"Hola {usuario} he pensado un numero entre 1 y 100, tienes 8 intentos para adivinar que numero es")
aleatorio = randint(1,100)

while intentos < 8:    
    numero  = int (input("Ingrese un numero: "))
    if numero < 1 and numero > 100:
        print("El numero elegido no esta permitido")     
        intentos += 1
        print(f"Intento actual: {intentos}")
    else:
        if numero < aleatorio:
            print(f"El numero aleatorio es: {aleatorio}")
            intentos += 1
            print("¡INCORRECTO! El numero que ha elegido es menor al numero secreto")
            print(f"Intento actual: {intentos}")
        elif numero > aleatorio:
            intentos += 1
            print("¡INCORRECTO! El numero que ha elegido es mayor al numero secreto")
            print(f"Intento actual: {intentos}")          
        elif numero == aleatorio:
            intentos += 1
            print("¡CORRECTO! Ha encontrado el numero secreto")
            print(f"Te ha tomado {intentos} intentos")
            break
else:
    print(f"Agotaste los intentos. No has podido adivinar el numero secreto, el numero secreto era {aleatorio}")






