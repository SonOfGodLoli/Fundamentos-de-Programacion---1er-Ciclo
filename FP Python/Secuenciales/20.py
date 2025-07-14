#Dada una cantidad de dinero en soles, desarrolle el programa que descomponga dicha cantidad en billetes de 200, 100, 50, 20, 10 y monedas de 5, 2, 1 nuevos soles. 

import os
os.system("cls")

Dinero = int(input ("Ingrese una cantidad de dinero : "))

D200 = Dinero // 200
Dinero = Dinero % 200

D100 = Dinero // 100
Dinero = Dinero % 100

D50 = Dinero // 50
Dinero = Dinero % 50

D20 = Dinero // 20
Dinero = Dinero % 20

D10 = Dinero // 10
Dinero = Dinero % 10

D5 = Dinero // 5
Dinero = Dinero % 5

D2 = Dinero // 2
Dinero = Dinero % 2

D1 = Dinero // 1
Dinero = Dinero % 1

print(f"Se necesitan {D200} billetes de 200")
print(f"Se necesitan {D100} billetes de 100")
print(f"Se necesitan {D50} billetes de 50")
print(f"Se necesitan {D20} billetes de 20")
print(f"Se necesitan {D10} billetes de 10")
print(f"Se necesitan {D5} Monedas de 5")
print(f"Se necesitan {D2} Monedas de 2")
print(f"Se necesitan {D1} Monedas de 1")