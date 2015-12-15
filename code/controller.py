# -*- coding: utf-8 -*-
import string
import re
import random
from elements import *

#//////////////////////////////////////////////////////////////////////
# Creando los objetos de la casa
#Telefono ubicado en el segundo piso
telefono      = Phone()

#Baño
ducha         = Shower(1)

#Cocina
lavaplatos    = Dishwasher(1)
estufa        = Stove()
horno         = Oven(1)
nevera        = Fridge()

#Pasillo
impresora     = Printer(1)
correos       = Email()

#Habitaciones
lamparas      = [Light(1), Light(2), Light(3)]
tvs           = [TV(1), TV(2), TV(3)]

#Sala y cuartos
ventanas      = [Curtains(1), Curtains(2), Curtains(3),
                Curtains(4), Curtains(5), Curtains(6),
                Curtains(7), Curtains(8), Curtains(9)]
luces         = [Light(1), Light(2), Light(3), Light(4), Light(5), Light(6),
                 Light(7), Light(8), Light(9), Light(10), Light(11), Light(12)]

#Patio
lavadora      = Washer(1)
secadora      = Dryer(1)

#Otros
acondicionado = Air(1)
sonido        = [SoundSystem(1), SoundSystem(2)]
alarmas       = [Alert(1), Alert(2)]
#//////////////////////////////////////////////////////////////////////

class Controller_house:
    def __init__(self):
        self.keys = map(lambda x: re.compile(x[0], re.IGNORECASE), gPats)
        self.values = map(lambda x: x[1], gPats)

    def questions(self):
        opc = ["Estoy preparado para una nueva orden.",
                "Que otra orden deseas darme?",
                "Puedo irme a descansar?",
                "Te sientes a gusto con lo que hago?"]
        ans = random.choice(opc)
        return ans

    def respond(self, str):
        #Modificarlo segun nuestro proyecto
        for i in range(0, len(self.keys)):
          match = self.keys[i].match(str)
          if match:
            resp = self.values[i]
            return resp[0](resp[1],resp[2])

    def stateHouse(self): #Aca se dira el estado actual de la casa
        pass

gPats = [
    #========================= TV ========================================
    [r"(.*)(enciende|prende|prenda|encienda|enciendete|enciendase|prendase|prendete)(.*)(tv|televisor|television|tele)(.*)",#cual?
        [ tvs[0].turn_on_off, True, None
        ]],

    [r"(.*)(tv|televisor|television|tele)(.*)(enciende|prende|prenda|encienda|enciendete|enciendase|prendase|prendete)(.*)",#cual?
        [ tvs[0].turn_on_off, True, None
        ]],

    [r"(.*)(apaga|apague|apaguese|apagate)(.*)(tv|televisor|television|tele)(.*)",#cual?
        [ tvs[0].turn_on_off, False, None
        ]],

    [r"(.*)(tv|televisor|television|tele)(.*)(apaga|apague|apaguese|apagate)(.*)",#cual?
        [ tvs[0].turn_on_off, False, None
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo) canal(.*)",
        [ tvs[0].change_channel, True, None
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo)(.*)",
        [ tvs[0].change_channel, True, None
        ]],

    [r"((.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(anterior) canal(.*)",
        [ tvs[0].change_channel, False, None
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)",
        [ tvs[0].change_channel, False, None
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)",
        [ tvs[0].change_channel, False, None
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)(.*)canal(.*)",
        [ tvs[0].change_channel, True, None
        ]],

    [r"(.*)(aumente|incremente|suba)?(.*)volumen(.*)(tv|televisor|television|tele)(.*)",
        [ tvs[0].change_channel, False, None
        ]],
     # falta
     # default: por favor especifica que tv quieres modificar
     # capturar datos de expresiones regulares
     #conflicto volumen tv y equipo?
     #======================================================================
]


<<<<<<< HEAD

# #Haciendo pruebas
# tvs[0].turn_on_off(True)
# print tvs[0]
control = Controller_house()
s = "init"
while(s != "salir"):
    s = raw_input("TÚ: ")
    print control.respond(s)
=======
#Haciendo pruebas
print tvs[0]
print tvs[1]
print tvs[2]

print telefono
print impresora
print correos

print ducha

print estufa
print lavaplatos
print horno
print nevera

print lamparas[0]
print lamparas[1]
print lamparas[2]
print ventanas[0]
print ventanas[1]
print ventanas[2]
print ventanas[3]
print ventanas[4]
print ventanas[5]
print ventanas[6]
print ventanas[7]
print ventanas[8]

print luces[0]
print luces[1]
print luces[2]
print luces[3]
print luces[4]
print luces[5]
print luces[6]
print luces[7]
print luces[8]
print luces[9]
print luces[10]
print luces[11]

print lavadora
print secadora

print acondicionado
print sonido[0]
print sonido[1]
print alarmas[0]
print alarmas[1]
>>>>>>> 10c82af9624cc42c75eeef014848665f86c6a4e4
