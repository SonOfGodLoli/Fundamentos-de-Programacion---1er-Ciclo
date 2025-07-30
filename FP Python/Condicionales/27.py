# Una empresa paga a sus vendedores un sueldo bruto igual a la suma de un sueldo básico de S/. 600 más una comisión igual al 15% del monto total vendido. Por otro lado, si el sueldo bruto es mayor a S/. 1800 se le descontará el 10%, en caso contrario será 5%. Además, como incentivo la empresa  obsequia  3  polos  si  el  monto  vendido  es  mayor  a  S/.  1000  sino  si  obsequia  sólo  1. Desarrolle el programa que determine el sueldo bruto, el descuento y el sueldo neto y el número de polos que son obsequiados

import os
os.system ("cls")

totalV = int (input ( " Monto total vendido : "))

sueldobruto = 600 + (totalV*0.15)

if sueldobruto>1800:
    descuento = sueldobruto*0.10
else:
    descuento = sueldobruto*0.05

obsequio = 1
if totalV>1000:
    obsequio=3
    
print (f"El sueldo bruto es : {sueldobruto:.2f} soles.")
print (f"El descuento es : {descuento:.2f} soles.")
print (f"El sueldo neto es : {sueldobruto - descuento:.2f} soles.")
print (f"le obequian : {obsequio} polos.")