# Una empresa paga a sus vendedores un sueldo que es la suma del sueldo básico de S/. 250 más una comisión que es igual a un porcentaje del monto total vendido, el porcentaje depende de la categoría del vendedor como se muestra en la tabla. Además, si el sueldo excedo los S/. 3500 se efectúa un descuento del 15% en caso contrario del 8%. Desarrolle el programa que muestre el sueldo bruto y neto a pagar, como también el descuento y la comisión aplicada. 

#       Monto         Comisión 
# ... 5000              5 % 
# 5000 ... 10000        8 % 
# 10000 ... 20000       10 % 
#    20000 ....         15 % 

import os
os.system ("cls")

totalventa = int ( input ( "Monto total vendido : " ) )

sueldo_base = 250
comision = totalventa * 0.05
if totalventa>5000:
    comision = totalventa * 0.08
if totalventa>10000:
    comision = totalventa * 0.10
if totalventa>20000:
    comision = totalventa * 0.15

sueldo_bruto = comision + sueldo_base
sueldo_real = sueldo_bruto - (sueldo_bruto*0.08)

if sueldo_bruto>3500:
    sueldo_real = sueldo_bruto - (sueldo_bruto*0.15)

print(f"Sueldo Bruto : {sueldo_bruto:.2f} soles.")
print(f"Sueldo Neto : {sueldo_real:.2f} soles.")
print(f"La comision fue de {comision:.2f} soles.")
print(f"El descuento fue de {sueldo_bruto-sueldo_real:.2f} soles.")