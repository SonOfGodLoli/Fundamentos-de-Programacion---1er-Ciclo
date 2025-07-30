# Un curso se evalúa sobre la base de 5 notas de las cuales se elimina las notas de mayor y menor puntaje. Desarrolle el programa que muestre las notas eliminadas y el promedio aprobatorio.

import os
os.system("cls")

n1 = int(input (" nota 1 : "))
n2 = int(input (" nota 2 : "))
n3 = int(input (" nota 3 : "))
n4 = int(input (" nota 4 : "))
n5 = int(input (" nota 5 : "))

mayor = n1

if n2 > n1:
    mayor = n2
if n3 > n2:
    mayor = n3
if n4 > n3:
    mayor = n4
if n5 > n4:
    mayor = n5
    
menor= n1

if n2 < n1:
    menor = n2
if n3 < n2:
    menor = n3
if n4 < n3:
    menor = n4
if n5 < n4:
    menor = n5

promedio = ((n1 + n2 + n3 + n4 +n5)-(mayor + menor))/3

print(f"promedio {promedio:.2f}")
print(f"Las notas eliminadas son {mayor} y {menor}")   


# if n1 != mayor and n1 != menor:
#     promedio += n1
#     print(promedio)
# if n2 != mayor and n2 != menor:
#     promedio += n2
#     print(promedio)
# if n3 != mayor and n3 != menor:
#     promedio += n3
#     print(promedio)
# if n4 != mayor and n4 != menor:
#     promedio += n4
#     print(promedio)
# if n5 != mayor and n5!= menor:
#     promedio += n5
#     print(promedio)
