#Una  institución  social  recibe  anualmente  una  donación  que  reparte  de  la  siguiente  forma:  25% para el centro de salud, 35% en el comedor infantil, 25% para la escuela infantil y el resto para el asilo de ancianos.  Desarrolle el programa que muestre los montos asignados.

import os
os.system("cls")

Donacion = int(input("Ingrese el monto de la donacion : "))

salud = (Donacion/100) * 25
comedor = (Donacion/100) * 35
escuela = (Donacion/100) * 25
anciano = (Donacion/100) * 15

print(f"Dinero destinado a Salud : {salud:.2f} soles.")
print("Dinero destinado a Comedor : ",comedor, " soles.")
print(f"Dinero destinado a Escuela : {escuela:.2f} soles.")
print(f"Dinero destinado a Ancianos : {anciano:.2f} soles.")