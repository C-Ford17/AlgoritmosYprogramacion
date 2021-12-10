'''import random
import json
class nosexd:
    FechaNumero = {}

    def __init__(self) -> None:
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
        hora = random.randint(1,24)
        minuto=random.randint(1,60)
        self.hora = {"hora":hora,"minuto":minuto}
        return self.hora

    def generarcalendario(self):
        for fechas in self.FechaNumero:
            
            self.FechaNumero[fechas]["fecha"].update(self.generarfecha())
            for i in range(9):
                self.FechaNumero[fechas]["partidos"][f"hora {i+1}"].update(self.generarhora())
        
        with open('calendarioPrubea.json','w') as file:
                json.dump(self.FechaNumero, file, indent=4)

nuevo = nosexd()
nuevo.generarcalendario()'''
xdd={"jugadores":{"jugador 1":{
                "nombre": "Jordi Alba",
                "pais": "Espa\u00f1a",
                "posicion": "Defensa",
                "dorsal": 18,
                "fechaDeNacimiento": {
                    "dia": 21,
                    "mes": 3,
                    "a\u00f1o": 1989
                },
                "puntos": 0},
                "jugador 2":{
                "nombre": "Gerard pique",
                "pais": "Espa\u00f1a",
                "posicion": "Defensa",
                "dorsal": 3,
                "fechaDeNacimiento": {
                    "dia": 2,
                    "mes": 2,
                    "a\u00f1o": 1987
                },
                "puntos": 0},
                "jugador 3":{},
                "jugador 4":{
                "nombre": "manolo",
                "pais": "Espa\u00f1a",
                "posicion": "Defensa",
                "dorsal": 3,
                "fechaDeNacimiento": {
                    "dia": 2,
                    "mes": 2,
                    "a\u00f1o": 1987
                }
                }
                }
                }
for i in range(4):
    if xdd["jugadores"][f"jugador {i+1}"]:
        print("no vacio")
        pass
    else:
        print("vacio")
        