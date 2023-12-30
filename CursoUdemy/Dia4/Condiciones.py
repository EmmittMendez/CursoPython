#Ejemplos de condiciones (if, else, elif)
print("\nVamos a verificar que tipo de mascota tienes")
mascota = input("Ingrese su mascota: ").lower()

if mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
elif mascota == 'pez':
    print("Tienes un pez")
else:
    print("No se que mascota tienes")
    
#Condiciones anidadas
print("\nVamos a verificar su edad")
edad = int (input("Ingresa tu edad: "))

if edad < 18:
    print("Eres menor de edad")
    calificacion = int(input("Ingrese su calificacion: "))
    if calificacion > 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Eres mayor de edad")

#Verificamos los diferentes numeros ingresados
print("\nVerificador de numeros")
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")

#Verificamos si una persona puede conducir
print("\nVamos a verificar si una persona puede conducir")
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad >= 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")
    
#Verificamos si los candidatos a un trabajo cumplen con los requisitos
habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python== False: 
    print("Para postularte, necesitas saber programar en Python")