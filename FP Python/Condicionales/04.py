# El promedio final de un curso se obtiene en base al promedio simple de tres prácticas calificadas.Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota de la tercera práctica calificada, si es que esta no es menor que 10. Desarrolle el programa que determine el promedio final de un alumno conociendo sus tres notas. 

import os
os.system("cls")

nota1 = int(input("Ingrese la nota 1 : "))
nota2 = int(input("Ingrese la nota 2 : "))
nota3 = int(input("Ingrese la nota 3 : "))

if nota3<10:
    nota3 +=0
else:
    nota3+=2

promedio = (nota1 + nota2 + nota3 )/3

print(f"el promedio es : {promedio:.2f}")