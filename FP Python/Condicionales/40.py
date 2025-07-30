# En  un  instituto  los  cursos  de  matemática,  física  y  química  se  evalúan  en  base  a  tres  prácticas 
# calificadas, examen parcial y final. Cada práctica tiene un peso dado. Desarrolle el programa que 
# determine el promedio final del curso y su condición de aprobado / desaprobado dado que la nota 
# mínima es de 13. 
# Curso        PC1 PC2 PC3  EP  EF 
# Matemática   10% 20% 10% 30% 30% 
# Física       20% 20% 20% 20% 20% 
# Química      10% 30% 10% 25% 25% 

curso = input("Ingrese el curso (Matematica|fisica|quimica) : ").upper()
n1 = int(input("ingrese su nota 1 : "))
n2 = int(input("ingrese su nota 1 : "))
n3 = int(input("ingrese su nota 1 : "))
parcial = int(input("ingrese la nota de su parcial : "))
final = int(input("ingrese la nota de su final : "))

promedioF = 0

if curso== "MATEMATICA":
    promedioF += (n1*0.10) + (n2*0.2) + (n3*0.1) + (parcial*0.3) + (final*0.3) 
elif curso== "FISICA":
    promedioF += (n1*0.20) + (n2*0.2) + (n3*0.2) + (parcial*0.2) + (final*0.2)
elif curso== "QUIMICA":
    promedioF += (n1*0.10) + (n2*0.3) + (n3*0.1) + (parcial*0.25) + (final*0.25)

print(f"El promedio es : {promedioF}")
print(f"Estadiante {"aprobado" if promedioF>=13 else "desaprobado"}")