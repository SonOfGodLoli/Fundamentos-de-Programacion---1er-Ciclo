#Desarrolle  el  programa  que  determine  el  área  y  el  perímetro  de  un  rectángulo  sabiendo  que  el área = b x h, perímetro = 2x (b+h).

import os
os.system("cls")

base = int ( input ( "Base = " ))
altura = int ( input ( "Altura = " ))

area = base * altura
perimetro = 2 * ( base + altura)

print ( f"Perimetro = {perimetro:.2f} " )
print ( f"Area = {area:.2f} " )
