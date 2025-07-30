# Una empresa evalúa a sus empleados bajo dos criterios: puntualidad y rendimiento. En cada caso, el empleado recibe un puntaje que va de 1 a 10, de acuerdo a los siguientes criterios: Puntaje por puntualidad, está en función a los minutos de tardanza. Puntaje por rendimiento, está en función a la cantidad de observaciones efectuadas al empleado por no cumplir sus obligaciones. El puntaje total del empleado es la suma del puntaje por puntualidad más el de rendimiento; en base a este puntaje total, el empleado recibe una bonificación anual. Desarrolle el programa que calcule los puntajes y la bonificación que le corresponde a un empleado.

# Tardanza(min) Puntaje Observaciones Puntaje  Total Bonificación 
#     0           10        0          10      < 11  S/.2.5 por punto
#     1 a 2       8         1          8    11 a 13  S/.5.0 por punto 
#     3 a 5       6         2          5    14 a 16  S/.7.5 por punto 
#     6 a 9       4         3          1    17 a 19  S/.10.0 por punto 
#     Más de 9    0      Más de 3      0      20 >   S/.12.5 por punto

import os
os.system("cls")

#hay un detalle en la tabla, la bonificacion de 12.5 nunca se aplicaria asi q la vamos a dejar en 20 fijo y no en mayor a 20

tardanza = int(input ("Ingrese su tardanza en minutos : "))
observaciones = int(input ("Ingrese el numero de las observaciones dadas : "))

puntos_t = 10
if 1<=tardanza<=2:
    puntos_t=8 
elif 3<=tardanza<=5:
    puntos_t=6
elif 6<=tardanza<=9:
    puntos_t=4
elif tardanza>9:
    puntos_t=0
    
puntos_o = 10
if observaciones==1:
    puntos_o=8
elif observaciones==2:
    puntos_o=5 
elif observaciones==3:
    puntos_o=1 
elif observaciones>3:
    puntos_o=0 
    
    
bonificacion = (puntos_o + puntos_t)*12.5
if 17<=puntos_t+puntos_o<=19:
    bonificacion = (puntos_o + puntos_t)*10
elif 14<=puntos_t+puntos_o<=16:
    bonificacion = (puntos_o + puntos_t)*7.5
elif 11<=puntos_t+puntos_o<=13:
    bonificacion = (puntos_o + puntos_t)*5
elif puntos_t+puntos_o<11:
    bonificacion = (puntos_o + puntos_t)*2.5


print(f"La bonificacion anual es de {bonificacion}")