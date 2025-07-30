# Desarrolle el programa que lea tres números a, b, c y determine si los números fueron ingresados en orden ascendente, descendente o en desorden.

import os
os.system("cls")

n1 = int (input ( "Ingrese el primer numero : "))
n2 = int (input ( "Ingrese el segundo numero : "))
n3 = int (input ( "Ingrese el tercer numero : "))


ingreso = "desorden"
if n1>n2>n3:
    ingreso = "descendente"
if n1<n2<n3:
    ingreso = "ascendente"
    
print (f"Los numero fueron ingresados en {ingreso}.")