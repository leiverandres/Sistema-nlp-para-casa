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
ducha         = Shower()

#Cocina
lavaplatos    = Dishwasher()
estufa        = Stove()
horno         = Oven()
nevera        = Fridge()

#Pasillo
impresora     = Printer()
correos       = Email()

#Habitaciones
lamparas      = [Light(), Light(), Light()]
tvs           = [TV(), TV(), TV()]

#Sala y cuartos
ventanas      = [Curtains(), Curtains(), Curtains(),
                Curtains(), Curtains(), Curtains(),
                Curtains(), Curtains(), Curtains()]
luces         = [Light(), Light(), Light(), Light(), Light(), Light(),
                 Light(), Light(), Light(), Light(), Light(), Light()]

#Patio
lavadora      = Washer()
secadora      = Dryer()

#Otros
acondicionado = Air()
sonido        = [SoundSystem(), SoundSystem()]
alarmas       = [Alert(), Alert()]


#///////////////////////////////////////////////////////////////////////

class namespace(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        self[atrr] = value

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
  [r'(.*)televisor(.*)',
  [ tvs[0].turn_on_off, True, None
    ]],
]



# #Haciendo pruebas
# tvs[0].turn_on_off(True)
# print tvs[0]
control = Controller_house()
s = raw_input("TÚ: ")
print control.respond(s)
