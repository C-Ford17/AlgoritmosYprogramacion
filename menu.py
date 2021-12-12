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
    print("G. Cantidad de goles del campeonato")
    print("H. Salir")
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
    if opcion == "G":
        jugador1=input("nombre del jugador: ")
        print(Copa.cantidadgolescampeonato(jugador1))
    if opcion == "H":
        jugador2=input("nombre del jugador: ")
        print(Copa.golescomolocal(jugador2))
    if opcion == "I":
        jugador3=input("nombre del jugador: ")
        print(Copa.golescomovisitante(jugador3))
    if opcion == "J":
        jugador4=input("nombre del jugador: ")
        print(Copa.golescontracontinente(jugador4,"Europa"))
    if opcion == "K":
        jugador5=input("nombre del jugador: ")
        print(Copa.golescontracontinente(jugador5,"Suramerica"))
    if opcion == "L":
        jugador6=input("nombre del jugador: ")
        print(Copa.golesportiempo(jugador6,0,45))
    if opcion == "M":
        jugador7=input("nombre del jugador: ")
        print(Copa.golesportiempo(jugador7,45,90))
    if opcion == "N":
        equipo1=input("nombre del equipo: ")
        print(Copa.golespromedio(equipo1))
    if opcion == "Ñ":
        equipo2=input("nombre del equipo: ")
        print(Copa.cantidadresultadopartido(equipo2))
    if opcion == "O":
        equipo3=input("nombre del equipo: ")
        print(Copa.equipojugadoresmasgoles(equipo3))
    if opcion == "P":
        equipo4=input("nombre del equipo: ")
        print(Copa.promedioedad(equipo4))
    if opcion== "Q":
        equipo5=input("nombre del equipo: ")
        print(Copa.promediogolesdelanteros(equipo5))
    if opcion=="R":
        equipo6=input("nombre del equipo: ")
        print(Copa.partidosganadossegun(equipo6,"local"))
    if opcion=="S":
        equipo6=input("nombre del equipo: ")
        print(Copa.partidosganadossegun(equipo6,"visitante"))
    if opcion == "T":
        equipo7=input("nombre del equipo: ")
        print(Copa.verpuntos(equipo7))
    if opcion == "U":
        equipo8=input("nombre del equipo: ")
        print(Copa.jugadormasjoven(equipo8))
    if opcion == "V":
        print(Copa.goleador())
    if opcion == "W":
        print(Copa.mejorsegun())
    if opcion == "X":
        print(Copa.promediogolespartido())
    if opcion == "Y":
        print(Copa.ranking())
    if opcion =="Z":
        break
    if opcion not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P"]:
        print("opcion no encontrada")


        


        


