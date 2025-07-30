#  Una  tienda  ha  puesto  en  oferta  la  venta,  por  docenas,  de  cierto  tipo  de  producto  ofreciendo  un descuento  del  15%  por  la  compra  de  no  menos  de  6  docenas  y  10%  en  caso  contrario. Adicionalmente, la empresa un obsequio de 2 lapiceros por cada 3 docenas por la compra de no menos de 30 docenas en caso contrario no efectúa ningún obsequio. Desarrolle el programa que determine el monto de la compra, el descuento, total a pagar y la cantidad de lapiceros de obsequio por la compra de cierta cantidad de docenas del producto.

import os
os.system("cls")

lapiceros = int( input ( "Ingrese la cantidad de lapiceros : " ))

precio = int ( input ( "Ingrese el precio por lapicero : " ) )

monto_t = lapiceros * precio

Docenas = lapiceros //12

descuento = monto_t * 0.10
if Docenas >= 6:
    descuento = monto_t * 0.15

obsequio = 0
if Docenas>=30:
    obsequio += (Docenas/3)*2
    
print(f"Monto de la compra : {monto_t:.2f} soles. ")
print(f"Descuento : {descuento:.2f} soles. ")
print(f"Total a pagar : {monto_t-descuento:.2f} soles. ")
print(f"El obsequio es de : {obsequio:.0f} Lapiceros. ")