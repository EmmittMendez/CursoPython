#Como seria resolver el ejercicio sin hacer el formateo de cadenas
x = 10
y = 5
print("\nSin formatear cadedenas de texto")
print("Mis numeros son: " + str(x) + " y " + str(y))

#Usando la funcion format
print("Usando la funcion format")
print("Mis numero son: {} y {}".format(x,y))
print("La suma de {} y {}, es {}".format(x,y,x+y))

#Usando la forma para python 3.6 en adelante
color = "rojo"
placas = 12345
print("Python apartir de la version 3.6")
print(f"Mi auto es color {color} y de placas {placas}")