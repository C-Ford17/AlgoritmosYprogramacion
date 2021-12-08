import json
from equipo import Equipo
from jugador import Jugador
from fecha import Fecha
import random
class Champion:
    equipos ={}
    FechaNumero={}

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

        if self.FechaNumero:
            with open('calendario.json') as file:
                self.FechaNumero=json.load(file)
        else:
            for i in range(34):
                self.FechaNumero.update({f"fecha {i+1}":{"fecha":{},"partidos":{}}})
            for fechas in self.FechaNumero:
                for i in range (9):
                    self.FechaNumero[fechas]["partidos"].update({f"hora {i+1}":{}})
        
    def generarfecha(self):
        self.fecha= {"dia":None,"mes":None,"año":2022}
        self.fecha["mes"]= random.randint(1,12)
        if self.fecha["mes"] in [1,3,5,7,8,10,12]:
            self.fecha["dia"] = random.randint(1,31)
        if self.fecha["mes"] in [4,6,9,11]:
            self.fecha["dia"] = random.randint(1,30)
        if self.fecha["mes"] == 2:
            self.fecha["dia"] = random.randint(1,28)
        
        return self.fecha
    
    def generarhora(self):
        hora = random.randint(1,5)
        minuto=random.randint(1,60)
        self.hora = {"hora":hora,"minuto":minuto}
        return self.hora

    def generarcalendario(self):
        for fechas in self.FechaNumero:
            i=1
            while i<35:
                x = self.generarfecha()
                for fecha in range(0,34):
                    if self.FechaNumero[fechas]["fecha"] == x:
                        break
                    else:
                        self.FechaNumero[fechas]["fecha"].update(x)
                        i+=1
            for i in range(9):
                if i == 0:
                    self.FechaNumero[fechas]["partidos"][f"hora {i+1}"].update(self.generarhora())
                else:
                    self.FechaNumero[fechas]["partidos"][f"hora {i+1}"]["hora"]=self.FechaNumero[fechas]["partidos"][f"hora {i}"]["hora"]+2
                    self.FechaNumero[fechas]["partidos"][f"hora {i+1}"]["minuto"]=self.FechaNumero[fechas]["partidos"][f"hora 1"]["minuto"]
        self.guardarenjson(f=1)
        

    def guardarenjson(self,f):
        if f ==1:
            with open('calendario.json','w') as file:
                json.dump(self.FechaNumero, file, indent=4)
        if f == None:
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




                
