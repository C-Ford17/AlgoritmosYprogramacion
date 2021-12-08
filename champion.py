import json
from equipo import Equipo
from jugador import Jugador
from fecha import Fecha
import random
class Champion:
    equipos ={}
    FechaNumero=[]

    def __init__(self):
        if self.equipos:
            with open('data.json') as file:
                self.equipos=json.load(file)            
        else:
            self.equipos = {"###": {
            "nombre": "###",
            "pais": "###",
            "apodo": "###",
            "estadio": "###",
            "fechaDeFundacion": {
                "dia": 1,
                "mes": 1,
                "a\u00f1o": 1
            },
            "jugadores": {},
            "continente": None,
            "puntos":0
            }}
        
                
    def generarcalendario(self):
        for i in range(38):
            dia=random.randint(1,28)
            mes=random.randint(1,12)
            año=2022
            fecha = (dia,mes,año)
            hora = (random.randint(1,24),random.randint(1,60))
            self.FechaNumero.append({f"fecha{i+1}":fecha,"hora":hora})
            with open('calendario.json','w') as file:
                json.dump(self.FechaNumero, file, indent=4)

    def guardarenjson(self):
        with open('data.json','w') as file:
            json.dump(self.equipos, file, indent=4)

    def partido(self):
        pass

    def agregarequipo(self):
        equipoNuevo = Equipo.crearequipo()
        self.equipos.update({equipoNuevo.nombre:{}})
        self.equipos[equipoNuevo.nombre].update({
            "nombre":equipoNuevo.nombre,
            "pais":equipoNuevo.pais,
            "apodo":equipoNuevo.apodo,
            "estadio":equipoNuevo.estadio,
            "fechaDeFundacion":equipoNuevo.fechadefundacion,
            "jugadores":equipoNuevo.jugadores,
            "continente":None,
            "puntos":equipoNuevo.puntos
            })
        self.guardarenjson()

    def verequipos(self, s):
        for equipos in self.equipos:
            if s =="s":
                print(equipos)
            else:
                print(equipos,",",self.equipos[equipos]["continente"])

    def eliminarequipo(self, equipo):
        for equipos in self.equipos:
            if equipos ==equipo:
                del self.equipos[equipo]
                print("se ha eliminado el equipo")
                self.guardarenjson()

    def equipoContinente(self):
        for equipos in self.equipos:
            if self.equipos[equipos]["pais"] in ["Albania","Alemania","Andorra","Armenia","Austria","Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina","Bulgaria","Chipre","Croacia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Georgia","Grecia","Hungría","Inglaterra","Irlanda","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Malta","Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia","Portugal","Reino Unido","República Checa","Rumania","Rusia","San Marino","Serbia","Suecia","Suiza","Ucrania","Vaticano"]:
                self.equipos[equipos]["continente"]="Europa"
                self.guardarenjson()
            if self.equipos[equipos]["pais"] in ["Brasil","Argentina","Colombia","Perú","Chile","Ecuador","Ecuador",
                "Venezuela","Bolivia","Uruguay","Guyana","Surinam","Paraguay","Guyana Francesa","Aruba",
                "Islas Malvinas","Curazao","Trinidad y Tobago","Caribe Neerlandés"]:
                self.equipos[equipos]["continente"]="Suramerica"
                self.guardarenjson()

    def agregarjugadoraequipo(self, equipo):
        for equipos in self.equipos:
            if equipos==equipo:
                jugadornuevo = Jugador.ingresarjugador()
                self.equipos[equipos]["jugadores"].update({
                    "nombre":jugadornuevo.nombre,
                    "pais":jugadornuevo.pais,
                    "posicion":jugadornuevo.posicion,
                    "dorsal":jugadornuevo.dorsal,
                    "fechaDeNacimiento":jugadornuevo.fdn,
                    "puntos":jugadornuevo.puntos
                    })
                self.guardarenjson()
            else:
                "Equipo no encontrado"




                
