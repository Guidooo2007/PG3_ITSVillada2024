def es_palindromo(palabra):
    
    palabra = palabra.lower()  
    return palabra == palabra[::-1]

palabra_ingresada = input("Ingrese una palabra: ")

resultado = es_palindromo(palabra_ingresada)

if resultado:
    print(f"{palabra_ingresada} es un palindromo")
else:
    print(f"{palabra_ingresada} no es un palindromo")
