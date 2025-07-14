#Una persona ha recorrido tres tramos de una carretera. La longitud del primer tramo está dada en kilómetros,  el  segundo  tramo  en  pies  y  el  tercer  tramo  en  millas.  Desarrolle  el  programa  que determine la longitud total recorrida en metros y en yardas. Considere los siguientes factores de conversión: 
# 1 metro = 3.2808 pies, 1 milla = 1609 metros, 1 metro = 100 cm, 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm , 1 yarda = 0.9144 metros

import os
os.system("cls")

Kilometros = int ( input ( "Ingrese el recorrido en Kilometros : " ))
Pies = int ( input ( "Ingrese el recorrido en Pies : " ))
Millas = int ( input ( "Ingrese el recorrido en Millas : " ))

CKilometros = Kilometros*1000
CPies = ( 1 / 3.2808 ) * Pies
CMillas = Millas*1609

Total_Metros = CKilometros + CPies + CMillas
Total_Yardas = Total_Metros/0.9144

Total_Recorrido_Metros = print(f"El Total Recorrido en Metros es de {Total_Metros:.2f}")
Total_Recorrido_Yardas = print(f"El Total Recorrido en Yardas es de {Total_Yardas:.2f}")