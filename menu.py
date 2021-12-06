from champion import Champion


while True:
    print("Bienvenido al menu")
    print("¿Que desea hacer?")
    print("A. Registrar un equipo")
    print("B. Eliminar un equipo")
    print("C. Registrar un jugador a un equipo")
    print("D. Generar calendario")
    print("E. Registrar goles de partido")
    print("F. Ver Equipos segun su continente")
    print("G. Salir")
    opcion =input("Escriba una de las opciones: ")
    Copa = Champion()
    if opcion =="A":
        Copa.agregarequipo()
        opcionA=input("desea agregar otro equipo? s/n: ")
        if opcionA == "s":
            Copa.agregarequipo()
    if opcion =="B":
        print(Copa.verequipos("f"))
        equipoeliminar=input("ingrese el nombre del equipo que quiere eliminar: ")
        Copa.eliminarequipo(equipoeliminar)
    if opcion =="C":
        print(Copa.verequipos("f"))
        equipo=input("ingrese el nombre del equipo en el que quiera al jugador: ")
        Copa.agregarjugadoraequipo(equipo)
    if opcion =="F":
        Copa.equipoContinente()
        Copa.verequipos("n")
        
    if opcion =="G":
        break
    else:
        "Opcion no entrada digite una nuevamente: "
        


        


