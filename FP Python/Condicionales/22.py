# Una empresa desea adquirir cierta cantidad de unidades de dos productos A y B a un proveedor cuyos precios son los siguientes: Producto A = S/. 25 x unidad y 15 % de descuento para más de 50  unidades  adquiridas.  Producto  B  =  S/.  30  x  unidad  y  10  %  de  descuento  para  más  de  60 unidades  adquiridas.  Desarrolle  el  programa  que  muestre  el  importe  bruto,  descuento  y  total  a pagar por la compra de ciertas unidades de ambos productos.

import os
os.system("cls")

Unidades_A = int (input ( "Ingrese la cantidad de unidades de producto A : " ))
Unidades_B = int (input ( "Ingrese la cantidad de unidades de producto B : " ))

precio_A = 25
precio_B = 30

total_A = precio_A*Unidades_A
total_B = precio_B*Unidades_B

descuento = 0
if Unidades_A>50:
    descuento += (precio_A*Unidades_A)*0.15
    total_A -= (precio_A*Unidades_A)*0.15
if Unidades_B>60:
    descuento += (precio_B*Unidades_B)*0.10
    total_B -= (precio_B*Unidades_B)*0.10

print(f"importe bruto : {(Unidades_A * precio_A) + (Unidades_B*precio_B):.2f} soles.")
print(f"El descuento es : {descuento:.2f} soles.")
print(f"El total por el producto A es de {total_A} soles y el B es de {total_B} soles.")
