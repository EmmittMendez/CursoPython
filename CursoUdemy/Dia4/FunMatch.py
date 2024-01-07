#Ejemplo de Match
serie = 'N-02'

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe el producto")

#Ejemplo de Match pero con diccionarios
cliente = {'nombre':'Emmitt',
           'edad': 21,
           'ocupacion': 'Estudiante'}

pelicula = {'titulo': 'Matix',
            'ficha_tecnica': {'protagonista':'Keanu Reeves',
                              'director': 'Lana'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("\nEs un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica':{'protagonista': protagonista,
                               'director': director}}:
            print("\nEs una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("\nNo se lo que es")