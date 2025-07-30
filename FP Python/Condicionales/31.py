# Una empresa calcula el sueldo bruto de sus trabajadores multiplicando las horas trabajadas por una tarifa horaria que depende de la categoría del trabajador. Por ley, todo trabajador se somete a un  porcentaje  de  descuento  del  sueldo  bruto  del  20%  si  supera  los  S/.  2500  y  15  %  en  caso contrario. Desarrolle el programa que determine el sueldo bruto, el descuento y el sueldo neto que le corresponde a un trabajador de la empresa. 

# Categoría         Pago por Hora 
#     A                S/. 21.00 
#     B                S/. 19.50 
#     C                S/. 17.00 
#     D                S/. 15.50

import os
os.system("cls")

cat =  input("Ingrese su categoria : ").upper()
horast = int (input ("ingrese sus horas trabajadas : "))

if cat== "A":
    precio= 21
elif cat== "B":
    precio= 19
elif cat== "C":
    precio= 17
elif cat== "D":
    precio= 15
else:
    print ("categoria incorrecta")
    
descuento = (precio*horast)*0.15
if precio*horast>2500:
    descuento = (precio*horast)*0.20

    
print(f"Sueldo Bruto : {precio*horast} soles.")
print(f"Descuento : {descuento} soles.")
print(f"Sueldo neto : {(precio*horast)-descuento} soles.")