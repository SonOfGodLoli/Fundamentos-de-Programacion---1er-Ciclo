# Desarrolle el programa que lea tres números enteros y determine el número intermedio. No use operadores lógicos en la solución.

import os
os.system("cls")

a = int(input(" ingrese el primer numero : "))
b = int(input(" ingrese el segundo numero : "))
c = int(input(" ingrese el tercer numero : "))

mayor = max(a,b,c)
menor = min(a,b,c)

intermedio = a

if mayor == intermedio: 
    intermedio = b
if menor == intermedio:
    intermedio = c
if mayor == intermedio:
    intermedio = b
    

print (f" El numero intermedio es {intermedio} ")

#forma larga
# if a>b>c:
#     intermedio = b
# if b>a>c:
#     intermedio = a
# if a>c>b:
#     intermedio = c
# if c>a>b:
#     intermedio = a
# if b>c>a:
#     intermedio = c
# if c>b>a:
#     intermedio = b

