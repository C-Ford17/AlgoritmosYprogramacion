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
        Copa.verequipos(1)
        equipoeliminar=input("ingrese el nombre del equipo que quiere eliminar: ")
        Copa.eliminarequipo(equipoeliminar)
    if opcion =="C":
        while True:
            Copa.verequipos(1)
            equipo=input("ingrese el nombre del equipo en el que quiera al jugador: ")
            Copa.agregarjugadoraequipo(equipo)
            opcionB=input("desea agregar otro jugador? s/n: ")
            if opcionB == "s":
                True
            else:
                break
    if opcion =="F":
        Copa.equipoContinente()
        Copa.verequipos(2)
    if opcion =="D":
        Copa.generarcalendario()
        Copa.partido()
    if opcion == "E":
        while True:
            print("escriba la fecha del partido: ")
            dia=int(input("dia: "))
            mes=int(input("mes: "))
            año=int(input("año: "))
            fecha= {"dia":dia,"mes":mes,"año":año}
            Copa.verequipos(fecha)
            hora=input("ingrese la hora (hora 1, hora 2, etc): ")
            minuto=int(input("ingrese el minuto en el que se realizo el gol: "))
            jugador=input("seleccione el jugador que hizo el gol: ")
            x=input("desea registrar otro gol? s/n: ")
            Copa.registrargoles(jugador,minuto,hora,fecha)
            if x=="s":
                True
            else:
                break
    if opcion =="G":
        break
    if opcion not in ["A","B","C","D","E","F","G"]:
        print("opcion no encontrada")


        


        


