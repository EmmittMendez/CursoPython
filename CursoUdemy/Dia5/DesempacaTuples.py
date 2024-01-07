#Ejemplo de una funcion que desempaca tuples
print("\nPrograma que imprime cual es la cafe mas caro de una lista de cafes")
precios_cafe = [('Capuchino', 1.5),('Expreso', 1.2),('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ' '
    
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
        
    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es el {cafe} con un precio de {precio}")








