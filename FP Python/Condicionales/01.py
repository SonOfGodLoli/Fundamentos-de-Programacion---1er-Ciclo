# Una  tienda  vende  un  producto  a  precios  unitarios  que  dependen  de  la  cantidad  de  unidades adquiridas. Adicionalmente, si el cliente adquiere más de 50 unidades la tienda le descuenta  el 15% del importe de la compra; en caso contrario, sólo le descuenta el 5%. Desarrolle el programa que  determine  el  importe  de  la  compra,  el  descuento  y  el  total  a  pagar  por  la  compra  de  cierta cantidad de unidades del producto. 1 a 25 unidades (S/. 27), 26 a 50 unidades (S/. 25), 51 en adelante unidades (S/. 23)

unidades = int(input("Ingrese las cantidades a comprar: "))

# precio = 0
# if unidades <= 25 : precio = 27
# elif unidades >= 26 and unidades <= 50: precio = 25
# else: precio = 23

# precio = 25
# if unidades <= 25 : precio = 27
# elif unidades >= 51 : precio = 23

precio = 27 if unidades <= 25 else 23 if unidades >= 51 else 25

importe = precio * unidades
descuento =importe * 0.15 if unidades>50 else importe *0.05
precio_total = importe - descuento

