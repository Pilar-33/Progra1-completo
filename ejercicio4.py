from os import system
system("cls")

#Desarrollar una función que calcule la media de ingresos por cuartil.

lista_numeros = [95, 3, 55, 4, 6, 9, 13, 12, 10, 99,
                33, 22, 53, 44, 67, 69, 34, 19, 86, 100]

def validar_lista(lista_numeros: list) -> list:
    """Valida si el elemento es una lista
    Args:
    lista_numeros(list): Es el elemento a verficar si es una lista
    
    Returns:
    list: Devuelve una lista si se verifica sino devuelve None
    """
    if type(lista_numeros)!= list:
        print("Error: La lista debe ser de tipo lista.")
        return None
    else:
        return lista_numeros

# Paso 1: Ordenar la lista de números
def ordenar_lista(lista_numeros: list) -> list:
    """Ordena una lista
    Args:
    lista_numeros(list): Lista a ordenar

    Returns:
    list: Devuelve lista ordena
    """
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[i] > lista_numeros[j]:
                temp = lista_numeros[i]
                lista_numeros[i] = lista_numeros[j]
                lista_numeros[j] = temp
    return lista_numeros

def calcular_media_cuartil(lista_numeros: list) -> list:
    cuartiles = []
    medias = []
    # Paso 2: Definir el tamaño de cada cuartil
    tam_cuartil = len(lista_numeros) // 4

    # Mostrar los elementos de cada cuartil y calcular la media
    for i in range(4):
        cuartil_inicial = i * tam_cuartil
        cuartil_final = (i + 1) * tam_cuartil

        # Para el último cuartil, incluir el resto de la lista
        if i == 3:
            cuartil_final = len(lista_numeros)

        # Extraer los elementos del cuartil sin usar los dos puntos
        cuartil = []
        for j in range(cuartil_inicial, cuartil_final):
            cuartil += [lista_numeros[j]]
        
        # Calcular la media del cuartil
        suma_cuartil = 0
        for num in cuartil:
            suma_cuartil += num
        media_cuartil = suma_cuartil / len(cuartil)

        cuartiles += [cuartil]
        medias += [media_cuartil]

        respuesta = [cuartiles, medias]
    return respuesta
    
valida = validar_lista(lista_numeros)
print(f"Lista desordenada: {lista_numeros}")
ordena = ordenar_lista(lista_numeros)
print(f"Lista ordenada: {ordena}")
resultados = calcular_media_cuartil(ordena)
cuartiles = resultados[0]
medias = resultados[1]

for i in range(len(cuartiles)):
    print(f"Cuartil {i+1}: {cuartiles[i]}")
    print(f"Media del cuartil {i+1}: {medias[i]}")
    print()
