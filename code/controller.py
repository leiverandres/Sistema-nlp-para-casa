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
lamparas      = [Light(1, "Lampara"), Light(2, "Lampara"), Light(3, "Lampara")]
tvs           = [TV(1), TV(2), TV(3)]

#Sala y cuartos
ventanas      = [Curtains(1), Curtains(2), Curtains(3),
                Curtains(4), Curtains(5), Curtains(6),
                Curtains(7), Curtains(8), Curtains(9)]
luces         = [Light(1, "Luz"), Light(2, "Luz"), Light(3, "Luz"), Light(4, "Luz"), Light(5, "Luz"), Light(6, "Luz"),
                 Light(7, "Luz"), Light(8, "Luz"), Light(9, "Luz"), Light(10, "Luz"), Light(11, "Luz"), Light(12, "Luz")]

#Patio
lavadora      = Washer(1)
secadora      = Dryer(1)

#Otros
acondicionado = Air(1)
sonido        = [SoundSystem(1), SoundSystem(2)]
alarmas       = [Alert(1), Alert(2)]
#//////////////////////////////////////////////////////////////////////
def print_objs(objs, state):
    s = ""
    for i in range(len(objs)):
        s += objs[i].turn_on_off(state) + "\n"
    return s

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
            if(len(resp) == 1):
                return resp[0]()
            elif(len(resp) == 2):
                return resp[0](resp[1])
            elif(len(resp) == 3):
                return resp[0](resp[1], resp[2])
            else:
                return "Error, no hay argumentos ni función"

    def stateHouse(self): #Aca se dira el estado actual de la casa
        pass

gPats = [
    #========================= TV ========================================
    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ tvs[0].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ tvs[1].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ tvs[2].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(todos )?(tvs|televisores|televisiones|teles)(.*)',
        [ print_objs, tvs, True
        ]],

    [r'(.*)(apaga|apague)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ tvs[0].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ tvs[1].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ tvs[2].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(todos )?(tvs|televisores|televisiones|teles)(.*)',
        [ print_objs, tvs, False
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo) canal(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)",
        [ tvs[0].change_channel, True
        ]],


    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo) canal(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)",
        [ tvs[1].change_channel, True
        ]],


    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo) canal(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)",
        [ tvs[2].change_channel, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)",
        [ tvs[0].change_channel, True
        ]],


    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)",
        [ tvs[1].change_channel, True
        ]],


    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)",
        [ tvs[2].change_channel, True
        ]],

    [r'(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ tvs[0].change_channel, False
        ]],

    [r'(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ tvs[1].change_channel, False
        ]],

    [r'(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ tvs[2].change_channel, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ tvs[0].change_volume, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ tvs[1].change_volume, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ tvs[2].change_volume, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|reduce|reduzca|merme|merma|menos)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ tvs[0].change_volume, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|reduce|reduzca|merme|merma|menos)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ tvs[1].change_volume, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|reduce|reduzca|merme|merma|menos)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ tvs[2].change_volume, False
        ]],

     # falta
     # set un vol o channel especefico
     # default: por favor especifica que tv quieres modificar
     # capturar datos de expresiones regulares
     # conflicto volumen tv y equipo?

     #============================= light ===================================

     [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)',
         [ lamparas[0].turn_on_off, True
         ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)',
        [ lamparas[0].turn_on_off, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)luz(.*)',
        [ lamparas[0].up_down_intensity, True
        ]],

    [r'(.*)(m(a|á)s)(.*)luz(.*)',
        [ lamparas[0].up_down_intensity, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje)(.*)luz(.*)',
        [ lamparas[0].up_down_intensity, False
        ]],

    [r'(.*)menos(.*)luz(.*)',
        [ lamparas[0].up_down_intensity, False
        ]],

    #falta
    #set un valor de intensidad
    #cual luz
    #luces otros sitios
    #=========================== shower =====================================

    [r'(.*)(abra|abre|activa|active|enciende|encienda|activa|active)(.*)(ducha|llave)(.*)',
        [ ducha.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)(ducha|llave)(.*)',
        [ ducha.turn_on_off, False
        ]],

    [r'(.*)(cierre|cierra|desactiva|desactive|apaga|apague)(.*)(ducha|llave)(.*)',
        [ ducha.turn_on_off, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)temperatura(.*)(ducha|llave)(.*)',
        [ ducha.up_down_temp, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje)(.*)temperatura(.*)(ducha|llave)(.*)',
        [ ducha.up_down_temp, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube)(.*)flujo(.*)(agua)?(.*)(ducha|llave)(.*)',
        [ ducha.up_down_flow, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje)(.*)flujo(.*)(agua)?(.*)(ducha|llave)?(.*)',
        [ ducha.up_down_flow, False
        ]],

    #================================= Dishwasher =============================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)lavaplatos(.*)',
        [ lavaplatos.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)lavaplatos(.*)',
        [ lavaplatos.turn_on_off, False
        ]],

    [r'(.*)(hay|todos|estan)(.*)platos(.*)(sucios|por lavar|para lavar)(\?)?(.*)',
        [ lavaplatos.get_have_dish
        ]],

    [r'(.*)(limpie|limpia|lave|lava)(.*)platos(.*)(sucios|por lavar|para lavar)?(.*)',
        [ lavaplatos.wash, 10
        ]],

    # capturar set time

    #================================ Sound System ============================

    #================================= ventanas ===============================

    #================================= printer ================================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)impresora(.*)',
        [ impresora.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)impresora(.*)',
        [ impresora.turn_on_off, False
        ]],

    [r'(.*)(imprima|imprime|imprimir)(.*)(copias)?(.*)',
        [ impresora.print_out, 5, 1
        ]],

    # falta
    # capturar copias y No paginas
    #================================= Email ==================================

    #================================= Air ====================================

    #================================= Alarmas ================================

]

#agregar ? computador, triturador de comida, licuadora,
#Haciendo pruebas
control = Controller_house()
# print print_all()
s = ''
while(s != "salir"):
    s = raw_input("TÚ: ")
    print control.respond(s)
