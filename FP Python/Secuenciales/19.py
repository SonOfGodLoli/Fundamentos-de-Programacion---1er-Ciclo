#Una empresa paga a sus vendedores un sueldo básico mensual de S/. 500. El sueldo bruto es igual al  sueldo  básico  más  una  comisión,  que  es  igual  al  9%  del  monto  total  vendido.  Por  ley,  todo vendedor se somete a un descuento del 11%. Desarrolle el programa que calcule la comisión, el sueldo bruto, el descuento y el sueldo neto de un vendedor de la empresa.

import os
os.system("cls")

Total_V = int(input("Ingrese el total de sus ventas en soles : "))

Sueldo_Ba = 500
Comision_D = (Total_V /100) * 9
Descuento = (Sueldo_Ba / 100) * 11
Sueldo_N = (Sueldo_Ba - Descuento) + Comision_D
Sueldo_Br = Sueldo_Ba + Comision_D

print(f"El sueldo bruto es {Sueldo_Br} soles.")
print(f"La comision es de {Comision_D} soles.")
print(f"El descuento es {Descuento} soles.")
print(f"El sueldo neto es {Sueldo_N} soles.")

