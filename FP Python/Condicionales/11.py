#Desarrolle el programa que determine el signo de un número entre positivo, negativo y cero.

import os
os.system("cls")

Num = float(input("Ingrese un numero: "))

if Num == 0:
    print("El numero es igual a 0")

elif Num > 0:
    print("El numero es positivo")

else:
    print("El numero es negativo")

print("positivo") if Num > 0 else print("cero") if Num == 0 else print("negativo")