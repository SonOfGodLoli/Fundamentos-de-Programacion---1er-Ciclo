# Desarrolle el programa que determine la edad menor y mayor de tres edades ingresadas.

import os 
os.system("cls")

edad1 = int(input (" ingrese la edad 1 : "))
edad2 = int(input (" ingrese la edad 2 : "))
edad3 = int(input (" ingrese la edad 3 : "))

edadM = 0
if edad1>edad2 and edad1>edad3:
    edadM = edad1
    
if edad2>edad1 and edad2>edad3:
    edadM = edad2

if edad3>edad2 and edad3>edad1:
    edadM = edad3
    
edadme = 0
if edad1>edad2 and edad3>edad2:
    edadme = edad2
    
if edad2>edad1 and edad3>edad1:
    edadme = edad1

if edad2>edad3 and edad1>edad3:
    edadme = edad3
    
print (f"La edad mayor y menor son es : {edadM} y {edadme}")