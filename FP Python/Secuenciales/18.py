#En  una  tienda  han  puesto  en  oferta  la  venta  de  todos  sus  artículos  por  cambio  de  estación ofreciendo  un  15%  +  15%  de  descuento.  El  primer  15%  se  aplica  al  importe  de  la  compra, mientras que el segundo 15% se aplica al importe que resulta de restar el importe de la compra menos el primer descuento. Dada la cantidad de unidades adquiridas de un mismo tipo de artículo por parte de un cliente y el precio unitario del artículo. Desarrolle el programa que determine el importe de la compra, el descuento y el importe a pagar.


import os
os.system("cls")

Cantidad = int(input("Ingrese la cantidad de unidades compradas : "))
Precio = int(input("Ingrese el precio del producto por unidad: "))

Total = Cantidad * Precio
Descuento_1 = Total*0.15
Descuento_2 = (Total - Descuento_1)*0.15

print(f"El importe de la compra es igual a {Total} soles.")
print(f"El descuento total es de {Descuento_1+Descuento_2}")
print(f"El importe a pagar es de {(Total-Descuento_1)-Descuento_2}")





# NA='\033[1;93m'
# N = '\033[0m'

# print(f"\nEl importe total es {NA}{Total}{N} Soles, con un descuento de {NA}{Descuento_1}{N} soles, dando el total de {NA}{Total-Descuento_1}{N} Soles, al que se le aplica un 2do Descuento de {NA}{Descuento_2}{N} soles, dando como importe a pagar de {NA}{(Total-Descuento_1)-Descuento_2}{N} Soles.")

