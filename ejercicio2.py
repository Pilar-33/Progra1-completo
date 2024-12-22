
from os import system
system("cls")

"""2- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = [“Juan”, “Matias”, “Carla”, “Susana”, “Olivia”, “Carlos”, “Daniel”, “Jimena”,
“Mariela”, “Ignacio”]
a) Devolver el nombre del respondiente más jóven y del más grande.
b) Usando break, busque en la lista si hay mayores de 65. En ese caso cortar la
iteración y mostrar mensaje por pantalla.
c) Utilizando continue, calcule la media etaria para mayores de 40 años"""

lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena",
"Mariela", "Ignacio"]

mas_joven = lista_edad[0]
nombre_joven = lista_nombres[0]

mas_grande = lista_edad[0]
nombre_grande = lista_nombres[0]

# a) Devolver el nombre del respondiente más jóven y del más grande.
for edad in range(len(lista_edad)):
    if lista_edad[edad] < mas_joven:
        mas_joven = lista_edad[edad]
        nombre_joven = lista_nombres[edad]

    if lista_edad[edad] > mas_grande:
        mas_grande = lista_edad[edad]
        nombre_grande = lista_nombres[edad]

#b) Usando break, busque en la lista si hay mayores de 65. En ese caso cortar la
#iteración y mostrar mensaje por pantalla.
mayor_sesenta = lista_edad[0]
nombre_mayor_sesenta = lista_nombres[0]
for mayor in range(len(lista_edad)):
    if lista_edad[mayor] > 65:
        mayor_sesenta = lista_edad[mayor]
        nombre_mayor_sesenta = lista_nombres[mayor]
        break


#c) Utilizando continue, calcule la media etaria para mayores de 40 años
media_mayores = 0
contador = 0

for edad in lista_edad:
    if edad < 40:
        continue
    else:
        media_mayores += edad
        contador += 1
media = media_mayores/contador

msje = (
    f"a) El nombre del respondiente más jóven y del más grande:\n"
    f"MásJoven:\nNombre y edad: {nombre_joven}||{mas_joven} años\n"
    f"Más grande:\nNombre y edad: {nombre_grande}||{mas_grande} años\n"
    )

if mayor_sesenta < 65:
    msje += f"\nb) No hay personas mayores de 65 años.\n"
else:
    msje += (f"\nb) La persona mayor a 65 años es:\n"
        f"NOmbre: {nombre_mayor_sesenta}\n"
        f"Edad: {mayor_sesenta} años\n"
        )
    
msje += f"\nc) La media etaria para mayores de 40 años: {media} años"
print(msje)
