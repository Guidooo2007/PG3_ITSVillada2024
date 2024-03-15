def es_bisiesto(anno):
    
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        return True
    else:
        return False

anno_ingresado = int(input("Ingrese un año: "))

if es_bisiesto(anno_ingresado):
    print(f"{anno_ingresado} es un año bisiesto")
else:
    print(f"{anno_ingresado} no es un año bisiesto")
