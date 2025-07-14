#Desarrolle el programa que lea un número entero y determine la suma de sus cifras. Asumir que 
#el número es positivo y de 4 cifras.

#FORMA 1 CON DIVISONES BASICAS

import os
os.system("cls")

Numero = int (input (" Ingrese un Numero de 4 cifras: "))

numero1 = Numero // 1000
numero2 = (Numero // 100) % 10
numero3 = (Numero // 10) % 10
numero4 = Numero % 10
totalN = numero1+numero2+numero3+numero4

print(f"La suma Total de cifras es {totalN}")




#FORMA 2 CON UN BUCLE ITERABLE
#import os
#os.system("cls")

#Numero = (input ( "Ingrese un numero : " ))

#contador = 0
#for i in Numero :
#    contador += int(i)
    
#print (f"La suma de cifras es de :{contador}")