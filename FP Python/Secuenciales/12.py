#Desarrolle el programa que permita calcular el resultado de la ecuación de segundo grado de la forma ax2 + bx +c. Usando la clase Math.

import sys
import math
import os
os.system("cls")

a = int(input("Ingrese el valor de a : "))
b = int(input("Ingrese el valor de b : "))
c = int(input("Ingrese el valor de c : "))

#Discriminante = D = b² - 4ac

D = (b*b) - (4*a*c) # D= math.pow(b , 2) - (4*a*c)
D < 0 and print("La discriminante es menor que '0' por lo que solo arroja numeros complejos")
D < 0 and sys.exit(0)

# x = −b±( D ) / 2a

Resultado_1 = (-b + (math.sqrt(D))) / (2*a)
Resulatdo_2 = (-b - (math.sqrt(D))) / (2*a)

print(f"Los Resultados Son : x1 = {Resultado_1:.2f} y x2 = {Resulatdo_2:.2f}.")















#import math  # Importamos la librería matemática

# 1. Pedimos los valores a, b y c al usuario
#a = float(input("Ingrese el valor de a: "))
#b = float(input("Ingrese el valor de b: "))
#c = float(input("Ingrese el valor de c: "))

# 2. Verificamos que sea una ecuación cuadrática (a ≠ 0)
#if a == 0:
#    print("No es una ecuación de segundo grado.")
#else:
    # 3. Calculamos el discriminante: D = b² - 4ac
#    discriminante = math.pow(b, 2) - 4 * a * c

    # 4. Dependiendo del discriminante, mostramos las soluciones
#    if discriminante > 0:
#        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
#        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
#        print("Tiene dos soluciones reales:")
#        print(f"x1 = {x1}")
#        print(f"x2 = {x2}")
#    elif discriminante == 0:
#        x = -b / (2 * a)
#        print("Tiene una única solución real:")
#        print(f"x = {x}")
#    else:
#        print("No tiene soluciones reales (el discriminante es negativo).")