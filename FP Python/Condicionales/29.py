# Una empresa calcula el sueldo bruto de sus trabajadores en base a las horas trabajadas. Hasta 48 horas, se paga una tarifa horaria normal. Para las horas extras se paga un recargo del 20%. Por otro lado, si el sueldo bruto es superior a S/. 1500 se aplica un descuento del 11%. Desarrolle el programa que muestre las horas trabajadas, el pago por hora, el sueldo bruto, el descuento y el total a pagar por la empresa a sus trabajadores.

import os
os.system("cls")
#sueldo bruto que incluye el 20% a las horas extra totales
horasT = int (input("Ingrese las horas trabajadas : "))
precioh = float (input ( "Ingrese su precio por hora : "))

sueldob = horasT*precioh 
if horasT>48:
    sueldob = (precioh*48) + ((horasT-48) * (precioh*1.2))

descuento = 0
if sueldob>1500:
    descuento = sueldob*0.11

print(f" Horas trabajadas : {horasT} horas.")
print(f" Pago por hora : {precioh:.2f} soles.")
print(f" sueldo bruto : {sueldob:.2f} soles.")
print(f"El descuento es de {descuento:.2f} soles.")
print(f"total a pagar {sueldob-descuento:.2f} soles.")