from champion import Champion


while True:
    print("Bienvenido al menu")
    print("¿Que desea hacer?")
    print("A. Registrar un equipo")
    print("B. Eliminar un equipo")
    print("C. Registrar un jugador a un equipo")
    print("D. Generar calendario")
    print("E. Registrar goles de partido")
    print("F. Ver Equipos con su continente")
    print("G. Salir")
    opcion =input("Escriba una de las opciones: ")
    Copa = Champion()
    if opcion =="A":
        while True:
            Copa.agregarequipo()
            opcionA=input("desea agregar otro equipo? s/n: ")
            if opcionA == "s":
                True
            else:
                break
    if opcion =="B":
        Copa.verequipos("s")
        equipoeliminar=input("ingrese el nombre del equipo que quiere eliminar: ")
        Copa.eliminarequipo(equipoeliminar)
    if opcion =="C":
        while True:
            Copa.verequipos("s")
            equipo=input("ingrese el nombre del equipo en el que quiera al jugador: ")
            Copa.agregarjugadoraequipo(equipo)
            opcionB=input("desea agregar otro jugador? s/n: ")
            if opcionB == "s":
                True
            else:
                break
    if opcion =="F":
        Copa.equipoContinente()
        Copa.verequipos(s="n")
    if opcion =="D":
        Copa.generarcalendario()
    if opcion =="G":
        break
    else:
        "Opcion no encontrada, digite una nuevamente: "


        


        

