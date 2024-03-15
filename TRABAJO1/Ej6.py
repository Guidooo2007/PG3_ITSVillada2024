def contar_vocales(frase):
    contador_vocales = 0
    vocales = "aeiouAEIOU"
    
    for caracter in frase:
        if caracter in vocales:
            contador_vocales += 1
    
    return contador_vocales

palabra_ingresada= input("Ingrese la palabra:")
resultado=contar_vocales(palabra_ingresada)
cantidad_vocales = contar_vocales(palabra_ingresada)
print(f"La frase {palabra_ingresada} tiene {cantidad_vocales} vocales")



