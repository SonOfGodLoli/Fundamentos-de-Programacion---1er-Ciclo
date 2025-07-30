# El índice de masa corporal (IMC) permite medir el grado de sobrepeso u obesidad de una persona, se  calcula  de  la  forma  IMC  =  peso  /  estatura2  Kg  /  m2,  el  resultado  se  muestra  en  la  tabla. Desarrolle el programa que calcule el IMC de una persona.

#   IMC         Grado de Obesidad 
#   < 20           Delgado 
#   20  a 25        Normal 
#   25 a 27         Sobrepeso 
#   > 27            Obesidad

import os
os.system

peso = float(input ("Ingrese su peso en kg (0.00) : "))
altura = float (input ("Ingrese su altura en metros (0.00) : "))

imc = peso/(altura*altura)

if imc<20:
    estado= "delgado"
if 20<=imc<=24:
    estado= "normal"
if 25<=imc<=27:
    estado= "sobrepeso"
if imc>27:
    estado= "obesidad"

print(f"EL imc es igual a {imc:.2f}")
print(f"Estado {estado}")