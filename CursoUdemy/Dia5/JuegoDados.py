from random import *
#Juego de dados 
#Funcion que lanza los dados
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    
    return(dado1, dado2)

#Funcion que evalua el resultado
def evaluar_jugada(dado1, dado2):
    mensaje = ''
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return mensaje

#Main
print("\nJuego de dados")
dado1, dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1, dado2)
print(resultado)