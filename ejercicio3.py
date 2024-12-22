

from os import system
system("cls")

"""3- Programar un algoritmo que permita crear una nueva lista de respondentes de manera
secuencial. Deberán ingresar su nombre, sexo, cantidad de horas trabajadas e ingreso
semanal en listas separadas"""

lista_nombre = []
lista_sexo = []
lista_horas = []
sexo = ["m", "f"]

cantidad_empleados = int(input("Ingrese cantidad de empleados: "))
for empleado in range(cantidad_empleados):
    nombres = input(f"Nombre del empleado para la posición {empleado}: ")
    lista_nombre += [nombres]

    sexos = input(f"Sexo del empleado para la posición {empleado} (m/f): ")
    while sexos not in sexo:
        sexos = input(f"Sexo invalido.\nSexo del empleado para la posición {empleado} (m/f): ")
    lista_sexo += [sexos]

    horas = int(input(f"Cantidad de horas trabajadas del empleado para la posición {empleado}: ") )
    while horas < -1:
        horas = int(input(f"Horas invalida.\nCantidad de horas trabajadas del empleado para la posición {empleado}: "))
    lista_horas += [horas]

msje = (
    f"\nNombres de los empleados: {lista_nombre}\n"
    f"Sexos de los empleados: {lista_sexo}\n"
    f"Cantidades de horas trabajadas de los empleados: {lista_horas}"
    )
