def ordenar_de_mayor_a_menor_burbuja(lista):
    
    n = len(lista)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

entrada_usuario = input("Ingrese una lista de números enteros separados por espacios: ")
mi_lista = [int(x) for x in entrada_usuario.split()]

lista_ordenada = ordenar_de_mayor_a_menor_burbuja(mi_lista)

print("Lista original:", mi_lista)
print("Lista ordenada de mayor a menor:", lista_ordenada)
