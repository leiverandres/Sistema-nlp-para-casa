# -*- coding: utf-8 -*-

# Mapea el id con la ubicacion de los sonidos
def place1(id):
    if(id == 1):
        return "del primer piso"
    return "del segunda piso"

# Mapea el id con la ubicacion de las alarmas
def place2(id):
    if(id == 1):
        return "de la puerta"
    return "de las ventanas"

# Mapea el id con la ubicacion de las luces
def place3(id):
    if(id == 1):
        return "de la entrada"
    if(id == 2):
        return "de la sala"
    if(id == 3):
        return "del patio"
    if(id == 4):
        return "del comedor"
    if(id == 5):
        return "de la cocina"
    if(id == 6):
        return "del pasillo del primer piso"
    if(id == 7):
        return "de las escaleras"
    if(id == 8):
        return "del pasillo del segundo piso"
    if(id == 9):
        return "de la sala del segundo piso"
    if(id == 10):
        return "de la primera habitacion"
    if(id == 11):
        return "de la segunda habitacion"
    if(id == 12):
        return "del baño"

# Mapea el id con la ubicacion de los lamparas
def place4(id):
    if(id == 1):
        return "de la izquierda de la primera habitacion"
    if(id == 2):
        return "de la derecha de la primera habitacion"
    return "de la segunda habitacion"

# Mapea el id con la ubicacion de las ventanas
def place5(id):
    if(id == 1):
        return "de la primera ventana de la sala"
    if(id == 2):
        return "de la segunda ventana de la sala"
    if(id == 3):
        return "de la ventana de la cocina"
    if(id == 4):
        return "de la primera ventana del comedor"
    if(id == 5):
        return "de la segunda ventana del comedor"
    if(id == 6):
        return "de la ventana de la primera habitacion"
    if(id == 7):
        return "de la ventana de la segunda habitacion"
    if(id == 8):
        return "de la ventana de la sala del segundo piso"
    if(id == 9):
        return "de la ventana del pasillo del segundo piso"

# Mapea el id con la ubicacion de los televisores
def place6(id):
    if(id == 1):
        return "de la sala"
    if(id == 2):
        return "de la primera habitacion"
    return "de la segunda habitacion"

class Power:
    def __init__(self, obj, id):
        self.isOn = False
        self.obj = obj
        self.name = id
        if self.name:
            self.name += " "

    def get_Power(self):
        return self.isOn

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                return "El/La(s) "+ self.obj + " " + self.name + "ya esta encendid(a/o)/abiert(a/o)(s)."
            else:
                self.isOn = True
                return self.obj + " " + self.name + "encendid(a/o)."
        else:
            if(not self.isOn):
                return "El/La(s) "+ self.obj + " " + self.name + "ya esta apagad(a/o)/cerrad(a/o)(s)."
            else:
                self.isOn = False
                return self.obj + " " + self.name + "apagad(a/o)."

#///////////////////////////////////////////////////////////////////////////////
class TV(Power):
    def __init__(self, id):
        Power.__init__(self, "TV", place6(id))
        self.channel = 1 #max 100
        self.volume = 10
        self.id = id

    def get_channel(self):
        if(self.isOn):
            return "El TV " + place6(self.id) + " esta en el canal " + str(self.channel)
        return "El TV " + place6(self.id) + " esta apagado, enciendalo."

    def get_volume(self):
        if(self.isOn):
            return "El TV " + place6(self.id) + " tiene el volumen en  " + str(self.volume)
        return "El TV " + place6(self.id) + " esta apagado, enciendalo."

    def change_channel(self, state):
        if(self.isOn):
            if (state):
                self.channel = (self.channel + 1) % 120
                return "El Canal siguiente en el TV " + place6(self.id) + " " + str(self.channel)
            else:
                if(self.channel - 1 <= 0):
                    self.set_channel(120);
                    return "El Canal anterior en el TV " + place6(self.id) + " " + str(self.channel)
                else:
                    self.channel -= 1
                    return "El Canal anterior en el TV " + place6(self.id) + " " + str(self.channel)
        else:
            return "El TV " + place6(self.id) + " esta apagado, enciendalo."

    def set_channel(self, channel):
        if(self.isOn):
            if(channel > 0 and channel < 121):
                self.channel = channel
                return "El Canal actual en el TV " + place6(self.id) + " " + str(self.channel)
            else:
                return "No existe este canal en el TV " + place6(self.id)
        else:
            return "El TV " + place6(self.id) + "esta apagado, enciendalo."

    def change_volume(self, state):
        if(self.isOn):
            if(state):
                self.volume += 1
                if(self.volume > 100):
                    self.volume = 100
                return "El TV "+ place6(self.id) +" tiene el volumen ++: " + str(self.volume)
            else:
                self.volume -= 1
                if(self.volume < 0):
                    self.volume = 0
                return "El TV "+ place6(self.id) +" tiene el volumen --: " + str(self.volume)
        else:
            return "El TV " + place6(self.id) + " esta apagado, enciendalo."

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "El TV " + place6(self.id) + " esta encendido, el canal actual es " + str(self.channel) + " y tiene un volumen de " + str(self.volume)
        else:
            s += "El TV " + place6(self.id) + " esta apagado"
        return s

#///////////////////////////////////////////////////////////////////////////////
class Light(Power): # Clase para las luces de la casa y para las lamparas
    def __init__ (self, id, obj):
        if(obj == "Luz"):
            Power.__init__(self, "Luz", place3(id))
        elif(obj == "Lampara"):
            Power.__init__(self, "Lampara", place4(id))
        self.intensity = 0
        self.id = id
        self.obj = obj
        if self.obj == "Luz":
            self.place = place3(self.id)
        else:
            self.place = place4(self.id)

    def get_intensity(self):
        if(self.isOn):
            return "La intensidad actual de la " + self.obj + " " + self.place + " es de " + str(self.intensity) + "%"
        else:
            return "La " + self.obj + " " + self.place + " esta apagada, enciendala"

    def set_intensity(self, cant):
        s = ""
        if(cant < 0 or cant > 2):
            cant = 0
            s += "La cantidad especificada no es valida, se tomara el valor por defecto "
        if(cant == 0):
            self.turn_on_off(True)
            self.intensity = 15
            return s + "Ud. ha puesto el modo " + str(cant) + " en la intensidad, la intensidad actual de la " + self.obj + " " + self.place + " es de " + str(self.intensity) + "%"
        elif(cant == 1):
            self.turn_on_off(True)
            self.intensity = 50
            return"Ud. ha puesto el modo " + str(cant) + " en la intensidad, la intensidad actual de la " + self.obj + " " + self.place + " es de " + str(self.intensity) + "%"
        elif(cant == 2):
            self.turn_on_off(True)
            self.intensity = 75
            return "Ud. ha puesto el modo " + str(cant) + " en la intensidad, la intensidad actual de la " + self.obj + " " + self.place + " es de " + str(self.intensity) + "%"

    def up_down_intensity(self, state):
        if(state):
            if((self.intensity + 10) > 100):
                self.intensity = 100
                return "La intensidad de la " + self.obj + " " + self.place + " esta en su maximo valor " + str(self.intensity) + "%"
            else:
                self.intensity += 10
                self.turn_on_off(True)
                return "La intensidad de la " + self.obj + " " + self.place + " esta en " + str(self.intensity) + "%"
        else:
            if((self.intensity - 10) < 0):
                self.intensity = 0
                self.turn_on_off(False)
                return "La intensidad de la " + self.obj + " " + self.place + " esta en su minimo valor " + str(self.intensity) + "%"
            else:
                self.intensity -= 10
                self.turn_on_off(True)
                return "La intensidad de la " + self.obj + " " + self.place + " esta en " + str(self.intensity) + "%"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La " + self.obj + " " + self.place + " esta encendida y su intensidad es de " + str(self.intensity) + "%"
        else:
            s += "La " + self.obj + " " + self.place + " esta apagada"
        return s
#///////////////////////////////////////////////////////////////////////////////

class Shower(Power):
    def __init__(self, id):
        Power.__init__(self, "Ducha", "")
        self.temp = 25 #temperatura
        self.flow = 0
        self.id = id

    def get_temp(self):
        if(self.isOn):
            return "El agua esta en " + str(self.temp) + "% de su temperatura maxima."
        return "La ducha esta cerrada, abrala"

    def get_flow(self):
        if(self.isOn):
            return "El nivel del flujo es " + str(self.flow)
        return "La ducha esta cerrada, abrala"

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                if((self.temp + 10) > 100):
                    self.temp = 100
                    return "El agua esta en su maxima temperatura"
                else:
                    self.temp += 10
                    return "El agua esta en " + str(self.temp) + "% de su temperatura maxima."
            else:
                if((self.temp - 10) < 0):
                    self.temp = 0
                    return "La ducha esta es su minima temperatura"
                else:
                    self.temp -= 10
        else:
            return "No puedo modificar la temperatura, la ducha esta cerrada"

    def up_down_flow(self, state):
        if(self.isOn):
            if(state):
                if((self.flow +  2) > 10):
                    self.flow = 10
                    self.isOn = True
                    return "El flujo de agua esta en su nivel maximo"
                else:
                    self.flow += 2
                    self.isOn = True
                    return "El nivel del flujo es " + str(self.flow)
            else:
                if((self.flow - 2) < 0):
                    self.flow = 0
                    self.isOn = False
                    return "La ducha se ha cerrado"
                else:
                    self.flow -= 2
        else:
            return "No puedo modificar el nivel de flujo, la ducha esta cerrada"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La ducha esta abierta, el agua esta en " + str(self.temp) + "% de su temperatura maxima y el flujo es " + str(self.flow)
        else:
            s += "La ducha esta cerrada"
        return s
#///////////////////////////////////////////////////////////////////////////////

class Dishwasher(Power):
    def __init__(self, id):
        Power.__init__(self, "Lavaplatos", "")
        self.haveDish = True
        self.time = 0
        self.id = id

    def get_have_dish(self):
        if(self.haveDish):
            return "Si, hay platos por lavar"
        else:
            return "No, no hay platos por lavar"
    
    def get_time(self):
        if(self.isOn):
            return "El tiempo de lavado actual es de " + str(self.time) + " minutos"
        return "El lavaplatos esta apagado, enciendalo"

    def set_time(self, time):
        self.time = time
        return "El tiempo de lavado sera de " + str(self.time) + " minutos"

    def set_have_dish(self, state):
        self.haveDish = state
        if(self.haveDish):
            return "Si, hay platos por lavar"
        else:
            return "No, no hay platos por lavar"

    def wash(self, time = 5):
        if(self.haveDish):
            self.isOn = True
            self.time = time
            self.haveDish = False
            return "Limpiando platos"
        else:
            self.haveDish = True
            return "No hay platos sucios para lavar en el lavaplatos"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "El lavaplatos esta encendido y el tiempo de lavado sera de " + str(self.time) + " minutos"
        else:
            s += "El lavaplatos esta apagado"
        return s
#///////////////////////////////////////////////////////////////////////////////

class SoundSystem(Power):
    def __init__ (self, id):
        Power.__init__(self, "Equipo", place1(id))
        self.volume = 0
        self.song = 0 #max 15
        self.stations = ["88.2", "89.6", "95.6", "98.4", "100.2", "102.5", "103.9", "105.7", "106.9", "107.9"]
        self.index_station = 0
        self.id = id

    def get_volume(self):
        if(self.isOn):
            return "El equipo " + place1(self.id) + " tiene un volumen de " + str(self.volume)
        return "El equipo "+ place1(self.id) + " esta apagado, enciendalo"

    def get_stations(self):
        if(self.isOn):
            return "El equipo " + place1(self.id) + " tiene " + self.stations + " emisoras disponibles"
        return "El equipo "+ place1(self.id) + " esta apagado, enciendalo"

    def get_num_song(self):
        if(self.isOn):
            return "La cancion actual en el equipo " + place1(self.id) + " es el track #" + str(self.song)
        return "El equipo "+ place1(self.id) + " esta apagado, enciendalo"
    
    def change_volume(self, state):
        if(self.isOn):
            if(state):
                self.volume += 1
                if(self.volume > 100):
                    self.volume = 100
                return "El equipo "+ place1(self.id) +" tiene el volumen ++: " + str(self.volume)
            else:
                self.volume -= 1
                if(self.volume < 0):
                    self.volume = 0
                return "El equipo"+ place1(self.id) +" tiene el volumen --: " + str(self.volume)
        else:
            return "El equipo" + place1(self.id) + " esta apagado, enciendalo."

    def change_station(self, station = "88.2"):
        if(self.isOn):
            if(station in self.stations):
                self.index_station = self.stations.index(station)
                return "La estacion actual en el equipo " + place1(self.id) + " es: " + self.stations[self.index_station]
            else:
                return "La estacion buscada en el equipo  "+ place1(self.id) + " no existe, se pondra la estacion por defecto"
        else:
            return "No puedo modificar, el equipo " + place1(self.id) + " esta apagado"

    def next_back_station(self, state):
        if(self.isOn):
            if(state):
                self.index_station = (self.index_station + 1) % 10
                return "La estacion actual en el equipo " + place1(self.id) + " es: " + self.stations[self.index_station]
            else:
                if((self.index_station - 1) < 0):
                    self.index_station += 10
                    return "La estacion actual en el equipo " + place1(self.id) + " es: " + self.stations[self.index_station]
                else:
                    self.index_station -= 1
                return "La estacion actual en el equipo " + place1(self.id) + " es: " + self.stations[self.index_station]
        else:
            return "No puedo modificar, el equipo " + place1(self.id) + " esta apagado"

    def next_back_song(self, state):
        if(self.isOn):
            if(state):
                self.song = (self.song + 1) % 15
                return "La cancion actual en el equipo " + place1(self.id) + " es el track #" + str(self.song)
            else:
                if((self.song - 1) < 0):
                    self.song += 15
                    return "La cancion actualen el equipo " + place1(self.id) + " es el track #" + str(self.song)
                else:
                    self.song -= 1
                return "La cancion actual en el equipo " + place1(self.id) + " es el track #" + str(self.song)
        else:
            return "No puedo modificar, el equipo " + place1(self.id) + " esta apagado"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "El equipo "+ place1(self.id) + " esta encendido, se encuentra en la emisora " + self.stations[self.index_station] + " y la cancion para reproducir es el track #" + str(self.song)
        else:
            s += "El equipo "+ place1(self.id) + " esta apagado"
        return s
#///////////////////////////////////////////////////////////////////////////////

class Curtains:
    def __init__(self, id):
        self.isOn = False
        self.cant = 0 #0 es cerrada, 100 es totalmente abierta
        self.id = id

    def get_cant(self):
        return "Las Cortinas " + place5(self.id) + " estan abiertas en un " + str(self.cant)+"%"

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                return "Las Cortinas " + place5(self.id) + " ya estan abiertas."
            else:
                self.isOn = True
                self.cant = 100
                return "Las Cortinas " + place5(self.id) + " estan abiertas."
        else:
            if(not self.isOn):
                return "Las Cortinas " + place5(self.id) + " ya estan cerradas."
            else:
                self.isOn = False
                self.cant = 0
                return "Las Cortinas " + place5(self.id) + " estan cerradaa."

    def up_down_cant(self, state):
        if(state):
            if(self.isOn):
                return "Las Cortinas " + place5(self.id) + " ya estan totalmente abiertas"
            else:
                if(self.cant + 10 > 100):
                    self.cant = 100
                    return "Las Cortinas " + place5(self.id) + " ya estan totalmente abiertas"
                else:
                    self.cant += 10
                    return "Las Cortinas " + place5(self.id) + " estan abiertas en un " + str(self.cant)+"%"
        else:
            if(not self.isOn):
                return "Las Cortinas " + place5(self.id) + " ya estan totalmente cerradas"
            else:
                if(self.cant - 10 < 0):
                    self.cant = 0
                    return "Las Cortinas " + place5(self.id) + " ya estan cerradas totalmente"
                else:
                    self.cant -= 10
                    return "Las Cortinas " + place5(self.id) + " estan abiertas en un " + str(self.cant)+"%"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "Las Cortinas " + place5(self.id) + " estan abiertas en un " + str(self.cant) + "%"
        else:
            s += "Las Cortinas " + place5(self.id) + " estan cerradas"
        return s
 #///////////////////////////////////////////////////////////////////////////////

class Printer(Power):
    def __init__(self, id):
        Power.__init__(self, "Impresora", "")
        self.sheets = 10 #Numero de hojas que tiene la impresora
        self.id = id

    def get_sheets(self):
        return "La impresora tiene " + str(self.sheets) + " hoja(s) disponibles"

    def put_sheets(self, sheets):
        self.sheets += sheets
        return "La impresora tiene " + str(self.sheets) + " hoja(s) disponibles"

    def print_out(self, pages, copies = 1):
        s = ""
        if(pages*copies <= self.sheets):
            self.sheets -= pages*copies
            s += "Documentos impresos ... ud. ha impreso " + str(pages) + " paginas y " + str(copies) + " copias\n"
            s += "La impresora tiene ahora " + str(self.sheets) + " hoja(s) disponibles"
            return s
        else:
            return "Por favor ponga al menos " + str(pages*copies - self.sheets) + " hoja(s) en la impresora para poder imprimir su documento"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La impresora esta encendida, tiene " + str(self.sheets) + " hoja(s) disponibles"
        else:
            s += "La impresora esta apagada"
        return s
#/////////////////////////////////////////////////////////////////////////////////////////////

class Email:
    def __init__(self):
        self.inbox = ["hi, need help", "meeting saturday", "another mail"] #numero de correos sin leer
        self.to_read = len(self.inbox)

    def get_mesa(self):
        return "Hay " + str(self.to_read) + " mensajes en la bandeja de entrada"

    def without_read(self):
        return "Hay " + str(self.to_read) + " mensajes sin leer"

    def list_mesa(self):
        s = ""
        if(self.to_read > 0):
            s += "Todos los mensajes:\n"
            for i in self.inbox:
                s += i + "\n"
            return s
        else:
            return "No hay mensajes por leer."

    def show_one_mesa(self, index):
        s = ""
        if(index > 0 and index <= self.to_read):
            index -= 1
            s += "Mesaje numero " + str(index + 1) + ": "
            return s + self.inbox[index]
        else:
            return "No existe el mensaje solicitado"

    def show_last_mesa(self):
        if(self.to_read > 0):
            return self.inbox[self.to_read - 1]
        else:
            return "No hay mensajes por leer."

    def show_oldest_mesa(self):
        if(self.to_read > 0):
            return self.inbox[0]
        else:
            return "No hay mensajes por leer."

    def remove_mesa(self, index): #index debe venir index 1
        if(index > 0 and index <= self.to_read):
            index -= 1
            self.to_read -= 1
            return "mensaje eliminado:\n" + self.inbox.pop(index)
        else:
            return "No existe el mensaje solicitado"

    def send_msj(self, string):
        return "Mensaje enviado:\n" + string

    def __str__(self):
        return self.list_mesa()
#//////////////////////////////////////////////////////////////////////////////

class Air(Power):
    def __init__(self, id):
        Power.__init__(self, "Aire acondicionado", "")
        self.temp = 25 #grados centigrados
        self.id = id

    def get_temp(self):
        if(self.isOn):
            return "La temperatura del Aire acondicionado esta en " + str(self.temp) + " °C"
        return "El Aire acondicionado esta apagado, enciendalo"

    def put_temp(self, temp):
        if(self.isOn):
            self.temp = temp
            return "La temperatura del Aire acondicionado esta en " + str(self.temp) + " °C"
        else:
            return "No puedo modifica la temperatura, el Aire acondicionado esta apagado"

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                self.temp += 1
            else:
                self.temp -= 1
            return "La temperatura esta en " + str(self.temp) + " °C"
        else:
            return "No puedo modifica la temperatura, el Aire esta apagado"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "El Aire acondicionado esta encendido y actualmente esta en una temperatura de " + str(self.temp) + "°C"
        else:
            s += "El Aire acondicionado esta apagado"
        return s
#////////////////////////////////////////////////////////////////////////////

#security alarm
class Alert(Power):
    def __init__(self, id):
        Power.__init__(self, "Alarma", place2(id))
        self.volume = 30 #max 100
        self.id = id
    
    def change_volume(self, state):
        if(self.isOn):
            if(state):
                self.volume += 1
                if(self.volume > 100):
                    self.volume = 100
                return "La alarma "+ place2(self.id) +" tiene el volumen ++: " + str(self.volume)
            else:
                self.volume -= 1
                if(self.volume < 0):
                    self.volume = 0
                return "La alarma "+ place2(self.id) +" tiene el volumen --: " + str(self.volume)
        else:
            return "La alarma " + place2(self.id) + " esta apagado, enciendalo."

    def get_volume(self):
        if(self.isOn):
            return "El volumen de la alarma " + place2(self.id) + " esta en " + str(self.volume)
        return "La alarma " + place2(self.id) + " esta apagada/desactivada"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La alarma " + place2(self.id) + " esta encendida/activada y esta con un volumen de " + str(self.volume)
        else:
            s += "La alarma " + place2(self.id) + " esta apagada/desactivada"
        return s
#///////////////////////////////////////////////////////////////////////////////

class Burner:
    def __init__(self):
        self.isOn = False
        self.id = 0
        self.intensity = 0

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                return "La hornilla " + str(self.id) + " ya esta encendida"
            else:
                return "La hornilla " + str(self.id) + " esta encendida"
        else:
            if(not self.isOn):
                return "La hornilla " + str(self.id) + " ya esta apagada"
            else:
                return "La hornilla" + str(self.id) + " esta apagada"

    def change_intensity(self, state):
        if(state):
            self.isOn = True
            if(self.intensity + 2 > 10):
                self.intensity = 10
                return "La hornilla " + str(self.id) + " esta en su maximo intensidad"
            else:
                self.intensity += 2
                return "La hornilla " + str(self.id) + " esta con una intensidad de " + str(self.intensity)
        else:
            if(self.intensity - 2 < 0):
                self.isOn = False
                self.intensity = 0
                return "La hornilla " + str(self.id) + " esta apagada"
            else:
                self.intensity -= 2
                return "La hornilla " + str(self.id) + " esta con una intensidad de " + str(self.intensity)

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La hornilla " + str(self.id) + " esta encendida y esta con una intensidad de " + str(self.intensity)
        else:
            s += "La hornilla " + str(self.id) + " esta apagada"
        return s
#///////////////////////////////////////////////////////////////////////////////

class Stove:
    def __init__(self):
        self.hornillas = [Burner(), Burner(), Burner(), Burner()]
        self.hornillas[0].id = 1
        self.hornillas[1].id = 2
        self.hornillas[2].id = 3
        self.hornillas[3].id = 4

    def get_hornilla(self, id): # id: 1-4
        if(id <= 0 or id > 4):
            return "La hornilla especificada no es valida"
        else:
            return self.hornillas[id - 1].__str__()

    def turn_on_off(self, id, state):
        if(id <= 0 or id > 4):
            return "La hornilla especificada no es valida"
        else:
            return self.hornillas[id - 1].turn_on_off(state)

    def change_intensity_hornilla(self, id, state):
        if(id <= 0 or id > 4):
            return "La hornilla especificada no es valida"
        else:
            return self.hornillas[id - 1].change_intensity(state)
    
    def all(self, state):
        s = ""
        for i in range(len(self.hornillas)):
            s += self.hornillas[i].turn_on_off(state) + "\n"
        return s

    def __str__(self):
        s = ""
        for index in range(len(self.hornillas)):
            s += self.hornillas[index].__str__() + "\n"
        return s
#////////////////////////////////////////////////////////////////////////////

class Fridge:
    def __init__(self):
        self.isOn = True
        self.temp = 15
        self.elements = ["pastel", "fruta", "carne", "pollo", "verduras", "quesadillas", "vino", "cerveza"]
        self.no_elem = len(self.elements)

    def get_no_elem(self):
        return "La nevera tiene una temperatura de " + str(self.temp) +" °C y tiene " + str(self.no_elem) + " articulos"

    def get_elements(self):
        s = ""
        s += "Elementos en la nevera:\n"
        for i in self.elements:
            s += i + "\n"
        return s

    def rm_element(self, elem):
        if(self.no_elem > 0):
            if(elem in self.elements):
                self.elements.remove(elem)
                return "Elemento removido " + elem
            else:
                return "El elemento no se encuentra en la nevera"
        else:
            return "No hay elementos, es hora de comprar!"

    def add_elements(self, elem):
        self.elements.append(elem)
        return "Elemento agregado " + elem

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                self.temp += 1
                return "La temperatura de la nevera esta en " + str(self.temp) + " °C"
            else:
                self.temp -=1
                return "La temperatura de la nevera esta en " + str(self.temp) + " °C"
        else:
            return "Nevera apagada"

    def put_temp(self, temp):
        if(self.isOn):
            self.temp = temp
            return "La temperatura de la nevera esta en " + str(self.temp) + " °C"
        else:
            return "La Nevera apagada"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La nevera esta encendida, esta con una temperatura de " + str(self.temp) + "°C\n" + self.get_elements()
        else:
            s += "La nevera esta apagada"
        return s
#/////////////////////////////////////////////////////////////////////////////////

class Washer(Power):
    def __init__(self, id):
      Power.__init__(self, "Lavadora", "")
      self.time = 0
      self.index_state = 4
      self.state = ["lana", "delicado", "sintetico", "resistente", "intensivo"]
      self.id = id
      
    def get_all_state(self):
        return "Los estados de la lavadora son " + self.state

    def get_time(self):
        if(self.isOn):
            return "El tiempo de lavado es de " + str(self.time) + " minutos"
        return "La lavadora esta apagada, enciendala"

    def get_state(self):
        if(self.isOn):
            return "El estado de la lavadora es " + self.state[self.index_state]
        return "La lavadora esta apagada, enciendala"

    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        return "El tiempo de lavado es de " + str(self.time) + " minutos"

    def change_state(self, state = "delicado"):
        state = state.lower()
        if(self.isOn):
            if(state in self.state):
                self.index_state = self.state.index(state)
                return "La estado actual de la lavadora es " + self.state[self.index_state]
            else:
                return "El estado que desea no existe, se pondra el estado por defecto"
        else:
            return "No es posible ir a ese estado porque la lavadora esta apagada"

    def wash(self, time = 5):
        self.isOn = True
        self.change_time(time)
        return "Lavando ..."

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La lavadora esta encendida, su estado actual es " + self.state[self.index_state] + " y el tiempo de lavado es de " +  str(self.time) + " minutos y " + self.get_all_state() 
        else:
            s += "La lavadora esta apagada"
        return s
#//////////////////////////////////////////////////////////////////////////////

class Phone:
    def __init__(self):
        self.last_number = ""
        self.agenda = ["321456789", "789456123", "741258963", "369852147", "3117231283", "3164328712"]
        self.numbers = len(self.agenda)
        self.last = ""
        self.mensajes = ["Hola, ¿Me va dar copia de IA?",
                        "¿Cuales materias perdio?",
                        "Por favor, mandeme el codigo yo lo miro, pero no se lo copio",
                        "¿Ya salio a vacaciones? Cuando es la farra? xD"];

    def llamar(self, num):
        if(num in self.agenda):
            self.last = num
        else:
            self.last = num
            self.agenda.append(num)
        return "Llamando a ... " + num

    def llamar_ult(self):
        if(not (self.last == "")):
            return "Llamando a ... " + self.last
        else:
            return "No hay llamadas registradas"

    def add_mesa(self, mesa):
        self.mensajes.append(mesa)
        return "El mensaje " + mesa +" ha sido agregado"

    def remove_mesa(self, index):
        if index <= len(self.mensajes) and index > 0:
            index -= 1
            msj = self.mensajes[index]
            self.mensajes.remove(msj)
            return "El mensaje: " + msj + " se ha eliminado"
        else:
            return "El mensaje #" + str(index + 1) + " no existe o no se encuentra disponible"

    def list_msj(self):
        s = ""
        if len(self.mensajes) > 0:
            s += "Todos los mensajes:\n"
            for i in self.mensajes:
                s += i + "\n"
            return s
        else:
            return "No hay mensajes en el telefono."

    def contesta(self, num = ""):
        if(not (num == "")):
            return "Hablando con " + num
        else:
            return "Hablando"

    def list_contacts(self):
        s = ""
        if len(self.agenda) > 0:
            s += "Todos los contactos:\n"
            for i in self.agenda:
                s += i + "\n"
            return s
        else:
            return "No hay contactos en el telefono."

    def add_agenda(self, num):
        self.agenda.append(num)
        return "Numero agregado " + num

    def remove_agenda(self, num):
        if(num in self.agenda):
            self.agenda.remove(num)
        return "EL contacto " + num + " ha sido removido"

    def __str__(self):
        s = ""
        s += self.list_contacts() + "\n"
        s += self.list_msj()
        return s
#///////////////////////////////////////////////////////////////////////////////

class Oven(Power):
    def __init__(self, id):
        Power.__init__(self, "Horno", "")
        self.temp = 0 #Centigrados
        self.time = 0 #Minutos
        self.id = id

    def get_temp(self):
        if(self.isOn):
            return "La temperatura del horno es de " + str(self.temp) + " °C"
        return "El horno esta apagado, prendalo"

    def get_time(self):
        if(self.isOn):
            return "El tiempo de coccion actual del horno es de " + str(self.time) + " minutos"
        return "El horno esta apagado, prendalo"

    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        return "EL tiempo para de coccion sera de " + str(self.time) + " minutos"

    def change_temp(self, temp):
        self.isOn = True
        self.temp = temp
        return "La temperatura para la coccion sera de " + str(self.temp) + " °C"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "El horno esta encendido, esta a una temperatura de " + str(self.temp) + " °C y esta programado para un tiempo de coccion de " + str(self.time) + " minutos"
        else:
            s += "El horno esta apagado"
        return s
#///////////////////////////////////////////////////////////////////////////////

class Dryer(Power):
    def __init__(self, id):
        Power.__init__(self, "Secadora", "")
        self.time = 0
        self.index_state = 0
        self.state = ["presecado", "delicado", "regular", "mix"]
        self.id = id

    def get_time(self):
        if(self.isOn):
            return "El tiempo de secado es de " + str(self.time) + " minutos"
        return "La secadora esta apagada, enciendala"

    def get_state(self):
        if(self.isOn):
            return "El estado de la secadora es " + self.state[self.index_state]
        return "La secadora esta apagada, enciendala"
    
    def get_all_state(self):
        return "Los estados de la secadora son " + self.state

    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        return "El tiempo de secado es de " + str(self.time) + " minutos"

    def dry(self, time = 5):
        self.isOn = True
        self.change_time(time)
        return "Secando..."

    def change_state(self, state = "regular"):
        state = state.lower()
        if(self.isOn):
            if(state in self.state):
                self.index_state = self.state.index(state)
                return "La estado actual de la secadora es " + self.state[self.index_state]
            else:
                return "El estado que desea no existe, se pondra el estado por defecto"
        else:
            return "No es posible ir a ese estado porque la secadora esta apagada"

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La secadora esta encendida, su estado actual es " + self.state[self.index_state] + " y el tiempo de secado es de " +  str(self.time) + " minutos y " + self.get_all_state()
        else:
            s += "La secadora esta apagada"
        return s

class Blender(Power):
    def __init__(self, id):
        Power.__init__(self, "Licuadora", "")
        self.mode = 0
        self.id = id
    
    def get_mode(self):
        if(self.isOn):
            return "La licuadora esta en el (modo/velocidad) " + str(self.mode)
        return "La licuadora esta apagada, enciendala"
    
    def twist(self, mode = 1):
        if(self.isOn):
            if(mode > 0 and mode <= 5):
                self.mode = mode
                return self.get_mode()
            else:
                if(mode == 0):
                    return "La licuadora ha sido apagada y esta en el (modo/velocidad) 0"
                else:
                    return "El modo pedido no es valido, por favor intentelo de nuevo"
        return "La licuadora esta apagada, enciendala"
    
    def __str__(self):
        s = ""
        if(self.isOn):
            s += "La licuadora esta encendida y esta en el (modo/velocidad) " + str(self.mode)
        else:
            s += "La licuadora esta apagada"
        return s
        
