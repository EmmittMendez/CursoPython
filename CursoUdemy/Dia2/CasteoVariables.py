#type obtiene el tipo de dato de una variable
print("\nObtener el tipo de dato de una variable")
num_entero = 35
print(type(num_entero))

#casteo de variables

#Conversion implicita (Python la hace de forma automatica)
print("Casteo de variables implicitas")
num1 = 20
num2 = 30.5

num1 = num1 + num2
print(type(num1))
print(type(num2))

#Conversion explicita
print("Casteo de variables explicitas")
num1 = 5.8
print(num1)
print(type(num1))

num2 = int (num1)
print(num2)
print(type(num2))

#Ejemplo de conversion explicita
print("Ejemplo de conversion explicita")
edad = input("Dime tu edad: ")
print(type(edad))

#se hace el casteo
edad = int (edad)
print(type(edad))

nueva_edad = edad + 1
print(nueva_edad)


