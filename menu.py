from champion import Champion
import time
from os import system

while True:
    print("Bienvenido al menu")
    print("¿Que desea hacer?")
    print("A. Registrar un equipo")
    print("B. Eliminar un equipo")
    print("C. Registrar un jugador a un equipo")
    print("D. Generar calendario")
    print("E. Registrar goles de partido")
    print("F. Ver Estadisticas")
    print("0. Salir")
    opcion =input("Escriba una de las opciones: ")
    Copa = Champion()
    if opcion =="A":
        while True:
            system("cls")
            Copa.agregarequipo()
            opcionA=input("desea agregar otro equipo? s/n: ")
            if opcionA == "s":
                True
            else:
                time.sleep(1)
                break
    if opcion =="B":
        system("cls")
        Copa.verequipos(1)
        equipoeliminar=input("ingrese el nombre del equipo que quiere eliminar: ")
        Copa.eliminarequipo(equipoeliminar)
        time.sleep(1)
    if opcion =="C":
        while True:
            system("cls")
            Copa.verequipos(1)
            equipo=input("ingrese el nombre del equipo en el que quiera al jugador: ")
            Copa.agregarjugadoraequipo(equipo)
            opcionB=input("desea agregar otro jugador? s/n: ")
            if opcionB == "s":
                system("cls")
                time.sleep(1)
                True
            else:
                time.sleep(1)
                break
    if opcion =="D":
        system("cls")
        Copa.generarcalendario()
        Copa.partido()
        time.sleep(1)
    if opcion == "E":
        system("cls")
        while True:
            system("cls")
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
                system("cls")
                time.sleep(1)
            else:
                time.sleep(1)
                break
    if opcion == "F":
        system("cls")
        print("1. Jugadores")
        print("2. Equipos")
        print("3. Campeonato")
        print("0. Volver al menu principal")
        opcion0=input("Digite una opcion: ")
        if opcion0=="1":
            system("cls")
            while True:
                system("cls")
                print("G. Ver goles marcados en el campeonato por el jugador")
                print("H. Ver goles marcados como local por el jugador")
                print("I. Ver goles marcados como visitante por el jugador")
                print("J. Ver goles marcados como europeos por el jugador")
                print("K. Ver goles marcados como suramericanos por el jugador")
                print("L. Ver goles marcados en el primer tiempo por el jugador")
                print("M. Ver goles marcados en el segundo tiempo por el jugador")
                print("0. Para volver al menu anterior")
                opcion1=input("Digite una opcion: ")
                if opcion1 == "G":
                    system("cls")
                    jugador1=input("nombre del jugador: ")
                    print(Copa.cantidadgolescampeonato(jugador1))
                    time.sleep(1)
                if opcion1 == "H":
                    system("cls")
                    jugador2=input("nombre del jugador: ")
                    print(Copa.golescomolocal(jugador2))
                    time.sleep(1)
                if opcion1 == "I":
                    system("cls")
                    jugador3=input("nombre del jugador: ")
                    print(Copa.golescomovisitante(jugador3))
                    time.sleep(1)
                if opcion1 == "J":
                    system("cls")
                    jugador4=input("nombre del jugador: ")
                    print(Copa.golescontracontinente(jugador4,"Europa"))
                    time.sleep(1)
                if opcion1 == "K":
                    system("cls")
                    jugador5=input("nombre del jugador: ")
                    print(Copa.golescontracontinente(jugador5,"Suramerica"))
                    time.sleep(1)
                if opcion1 == "L":
                    system("cls")
                    jugador6=input("nombre del jugador: ")
                    print(Copa.golesportiempo(jugador6,0,45))
                    time.sleep(1)
                if opcion1 == "M":
                    system("cls")
                    jugador7=input("nombre del jugador: ")
                    print(Copa.golesportiempo(jugador7,45,90))
                    time.sleep(1)
                if opcion1 == "0":
                    system("cls")
                    time.sleep(1)
                    break
                if opcion1 not in ["G","H","I","J","K","L","M","0"]:
                    print("opcion no encontrada")
                    time.sleep(1)
        if opcion0=="2":
            system("cls")
            while True:
                system("cls")
                print("N. Ver goles promedio marcados por el equipo")
                print("Ñ. Ver los partidos ganados, perdidos y empatados por el equipo")
                print("O. Ver el jugador con mas goles del equipo")
                print("P. Ver el promedio de edad del equipo")
                print("Q. Ver el promedio de goles de los delanteros del equipo")
                print("R. Ver partidos ganados como local del equipo")
                print("S. Ver partidos ganados como visitante del equipo")
                print("T. Ver puntos del equipo")
                print("U. Ver el jugador mas joven del equipo")
                print("0. Para volver al menu anterior")
                opcion2=input("Escriba una de las opciones: ")
                if opcion2 == "N":
                    system("cls")
                    equipo1=input("nombre del equipo: ")
                    print(Copa.golespromedio(equipo1))
                    time.sleep(1)
                if opcion2 == "Ñ":
                    system("cls")
                    equipo2=input("nombre del equipo: ")
                    print(Copa.cantidadresultadopartido(equipo2))
                    time.sleep(1)
                if opcion2 == "O":
                    system("cls")
                    equipo3=input("nombre del equipo: ")
                    print(Copa.equipojugadoresmasgoles(equipo3))
                    time.sleep(1)
                if opcion2 == "P":
                    system("cls")
                    equipo4=input("nombre del equipo: ")
                    print(Copa.promedioedad(equipo4))
                    time.sleep(1)
                if opcion2== "Q":
                    system("cls")
                    equipo5=input("nombre del equipo: ")
                    print(Copa.promediogolesdelanteros(equipo5))
                    time.sleep(1)
                if opcion2=="R":
                    system("cls")
                    equipo6=input("nombre del equipo: ")
                    print(Copa.partidosganadossegun(equipo6,"local"))
                    time.sleep(1)
                if opcion2=="S":
                    system("cls")
                    equipo6=input("nombre del equipo: ")
                    print(Copa.partidosganadossegun(equipo6,"visitante"))
                    time.sleep(1)
                if opcion2 == "T":
                    system("cls")
                    equipo7=input("nombre del equipo: ")
                    print(Copa.verpuntos(equipo7))
                    time.sleep(1)
                if opcion2 == "U":
                    system("cls")
                    equipo8=input("nombre del equipo: ")
                    print(Copa.jugadormasjoven(equipo8))
                    time.sleep(1)
                if opcion2 == "0":
                    system("cls")
                    time.sleep(1)
                    break
                if opcion2 not in ["N","Ñ","O","P","Q","R","S","T","U","0"]:
                    print("opcion no encontrada")
                    time.sleep(1)
        if opcion0=="3":
            system("cls")
            while True:
                system("cls")
                print("V. Para ver el goleador del campeonato")
                print("W. Para ver el mejor local y el mejor visitante del campeonato")
                print("X. Para ver el promedio de goles por partido del campeonato")
                print("Y. Para ver el ranking del campeonato")
                print("0. Para volver al menu anterior")
                opcion3=input("Digite una opcion: ")
                if opcion3 == "V":
                    system("cls")
                    print(Copa.goleador())
                    time.sleep(1)
                if opcion3 == "W":
                    system("cls")
                    print(Copa.mejorsegun())
                    time.sleep(1)
                if opcion3 == "X":
                    system("cls")
                    print(Copa.promediogolespartido())
                    time.sleep(1)
                if opcion3 == "Y":
                    system("cls")
                    print(Copa.ranking())
                    time.sleep(1)
                if opcion3 =="0":
                    system("cls")
                    time.sleep(1)
                    break
                if opcion3 not in ["V","W","X","Y","0"]:
                    time.sleep(1)
                    print("opcion no encontrada")
        if opcion0 =="0":
            time.sleep(1)
            break
    if opcion not in ["A","B","C","D","E","F","0"]:
        system("cls")
        time.sleep(1)
        print("opcion no encontrada")
    if opcion=="0":
        break


        


        


