#En países de habla inglesa, es común dar la estatura de una persona como la suma de una cantidad de pies, más una cantidad de pulgadas, por ejemplo 3’ 2”. Desarrolle el programa que determine la estatura en metros dada su estatura en el formato inglés.
#conversión: 1 metro = 3.2808 pies, 1 milla = 1609 metros, 1 metro = 100 cm, 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm , 1 yarda = 0.9144 metros , 1 Pie =0.3048 metros 

import os
os.system("cls")

Altura_Pies = int (input ( "Ingrese la parte en Pies : " ))
Altura_Pulgadas = int ( input ( "Ingrese la parte en Pulgadas : " ))

Conversion_de_Pies = Altura_Pies*0.3048
Conversion_de_Pulgadas = Altura_Pulgadas*0.0254

Medida_en_Metros = print(f"La altura es {Conversion_de_Pies + Conversion_de_Pulgadas:.3f} metros" )