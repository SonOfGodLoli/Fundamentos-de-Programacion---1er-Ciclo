# Un padre ha decido dar una propina a su hijo en base a las notas en Matemáticas y Física. Si la nota de Matemáticas es  mayor a  17, le dará S/. 3, en caso contrario sólo le dará S/. 1 por cada punto. Si la nota de Física es mayor a S/. 15, le dará S/. 2, en caso contrario solo S/. 0.50 Además, si el promedio de las notas es mayor a 16, le obsequiará un reloj

import os
os.system("cls")



#Profe forma 1
matematica = int(input("Matematica : "))
fisica = int(input("Fisica : "))

propina = matematica + (fisica /2)
if matematica > 17 : propina += ( matematica - 17) * 2
if fisica > 15 : propina += ( fisica - 15 ) * 1.5

promedio = (matematica + fisica) / 2
reloj = "si" if promedio > 16 else "no"

print (f"{propina}")
print (f"{reloj}")



#forma 2
# def Mat():
#     Mate = int (input("Ingrese la nota de Matemáticas : "))
#     Fisi = int (input("Ingrese la nota de Física : "))

#     Propina = (Mate * 1  if Mate<=17 else Mate * 3 ) + (Fisi * 0.50  if Fisi<=15 else Fisi * 2 )

#     reloj = (Mate + Fisi) / 2
#     if reloj>=17:
#         print(f"La propina es de {Propina} y su promedio es mayor de 16, se le regalo un reloj")
#         print("")
#         return Mat()
#     else:
#         print(f"La propina es de {Propina} y su promedio es menor de 16, no se le regalo un reloj")
#         print("")
#         return Mat()

# Mat()