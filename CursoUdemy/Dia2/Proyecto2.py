#Programa que calcula las comisiones de un vendedor

nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese cuanto ha vendido este mes: "))

comision = round(ventas * 0.13, 2)

print(f"{nombre} la comision que le corresponde este mes es de ${comision}")

