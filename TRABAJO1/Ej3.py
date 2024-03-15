def dibujar_rectangulo(ancho, alto, caracter):
    
    for i in range(alto):
        fila = [caracter] * ancho
        print(" ".join(fila))

ancho_rectangulo = int(input("Ingrese el ancho del rectangulo: "))
alto_rectangulo = int(input("Ingrese el alto del rectangulo: "))
caracter = input("Ingrese el caracter para dibujar el rectangulo: ")

dibujar_rectangulo(ancho_rectangulo, alto_rectangulo, caracter)

