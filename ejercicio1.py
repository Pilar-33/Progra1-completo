
from os import system
system("cls")
"""1 - Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana. No es necesario
ordenar, se puede usar continue y resolver mediante programación estructurada
usando listas.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite. En caso de ser varios, devolverlos todos.
d) Calcular la media geométrica. La media geométrica es la raíz de los productos.
e) Crear una función que permita recorrer las listas en ambos sentidos."""

lista_ingresos = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
#a) Calcular el promedio de ingresos/hora del 20% que más gana. No es necesario
#ordenar, se puede usar continue y resolver mediante programación estructurada
#usando listas.
tamanio = len(lista_ingresos)
porcentaje_personas = 0.20 * tamanio
maximos = []
for ingreso in lista_ingresos:
    if len(maximos) < porcentaje_personas:
        # Si hay menos de 4 elementos en'maximos', añadimos el valor
        maximos += [ingreso]
    else:
        indice_menor = 0
        for i in range(1, 4):
            if maximos[i] < maximos[indice_menor]: # 15 < 10, 33 < 10, 8 < 10
                indice_menor = i
        if ingreso > maximos[indice_menor]:
            maximos[indice_menor] = ingreso


#b) Calcular el promedio de ingresos/hora de todos los respondentes.
suma = 0
for ingreso in lista_ingresos:
    suma += ingreso

promedio = suma / len(lista_ingresos)


#c) Buscar cuál es el valor que más se repite. En caso de ser varios, devolverlos todos.
repetidos = []

for i in range(len(lista_ingresos)):
    num_actual = lista_ingresos[i]
    for j in range(i+1, len(lista_ingresos)):
        if lista_ingresos[j] == num_actual:
            num_actual = lista_ingresos[j]
            repetidos += [num_actual]


# d) Calcular la media geométrica. La media geométrica es la raíz de los productos.
producto = 1
for  i in  lista_ingresos:
    producto *= i
n = len(lista_ingresos)
media_geometrica = producto ** (1/n)

#e) Crear una función que permita recorrer las listas en ambos sentidos.

def recorrer_lista(lista_ingresos: list) -> list:
    """
    Recibe una lista y devuelve una lista con los elementos en orden inverso.
    Args:
    lista_ingresos (list): Lista de números a recorrer.
    
    Returns:
    List: Lista con los elementos en orden ambos sentidos."""
    tamanio = len(lista_ingresos)
    regreso = []

    for i in range(tamanio):
        ida = lista_ingresos

    for i in range(tamanio-1, -1, -1):
        retro = lista_ingresos[i]
        regreso += [retro]
    
    ambos = ida + regreso
    return ambos

ida_vuelta = recorrer_lista(lista_ingresos)
msje = f"a) El promedio de ingresos/hora de todos los respondentes: {maximos}\n"
msje += f"b) El promedio de ingresos por hora es: {promedio} ingresos/hora\n"
msje += f"c)Los valores que más se repiten son: {repetidos}\n"
msje += f"d) La media geométrica es: {media_geometrica:.2f}\n"
msje += f"e) Lista ida y vuelta: {ida_vuelta}"

print(msje)

	
