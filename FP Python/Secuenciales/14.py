#Calcule el promedio de los 3 números mayores de 5 números ingresados. Usando la clase Math.

import math
import os
os.system("cls")

a= int(input("ingrese un numero : "))
b= int(input("ingrese un numero : "))
c= int(input("ingrese un numero : "))
d= int(input("ingrese un numero : "))
e= int(input("ingrese un numero : "))

Lista_Num = [a,b,c,d,e]

Lista_ordenada = sorted(Lista_Num)
print(Lista_ordenada[-1:1:-1])

promedio= math.fsum(Lista_ordenada[-1:1:-1]) /3
print(promedio)