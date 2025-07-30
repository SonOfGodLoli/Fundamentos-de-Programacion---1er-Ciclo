#  En  una  oficina  de  empleos  categorizan  a  los  postulantes  en  función  del  sexo  y  de  la  edad  de acuerdo a lo siguiente: Si la persona es de sexo femenino: categoría FA, si tiene menos de 23 años y FB, en caso contrario. Si la persona es de sexo masculino: categoría MA si tiene menos de 25 años y MB, en caso contrario. 

import os
os.system ("cls")

edad = int (input ("Ingrese su edad : "))
sexo = input("Ingrese su sexo (F / M ) : ").upper()

categoria = "FA"
if edad>=23 and sexo== "F":
    categoria = "FB"
if edad<25 and sexo== "M":
    categoria = "MA"
if edad>=25 and sexo== "M":
    categoria = "MB"

print (f" Es de categoria {categoria}")