#Dado  dos  números  enteros  de  3  cifras,  desarrolle  el  programa  que  muestre  la  cifra  primera  y tercera cifras intercambiadas entre ambos números. Ejemplo 123 y 456 → 624 y 351

import os
os.system("cls")

numero_1 = int(input("Ingrese un numero de 3 cifras : "))
numero_2 = int(input("Ingrese un segundo numero de 3 cifras : "))

N1_1 = numero_1 // 100
N1_2 = (numero_1 // 10) % 10
N1_3 = numero_1 % 10

N2_1 = numero_2 // 100
N2_2 = (numero_2 // 10) % 10
N2_3 = numero_2 % 10

print(f"Los numeros han cambiado a {N2_3}{N1_2}{N2_1} y {N1_3}{N2_2}{N1_1} ")












# numero_1=(str(numero_1))
# numero_2=(str(numero_2))

# N1 = numero_2[2] + numero_1[1] + numero_2[0]
# N2 = numero_1[2] + numero_2[1] + numero_1 [0]

# print(f"Los numeros nuevos son : {N1} y {N2}")