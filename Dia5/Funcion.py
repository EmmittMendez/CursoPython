#Ejemplos de funciones
nombre_persona = "Emmitt"
print("\nFuncion que imprime el nombre de una persona") 
def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')
#Invocacion
bienvenida(nombre_persona)

#Segundo ejemplo
un_numero = 2
print("\nFuncion que imprime el cuadrado de un numero")
def cuadrado(un_numero):
    resultado = un_numero**2
    print(resultado)
#Invocacion
cuadrado(un_numero)

#Tercer ejemplo
print("\nFuncion que eleva un numero a alguna potencia")
num1 = 5
num2 = 2
def potencia(primer_argumento, segundo_argumento):
    resultado = primer_argumento ** segundo_argumento
    return resultado
#Invocacion
resultado = potencia(num1, num2)
print(resultado)

#Ejemplo 3
print("\nFuncion que hace la conversion de dolares a euros")
dolares = 10
def usd_a_eur(dolares):
    euros = dolares*0.90
    return euros
#Invocacion
euros = usd_a_eur(dolares)
print(euros)

#Ejemplo 4
print("\nFuncion que invierte una palabra y la pone en mayusculas")
palabra = "Python"
def invertir_palabra(palabra):
    letras = [letra for letra in palabra]   #Usando compresion de listas
    letras.reverse()
    texto = "".join(letras)
    return texto.upper()
""" tambien se puede hacer la funcion asi
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra
"""
#Invocacion
inversa = invertir_palabra(palabra)
print(f"La palabra original era '{palabra}' y el resultado es '{inversa}'")

    
    
    





