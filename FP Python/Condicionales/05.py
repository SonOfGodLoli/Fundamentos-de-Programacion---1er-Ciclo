# Desarrolle el programa que, dado un número de 4 cifras, forme el mayor número posible de dos cifras usando la mayor y menor cifra del número ingresado.

import os
os.system("cls")

numero = int(input ("Ingrese un numero de 4 cifras : "))

n1 = numero // 1000
n2 = (numero //100)%10
n3 = (numero % 100)//10
n4 = numero % 10

n_alto = 0

if n1>n2:
    n_alto = n1
else:
    n_alto = n2
    
if n_alto<n3:
    n_alto = n3

if n_alto < n4:
    n_alto = n4

n_bajo = 0

if n1>n2:
    n_bajo = n2
else:
    n_bajo = n1

if n_bajo>n3:
    n_bajo = n3

if n_bajo>n4:
    n_bajo = n4
    
numero_n = (n_alto*10) + n_bajo

print(f"el numero de 2 cifras es : {numero_n}")