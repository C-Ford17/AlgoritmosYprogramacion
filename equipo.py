from jugador import Jugador
class Equipo:
    jugadores = {}
    jugadores["jugadores"]=[]
    nombre= str
    apodo = str
    pais = str
    estadio = str
    fechadefundacion = None

    def __init__(self, nombre, apodo, pais, estadio, fechadefundacion):
        self.nombre= nombre
        self.apodo = apodo
        self.pais = pais
        self.estadio = estadio
        self.fechadefundacion = fechadefundacion

    def agregarjugador(self):
        jugadornuevo = Jugador.ingresarjugador()
        self.jugadores["jugadores"].append({
            "nombre":jugadornuevo.nombre,
            "pais":jugadornuevo.pais,
            "estadio":jugadornuevo.estadio,
            "jugadores":jugadornuevo.jugadores
            })
         
    def crearequipo():
        nombre = input("nombre del equipo: ")
        apodo= input("apodo del equipo: ")
        pais= input("pais del equipo: ")
        estadio= input("estadio del equipo: ")
        dia=int((input("dia: ")))
        mes=int((input("mes: ")))
        año=int((input("año: ")))
        fechadefundacion = {"dia":dia,"mes":mes,"año":año}
        return Equipo(nombre,apodo,pais,estadio,fechadefundacion)

