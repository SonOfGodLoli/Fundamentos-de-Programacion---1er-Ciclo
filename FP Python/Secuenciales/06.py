#Desarrolle  el  programa  que  calcule  el  área  total  y  el  volumen  de  un  cilindro.  Considere  las 
#siguientes formulas: Área = 2πr(r+h) y Volumen = πr2h. Siendo r el radio y h la altura. 

import os
os.system("cls")

Radio = int(input("Ingrese el Radio del Cilindro :"))
Altura = int(input("Ingrese la altura del Cilindro :"))

pi = 3.1416
Area = (2*(pi*Radio))*(Radio+Altura)
Volumen = (pi*(Radio*Radio))*Altura
 
print(f"El area del cilindro es de {Area:.3f}")
print(f"El Volumen del cilindro es de {Volumen:.3f}")
