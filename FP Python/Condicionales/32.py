# En  una  universidad,  los  alumnos  están  categorizados  en  cuatro  categorías,  según  tabla  01. Semestralmente  la  universidad  efectúa  rebajas  en  las  pensiones  de  sus  estudiantes  a  partir  del segundo ciclo sobre la base del promedio ponderado del ciclo anterior en porcentajes dados en la tabla 02. Desarrolle el programa que determine la pensión actual, el descuento y la nueva pensión del estudiante.

# Categoría       Pensión         Promedio        Descuento 
#     A           S/. 550         0 a 13.99         No hay 
#     B           S/. 500        14 a 15.99         10 % 
#     C           S/. 450        16 a 17.99         12 % 
#     D           S/. 400        18 a 20            15 %

import os
os.system("cls")

categoria = input("ingrese su categoria (A|B|C|D): ").upper()
promedio = float (input ("ingrese su promedio : "))

if categoria == "A":
    pension= 550
elif categoria == "B":
    pension= 500
elif categoria == "C":
    pension= 450
elif categoria == "D":
    pension= 400

descuento = 0
if 14<=promedio<16:
   descuento = pension*0.10
elif 16<=promedio<18:
   descuento = pension*0.12
elif 18<=promedio<=20:
   descuento = pension*0.15
   
print(f"La pension es de {pension} soles")
print(f"El descuento es de {descuento:.2f} soles")
print(f"La nueva pension es de {pension-descuento:.2f}")