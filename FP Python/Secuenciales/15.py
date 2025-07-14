# Juan, Rosa y Daniel aportan cantidades de dinero para formar un capital. Juan y Rosa aportan en dólares y Daniel, en soles. Desarrolle el programa que determine el capital total en dólares y que porcentaje de dicho capital aporta cada uno. Dólar = S/. 3.00 nuevos soles.

import os
os.system("cls")

Juan = int(input("Monto en Dolares : "))
Rosa = int(input("Monto en Dolares : "))
Daniel = int(input("Monto en soles : "))

dolar = 3.00

DanielD = Daniel / dolar
totalD = DanielD + Rosa + Juan
jp= (Juan/totalD)*100
rp= (Rosa/totalD)*100
dp= (DanielD/totalD)*100

print(f"El capital total es de {totalD:.2f} dolares.")
print(f"Juan aporto el {jp:.2f}")
print(f"Rosa aporto el {rp:.2f}")
print(f"Daniel aporto el {dp:.2f}")
