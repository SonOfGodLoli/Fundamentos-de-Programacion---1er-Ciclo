#Desarrolle  el  programa  que,  dada  la  capacidad  de  un  disco  duro  en  gigabytes,  lo  convierta  a 
#megabytes, kilobytes y bytes. 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB.

import os
os.system("cls")

Gigabyte = int(input ("Ingrese La capacidad en Gigabytes : "))

Megabytes = Gigabyte*1024
Kilobytes = Megabytes*1024
Bytes = Kilobytes*1024

print(f"Cantidad en Megabytes del disco : {Megabytes} MB")
print(f"Cantidad en Kilobytes del disco : {Kilobytes} KB")
print(f"Cantidad en Bytes del disco : {Bytes} B")
