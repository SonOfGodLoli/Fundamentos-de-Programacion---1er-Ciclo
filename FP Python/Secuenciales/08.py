#Desarrolle el programa que determine de un cilindro el área base = π r2, área lateral = 2 π r h, área total = 2 x área base x área lateral. Siendo r el radio y h la altura.

import os
os.system("cls")

Radio = int(input("Ingrese el Radio del cilindro :"))
Altura = int(input("Ingrese la Altura del cilindro :"))

pi = 3.1416
Area_Base = pi*(Radio*Radio)
Area_Lateral = ((2*pi)*Radio)*Altura
Area_Total = (2*Area_Base)*Area_Lateral

print(f"El Area Base es : {Area_Base:.2f}")
print(f"El Area Lateral es : {Area_Lateral:.2f}")
print(f"El Area Base es : {Area_Total:.2f}")
