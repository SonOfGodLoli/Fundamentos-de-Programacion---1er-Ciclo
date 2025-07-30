#Una tienda vende un producto a un precio unitario igual a S/. 20. Como oferta la tienda ofrece un porcentaje de descuento sobre el importe de la compra. Adicionalmente la tienda regala caramelos en base al número de unidades adquiridas del producto.Desarrolle el programa que determine el importe de la compra, el descuento, total a pagar y el número de caramelos del obsequio que se da al cliente por la compra realizada.

import os
os.system("cls")

caramelos = int(input( "Ingrese el numero total de Caramelos adquiridos : " ))

precio_u = 20

importe_C = caramelos * precio_u

descuento = 0

if importe_C >=701 :
    descuento = importe_C * 0.16

if importe_C <701 and importe_C >= 501:
    descuento = importe_C * 0.14

else:
    descuento == importe_C * 0.12
    
regalo = 5 if caramelos <= 50 else 10 if caramelos <=100 else 15 

print (f"el importe es : {importe_C} ")
print (f"el Descuento es : {descuento:.2f} ")
print (f"Total a pagar : {importe_C - descuento} ")
print (f"numero de caramelos de regalo :  {regalo}")