#Desarrolle el programa que lea un número entero en el intervalo de 1 a 7 correspondiente a un día de la semana, y determine el nombre del día. Considere 1 - lunes, 2 – martes, ...

import os
os.system("cls")

numero = int(input("Ingrese un numero del 1 al 7 : "))
# if numero == 1 : print("Lunes")
# if numero == 2 : print("Martes")
# if numero == 3 : print("Miercoles")
# if numero == 4 : print("Jueves")
# if numero == 5 : print("Viernes")
# if numero == 6 : print("Sabado")
# if numero == 7 : print("Domingo")
# else: print("Error")
dia = "Lunes"
if numero == 2:
    dia = "Martes"
if numero == 3:
    dia = "Miercoles"
if numero == 4:
    dia = "Jueves"
if numero == 5:
    dia = "Viernes"
if numero == 6:
    dia = "Sabado"
if numero == 7:
    dia = "Domingo"
if numero>=8:
    dia = "incorrecto"
    
print(f"El dia es {dia}")



