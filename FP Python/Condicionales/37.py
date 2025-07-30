# En  una  elección  democrática  a  la  presidencia  de  un  club  femenino  participan  Pamela,  Carol  y Fanny. Para ganar la elección se requiere obtener la mitad de los votos emitidos más uno. En caso de no haber ganador, pasan a una segunda vuelta los candidatos que alcanzaron los dos primeros puestos; se anula la elección si hay empate entre los tres o si hay empate por el segundo puesto. Desarrolle el programa que muestre en que puesto quedaron los candidatos. 

import os
os.system ("cls")

#considerando q en 2da velta ya no hay empates
vpamela = int (input (" Ingrese los votos de pamela : "))
vcarol = int (input (" Ingrese los votos de carol : "))
vfanny = int (input (" Ingrese los votos de fanny : "))

votosMayoria = (vcarol + vfanny + vpamela)//2 + 1

ganadora = ""
if vcarol==vpamela==vfanny:
    print("Eleccion anulada por triple empate :) .")
elif vpamela>= votosMayoria:
    ganadora = "pamela"
elif vcarol>= votosMayoria:
    ganadora = "carol"
elif vfanny>= votosMayoria:
    ganadora = "fanny"
elif ganadora == "" and max(vpamela, vfanny, vcarol)==(vfanny+vcarol+vpamela)-(min(vpamela, vfanny, vcarol)+ max(vpamela, vfanny, vcarol)):
    print("Empate por el segundo puesto, eleccion anulada.")
else:
    vuelta1 = max(vpamela, vfanny, vcarol)
    vuelta2 = (vfanny+vcarol+vpamela) - (vuelta1 + min(vpamela, vfanny, vcarol))
    print(f"Pasa a segunda vuelta {"pamela" if vpamela==vuelta1 else "carol" if vcarol==vuelta1 else "fanny"}")
    print(f"Pasa a segunda vuelta {"pamela" if vpamela==vuelta2 else "carol" if vcarol==vuelta2 else "fanny"}")
 
if ganadora == "pamela" and vcarol>vfanny:
    segundo = "carol"
    tercero = "fanny"
    print(f"La ganadora es {ganadora}")
    print(f"El segundo Puesto es {segundo}")
    print(f"El tercer puesto es {tercero}")
elif ganadora == "pamela" and vcarol<vfanny:
    segundo = "fanny"
    tercero = "carol"
    print(f"La ganadora es {ganadora}")
    print(f"El segundo Puesto es {segundo}")
    print(f"El tercer puesto es {tercero}")
elif ganadora == "carol" and vpamela>vfanny:
    segundo = "pamela"
    tercero = "fanny"
    print(f"La ganadora es {ganadora}")
    print(f"El segundo Puesto es {segundo}")
    print(f"El tercer puesto es {tercero}")
elif ganadora == "carol" and vpamela<vfanny:
    segundo = "fanny"
    tercero = "pamela"
    print(f"La ganadora es {ganadora}")
    print(f"El segundo Puesto es {segundo}")
    print(f"El tercer puesto es {tercero}")
elif ganadora == "fanny" and vpamela>vcarol:
    segundo = "pamela"
    tercero = "carol"
    print(f"La ganadora es {ganadora}")
    print(f"El segundo Puesto es {segundo}")
    print(f"El tercer puesto es {tercero}")
elif ganadora == "fanny" and vpamela<vcarol:
    segundo = "carol"
    tercero = "pamela"
    print(f"La ganadora es {ganadora}")
    print(f"El segundo Puesto es {segundo}")
    print(f"El tercer puesto es {tercero}")
