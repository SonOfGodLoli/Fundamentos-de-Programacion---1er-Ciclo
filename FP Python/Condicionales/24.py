# Una empresa paga a sus vendedores un sueldo igual al 10% del monto total vendido más S/. 25 por cada S/. 500 de venta en exceso sobre S/. 5000. Desarrolle el programa que permita calcular el sueldo de un vendedor.

import os
os.system("cls")

Tventas = int(input("Ingrese el total vendido : "))

Sueldo = Tventas * 0.10 + ( 25 * ((Tventas-5000)//500) if Tventas>5000 else 25 * 0 ) 

print (f"El sueldo es : {Sueldo}")