# Un  estudiante  recibe  una  propina  mensual S/.  20.  El  estudiante  rinde  mensualmente tres exámenes.  Su  papá  ha  decidido incentivarlo  dándole  una  propina adicional  de  S/.  5  por  cada examen aprobado. Desarrolle el programa que determine el monto total de la propina.

import os
os.system("cls")

Nota1 = int(input(" Nota 1 :"))
Nota2 = int(input(" Nota 2 :"))
Nota3 = int(input(" Nota 3 :"))

propinaBase = 20
propina = 0

if Nota1>13:
    propina += 5 
if Nota2>13:
    propina += 5 
if Nota3>13:
    propina += 5
    
print(f" La propina total es {propinaBase + propina}")