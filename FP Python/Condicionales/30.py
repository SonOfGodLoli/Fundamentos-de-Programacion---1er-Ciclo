# Una compañía cobra las cuotas mensuales de sus clientes de acuerdo a lo siguiente: Si el cliente paga dentro de los primeros diez días del mes, obtiene un descuento igual al mayor valor entre $5 y  el  2%  de  la  cuota.  Si  el  cliente  paga  en  los  siguientes  diez  días,  no  tiene  derecho  a  ningún descuento. Si el cliente paga dentro de los restantes días del mes, tendrá un recargo igual al mayor valor entre $ 10 y el 3% de la cuota. Desarrolle el programa que determine cuánto debe pagar un cliente en un mes dado.

import os
os.system("cls")

cuotaM = int(input ("ingresa el monto mensual : "))
fecha = int(input ("Ingrese el numero de fecha del dia de hoy : "))

#esta forma considera los numeros decimales, estos estan entre el $5 y 2%, $10 y 3%, ademas considera q el 2% y 3% es menor q sus comparaciones respectivas, el $5 y $10 se les resta 1

descuento = 0
if cuotaM*0.02>5:
    descuento = (cuotaM*0.02)//1 if (cuotaM*0.02)%1!= 0 else (cuotaM*0.02)-1
if cuotaM*0.02<5:
    descuento= 4

recargo = 0
if cuotaM*0.03>10:
    recargo = (cuotaM*0.03)//1 if (cuotaM*0.03)%1!= 0 else (cuotaM*0.03)-1
if cuotaM*0.03<10:
    recargo = 9

pago = cuotaM
if fecha<=10:
    pago= cuotaM - descuento
if fecha>=21:
    pago = cuotaM + recargo
    
    
print(f"El pago es de {pago}")