# En una tienda obsequian lapiceros Lucas, Faber y Pilot por la compra de cuadernos de acuerdo a lo  siguiente:  Si  el  número  de  cuadernos  adquiridos  es  menos  que  12,  no  se  obsequia  ningún lapicero.  Si  el  número  de  cuadernos  adquiridos  es  no  menos  que  12,  pero  menos  que  24,  se obsequia 1 lapicero Lucas por cada 4 cuadernos adquiridos. Si el número de cuadernos adquiridos es  no  menos  de  24,  pero  menos  que  36,  se  obsequia  2  lapiceros  Faber  por  cada  4  cuadernos adquiridos. Si el número de cuadernos adquiridos es no menos de 36, se obsequia 2 lapiceros Pilot por  cada  4  cuadernos  adquiridos,  más  1  lapicero  Faber  por  cada  6  cuadernos  adquiridos  y  1 lapicero Lucas por cada 12 cuadernos adquiridos. Desarrolle el programa que determine cuántos lapiceros se obsequia a un cliente. 
import os
os.system("cls")

cuadernos = int (input("ingrese el numero de cuadernos comprados : "))

obsequio= 0
if 12<=cuadernos<24:
    obsequio = (cuadernos//4)*1
    tipo = "lucas"
elif 24<=cuadernos<36:
    obsequio = (cuadernos//4)*2
    tipo = "faber"
elif 36<=cuadernos:
    obsequio = (cuadernos//4)*2 + ((cuadernos//6)*1) + ((cuadernos//12)*1)
    tipo = (f", {(cuadernos//4)*2} pilot, {((cuadernos//6)*1)} faber y {((cuadernos//12)*1)} lucas")
    
print(f"El cliente recibe en total {obsequio} lapiceros {tipo}.")
