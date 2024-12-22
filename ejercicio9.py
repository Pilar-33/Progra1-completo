from os import system
system("cls")

"""9- Desarrollar una función que permita cargar nuevos valores a una lista cualquiera. Se
debe poder validar el tipo de datos que contiene la lista"""

def validar_lista(lista: list) -> list:
    """
    Valida que la lista sea de tipo lista.
    Args:
    lista (list): Lista a validar.

    Returns:
    list: Devuelve None si no es una lista

    """
    if type(lista) != list:
        print("Error: La lista debe ser de tipo lista.")
        return None
    else:
        return lista

def verificar_tipo(lista: list) -> type:
    """
    Valida que los elementos de la lista sean del mismo tipo.
    Args:
    lista (list): Lista a validar.
    Returns:
    type: Devuelve el tipo de datos que todos los elementos de la lista tienen.
    """
    tipo = type(lista[0])
    for i in lista:
        if tipo != i:
            return None
    return tipo


def cargar_lista(lista: list, valor: any) -> list:
    """
    Carga un nuevo valor a una lista. Valida el tipo de datos de entrada.
    Si el valor es de tipo correcto, lo agrega a la lista, si no, lo ignora.
    Args:
    lista (list): Lista en la que se cargará el nuevo valor.
    valor (any): Valor a cargar en la lista.

    Returns:
    list: Lista con el nuevo valor agregado."""

    dato_nuevo = type(valor)
    rpta = verificar_tipo(lista)

    if rpta is not None:
        if dato_nuevo != rpta:
            print(f"El nuevo dato tipo {dato_nuevo} != {rpta} de la lista")
        else:
            lista += [valor]
            return lista
        
lista = [1, 2, 3, "Hola"]
valida = validar_lista(lista)
if valida is not None:
    print("Lista válida:", valida) 

#cargado = cargar_lista(valida, "hola")
cargado1 = cargar_lista(valida, 12)

if cargado1 is not None:
    print("Nueva lista:", cargado1)
else:
    print("Lo tipos de datos son distintos")


    

