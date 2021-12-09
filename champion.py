import json
from equipo import Equipo
from jugador import Jugador
import random
class Champion:
    equipos ={}
    FechaNumero={}

    def __init__(self):
        with open('equipos.json') as file1:
                self.equipos=json.load(file1)
        if self.equipos:
            with open('equipos.json') as file1:
                self.equipos=json.load(file1)

            if self.FechaNumero:
                with open('calendario.json') as file2:
                    self.FechaNumero=json.load(file2)
            else:
                for i in range(34):
                    self.FechaNumero.update({f"fecha {i+1}":{"fecha":{},"partidos":{}}})
                for fechas in self.FechaNumero:
                    for i in range (9):
                        self.FechaNumero[fechas]["partidos"].update({f"hora {i+1}":{}})
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
                with open('calendario.json') as file2:
                    self.FechaNumero=json.load(file2)
            else:
                for i in range(34):
                    self.FechaNumero.update({f"fecha {i+1}":{"fecha":{},"partidos":{}}})
                for fechas in self.FechaNumero:
                    for i in range (9):
                        self.FechaNumero[fechas]["partidos"].update({f"hora {i+1}":{}})
        

        
        
    def generarfecha(self):
        self.fecha= {"dia":random.randint(1,7),"mes":random.randint(1,3),"año":2022}
        return self.fecha
    
    def generarhora(self):
        hora = random.randint(1,5)
        minuto=random.randint(1,60)
        self.hora = {"hora":hora,"minuto":minuto}
        return self.hora

    def generarcalendario(self):
        x=0
        for fechas in self.FechaNumero:
            if fechas=="fecha 1":
                self.FechaNumero[fechas]["fecha"].update(self.generarfecha())
            else:
                self.FechaNumero[fechas]["fecha"]["dia"]=(self.FechaNumero[f"fecha {x+1}"]["fecha"]["dia"])+7
                self.FechaNumero[fechas]["fecha"]["mes"]=self.FechaNumero[f"fecha {x+1}"]["fecha"]["mes"]
                self.FechaNumero[fechas]["fecha"]["año"]=2022
                x+=1
                if self.FechaNumero[fechas]["fecha"]["dia"]>28:
                    self.FechaNumero[fechas]["fecha"]["dia"]=self.fecha["dia"]
                    self.FechaNumero[fechas]["fecha"]["mes"]=self.FechaNumero[f"fecha {x-1}"]["fecha"]["mes"]+1
            for i in range(9):
                if i == 0:
                    self.FechaNumero[fechas]["partidos"][f"hora {i+1}"].update(self.generarhora())
                else:
                    self.FechaNumero[fechas]["partidos"][f"hora {i+1}"]["hora"]=self.FechaNumero[fechas]["partidos"][f"hora {i}"]["hora"]+2
                    self.FechaNumero[fechas]["partidos"][f"hora {i+1}"]["minuto"]=self.FechaNumero[fechas]["partidos"][f"hora 1"]["minuto"]
        self.guardarenjson(1)
        

    def guardarenjson(self,f):
        if f ==1:
            with open('calendario.json','w') as file:
                json.dump(self.FechaNumero, file, indent=4)
        if f == 2:
            with open('equipos.json','w') as file:
                json.dump(self.equipos, file, indent=4)

    def registrargoles(self, equipo, goles):
        pass

    def partido(self):
        self.goleslocal = 0
        self.golesvisitante= 0


    def agregarequipo(self):
        self.equipoContinente()
        x=0
        x2=0
        for equipos in self.equipos:
            if self.equipos[equipos]["continente"]=="Europa":
                x+=1
        
        for equipos in self.equipos:
            if self.equipos[equipos]["continente"]=="Suramerica":
                x2+=1
        equipoNuevo = Equipo.crearequipo()
        if equipoNuevo.pais in ["Albania","Alemania","Andorra","Armenia","Austria","Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina","Bulgaria","Chipre","Croacia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Georgia","Grecia","Hungría","Inglaterra","Irlanda","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Malta","Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia","Portugal","Reino Unido","República Checa","Rumania","Rusia","San Marino","Serbia","Suecia","Suiza","Ucrania","Vaticano"]:
            if x<9:
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
                print("equipo agregado")
            else:
                print("El maximo de equipos europeos es 9")
        if equipoNuevo.pais in ["Brasil","Argentina","Colombia","Perú","Chile","Ecuador","Ecuador",
                "Venezuela","Bolivia","Uruguay","Guyana","Surinam","Paraguay","Guyana Francesa","Aruba",
                "Islas Malvinas","Curazao","Trinidad y Tobago","Caribe Neerlandés"]:
            if x2<9:
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
                print("equipo agregado")
            else:
                print("El maximo de equipos suramericanos es 9")
        if equipoNuevo.pais not in ["Brasil","Argentina","Colombia","Perú","Chile","Ecuador","Ecuador",
                "Venezuela","Bolivia","Uruguay","Guyana","Surinam","Paraguay","Guyana Francesa","Aruba",
                "Islas Malvinas","Curazao","Trinidad y Tobago","Caribe Neerlandés","Albania","Alemania",
                "Andorra","Armenia","Austria","Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina",
                "Bulgaria","Chipre","Croacia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia",
                "Finlandia","Francia","Georgia","Grecia","Hungría","Inglaterra","Irlanda","Islandia",
                "Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Malta",
                "Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia","Portugal","Reino Unido",
                "República Checa","Rumania","Rusia","San Marino","Serbia","Suecia","Suiza","Ucrania","Vaticano"]:
                print("El equipo no es suramericano o europeo")
        self.guardarenjson(2)

    def verequipos(self, s):
        for equipos in self.equipos:
            if s ==1:
                print(equipos)
            if s==2:
                print(equipos,":",self.equipos[equipos]["continente"])

    def eliminarequipo(self, equipo):
        for equipos in self.equipos:
            if equipos ==equipo:
                del self.equipos[equipo]
                print("se ha eliminado el equipo")
                self.guardarenjson(2)

    def equipoContinente(self):
        for equipos in self.equipos:
            if self.equipos[equipos]["pais"] in ["Albania","Alemania","Andorra","Armenia","Austria","Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina","Bulgaria","Chipre","Croacia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Georgia","Grecia","Hungría","Inglaterra","Irlanda","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Malta","Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia","Portugal","Reino Unido","República Checa","Rumania","Rusia","San Marino","Serbia","Suecia","Suiza","Ucrania","Vaticano"]:
                self.equipos[equipos]["continente"]="Europa"
                self.guardarenjson(2)
            if self.equipos[equipos]["pais"] in ["Brasil","Argentina","Colombia","Perú","Chile","Ecuador","Ecuador",
                "Venezuela","Bolivia","Uruguay","Guyana","Surinam","Paraguay","Guyana Francesa","Aruba",
                "Islas Malvinas","Curazao","Trinidad y Tobago","Caribe Neerlandés"]:
                self.equipos[equipos]["continente"]="Suramerica"
                self.guardarenjson(2)

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
                self.guardarenjson(2)
            else:
                "Equipo no encontrado"




                
