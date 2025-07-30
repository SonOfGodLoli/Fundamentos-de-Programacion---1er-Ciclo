# Desarrolle el programa para obtener el grado de eficiencia de un operario de torno para obtener el grado de eficiencia de un operario de torno de una fábrica productora de tornillos de acuerdo a las siguientes condiciones: No más de 1.5 horas de ausencia al trabajo. Menos de 300 tornillos defectuosos  producidos.  Más  de  10000  tornillos  no  defectuosos  producidos.  Los  grados  de eficiencia  para  cada  trabajador  son  asignados  de  la  siguiente  manera:  Si  no  cumple  ninguna condición, grado 5. Si sólo cumple la primera, grado 7.  Si sólo cumple la segunda, grado 8. Si sólo cumple la tercera, grado 9. Si cumple la primera y segunda condición, grado 12. Si cumple la primera y tercera condición, grado 13. Si cumple la segunda y tercera condición, grado 15. Si cumple las tres condiciones, grado 20.

import os
os.system("cls")

ausencia = float(input (" Ingrese las horas de ausencia : (#.#)"))
Tornillo_defect = int(input ( "Ingresa los tornillos defectuosos producidos : "))
tornillos_perfect= int (input ( "Ingresa los tornillos bien producidos : " ))

grado = 5
if ausencia<=1.5:
    grado = 7
if Tornillo_defect<300:
    grado = 8
if tornillos_perfect>10000:
    grado = 9
if ausencia<=1.5 and Tornillo_defect<300:
    grado = 12
if ausencia<=1.5 and tornillos_perfect>10000:
    grado = 13
if Tornillo_defect<300 and tornillos_perfect>10000:
    grado = 15
if ausencia<=1.5 and Tornillo_defect<300 and tornillos_perfect>10000:
    grado = 20
    
print (f" El grado de eficiencia de la persona es de {grado}")