
import pygame
import random
import textwrap

if __name__ == '__main__':
    opciones=[torre,cojin,sofa]
    ancho_linea=72
    linea_punteada=ancho_linea*"-"
    print(linea_punteada)
    print("\033[1m"+"La Conquista de Executus y Apocalipsis "+"\033[0m")

    # mensaje de introduccion
    msg=("Miles de años llevan los gatos preparando la conquista del planeta."
         "Han sido laboriosos los esfuerzos por encontrar las debilidades de otras espécies"
         "Después de la reunión del Clan de la Zarpa de este año salieron dos conclusiones :"
         "1:Se determina el comienzo del extermínio a la raza humana"
         "2:Los designados para el comienzo de tal función son Executus y Apocalipsis")

# primera mision
print(textwrap.fill(msg,whidth=ancho_linea))
print("\033[1m"+"Misión :"+"\033[0m")
print("El primer contacto,encontrar al guia ")
print("Busca en los diferentes puestos")
print("\033[1m"+"NOTA :"+"\033[0m")
print("Encuentra el intercat-municador para ponerte en contacto con Cos")
print("Pulsa 1 para La Torre / 2 para El Cojín / 3 para El Sofá")
print(linea_punteada)

while seguir_jugando==4:
    puestos=[torre,cojin,sofa]
    puesto=print("PULSA NUMERO")
    1=torre
    2=cojin
    3=sofa
    while len(puestos):
        def torre():
            print("La Torre: Puesto de control del exterior ")
            print("En el hueco de la segunda planta hay escondido un intercat-municador")
            print("¿quieres activarlo? sí-Y / no-N ")
            y=("llamada:llamando a Cos")
            n=print("pues...se ha quedau buena tarde")

        def cojin():
            print("El Cojín: Centro de control")
            print("Centro de reuniones ")
            print("¡Es mullidito y esponjosable!")

        def sofa():
            print("El Gran Sofá: Arsenal")
            print("El mejor sitio para enconder todo tipo de objetos")
    
    # carga de opciones 
    if puesto==1:
        torre()
    else:
        if puesto==2:
            cojin()
        else:
            sofa()
