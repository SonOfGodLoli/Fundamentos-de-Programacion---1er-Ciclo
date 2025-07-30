#  Una empresa inmobiliaria ofrece casas bajo las siguientes condiciones: si el ingreso mensual del  comprador es menos de S/. 1250, la cuota inicial será igual al 15% del costo de la casa y el resto se distribuirá en 120 cuotas mensuales; pero si el ingreso mensual es mayor o igual a S/. 1250, la cuota inicial será del 30% del costo de la casa y el resto en 75 cuotas mensuales.  Desarrolle el programa que muestre la cuota inicial y el monto de la cuota mensual. 

import os
os.system("cls")

ingreso = int ( input ( "Ingrese su ingreso mensual : " ))
casa = int ( input ( "Ingrese el costo de la casa : " ) )

cuota_inicial = casa * 0.15
if ingreso>=1250:
    cuota_inicial = casa * 0.30

cuota_mensual = (casa - cuota_inicial)/120
if cuota_inicial == casa * 0.30:
    cuota_mensual = (casa - cuota_inicial)/75
    
print(f"La cuota inicial es : {cuota_inicial:.2f} soles.")
print(f"La cuota mensual es de : {cuota_mensual:.2f} soles.")