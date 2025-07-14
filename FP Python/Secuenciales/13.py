#Desarrolle el programa que permita calcular la hipotenusa de un triángulo. Usando la clase Math.

import os
import math
os.system("cls")

a = int(input("Ingrese el lado a : "))
b = int(input("Ingrese el lado b : "))

#Formula a2 + b2 = h2

Hipo = math.sqrt(math.pow(a,2) + math.pow(b,2))

print(f"La hipotenusa es {Hipo}.")