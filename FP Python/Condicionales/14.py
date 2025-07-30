#En un supermercado hay una promoción según la cual el cliente raspa una tarjeta que contiene un 
#número oculto. Si el número de la tarjeta es par no menor de 100, el cliente obtiene un descuento 
#del 15 %, caso contrario será del 5 % sobre el importe de la compra.  Desarrolle el programa que 
#muestre el número de la tarjeta, el monto de la compra y el descuento.

import os
os.system("cls")

compra = int(input("compra = "))
tarjeta = int(input("Numero = "))

if tarjeta > 100 and tarjeta % 2 == 0:
    descuento = 0.15 * compra
else: descuento = 0.05 * compra

# descuento = compra*(0.15 if tarjeta >100 and tarjeta % 2== 0 else 0.05)

print (f" Tarjeta = {tarjeta}")
print (f" Compra = {compra}")
print (f" Descuento = {descuento}")
print (f" Monto total = {compra - descuento:.2f}")
