#Desarrolle  el  programa  que  permite  convertir  una  cantidad  dada  en  metros  a  su  equivalente  en centímetros, pulgadas, pies y yardas. Considere los siguientes factores de conversión:  
#1 metro = 100 cm, 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm

import os
os.system("cls")

metros = int(input("metros : "))

centimetros = metros * 100.0
Pulgadas = centimetros / 2.54
Pies = Pulgadas / 12
Yardas = Pies / 3

print(f"Centimetros = {centimetros:.2f}")
print(f"Pulgadas = {Pulgadas:.2f}")
print(f"Pies = {Pies:.2f}")
print(f"Yardas = {Yardas:.2f}")
