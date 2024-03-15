def es_numero_step(numero):
    str_numero = str(numero)
    
    for i in range(len(str_numero) - 1):
        if abs(int(str_numero[i]) - int(str_numero[i + 1])) != 1:
            return False
    
    return True

numero_ingresado = input("Ingrese un numero para verificar si es un numero step: ")

try:
    numero_ingresado = int(numero_ingresado)
    resultado = es_numero_step(numero_ingresado)
    print(f"¿{numero_ingresado} es un numero step? {resultado}")
except ValueError:
    print("Por favor ingrese un numero valido")


