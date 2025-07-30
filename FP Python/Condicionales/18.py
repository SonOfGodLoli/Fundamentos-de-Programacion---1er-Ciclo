# Una institución benéfica recibe anualmente una donación y lo reparte de la siguiente manera: Si el monto es de $ 10000 o más, 30% se destina al centro de salud; 50% al comedor de niños, y el resto se invierte en la bolsa. Si el monto de la donación es menor a 10000, 25% se destina al centro de salud; 60% al comedor de niños, y el resto se invierte en la bolsa.

import os
os.system("cls")

Donacion = int (input ("Ingrese el monto : "))

if Donacion>=10000:
    salud = Donacion*0.30
    niños = Donacion*0.50
    bolsa = Donacion*0.20
else:
    salud = Donacion*0.25
    niños = Donacion*0.60
    bolsa = Donacion*0.15
    
print(f"A salud van {salud:.2f} dolares.")
print(f"A salud van {niños:.2f} dolares.")
print(f"A salud van {bolsa:.2f} dolares.")
