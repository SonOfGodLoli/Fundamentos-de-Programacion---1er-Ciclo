# El cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente manera: el sueldo básico se calcula sobre la base del número total de horas trabajadas basado en una tarifa horaria, al sueldo básico, se le aplica una bonificación del 20% obteniéndose el sueldo bruto; al sueldo  bruto,  se  le  aplica  un  descuento  del  10%  obteniéndose  el  sueldo  neto.  Desarrolle  el programa que muestre el sueldo básico, bruto y neto de un trabajador.

import os
os.system("cls")

tarifa_H = int(input("Ingrese el precio por hora : "))
horasT = int(input("Ingrese el numero de horas trabajadas: "))

sueldo_base = tarifa_H * horasT
sueldo_bruto = sueldo_base + ((sueldo_base/100)*20)
sueldo_neto = sueldo_bruto - ((sueldo_bruto/100)*10)

print(f"El sueldo base es de : {sueldo_base:.2f}")
print(f"El sueldo bruto es de : {sueldo_bruto:.2f}")
print(f"El sueldo neto es de : {sueldo_neto:.2f}")
