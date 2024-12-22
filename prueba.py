from os import system
system("cls")
lista_nombres = ["Maria", "Juan", "Pedro", "Ana", "Luis", "Carlos", "Laura", "Sofia"]
#lista_nombres = "mirtga"
posicion = 7
nuevo_dato = "Miriam"
def validar_lista(lista_nombres: list) -> list:
    """
    Valida que el dato ingresado sea una lista.
    Si no lo es, imprime un mensaje de error y retorna None.
    
    Args:
    lista_nombres (list): Lista para validar
    
    Returns:
    list: La lista validada o None en caso de error"""

    if type(lista_nombres) != list:
        print("El dato ingresado no es una lista")
        return None
    else:
        return lista_nombres

prueba = validar_lista(lista_nombres)
print(prueba)

if prueba is not None:
    if posicion >= len(prueba):
        print("El indice no existe")
    else:
        prueba[posicion] = nuevo_dato
        print(prueba)
