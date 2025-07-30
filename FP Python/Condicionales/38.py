# Desarrolle  el  programa  que  determine  la  cantidad  de  días  y  el  nombre  del  mes  conociendo  los valores numéricos del mes y del año. Un año es bisiesto si es divisible por 4 y no es divisible por 100, o no es divisible por 400.

import os
os.system("cls")

mes = int (input ("ingrese el numero de mes (1 al 12) : "))
año = int (input ("ingrese el numero del año : "))

if mes == 1:
    dias = 31
    nombre = "Enero"
elif mes == 2:
    nombre= "Febrero"
    dias = 29 if (año%4 == 0 and año%100!=0) or año%400==0 or (año%4==0 and año%100==0 and año%400==0) else 28
elif mes == 3:
    dias = 31
    nombre = "Marzo"
elif mes == 4:
    dias = 30
    nombre = "Abril"
elif mes == 5:
    dias = 31
    nombre = "Mayo"
elif mes == 6:
    dias = 30
    nombre = "Junio"
elif mes == 7:
    dias = 31
    nombre = "Julio"
elif mes == 8:
    dias = 31
    nombre = "Agosto"
elif mes == 9:
    dias = 30
    nombre = "Septiembre"
elif mes == 10:
    dias = 31
    nombre = "Octubre"
elif mes == 11:
    dias = 30
    nombre = "Noviembre"
elif mes == 12:
    dias = 31
    nombre = "Diciembre"
    
print (f"El mes es {nombre} y tiene {dias}")
    