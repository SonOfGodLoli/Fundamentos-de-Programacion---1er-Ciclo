# Los ángulos se clasifican de la siguiente manera:  nulo (0°), Agudo (0°< x < 90°), Recto (90°), Obtuso (90° < x <180°), Llano (180°), Cóncavo (180°< x < 360°), Completo (360°). Desarrolle. el programa que determine la clasificación de un ángulo dado en grados

import os
os.system("cls")

grados = int(input (" Ingrese el numero de grados :"))

clase = "nulo" if grados == 0 else "agudo" if 0<grados<90 else "recto" if grados == 90 else "obtuso" if 90<grados<180 else "llano" if grados == 180 else "concavo" if 180<grados<360 else "completo" if grados == 360 else "superior a 360"

tipo = "nulo"
if 0<grados<90:
    tipo="agudo"
if grados == 90:
    tipo="recto"
if 90<grados<180:
    "obtuso"
if grados == 180:
    tipo="llano"
if 180<grados<360:
    tipo="Cóncavo"
if grados == 360:
    tipo="completo"
if grados>360:
    tipo="superior a 360" 
    


print (f"el angulo es : {clase}")
print (f"el angulo es : {tipo}")