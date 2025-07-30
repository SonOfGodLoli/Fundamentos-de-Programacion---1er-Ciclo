# Una empresa registra el sexo, edad y estado civil de sus empleados a través de un número entero positivo de cuatro cifras de acuerdo a lo siguiente: la primera cifra de la izquierda representa el estado civil (1 soltero, 2 casado, 3 divorciado, 4 viudo); las siguientes dos cifras representan la edad y la tercera cifra representa el sexo (1 masculino, 2 femenino).  Desarrolle el programa de determine el estado civil, edad y sexo de un empleado conociendo su número asignado.

import os
os.system("cls")

numero = int(input ( " Ingrese su numero asignado : " ))

estado = "soltera"
if numero//1000==2:
    estado= "casada"
if numero//1000==3:
    estado = "divorciada"
if numero//1000==4:
    estado = "viuda"
if numero//1000>=5:
    estado = "no valido"

edad= (numero%1000)//10

sexo = "Masculino"
if numero%10==2:
    sexo = "Femenino"
if numero%10>=3:
    sexo= "no invalido"

print(f"Es una persona {estado}, de {edad} años y de sexo {sexo}.")