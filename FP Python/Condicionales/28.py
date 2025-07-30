# Desarrolle el programa que, ingresado una hora en formato de 24 horas, la muestre en formato de 12 horas am / pm. Además, si la hora es inválida mostrar el mensaje de error respectivo.

import os
os.system("cls")

hora = int(input (" Ingrese la hora : "))
minutos = int (input (" Ingrese los minutos : "))

if hora//12==1 and minutos==0:
    nueva_hora = "12:00 pm"
if hora//12>=1 and minutos>0:
    nueva_hora = f"{hora-12 if hora>=13 else 12}:{minutos:02d} pm"
elif hora//12==0:
    nueva_hora = f"{hora if hora!= 0 else 12}:{minutos:02d} am"

print (f" Nueva hora : {nueva_hora}")

