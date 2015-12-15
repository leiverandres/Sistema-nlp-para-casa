# -*- coding: utf-8 -*-
class Power:
    def __init__(self, obj):
        self.isOn = False
        self.obj = obj

    def get_Power(self):
        return self.isOn

    def turn_on_off(self, state, id = None):
        if(state):
            if(self.isOn):
                return "El/La(s) "+ self.obj + " ya esta encendida/abierta(s)."
            else:
                self.isOn = True
                return  self.obj + " encendida."
        else:
            if(not self.isOn):
                return "El/La(s) "+ self.obj + " ya esta apagada/cerrada(s)."
            else:
                self.isOn = False
                return self.obj + " apagada."

#///////////////////////////////////////////////////////////////////////////////
class TV(Power):
    def __init__(self):
        Power.__init__(self, "TV")
        self.channel = 1 #max 100
        self.volume = 10

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

    def change_channel(self, state, id = None):
        if(self.isOn):
            if (state):
                self.channel = (self.channel + 1) % 120
                return "Canal next: " + str(self.channel)
            else:
                if(self.channel - 1 <= 0):
                    self.set_channel(120);
                    return "Canal prev: " + str(self.channel)
                else:
                    self.channel -= 1
                    return "Canal prev: " + str(self.channel)
        else:
            return "El tv esta apagado, enciendalo."

    def set_channel(self, channel):
        if(self.isOn):
            if(channel > 0 and channel < 121):
                self.channel = channel
                return "Canal actual: " + str(channel)
            else:
                return "No existe este canal."
        else:
            return "El tv esta apagado, enciendalo."

    def change_volume(self, state):
        if(self.isOn):
            if(state):
                self.volume += 1
                return "Volumen ++: " + str(self.volume)
            else:
                self.volume -= 1
                return "Volumen --: " + str(self.volume)
        else:
            return "El tv esta apagado, enciendalo."

    def __str__(self):
        s = ""
        if(self.isOn):
            s += "El tv esta encendido, el canal actual es " + str(self.channel) + " y tiene un volumen de " + str(self.volume)
        else:
            s += "El tv esta apagado"
        return s

#///////////////////////////////////////////////////////////////////////////////
class Light(Power): # Clase para las luces de la casa y para las lamparas
    def __init__ (self):
        Power.__init__(self, "Luz/Lampara")
        self.intensity = 0

    def get_intensity(self):
        return self.intensity

    def set_intensity(self, cant):
        if(cant == 0):
            self.turn_on_off(True)
            self.intensity = 15
            self.turn_on_off(True)
            return "Canal intensidad actual: " + str(self.intensity)
        elif(cant == 1):
            self.turn_on_off(True)
            self.intensity = 50
            return "Canal intensidad actual: " + str(self.intensity)
        elif(cant == 2):
            #self.turn_on_off(True)
            self.intensity = 75
            return "Canal intensidad actual: " + str(self.intensity)

    def up_down_intensity(self, state):
        if(state):
            if((self.intensity + 10) > 100):
                self.intensity = 100
                return "La intensidad esta en su maximo valor " + str(self.intensity)
            else:
                self.intensity += 10
                self.turn_on_off(True)
                return "Intensidad en: " + str(self.intensity)
        else:
            if((self.intensity - 10) < 0):
                self.intensity = 0
                self.turn_on_off(False)
                return "La intesidad esta en su minimo valor." + str(self.intensity)
            else:
                self.intensity -= 10
                self.turn_on_off(True)
                return "Intensidad en: " + str(self.intensity)
#///////////////////////////////////////////////////////////////////////////////

class Shower(Power):
    def __init__(self):
        Power.__init__(self, "Ducha")
        self.temp = 25 #temperatura
        self.flow = 0

    def get_temp(self):
        return self.temp

    def get_flow(self):
        return self.flow

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                if((self.temp + 10) > 100):
                    self.temp = 100
                    return "El agua esta en su maxima temperatura"
                else:
                    self.temp += 10
                    return "El agua esta en " + str(self.temp) + "%."
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
#///////////////////////////////////////////////////////////////////////////////

class Dishwasher(Power):
    def __init__(self):
        Power.__init__(self, "Lavaplatos")
        self.haveDish = False
        self.time = 0

    def get_have_dish(self):
        return self.haveDish

    def set_time(self, time):
        self.time = time

    def set_have_dish(self, state):
        self.haveDish = state

    def wash(self, time = 5):
        if(self.haveDish):
            self.isOn = True
            self.set_time(time)
        else:
            return "No hay platos sucios para lavar en el lavaplatos"
#///////////////////////////////////////////////////////////////////////////////

class SoundSystem(Power):
    def __init__ (self):
        Power.__init__(self, "Equipo")
        self.volume = 0
        self.song = 0 #max 15
        self.stations = ["88.2", "89.6", "95.6", "98.4", "100.2", "102.5", "103.9", "105.7", "106.9", "107.9"]
        self.index_station = 0

    def get_volume(self):
        return self.volume

    def get_stations(self):
        return self.stations

    def get_num_song(self):
        return self.song

    def change_station(self, station = "88.2"):
        if(self.isOn):
            if(station in self.stations):
                self.index_station = self.stations.index(station)
                return "La estacion actual es : " + self.stations[self.index_station]
            else:
                return "La estacion buscada no existe, se pondra la estacion por defecto"
        else:
            return "No puedo modificar, esta apagado"

    def next_back_station(self, state):
        if(self.isOn):
            if(state):
                self.index_station = (self.index_station + 1) % 10
                return "La estacion actual es : " + self.stations[self.index_station]
            else:
                if((self.index_station - 1) < 0):
                    self.index_station += 10
                    return "La estacion actual es : " + self.stations[self.index_station]
                else:
                    self.index_station -= 1
                return "La estacion actual es : " + self.stations[self.index_station]
        else:
            return "No puedo modificar, esta apagado"

    def next_back_song(self, state):
        if(self.isOn):
            if(state):
                self.song = (self.song + 1) % 15
                return "La cancion actual es : " + str(self.song)
            else:
                if((self.song - 1) < 0):
                    self.song += 15
                    return "La cancion actual es : " + str(self.song)
                else:
                    self.song -= 1
                return "La cancion actual es : " + str(self.song)
        else:
            return "No puedo modificar, esta apagado"
#///////////////////////////////////////////////////////////////////////////////

class Curtains(Power):
    def __init__(self):
        Power.__init__(self, "Cortinas")
        self.cant = 0 #0 es cerrada, 100 es totalmente abierta

    def get_cant(self):
        return self.cant

    def turn_open_closed(self, state):
        if(state):
            if(self.isOn):
                return "Las cortinas ya estan abiertas."
            else:
                self.isOn = True
                self.cant = 100
                return "Cortinas abiertas."
        else:
            if(not self.isOn):
                return "Las cortinas ya estan cerradas."
            else:
                self.isOn = False
                self.cant = 0
                return "Cortinas cerradaa."

    def up_down_cant(self, state):
        if(state):
            if(self.isOn):
                return "Las cortinas ya estan totalmente abiertas"
            else:
                if(self.cant + 10 > 100):
                    self.cant = 100
                    return "Las cortinas ya estan totalmente abiertas"
                else:
                    self.cant += 10
                    return "Las cortinas estan abiertas en un " + str(self.cant)+"%"
        else:
            if(not self.isOn):
                return "Las cortinas ya estan totalmente cerradas"
            else:
                if(self.cant - 10 < 0):
                    self.cant = 0
                    return "Las cortinas ya estan cerradas totalmente"
                else:
                    self.cant -= 10
                    return "Las cortinas estan abiertas en un " + str(self.cant)+"%"
 #///////////////////////////////////////////////////////////////////////////////

class Printer(Power):
    def __init__(self):
        Power.__init__(self, "Impresora")
        self.sheets = 10 #Numero de hojas que tiene la impresora

    def get_sheets(self):
        return self.sheets

    def put_sheets(self, sheets):
        self.sheets += sheets

    def print_out(self, pages, copies = 1):
        if(pages*copies <= self.sheets):
            self.sheets -= pages*copies
            return "Documentos impresos...","La impresora tiene ahora " + str(self.sheets) + " hoja(s) disponibles"
        else:
            return "Por favor ponga al menos " + str(pages*copies - self.sheets) + " hoja(s) en la impresora para poder imprimir su documento"
#/////////////////////////////////////////////////////////////////////////////////////////////

class Email:
    def __init__(self):
        self.inbox = ["hi, need help", "meeting saturday", "another mail"] #numero de corros sin leer
        self.to_read = len(self.inbox)

    def get_mesa(self):
        return self.to_read

    def without_read(self):
        return "Hay " + str(self.get_mesa()) + " mensajes sin leer"

    def list_mesa(self):
        if(self.to_read > 0):
            return "Todos los mensajes"
            for i in self.inbox:
                return i
        else:
            return "No hay mensajes por leer."

    def show_one_mesa(self, index):
        if(index <= self.to_read):
            return "Mesaje numero " + str(index)
            return self.inbox[index]
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

    def remove_mesa(self, index):#index debe venir index 1
        if(index <= self.to_read):
            return "mensaje eliminado:\n" + self.inbox.pop(index)
            self.to_read -= 1
        else:
            return "No existe el mensaje solicitado"

    def send_mesaje(self, string):
        return "Mensaje enviado:\n" + string
#//////////////////////////////////////////////////////////////////////////////

class Air(Power):
    def __init__(self):
        Power.__init__(self, "Aire acondicionado")
        self.temp = 25 #grados centigrados

    def get_temp(self):
        return self.temp

    def put_temp(self, temp):
        if(self.isOn):
            self.temp = temp
            return "La temperatura esta en " + str(self.temp) + " grados °C"
        else:
            return "No puedo modifica la temperatura, el aire esta apagado"

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                self.temp += 1
            else:
                self.temp -= 1
            return "La temperatura esta en " + str(self.temp) + " grados °C"
        else:
            return "No puedo modifica la temperatura, el aire esta apagado"

#////////////////////////////////////////////////////////////////////////////

#security alarm
class Alert(Power):
    def __init__(self):
        Power.__init__(self, "Alarma")
        self.volume = 7 #max 10

    def get_volume(self):
        return self.volume

    def up_down_vol(self, state):
        if(self.isOn):
            if(state):
                if((self.volume + 1) > 10):
                    self.volume =  10
                    return "El volumen esta en su maximo valor: 10"
                else:
                    self.volume += 1
                    return "El volumen de la alarma es: " + str(self.volume)
            else:
                if((self.volume - 1) < 2):
                    self.volumen = 2
                    return "El volumen esta en su minimo valor: 2"
                else:
                    self.volume -= 1
                    return "El volumen de la alarma es: " + str(self.volume)
        else:
            return "No puedo modificar el volumen, la alarma esta apagada"
#///////////////////////////////////////////////////////////////////////////////

class Burner:
    def __init__(self):
        self.isOn = False
        self.id = 0
        self.intensity = 0

    def get_Power(self):
        return self.isOn

    def get_id(self):
        return self.id

    def get_intensity(self):
        return self.intensity

    def set_id(self, id):
        self.id = id

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
                return "La hornilla " + str(self.id) + " es con una intensidad de " + str(self.intensity)
        else:
            if(self.intensity - 2 < 0):
                self.isOn = False
                self.intensity = 0
                return "La hornilla " + str(self.id) + " esta apagada"
            else:
                self.intensity -= 2
                return "La hornilla " + str(self.id) + " es con una intensidad de " + str(self.intensity)
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
            return self.hornillas[id - 1]

    def turn_on_off(self, id, state):
        if(id <= 0 or id > 4):
            return "La hornilla especificada no es valida"
        else:
            self.hornillas[id - 1].turn_on_off(state)

    def change_intensity_hornilla(self, id, state):
        if(id <= 0 or id > 4):
            return "La hornilla especificada no es valida"
        else:
            self.hornillas[id - 1].change_intensity(state)
#////////////////////////////////////////////////////////////////////////////

class Fridge:
    def __init__(self):
        self.isOn = False
        self.temp = 12
        self.elements = ["pastel", "fruta", "carne", "pollo", "verduras", "quesadillas", "vino", "cerveza"]
        self.no_elem = len(self.elements)

    def get_no_elem(self):
        return self.no_elem

    def get_elements(self):
        return "Elementos en la nevera: "
        for i in self.elements:
            return i

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
            else:
                self.temp -=1
        else:
            return "Nevera apagada"

    def put_temp(self, temp):
        if(self.isOn):
            self.temp = temp
        else:
            return "Nevera apagada"
#/////////////////////////////////////////////////////////////////////////////////

class Washer(Power):
  def __init__(self):
      Power.__init__(self, "Lavadora")
      self.time = 0
      self.index_state = 4
      self.state = ["Lana", "Delicado", "Sintetico", "Resistente", "Intensivo"]

  def get_time(self):
      return self.time

  def get_state(self):
      return self.state

  def change_time(self, minute):
      self.isOn = True
      self.time = minute
      return "El tiempo de lavado es de " + self.time + " minutos"

  def change_state(self, state = "Delicado"):
      if(self.isOn):
          if(state in self.state):
              self.index_state = self.state.index(state)
              return "La estado actual es : " + self.state[self.index_state]
          else:
              return "El estado que desea no existe, se pondra el estado por defecto"
      else:
          return "No es posible ir a ese estado porque la lavadora esta apagada"

#//////////////////////////////////////////////////////////////////////////////

class Phone:
    def __init__(self):
        self.last_number = ""
        self.agenda = ["321456789", "789456123", "741258963", "369852147"]
        self.numbers = len(self.agenda)
        self.last = ""
        self.mensajes = ["pjfpjapsfj djf ao jdfjasdfpjasdp fasoj fd",
                        "asfdjikajfi afj kfa ff kafj kajfk ajkfa jskfj",
                        "koaj faś jfáo jsofj aoś jfo af'jaojfóa fsaój"];

    def llamar(self, num, id):
        if(num in self.agenda):
            return "Llamando ... "
            self.last = num
        else:
            return "el numero no se encuentra en la agenda"

    def llamar_ult(self, state, id):
        if(not (self.last == "")):
            return "Llamando a ... " + self.last
        else:
            return "No hay llamadas registradas"

    def add_mesa(self, mesa):
        self.mensajes.append(mesa)
        return "mensaje agregado"

    def contesta(self, num = ""):
        if(not (num == "")):
            return "Hablando con " + num
        else:
            return "Hablando"

    def add_agenda(self, num):
        self.agenda.append(num)
        return "Numero agregado " + num

    def remove_agenda(self, num):
        if(num in self.agenda):
            self.agenda.remove(num)

#///////////////////////////////////////////////////////////////////////////////

class Oven(Power):
    def __init__(self):
        Power.__init__(self, "Horno")
        self.temp = 0 #Centigrados
        self.time = 0 #Minutos

    def get_temp(self):
        return self.temp

    def get_time(self):
        return self.time

    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        return "EL tiempo para de coccion sera de " + self.time + " minutos"

    def change_temp(self, temp):
        self.isOn = True
        self.temp = temp
        return "La temperatura para la coccion sera de " + self.temp + " °C"
#///////////////////////////////////////////////////////////////////////////////

class Dryer(Power):
    def __init__(self):
        Power.__init__(self, "Secadora")
        self.time = 0
        self.index_state = 0
        self.state = ["Presecado", "Delicado", "Regular", "Mix"]

    def get_time(self):
        return self.time

    def get_state(self):
        return self.state

    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        return "El tiempo de secado es de " + self.time + " minutos"

    def change_state(self, state = "Regular"):
        if(self.isOn):
            if(state in self.state):
                self.index_state = self.state.index(state)
                return "La estado actual es : " + self.state[self.index_state]
            else:
                return "El estado que desea no existe, se pondra el estado por defecto"
        else:
            return "No es posible ir a ese estado porque la secadora esta apagada"
