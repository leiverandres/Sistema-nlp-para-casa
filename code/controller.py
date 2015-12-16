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

def ans_default():
    ans = ["No entiendo su consulta, por favor intentelo de nuevo",
            "Por favor sea más especifico",
            "Su consulta no es valida, vuelva a intentarlo"]
    s = random.choice(ans)
    return s

def exit_default():
    ans = ["Hasta pronto, que tenga un buen dia",
            "May the force be with you",
            "Nos vemos en una proxima ocasión",
            "Hasta luego"]
    s = random.choice(ans)
    return s

def tv_default():
    ans = ["Especifique el televisor sobre el que quiere actuar",
            "No puedo definir a que luz te refieres",
            "Dame un poco mas de detalle, que televisor quieres modificar",
            "Repite la instrucción especificando el televisor"]
    s = random.choice(ans)
    return s

def luz_default():
    ans = ["Especifique la luz sobre la que quiere actuar",
            "No puedo definir a que luz te refieres",
            "Dame un poco mas de detalle, que luz quieres modificar",
            "Repite la instrucción especificando la luz"]
    s = random.choice(ans)
    return s

def lampara_default():
    ans = ["Especifique la lampara sobre la que quiere actuar",
            "No puedo definir a que lampara te refieres",
            "Dame un poco mas de detalle, que lampara quieres modificar",
            "Repite la instrucción especificando la lampara"]
    s = random.choice(ans)
    return s

def estufa_default():
    ans = ["Especifique la hornilla sobre la que quiere actuar",
            "No puedo definir a que hornilla te refieres",
            "Dame un poco mas de detalle, que hornilla quieres modificar",
            "Repite la instrucción especificando la hornilla"]
    s = random.choice(ans)
    return s

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

    s += "Estado de las ventanas:"
    s += "\n" + ventanas[0].__str__() + "\n" + ventanas[1].__str__() + "\n"
    s += ventanas[2].__str__() + "\n" + ventanas[3].__str__() + "\n"
    s += ventanas[4].__str__() + "\n" + ventanas[5].__str__() + "\n"
    s += ventanas[6].__str__() + "\n" + ventanas[7].__str__() + "\n"
    s += ventanas[8].__str__() + "\n\n"

    s += "Estado de las luces:"
    s += "\n" + luces[0].__str__() + "\n" + luces[1].__str__() + "\n" + luces[2].__str__() + "\n"
    s += luces[3].__str__() + "\n" + luces[4].__str__() + "\n" + luces[5].__str__() + "\n"
    s += luces[6].__str__() + "\n" + luces[7].__str__() + "\n" + luces[8].__str__() + "\n"
    s += luces[9].__str__() + "\n" + luces[10].__str__() + "\n" + luces[11].__str__() + "\n\n"

    s += "Estado de las lamparas:"
    s += "\n" + lamparas[0].__str__() + "\n" + lamparas[1].__str__() + "\n" + lamparas[2].__str__() + "\n\n"

    s += "Estado de los televisores:"
    s += "\n" + tvs[0].__str__() + "\n" + tvs[1].__str__() + "\n" + tvs[2].__str__() + "\n\n"

    s += "Estado de los equipos de sonido:"
    s += "\n" + sonido[0].__str__() + "\n" + sonido[1].__str__() + "\n\n"

    s += "Estado del telefono:"
    s += "\n" + telefono.__str__() + "\n\n"

    s += "Estado de la impresora:"
    s += "\n" + impresora.__str__() + "\n\n"

    s += "Estado de los Emails:"
    s += "\n" + correos.__str__() + "\n\n"

    s += "Estado de las alarmas:"
    s += "\n" + alarmas[0].__str__() + "\n" + alarmas[1].__str__() + "\n\n"

    s += "Estado del aire acondicionado:"
    s += "\n" + acondicionado.__str__() + "\n\n"

    s += "Estado de la ducha:"
    s += "\n" + ducha.__str__() + "\n\n"

    s += "Estado de la lavadora:"
    s += "\n" + lavadora.__str__() + "\n\n"

    s += "Estado de la secadora:"
    s += "\n" + secadora.__str__() + "\n\n"

    s += "Estado del lavaplatos:"
    s += "\n" + lavaplatos.__str__() + "\n\n"

    s += "Estado de la estufa:"
    s += "\n" + estufa.__str__() + "\n\n"

    s += "Estado del horno:"
    s += "\n" + horno.__str__() + "\n\n"

    s += "Estado de la nevera:"
    s += "\n" + nevera.__str__() + "\n\n"
    return s

def pull_data(extract, match, current, opc = False):
    if(extract):
        if(not opc):
            if(match.group("numbers1")):
                return int(match.group("numbers1"))
            elif(match.group("msj")):
                return match.group("msj")
        if(opc):
            return [int(match.group("numbers1")), int(match.group("numbers2"))]
    return current

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
        for i in range(0, len(self.keys)):
          match = self.keys[i].match(str)
          if match:
            resp = self.values[i]
            if(len(resp) == 2):
                return resp[1]()
            elif(len(resp) == 3):
                s = pull_data(resp[0], match, resp[2])
                return resp[1](s)
            elif(len(resp) == 4):
                s1 = pull_data(resp[0], match, resp[2])
                s2 = pull_data(resp[0], match, resp[3])
                return resp[1](s1, s2)
            elif(len(resp) == 5):
                s = pull_data(resp[0], match, resp[3], resp[4]) # Caso especial para impresora
                return resp[1](s[0], s[1])
            else:
                return "Error, no hay argumentos ni función"

gPats = [
    #========================= TV =============================================
    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].turn_on_off, True
        ]],

    [r"(pon|pasalo|ponlo|cambia|pasa|pase|ponga|cambie)( el| en el| al) canal (?P<numbers1>[0-9]+)( en el| del)( tv| televisor| television| tele)( del| de la)( sala| primer piso| piso (primero|1|uno))(.*)",
        [ True, tvs[0].set_channel, 1
        ]],

    [r"(pon|pasalo|ponlo|cambia|pasa|pase|ponga|cambie)( el| en el| al) canal (?P<numbers1>[0-9]+)( en el| del)( tv| televisor| television| tele)( del| de la)( primera habitaci(o|ó)n)(.*)",
        [ True, tvs[1].set_channel, 1
        ]],

    [r"(pon|pasalo|ponlo|cambia|pasa|pase|ponga|cambie)( el| en el| al) canal (?P<numbers1>[0-9]+)( en el| del)( tv| televisor| television| tele)( del| de la)( segunda habitaci(o|ó)n)(.*)",
        [ True, tvs[2].set_channel, 1
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(todos )?(tvs|televisores|televisiones|teles)(.*)',
        [ False, print_objs, tvs, True
        ]],

    [r'(.*)(apaga|apague)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(todos )?(tvs|televisores|televisiones|teles)(.*)',
        [ False, print_objs, tvs, False
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo) canal(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)",
        [ False, tvs[0].change_channel, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo|al) canal(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)",
        [ False, tvs[1].change_channel, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo|al) canal(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)",
        [ False, tvs[2].change_channel, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo|al)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)",
        [ False, tvs[0].change_channel, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo|al)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)",
        [ False, tvs[1].change_channel, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (siguiente|pr(o|ó)ximo|al)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)",
        [ False, tvs[2].change_channel, True
        ]],

    [r'(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].change_channel, False
        ]],

    [r'(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].change_channel, False
        ]],

    [r'(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)canal (pasado|anterior)(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].change_channel, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].change_volume, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].change_volume, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].change_volume, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|reduce|reduzca|merme|merma|menos)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].change_volume, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|reduce|reduzca|merme|merma|menos)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].change_volume, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|reduce|reduzca|merme|merma|menos)(.*)volumen(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].change_volume, False
        ]],

    [r'(.*)volumen(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].get_volume
        ]],

    [r'(.*)volumen(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].get_volume
        ]],

    [r'(.*)volumen(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].get_volume
        ]],

    [r'(.*)canal(.*)(tv|televisor|television|tele)(.*)(sala|primer piso|piso (primero|1|uno))(.*)',
        [ False, tvs[0].get_channel
        ]],

    [r'(.*)canal(.*)(tv|televisor|television|tele)(.*)(primera habitaci(o|ó)n)(.*)',
        [ False, tvs[1].get_channel
        ]],

    [r'(.*)canal(.*)(tv|televisor|television|tele)(.*)(segunda habitaci(o|ó)n)(.*)',
        [ False, tvs[2].get_channel
        ]],

    [r'(.*)(tv|televisor|television|tele)(.*)',
        [ False, tv_default
        ]],

  #============================= light ========================================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)entrada(.*)',
        [ False, luces[0].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)sala(.*)',
        [ False, luces[1].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)(patio|zona de lavado)(.*)',
        [ False, luces[2].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)comedor(.*)',
        [ False, luces[3].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)cocina(.*)',
        [ False, luces[4].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)(pasillo|corredor)(.*)primer piso(.*)',
        [ False, luces[5].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)escaleras(.*)',
        [ False, luces[6].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)(pasillo|corredor)(.*)segundo piso(.*)',
        [ False, luces[7].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)sala(.*)segundo piso(.*)',
        [ False, luces[8].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)primera habitaci(o|ó)n(.*)',
        [ False, luces[9].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)segunda habitaci(o|ó)n(.*)',
        [ False, luces[10].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)luz(.*)baño(.*)',
        [ False, luces[11].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(todas)?(.*)luces(.*)',
        [ False, print_objs, luces, True
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)entrada(.*)',
        [ False, luces[0].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)sala(.*)',
        [ False, luces[1].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)(patio|zona de lavado)(.*)',
        [ False, luces[2].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)comedor(.*)',
        [ False, luces[3].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)cocina(.*)',
        [ False, luces[4].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)(pasillo|corredor)(.*)primer piso(.*)',
        [ False, luces[5].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)escaleras(.*)',
        [ False, luces[6].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)(pasillo|corredor)(.*)segundo piso(.*)',
        [ False, luces[7].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)sala(.*)segundo piso(.*)',
        [ False, luces[8].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)primera habitaci(o|ó)n(.*)',
        [ False, luces[9].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)segunda habitaci(o|ó)n(.*)',
        [ False, luces[10].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)luz(.*)baño(.*)',
        [ False, luces[11].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(todas)?(.*)luces(.*)',
        [ False, print_objs, luces, False
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz de la entrada(.*)',
        [ True, luces[0].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz de la sala(.*)',
        [ True, luces[1].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz del (patio|zona de lavado)(.*)',
        [ True, luces[2].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz del comedor(.*)',
        [ True, luces[3].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz de la cocina(.*)',
        [ True, luces[4].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz del (pasillo|corredor) del primer piso(.*)',
        [ True, luces[5].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz de las escaleras(.*)',
        [ True, luces[6].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz del (pasillo|corredor) del segundo piso(.*)',
        [ True, luces[7].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz la sala del segundo piso(.*)',
        [ True, luces[8].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz de la primera habitaci(o|ó)n(.*)',
        [ True, luces[9].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz de la segunda habitaci(o|ó)n(.*)',
        [ True, luces[10].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad)(.*)luz del baño(.*)',
        [ True, luces[11].set_intensity, 1
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)entrada(.*)',
        [ False, luces[0].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)sala(.*)',
        [ False, luces[1].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)(patio|zona de lavado)(.*)',
        [ False, luces[2].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)comedor(.*)',
        [ False, luces[3].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)cocina(.*)',
        [ False, luces[4].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)(pasillo|corredor)(.*)primer piso(.*)',
        [ False, luces[5].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)escaleras(.*)',
        [ False, luces[6].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)(pasillo|corredor)(.*)segundo piso(.*)',
        [ False, luces[7].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)sala(.*)segundo piso(.*)',
        [ False, luces[8].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)primera habitaci(o|ó)n(.*)',
        [ False, luces[9].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)segunda habitaci(o|ó)n(.*)',
        [ False, luces[10].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)luz(.*)baño(.*)',
        [ False, luces[11].up_down_intensity, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)entrada(.*)',
        [ False, luces[0].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)sala(.*)',
        [ False, luces[1].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)(patio|zona de lavado)(.*)',
        [ False, luces[2].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)comedor(.*)',
        [ False, luces[3].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)cocina(.*)',
        [ False, luces[4].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)(pasillo|corredor)(.*)primer piso(.*)',
        [ False, luces[5].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)escaleras(.*)',
        [ False, luces[6].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)(pasillo|corredor)(.*)segundo piso(.*)',
        [ False, luces[7].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)sala(.*)segundo piso(.*)',
        [ False, luces[8].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)primera habitaci(o|ó)n(.*)',
        [ False, luces[9].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)segunda habitaci(o|ó)n(.*)',
        [ False, luces[10].up_down_intensity, False
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)luz(.*)baño(.*)',
        [ False, luces[11].up_down_intensity, False
        ]],

    [r'(.*)intensidad(.*)luz(.*)entrada(.*)',
        [ False, luces[0].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)sala(.*)',
        [ False, luces[1].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)(patio|zona de lavado)(.*)',
        [ False, luces[2].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)comedor(.*)',
        [ False, luces[3].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)cocina(.*)',
        [ False, luces[4].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)(pasillo|corredor)(.*)primer piso(.*)',
        [ False, luces[5].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)escaleras(.*)',
        [ False, luces[6].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)(pasillo|corredor)(.*)segundo piso(.*)',
        [ False, luces[7].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)sala(.*)segundo piso(.*)',
        [ False, luces[8].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)primera habitaci(o|ó)n(.*)',
        [ False, luces[9].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)segunda habitaci(o|ó)n(.*)',
        [ False, luces[10].get_intensity
        ]],

    [r'(.*)intensidad(.*)luz(.*)baño(.*)',
        [ False, luces[11].get_intensity
        ]],

    [r'(.*)luz(.*)',
        [ False, luz_default
        ]],

     #================================= Lamparas ==============================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)l(á|a)mpara(.*)de la izquierda de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[0].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)l(á|a)mpara(.*)de la derecha de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[1].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)l(á|a)mpara(.*)de la segunda habitaci(o|ó)n(.*)',
        [ False, lamparas[2].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(todas)?(.*)l(á|a)mparas(.*)',
        [ False, print_objs, lamparas, True
        ]],

    [r'(.*)(apaga|apague)(.*)(.*)l(á|a)mpara(.*)de la izquierda de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[0].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(.*)l(á|a)mpara(.*)de la derecha de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[1].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(.*)l(á|a)mpara(.*)de la segunda habitaci(o|ó)n(.*)',
        [ False, lamparas[2].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(todas)?(.*)l(á|a)mparas(.*)',
        [ False, print_objs, lamparas, False
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad )(.*)l(á|a)mpara(.*)de la izquierda de la primera habitaci(o|ó)n(.*)',
        [ True, lamparas[0].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad )(.*)l(á|a)mpara(.*)de la derecha de la primera habitaci(o|ó)n(.*)',
        [ True, lamparas[1].set_intensity, 1
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca) (?P<numbers1>[0-9]+)( (de|en|como) intensidad )(.*)l(á|a)mpara(.*)de la segunda habitaci(o|ó)n(.*)',
        [ True, lamparas[2].set_intensity, 1
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)l(á|a)mpara(.*)de la izquierda de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[0].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)l(á|a)mpara(.*)de la derecha de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[1].up_down_intensity, True
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)l(á|a)mpara(.*)de la segunda habitaci(o|ó)n(.*)',
        [ False, lamparas[2].up_down_intensity, True
        ]],

    [r'(.*)intensidad(.*)l(á|a)mpara(.*)de la izquierda de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[0].get_intensity
        ]],

    [r'(.*)intensidad(.*)l(á|a)mpara(.*)de la derecha de la primera habitaci(o|ó)n(.*)',
        [ False, lamparas[1].get_intensity
        ]],

    [r'(.*)intensidad(.*)l(á|a)mpara(.*)de la segunda habitaci(o|ó)n(.*)',
        [ False, lamparas[2].get_intensity
        ]],

    [r'(.*)l(á|a)mpara(.*)',
        [ False, lampara_default
        ]],

     #================================= Air ===================================

    [r'(.*)(apaga|apague|desactive|desactiva)(.*)aire(.*)',
        [ False, acondicionado.turn_on_off, False
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)aire(.*)',
        [ False, acondicionado.turn_on_off, True
        ]],

    [r'(por favor )?(ponga|pon|pongale|coloque|coloquele|coloca) (?P<numbers1>[0-9]+)( grados)?((.*)temperatura)(.*)aire(.*)',
        [ True, acondicionado.put_temp, 1
        ]],

    [r'(.*)(suba|sube|aumente|aumenta|incremente|incrementa|m(a|á)s)(.*)temperatura(.*)aire(.*)',
        [ False, acondicionado.up_down_temp, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje)(.*)temperatura(.*)aire(.*)',
        [ False, acondicionado.up_down_temp, False
        ]],

    [r'(.*)temperatura(.*)aire(.*)',
        [ False, acondicionado.get_temp
        ]],

     #=========================== shower ======================================

    [r'(.*)(abra|abre|activa|active|enciende|encienda|activa|active)(.*)(ducha|llave)(.*)',
        [ False, ducha.turn_on_off, True
        ]],

    [r'(.*)(cierre|cierra|desactiva|desactive|apaga|apague)(.*)(ducha|llave)(.*)',
        [ False, ducha.turn_on_off, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)temperatura(.*)(ducha|llave)(.*)',
        [ False, ducha.up_down_temp, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|merme)(.*)temperatura(.*)(ducha|llave)(.*)',
        [ False, ducha.up_down_temp, False
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)(flujo|corriente|salida)(.*)(ducha|llave)(.*)',
        [ False, ducha.up_down_flow, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje)(.*)(flujo|corriente|salida)(.*)(ducha|llave)(.*)',
        [ False, ducha.up_down_flow, False
        ]],

    [r'(.*)(flujo|corriente|salida)(.*)(ducha|llave)(.*)',
        [ False, ducha.get_flow
        ]],

    [r'(.*)temperatura(.*)(ducha|llave)(.*)',
        [ False, ducha.get_temp
        ]],

     #================================= Dishwasher =============================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)lavaplatos(.*)',
        [ False, lavaplatos.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)lavaplatos(.*)',
        [ False, lavaplatos.turn_on_off, False
        ]],

    [r'(por favor )?(ponga|pon|pongale|coloque|coloquele|coloca) (?P<numbers1>[0-9]+) (min|minutos)(.*)lavaplatos(.*)',
        [ True, lavaplatos.set_time, 1
        ]],

    [r'(.*)(hay|todos|estan)(.*)platos(.*)(sucios|por lavar|para lavar)(.*)',
        [ False, lavaplatos.get_have_dish
        ]],

    [r'(por favor )?(limpie|limpia|lave|lava) (el|los) plato(s)?( sucios| por lavar| para lavar)?( en| durante)? (?P<numbers1>[0-9]+) (min|minutos)(.*)',
        [ True, lavaplatos.wash, 1
        ]],

    [r'(.*)tiempo(.*)(limpieza|lavado)(.*)',
        [ False, lavaplatos.get_time
        ]],

     #================================ Equipos de Sonido ======================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(equipo( de sonido)?|sonido)(.*)primer piso(.*)',
        [ False, sonido[0].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(equipo( de sonido)?|sonido)(.*)segundo piso(.*)',
        [ False, sonido[1].turn_on_off, True
        ]],

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)(todos)?(.*)(equipos( de sonido)?|sonidos)(.*)',
        [ False, print_objs, sonido, True
        ]],

    [r'(.*)(apaga|apague)(.*)(todos)?(.*)(equipos( de sonido)?|sonidos)(.*)',
        [ False, print_objs, sonido, False
        ]],

    [r'(.*)(apaga|apague)(.*)(equipo( de sonido)?|sonido)(.*)',
        [ False, sonido[0].turn_on_off, False
        ]],

    [r'(.*)(apaga|apague)(.*)(equipo( de sonido)?|sonido)(.*)',
        [ False, sonido[1].turn_on_off, False
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)ximo) (estaci(o|ó)n|emisora)(.*)(equipo( de sonido)?|sonido)(.*)primer piso(.*)",
        [ False, sonido[0].next_back_station, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)xima) (canci(o|ó)n|tema)(.*)(equipo( de sonido)?|sonido)(.*)primer piso(.*)",
        [ False, sonido[0].next_back_song, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)xima) (estaci(o|ó)n|emisora)(.*)(equipo( de sonido)?|sonido)(.*)segundo piso(.*)",
        [ False, sonido[1].next_back_station, True
        ]],

    [r"(.*)(pon|pasalo|cambia|pasa|pase|ponga|cambie)?(.*)(siguiente|pr(o|ó)xima) (canci(o|ó)n|tema)(.*)(equipo( de sonido)?|sonido)(.*)segundo piso(.*)",
        [ False, sonido[1].next_back_song, True
        ]],

     #================================= Ventanas ==============================

     #================================= Impresora =============================

    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)impresora(.*)',
        [ False, impresora.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)impresora(.*)',
        [ False, impresora.turn_on_off, False
        ]],

    [r'(por favor )?(ponga|pon|coloque|coloca|añada|agregue|agrega) (?P<numbers1>[0-9]+) hoja(.*)impresora(.*)',
        [ True, impresora.put_sheets, 1
        ]],

    [r'(por favor )?(pon a)?(imprima|imprime|imprimir) (?P<numbers1>[0-9]+) (hoja(s)?|p(a|á)gina(s)?) (y saca |y )?(?P<numbers2>[0-9]+) (copia(s)|duplicado(s)|fotocopia(s))(.*)',
        [ True, impresora.print_out, 1, 1, True
        ]],

    [r'(por favor )?(pon a)?(imprima|imprime|imprimir) (?P<numbers1>[0-9]+) (copia(s)?|hoja(s)?|p(a|á)gina(s)?)(.*)',
        [ True, impresora.print_out, 1
        ]],

    [r'(.*)hojas(.*)impresora(.*)',
        [ False, impresora.get_sheets
        ]],

     #================================= Email ==================================
    [r'(.*)(muestra|muestre|muestrame|muestreme|liste|lista|listame|listeme)(.*)(mensajes|correos)(.*)',
        [ False, correos.list_mesa
        ]],

    [r'(.*)(muestra|muestre|muestrame|muestreme|liste|lista|listame|listeme)(.*) ultimo (mensaje|correo)(.*)',
        [ False, correos.show_last_mesa
        ]],

    [r'(.*)(muestra|muestre|muestrame|muestreme|liste|lista|listame|listeme)(.*)(mensaje|correo) m(a|á)s nuevo(.*)',
        [ False, correos.show_last_mesa
        ]],

    [r'(.*)(muestra|muestre|muestrame|muestreme|liste|lista|listame|listeme)(.*) primer (mensaje|correo)(.*)',
        [ False, correos.show_oldest_mesa
        ]],

    [r'(.*)(muestra|muestre|muestrame|muestreme|liste|lista|listame|listeme)(.*)(mensaje|correo) m(a|á)s viejo(.*)',
        [ False, correos.show_oldest_mesa
        ]],

    [r'(.*)(hay)?(mensajes|correos)( por leer| sin leer)?( \?)?(.*)',
        [ False, correos.without_read
        ]],

     # falta
     # mostrar x mensaje
     # enviar correo
     #================================= Alarmas ================================

     #================================= fridge =================================
    [r'(.*)(cuant(os|a))( comida| alimentos| articulos) hay(.*)(nevera|refrigerador)(.*)',
        [ False, nevera.get_no_elem
        ]],

    [r'(.*)(muestra|muestre|muestrame|muestreme|liste|lista|listame|listeme)(.*)(comida|alimentos|articulos)(.*)(hay)?(.*)(nevera|refrigerador)(.*)',
        [ False, nevera.get_elements
        ]],

    [r'(.*)(aumente|aumenta|incremente|incrementa|suba|sube|m(a|á)s)(.*)temperatura(.*)(nevera|refrigerador)(.*)',
        [ False, nevera.up_down_temp, True
        ]],

    [r'(.*)(disminuya|disminuye|baja|baje|menos)(.*)temperatura(.*)(nevera|refrigerador)(.*)',
        [ False, nevera.up_down_temp, False
        ]],

     # falta
     # add and rm elementos
     # put temperatura

     #================================= dryer ==================================
    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)secadora(.*)',
        [ False, secadora.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)secadora(.*)',
        [ False, secadora.turn_on_off, False
        ]],

    [r'(.*)(seque|seca)(.*)ropa(.*)(lavada|mojada)?(.*)',
        [ False, secadora.dry, 8
        ]],

    [r'(.*)(cuanto)?(.*)tiempo(.*)secadora(.*)',
        [ False, secadora.get_time
        ]],

    [r'(.*)(cual)?(.*)estado(.*)secadora(.*)',
        [ False, secadora.get_state
        ]],
     #================================= washer =================================
    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)lavadora(.*)',
        [ False, lavadora.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)lavadora(.*)',
        [ False, lavadora.turn_on_off, False
        ]],

    [r'(.*)(limpie|limpia|lave|lava)(.*)ropa(.*)(sucia|por lavar|para lavar)?(.*)',
        [ False, lavadora.wash, 10
        ]],

    [r'(.*)(cuanto)?(.*)tiempo(.*)lavadora(.*)',
        [ False, lavadora.get_time
        ]],

    [r'(.*)(cual)?(.*)estado(.*)lavadora(.*)',
        [ False, lavadora.get_state
        ]],

     # falta
     # set time and state

     #=================================  Stove ==================================
    [r'(por favor )?(enciende|prende|prenda|encienda) la hornilla (?P<numbers1>[0-9]+)(( )(.*))?',
        [ True, estufa.turn_on_off, 1, True
        ]],

    [r'(por favor )?(apaga|apague) la hornilla (?P<numbers1>[0-9]+)(( )(.*))?',
        [ True, estufa.turn_on_off, 1, False
        ]],

    [r'(por favor )?((¿)cual es|muestreme|digame) el estado de la hornilla (?P<numbers1>[0-9]+)(( )(.*))?',
        [ True, estufa.get_hornilla, 1
        ]],

    [r'(por favor )?(suba|sube|aumente|aumenta|incremente|incrementa|m(a|á)s) la intensidad de la hornilla (?P<numbers1>[0-9]+)(( )(.*))?',
        [ True, estufa.change_intensity_hornilla, 1, True
        ]],

    [r'(por favor )?(disminuya|disminuye|baja|baje|menos|merme) la intensidad de la hornilla (?P<numbers1>[0-9]+)(( )(.*))?',
        [ True, estufa.change_intensity_hornilla, 1, False
        ]],

     [r'(.*)(enciende|prende|prenda|encienda)(.*)(todas)? las hornillas(.*)',
        [ False, estufa.all, True
        ]],

    [r'(.*)(apaga|apague)(.*)(todas)? las hornillas(.*)',
        [ False, estufa.all, False
        ]],

    [r'(.*)hornilla(.*)',
        [ False, estufa_default
        ]],

     #================================= phone ==================================

     #================================= oven ===================================
    [r'(.*)(enciende|prende|prenda|encienda|activa|active)(.*)horno(.*)',
        [ False, horno.turn_on_off, True
        ]],

    [r'(.*)(apaga|apague)(.*)horno(.*)',
        [ False, horno.turn_on_off, False
        ]],

    [r'(.*)(cuanto)?(.*)tiempo(.*)horno(.*)',
        [ False, horno.get_time
        ]],

    [r'(.*)(cual)?(.*)temperatura(.*)horno(.*)',
        [ False, horno.get_temp
        ]],

     # falta change time and temp

     # respuesta de salida
    [r'(salir|adios|hasta luego|hasta pronto|chao)(.*)',
        [ False, exit_default
        ]],

     # respuesta por defecto
    [r'(.*)',
        [ False, ans_default
        ]],
]
#apague .. no puedo determinar que apagar
#agregar ? computador, triturador de comida, licuadora,
#Haciendo pruebas
#print print_all()
control = Controller_house()
# print print_all()
exit = ["salir", "adios", "hasta luego", "hasta pronto", "chao"]
s = ''
#tvs[0].turn_on_off(True)
while(s not in exit):
    s = raw_input("TÚ: ")
    print control.respond(s)
