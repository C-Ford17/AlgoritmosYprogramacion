import datetime
import json
from equipo import Equipo
from jugador import Jugador
class Champion:
    equipos= {}
    equipos["equipos"]=[]
    with open('data.json') as file:
        equipos = json.load(file)

    def __init__(self):
        pass

    def __repr__(self):
        for equipos in self.equipos:
            return f"{self.equipos[equipos.nombre]} : {self.equipos[equipos.nombre.pais]}"

    def generarcalendario(self):
        pass

    def agregarequipo(self):
        equipoNuevo = Equipo.crearequipo()
        self.equipos["equipos"].append({
            "nombre":equipoNuevo.nombre,
            "pais":equipoNuevo.pais,
            "apodo":equipoNuevo.apodo,
            "estadio":equipoNuevo.estadio,
            "fechaDeFundacion":equipoNuevo.fechadefundacion,
            "jugadores":equipoNuevo.jugadores["jugadores"],
            "continente":None
        })
        with open('data.json','w') as file:
            json.dump(self.equipos.copy(), file, indent=4)

    def verequipos(self, s):
        for equipos in self.equipos["equipos"]:
            if s == "n":
                print({equipos["nombre"]:equipos["continente"]})
            else:
                print(equipos["nombre"])

    def eliminarequipo(self, equipo):
        for equipos in self.equipos["equipos"]:
            if equipos["nombre"] ==equipo:
                del(equipos)
                with open('data.json','w') as file:
                    json.dump(self.equipos.copy(), file, indent=4)

    def equipoContinente(self):
        for equipos in self.equipos["equipos"]:
            if equipos["pais"] in ["Albania","Alemania","Andorra","Armenia","Austria","Azerbaiyán",
            "Bélgica","Bielorrusia","Bosnia y Herzegovina","Bulgaria","Chipre","Croacia","Dinamarca",
            "Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Georgia","Grecia","Hungría",
            "Inglaterra","Irlanda","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo",
            "Macedonia del Norte","Malta","Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia",
            "Portugal","Reino Unido","República Checa","Rumania","Rusia","San Marino","Serbia","Suecia",
            "Suiza","Ucrania","Unión Europea","Vaticano"]:
                equipos["continente"]="Europa"
                with open('data.json','w') as file:
                    json.dump(self.equipos.copy(), file, indent=4)

            if equipos["pais"] in ["Brasil","Argentina","Colombia","Perú","Chile","Ecuador","Ecuador",
            "Venezuela","Bolivia","Uruguay","Guyana","Surinam","Paraguay","Guyana Francesa","Aruba",
            "Islas Malvinas","Curazao","Trinidad y Tobago","Caribe Neerlandés"]:
                equipos["continente"]="Suramerica"
                with open('data.json','w') as file:
                    json.dump(self.equipos.copy(), file, indent=4)

    def agregarjugadoraequipo(self, equipo):
        for equipos in self.equipos["equipos"]:
            if equipos["nombre"]==equipo:
                jugadornuevo = Jugador.ingresarjugador()
                equipos["jugadores"].append({
                    "nombre":jugadornuevo.nombre,
                    "pais":jugadornuevo.pais,
                    "posicion":jugadornuevo.posicion,
                    "dorsal":jugadornuevo.dorsal,
                    "fechaDeNacimiento":jugadornuevo.fdn
                    })
                with open('data.json','w') as file:
                    json.dump(self.equipos.copy(), file, indent=4)
            else:
                "Equipo no encontrado"




                
