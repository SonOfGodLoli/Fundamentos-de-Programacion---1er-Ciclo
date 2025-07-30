# Una  empresa  ha  decidido  otorgar  una  bonificación  por  fiestas  patrias  a  sus  empleados.  Si  el empleado tiene más de un hijo, recibirá una bonificación igual al 12.5% de su sueldo bruto más S/.  40  por  cada  hijo;  en  caso  contrario,  solo  recibirá  una  bonificación  del  10%.  Elaborar  el programa que muestre la bonificación y el sueldo neto a pagar. 

import os
os.system("cls")

hijos = int (input ("ingrese el numero de hijos : "))
sueldob = int (input ("ingrese su sueldo bruto : "))

bonificacion = sueldob*0.10
if hijos>=1:
    bonificacion = (sueldob*0.125) + 40*hijos
    
sueldo_neto = sueldob + bonificacion

print (f"La bonificacion es de {bonificacion:.2f} soles.")
print (f"El sueldo neto es de {sueldo_neto:.2f} soles.")