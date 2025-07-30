# Una tienda ofrece un porcentaje de descuento sobre el importe de la compra de los cuatro tipos de productos cuyos códigos, precios unitarios y descuentos se muestran en las siguientes tablas. Desarrolle el programa que determine el importe de la compra, el descuento y el total a pagar por la compra de cierta cantidad de unidades de un mismo tipo de producto.

# Código Precio Unitario  Unidades Descuento 
# 101         17          1 a 10      5 % 
# 102         25          11 a 20     8 % 
# 103         16          21 a 30     10 % 
# 104         27          31 a mas    13 % 

import os
os.system("cls")

codigo = int(input("codigo = "))
unidades = int(input("unidades = "))

precio = 0
if codigo == 101 : precio =17 
elif codigo== 102: precio =25
elif codigo== 103: precio =16
elif codigo== 104: precio =27


compra = precio * unidades
Descuento = compra * 0.05 if unidades<=10 else compra*0.08 if unidades<=20 else compra*0.10 if unidades<=30 else compra*0.13 
#Descuento*=compra #descuento = descuento*compra
total = compra-Descuento

print(f"compra  = {compra:.2f}")
print(f"Descuento  = {Descuento:.2f}")
print(f"Total  = {total:.2f}")