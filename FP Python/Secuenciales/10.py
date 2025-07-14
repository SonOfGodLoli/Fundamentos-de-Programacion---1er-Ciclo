#Dado un número natural de cuatro cifras, desarrolle el programa que permite obtener el número  al revés. Ejemplo 1234  → 4321.

#Forma 1
import os
os.system("cls")

Numero = int(input(" Ingrese un numero de 4 Cifras : "))


N1= Numero // 1000
N2= (Numero // 100) % 10
N3= (Numero // 10) % 10
N4= Numero % 10

Num_inverti = (f"{N4}"+f"{N3}"+f"{N2}"+f"{N1}")

print(f"El numero invertido es {Num_inverti}")


#Forma 2
Numero = int(input(" Ingrese un numero de 4 Cifras : "))

N1= Numero // 1000
N2= (Numero // 100) % 10
N3= (Numero // 10) % 10
N4= Numero % 10

Num_inverti = (N4*1000 + N3*100 + N2*10 + N1)

print(f"El numero invertido es {Num_inverti}")


#Forma 3
invertido = str(Numero)[::-1]
print(invertido)