# Una empresa ha decidido adquirir varias piezas de la misma clase a una fábrica de refacciones. La empresa dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $ 5000, la empresa pedirá prestado al banco el 30%; en caso contrario, el préstamo será del 20%. La diferencia la cubrirá con su propio dinero. Desarrolle el programa que determine cuánto tendrá que pagar la empresa de su propio dinero y del préstamo considerando que el banco le cobrará el 10% por concepto de interés.

import os
os.system("cls")

monto = int (input ( "Ingrese el monto de total de la compra : "))

prestamo = monto * 0.2
if monto>5000:
    prestamo = monto * 0.3

totalPagoE = monto - prestamo
totalPagoP = prestamo + (prestamo*0.1)

print(f"La empresa pago de su dinero {totalPagoE} soles.")
print(f"La empresa pago al banco {totalPagoP} soles.")