import json
from os import path
from equipo import Equipo
from jugador import Jugador
import random
from itertools import product


class Champion:
    equipos ={}
    FechaNumero={}
    Partidos={}

    def __init__(self):
        with open('equipos.json') as file1:
                self.equipos=json.load(file1)
        if self.equipos:
            with open('calendario.json') as file2:
                self.FechaNumero=json.load(file2)

            if self.FechaNumero:
                
                with open('partidos.json') as file3:
                    self.Partidos=json.load(file3)
                if self.Partidos:
                    pass
                else:
                    for i in range(306):
                        self.Partidos.update({f"partido {i+1}":{"equipo local":{"nombre":"","puntos":None,"jugadores":{}},"equipo visitante":{"nombre":"","puntos":None,"jugadores":{}},"equipo ganador":None,"equipo perdedor":None}})
            else:
                for i in range(34):
                    self.FechaNumero.update({f"fecha {i+1}":{"fecha":{},"partidos":{}}})
                for fechas in self.FechaNumero:
                    for i in range (9):
                        self.FechaNumero[fechas]["partidos"].update({f"hora {i+1}":{}})
        else:
            for i in range(18):
                self.equipos.update({f"equipos {i+1}":{}})
            for i in range(306):
                    self.Partidos.update({f"partido {i+1}":{"equipo local":{"nombre":None,"puntos":None,"jugadores":{}},"equipo visitante":{"nombre":None,"puntos":None,"jugadores":{}},"equipo ganador":None,"equipo perdedor":None}})
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
        self.partidosenfechas()
        self.guardarenjson(1)
        

    def guardarenjson(self,f):
        if f ==1:
            with open('calendario.json','w') as file:
                json.dump(self.FechaNumero, file, indent=4)
        if f == 2:
            with open('equipos.json','w') as file:
                json.dump(self.equipos, file, indent=4)
        if f == 3:
            with open('partidos.json','w') as file:
                json.dump(self.Partidos, file, indent=4)

    def partido(self):
        k=self.permutations(self.equipos,2)
        m=[]
        for permu in k:
            m.append(permu)

        i=0
        for partido in self.Partidos:
            self.Partidos[partido]["equipo local"]["nombre"]=self.equipos[m[i][0]]["nombre"]
            self.Partidos[partido]["equipo local"]["puntos"]=self.equipos[m[i][0]]["puntos"]
            self.Partidos[partido]["equipo local"]["jugadores"]=self.equipos[m[i][0]]["jugadores"]
            self.Partidos[partido]["equipo visitante"]["nombre"]=self.equipos[m[i][1]]["nombre"]
            self.Partidos[partido]["equipo visitante"]["puntos"]=self.equipos[m[i][1]]["puntos"]
            self.Partidos[partido]["equipo visitante"]["jugadores"]=self.equipos[m[i][1]]["jugadores"]
            i+=1
        self.guardarenjson(3)

    def registrargoles(self,jugador, minuto,hora, fecha):
        golesvisitante=0
        goleslocal=0
        for fechas in self.FechaNumero:
            if self.FechaNumero[fechas]["fecha"]==fecha:
                for horas in self.FechaNumero[fechas]["partidos"]:
                    if horas==hora:
                        for equipos in self.equipos:
                            for jugadores in self.equipos[equipos]["jugadores"]:
                                if self.equipos[equipos]["jugadores"][jugadores]:
                                    if self.equipos[equipos]["jugadores"][jugadores]["nombre"]==jugador:
                                        self.equipos[equipos]["jugadores"][jugadores]["goles total"]+=1
                                        print("goles totales agregados")
                                else:
                                    pass
                        for partidos in self.Partidos:
                            if self.Partidos[partidos]["equipo local"]["nombre"]==self.FechaNumero[fechas]["partidos"][horas]["equipo local"] and self.Partidos[partidos]["equipo visitante"]["nombre"]==self.FechaNumero[fechas]["partidos"][horas]["equipo visitante"]:
                                for jugadoreslocal in self.Partidos[partidos]["equipo local"]["jugadores"]:
                                    if self.Partidos[partidos]["equipo local"]["jugadores"][jugadoreslocal]["nombre"]==jugador:
                                        self.Partidos[partidos]["equipo local"]["jugadores"][jugadoreslocal]["goles"].append(minuto)
                                        goleslocal+=len(self.Partidos[partidos]["equipo local"]["jugadores"][jugadoreslocal]["goles"])
                                for jugadoresvisitante in self.Partidos[partidos]["equipo visitante"]["jugadores"]:
                                    if self.Partidos[partidos]["equipo visitante"]["jugadores"][jugadoresvisitante]["nombre"]==jugador:
                                        self.Partidos[partidos]["equipo visitante"]["jugadores"][jugadoresvisitante]["goles"].append(minuto)
                                        golesvisitante+=len(self.Partidos[partidos]["equipo visitante"]["jugadores"][jugadoresvisitante]["goles"])
                                
                                if goleslocal>golesvisitante:
                                    self.Partidos[partidos]["equipo local"]["puntos"]+=3
                                    self.Partidos[partidos]["equipo ganador"]=self.Partidos[partidos]["equipo local"]["nombre"]
                                    self.Partidos[partidos]["equipo perdedor"]=self.Partidos[partidos]["equipo visitante"]["nombre"]
                                if golesvisitante>goleslocal:
                                    self.Partidos[partidos]["equipo visitante"]["puntos"]+=3
                                    self.Partidos[partidos]["equipo ganador"]=self.Partidos[partidos]["equipo visitante"]["nombre"]
                                    self.Partidos[partidos]["equipo perdedor"]=self.Partidos[partidos]["equipo local"]["nombre"]
                                if goleslocal==golesvisitante:
                                    self.Partidos[partidos]["equipo visitante"]["puntos"]+=1
                                    self.Partidos[partidos]["equipo local"]["puntos"]+=1
                                    self.Partidos[partidos]["equipo ganador"]="empate"
                                    self.Partidos[partidos]["equipo perdedor"]="empate"
        self.guardarenjson(3)
        self.guardarenjson(2)

    def permutations(self,iterable, r=None):
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        for indices in product(range(n), repeat=r):
            if len(set(indices)) == r:
                yield tuple(pool[i] for i in indices)

    def partidosenfechas(self):
        k=self.permutations(self.equipos,2)
        m=[]
        for permu in k:
            m.append(permu)
        i=0
        if len(self.equipos)==18:
            for fechas in self.FechaNumero:
                for x in range(9):
                    self.FechaNumero[fechas]["partidos"][f"hora {x+1}"]["equipo local"]=self.equipos[m[i][0]]["nombre"]
                    i+=1
            i=0
            for fechas in self.FechaNumero:
                for x in range(9):
                    self.FechaNumero[fechas]["partidos"][f"hora {x+1}"]["equipo visitante"]=self.equipos[m[i][1]]["nombre"]
                    i+=1
        self.guardarenjson(1)

    def agregarequipo(self):
        self.equipoContinente()
        x=0
        x2=0
        for equipos in self.equipos:
            if self.equipos[equipos]:
                if self.equipos[equipos]["continente"]=="Europa":
                    x+=1
        
        for equipos in self.equipos:
            if self.equipos[equipos]:
                if self.equipos[equipos]["continente"]=="Suramerica":
                    x2+=1
        equipoNuevo = Equipo.crearequipo()
        if equipoNuevo.pais in ["Albania","Alemania","Andorra","Armenia","Austria","Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina","Bulgaria","Chipre","Croacia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Georgia","Grecia","Hungría","Inglaterra","Irlanda","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Malta","Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia","Portugal","Reino Unido","República Checa","Rumania","Rusia","San Marino","Serbia","Suecia","Suiza","Ucrania","Vaticano"]:
            if x<9:
                for equipos in self.equipos:
                    if self.equipos[equipos]:
                        pass
                    else:
                        self.equipos[equipos].update({
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
                for equipos in self.equipos:
                    if self.equipos[equipos]:
                        pass
                    else:
                        self.equipos[equipos].update({
                        "nombre":equipoNuevo.nombre,
                        "pais":equipoNuevo.pais,
                        "apodo":equipoNuevo.apodo,
                        "estadio":equipoNuevo.estadio,
                        "fechaDeFundacion":equipoNuevo.fechadefundacion,
                        "jugadores":equipoNuevo.jugadores,
                        "continente":None,
                        "puntos":equipoNuevo.puntos,
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
            if self.equipos[equipos]:
                if s ==1:
                    print(self.equipos[equipos]["nombre"])
                if s==2:
                    print(self.equipos[equipos]["nombre"],":",self.equipos[equipos]["continente"])
        for fechas in self.FechaNumero:
            if self.FechaNumero[fechas]["fecha"]==s:
                for hora in self.FechaNumero[fechas]["partidos"]:
                    print(hora)

    def eliminarequipo(self, equipo):
        for equipos in self.equipos:
            if self.equipos[equipos]["nombre"] ==equipo:
                self.equipos[equipos].clear()
                print("se ha eliminado el equipo")
                self.guardarenjson(2)

    def equipoContinente(self):
        for equipos in self.equipos:
            if self.equipos[equipos]:
                if self.equipos[equipos]["pais"] in ["Albania","Alemania","Andorra","Armenia","Austria","Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina","Bulgaria","Chipre","Croacia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Georgia","Grecia","Hungría","Inglaterra","Irlanda","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Macedonia del Norte","Malta","Moldavia","Mónaco","Montenegro","Noruega","Países Bajos","Polonia","Portugal","Reino Unido","República Checa","Rumania","Rusia","San Marino","Serbia","Suecia","Suiza","Ucrania","Vaticano"]:
                    self.equipos[equipos]["continente"]="Europa"
                    self.guardarenjson(2)
                if self.equipos[equipos]["pais"] in ["Brasil","Argentina","Colombia","Perú","Chile","Ecuador","Ecuador",
                    "Venezuela","Bolivia","Uruguay","Guyana","Surinam","Paraguay","Guyana Francesa","Aruba",
                    "Islas Malvinas","Curazao","Trinidad y Tobago","Caribe Neerlandés"]:
                    self.equipos[equipos]["continente"]="Suramerica"
                    self.guardarenjson(2)
            else:
                pass

    def agregarjugadoraequipo(self, equipo):
        for equipos in self.equipos:
            if self.equipos[equipos]["nombre"]==equipo:
                for jugador in self.equipos[equipos]["jugadores"]:
                    if self.equipos[equipos]["jugadores"][jugador]:
                        if self.equipos[equipos]["jugadores"][jugador] ==self.equipos[equipos]["jugadores"]["jugador 12"]:
                            return "equipo lleno"
                        else:
                            pass
                    else:
                        jugadornuevo = Jugador.ingresarjugador()
                        self.equipos[equipos]["jugadores"][jugador].update({
                            "nombre":jugadornuevo.nombre,
                            "pais":jugadornuevo.pais,
                            "posicion":jugadornuevo.posicion,
                            "dorsal":jugadornuevo.dorsal,
                            "fechaDeNacimiento":jugadornuevo.fdn,
                            "goles":jugadornuevo.goles,
                            "goles total":0
                        })
                        break
                    
        self.guardarenjson(2)



                
