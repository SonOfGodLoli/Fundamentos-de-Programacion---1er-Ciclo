# Desarrolle el programa que lea un número entero positivo de tres cifras y determine si las cifras son o no consecutivas (en orden ascendente o descendente). En caso contrario mostrar mensaje.

import os
os.system("cls")

numero = int(input("Numero de 3 cifras : "))

n1 = numero//100
n2 = (numero//10)%10
n3 = numero%10

modo= 0

if n1>n2>n3:
    modo = "consecutiva y descendente"
elif n3>n2>n1:
    modo = "consecutiva y ascendente"
elif numero // 1000 != 0 :
    modo = "numero invalido"
else:
    modo = "no consecutivo"
    
print(f"El numero es {modo}.")