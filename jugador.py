class Jugador:
    nombre = str
    pais = str
    posicion = str
    dorsal = int
    fdn = None
    
    def __init__(self, nombre, pais, posicion, dorsal, fechadenacimiento):
        self.nombre = nombre
        self.pais= pais
        self.posicion = posicion
        self.dorsal = dorsal
        self.fdn = fechadenacimiento

    def ingresarjugador():
        nombre= input("nombre del jugador: ")
        pais=input("pais del jugador: ")
        posicion=input("posición del jugador: ")
        dorsal=int(input("dorsal del jugador: "))
        print("fecha de nacimiento: ")
        dia=int((input("dia: ")))
        mes=int((input("mes: ")))
        año=int((input("año: ")))
        fechadenacimiento = {"dia":dia,"mes":mes,"año":año}
        return Jugador(nombre, pais, posicion, dorsal, fechadenacimiento)
