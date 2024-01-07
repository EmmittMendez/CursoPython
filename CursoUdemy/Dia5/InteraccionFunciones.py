#Recreamos el juego de escoger el palito mas corto
from random import *

#Lista inicial
palitos = ['-', '--', '---', '----']

#Funcion que mezca los palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Funcion para hacer intentos
def hacer_intento():
    intento = ''
    
    while intento not in ['1', '2', '3', '4']:
        intento = input("Ingrese un numero del 1 al 4: ")
    
    return int (intento)

#Funcion que verifica el intento 
def verificar_intento(lista, intento):
    #Los intentos del usuario empiezan desde el 1, por eso buscamos en el lugar -1
    if lista[intento - 1] == '-':
        print("Has perdido")
    else:
        print("Te has salvado")
    print(f"Te ha tocado {lista[intento - 1]}")

#Main
palitos_mezclados = mezclar(palitos)
intento = hacer_intento()
verificar_intento(palitos_mezclados, intento)
