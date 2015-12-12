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
def print_all():
    s =  "\t\t\t _____________________________________________\n"
    s += "\t\t\t|                                             |\n"
    s += "\t\t\t| El estado de todos los elementos de la casa |\n"
    s += "\t\t\t|_____________________________________________|\n\n"

    s += "Estado de las ventanas:\n\n"
    s += ventanas[0].__str__() + "\n" + ventanas[1].__str__() + "\n"
    s += ventanas[2].__str__() + "\n" + ventanas[3].__str__() + "\n"
    s += ventanas[4].__str__() + "\n" + ventanas[5].__str__() + "\n"
    s += ventanas[6].__str__() + "\n" + ventanas[7].__str__() + "\n"
    s += ventanas[8].__str__() + "\n\n"

    s += "Estado de las luces:\n\n"
    s += luces[0].__str__() + "\n" + luces[1].__str__() + "\n" + luces[2].__str__() + "\n"
    s += luces[3].__str__() + "\n" + luces[4].__str__() + "\n" + luces[5].__str__() + "\n"
    s += luces[6].__str__() + "\n" + luces[7].__str__() + "\n" + luces[8].__str__() + "\n"
    s += luces[9].__str__() + "\n" + luces[10].__str__() + "\n" + luces[11].__str__() + "\n\n"

    s += "Estado de las lamparas:\n\n"
    s += lamparas[0].__str__() + "\n" + lamparas[1].__str__() + "\n" + lamparas[2].__str__() + "\n\n"

    s += "Estado de los televisores:\n\n"
    s += tvs[0].__str__() + "\n" + tvs[1].__str__() + "\n" + tvs[2].__str__() + "\n\n"

    s += "Estado de los equipos de sonido: \n\n"
    s += sonido[0].__str__() + "\n" + sonido[1].__str__() + "\n\n"

    s += "Estado del telefono:\n\n"
    s += telefono.__str__() + "\n\n"

    s += "Estado de la impresora:\n\n"
    s += impresora.__str__() + "\n\n"

    s += "Estado de los Emails:\n\n"
    s += correos.__str__() + "\n\n"

    s += "Estado de las alarmas:\n\n"
    s += alarmas[0].__str__() + "\n" + alarmas[1].__str__() + "\n\n"

    s += "Estado del aire acondicionado:\n\n"
    s += acondicionado.__str__() + "\n\n"

    s += "Estado de la ducha:\n\n"
    s += ducha.__str__() + "\n\n"

    s += "Estado de la lavadora:\n\n"
    s += lavadora.__str__() + "\n\n"

    s += "Estado de la secadora:\n\n"
    s += secadora.__str__() + "\n\n"

    s += "Estado del lavaplatos:\n\n"
    s += lavaplatos.__str__() + "\n\n"

    s += "Estado de la estufa:\n\n"
    s += estufa.__str__() + "\n\n"

    s += "Estado del horno:\n\n"
    s += horno.__str__() + "\n\n"

    s += "Estado de la nevera:\n\n"
    s += nevera.__str__() + "\n\n"

    return s
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

    [r"(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)volumen(.*)(tv|televisor|television|tele)(.*)",
        [ tvs[0].change_volume, True, None
        ]],

    [r"(.*)m(a|á)s(.*)volumen(.*)",
        [ tvs[0].change_volume, True, None
        ]],

    [r"(.*)(disminuya|disminuye|baja|baje)(.*)volumen(.*)(tv|televisor|television|tele)(.*)",
        [ tvs[0].change_volume, False, None
        ]],
     # falta
     # hace tv cada piso
     # set un vol o channel especefico
     # default: por favor especifica que tv quieres modificar
     # capturar datos de expresiones regulares
     # conflicto volumen tv y equipo?

     #============================= light ===================================

     [r"(.*)(enciende|prende|prenda|encienda|enciendete|enciendase|prendase|prendete)(.*)luz(.*)",
         [ lamparas[0].turn_on_off, True, None
         ]],

    [r"(.*)(apaga|apague|apaguese|apagate)(.*)luz(.*)",
        [ lamparas[0].turn_on_off, False, None
        ]],

    [r"(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)luz(.*)",
        [ lamparas[0].up_down_intensity, True, None
        ]],

    [r"(.*)m(a|á)s(.*)luz(.*)",
        [ lamparas[0].up_down_intensity, True, None
        ]],

    [r"(.*)(disminuya|disminuye|baja|baje)(.*)luz(.*)",
        [ lamparas[0].up_down_intensity, False, None
        ]],

    [r"(.*)menos(.*)luz(.*)",
        [ lamparas[0].up_down_intensity, False, None
        ]],

    #falta
    #set un valor de intensidad
    #cual luz
    #=========================== shower =====================================

    [r"(.*)(abra|abre|activa|active|enciende|encienda)(.*)(ducha|llave)(.*)",
        [ ducha.turn_on_off, True, None
        ]],

    [r"(.*)(cierre|cierra|desactiva|desactive|apaga|apague)(.*)(ducha|llave)(.*)",
        [ ducha.turn_on_off, False, None
        ]],

    [r"(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)temperatura(.*)(ducha|llave)(.*)",
        [ ducha.up_down_temp, True, None
        ]],

    [r"(.*)(disminuya|disminuye|baja|baje)(.*)temperatura(.*)(ducha|llave)(.*)",
        [ ducha.up_down_temp, False, None
        ]],

    [r"(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)flujo(.*)agua(.*)(ducha|llave)?(.*)",
        [ ducha.up_down_flow, True, None
        ]],

    [r"(.*)(disminuya|disminuye|baja|baje)(.*)flujo(.*)agua(.*)(ducha|llave)?(.*)",
        [ ducha.up_down_flow, False, None
        ]],

    #============================ Dishwasher =================================


]
#Haciendo pruebas
control = Controller_house()
print print_all()
s = "init"
while(s != "salir"):
    s = raw_input("TÚ: ")
    print control.respond(s)
