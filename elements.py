class TV:
    def __init__(self):
        self.isOn = False
        self.channel = 1#max 100
        self.volume = 10

    def get_state(self):
        return self.isOn;
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume

    def change_channel(self, state):
        if(self.isOn):
            if (state):
                self.channel = (self.channel + 1) % 120
                print "Canal next: " + str(self.channel)
            else:
                if(self.channel - 1 <= 0):
                    self.set_channel(120);
                    print "Canal prev: " + str(self.channel)
                else:
                    self.channel -= 1
                    print "Canal prev: " + str(self.channel)
        else:
            print "El tv esta apagado, enciendalo."

    def set_channel(self, channel):
        if(self.isOn):
            if(channel > 0 and channel < 121):
                self.channel = channel
                print "Canal actual: " + str(channel)
            else:
                print "No existe este canal."
        else:
            print "El tv esta apagado, enciendalo."

    def change_volume(self, state):
        if(self.isOn):
            if(state):
                self.volume += 1
                print "Volumen ++: " + str(self.volume)
            else:
                self.volume -= 1
                print "Volumen --: " + str(self.volume)
        else:
            print "El tv esta apagado, enciendalo."

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "El tv ya esta encendida."
            else:
                self.isOn = True
                print "Tv encendida."
        else:
            if(not self.isOn):
                print "El tv ya esta apagada."
            else:
                self.isOn = False
                print "Tv apagada."
#///////////////////////////////////////////////////////////////////////////////
class Light:
    def __init__ (self):
        self.isOn = False
        self.intensity = 0

    def get_state(self):
        return self.isOn;
    def get_intensity(self):
        return self.intensity

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "La Luz ya esta encedida."
            else:
                self.isOn = True
                print "Luz encendida."
        else:
            if(not self.isOn):
                print "La luz ya esta apagada."
            else:
                self.isOn = False
                print "Luz apagada."

    def set_intensity(self, cant):
        if(cant == 0):
            self.turn_on_off(True)
            self.intensity = 15
            self.turn_on_off(True)
            print "Canal intensidad actual: " + str(self.intensity)
        elif(cant == 1):
            self.turn_on_off(True)
            self.intensity = 50
            print "Canal intensidad actual: " + str(self.intensity)
        elif(cant == 2):
            #self.turn_on_off(True)
            self.intensity = 75
            print "Canal intensidad actual: " + str(self.intensity)

    def up_down_intensity(self, state):
        if(state):
            if((self.intensity + 10) > 100):
                self.intensity = 100
                print "La intensidad esta en su maximo valor " + str(self.intensity)
            else:
                self.intensity += 10
                self.turn_on_off(True)
                print "Intensidad en: " + str(self.intensity)
        else:
            if((self.intensity - 10) < 0):
                self.intensity = 0
                self.turn_on_off(False)
                print "La intesidad esta en su minimo valor." + str(self.intensity)
            else:
                self.intensity -= 10
                self.turn_on_off(True)
                print "Intensidad en: " + str(self.intensity)
#///////////////////////////////////////////////////////////////////////////////
class Shower:
    def __init__(self):
        self.isOn = False
        self.temp = 25 #temperatura
        self.flow = 0

    def get_state(self):
        return self.isOn
    def get_temp(self):
        return self.temp
    def get_flow(self):
        return self.flow

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "La ducha ya esta abierta."
            else:
                self.isOn = True
                print "Ducha abierta."
        else:
            if(not self.isOn):
                print "La ducha ya esta cerrada."
            else:
                self.isOn = False
                print "Ducha cerrada."

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                if((self.temp + 10) > 100):
                    self.temp = 100
                    print "El agua esta en su maxima temperatura"
                else:
                    self.temp += 10
                    print "El agua esta en " + str(self.temp) + "%."
            else:
                if((self.temp - 10) < 0):
                    self.temp = 0
                    print "La ducha esta es su minima temperatura"
                else:
                    self.temp -= 10
        else:
            print "No puedo modificar la temperatura, la ducha esta cerrada"

    def up_down_flow(self, state):
        if(self.isOn):
            if(state):
                if((self.flow +  2) > 10):
                    self.flow = 10
                    self.isOn = True
                    print "El flujo de agua esta en su nivel maximo"
                else:
                    self.flow += 2
                    self.isOn = True
                    print "El nivel del flujo es " + str(self.flow)
            else:
                if((self.flow - 2) < 0):
                    self.flow = 0
                    self.isOn = False
                    print "La ducha se ha cerrado"
                else:
                    self.flow -= 2
        else:
            print "No puedo modificar el nivel de flujo, la ducha esta cerrada"
#///////////////////////////////////////////////////////////////////////////////
class Dishwasher:

    def __init__(self):
        self.isOn = False
        self.haveDish = False
        self.time = 0

    def get_Power(self):
        return self.isOn
    def get_have_dish(self):
        return self.haveDish
    def set_time(self, time):
        self.time = time
    def set_have_dish(self, state):
        self.haveDish = state

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "El lavaplatos ya esta encedido"
            else:
                self.isOn = True
                print "Lavaplatos encendio"
        else:
            if(not self.isOn):
                print "El lavaplatos ya esta apagado"
            else:
                self.isOn = False
                print "Lavaplatos apagado"

    def wash(self, time = 5):
        if(self.haveDish):
            self.isOn = True
            self.set_time(time)
        else:
            print "No hay platos sucios para lavar en el lavaplatos"
#///////////////////////////////////////////////////////////////////////////////
class SoundSystem:

    def __init__ (self):
        self.isOn = False
        self.volume = 0
        self.song = 0 #max 15
        self.stations = ["88.2", "89.6", "95.6", "98.4", "100.2", "102.5", "103.9", "105.7", "106.9", "107.9"]
        self.index_station = 0

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "El equipo ya esta encendido"
            else:
                self.isOn = True
        else:
            if(not self.isOn):
                print "El equipo ya esta apagado"
            else:
                self.isOn = False

    def change_station(self, station = "88.2"):
        if(self.isOn):
            if(station in self.stations):
                self.index_station = self.stations.index(station)
                print "La estacion actual es : " + self.stations[self.index_station]
            else:
                print "La estacion buscada no existe, se pondra la estacion por defecto"
        else:
            print "No puedo modificar, esta apagado"

    def next_back_station(self, state):
        if(self.isOn):
            if(state):
                self.index_station = (self.index_station + 1) % 10
                print "La estacion actual es : " + self.stations[self.index_station]
            else:
                if((self.index_station - 1) < 0):
                    self.index_station += 10
                    print "La estacion actual es : " + self.stations[self.index_station]
                else:
                    self.index_station -= 1
                print "La estacion actual es : " + self.stations[self.index_station]
        else:
            print "No puedo modificar, esta apagado"

    def next_back_song(self, state):
        if(self.isOn):
            if(state):
                self.song = (self.song + 1) % 15
                print "La cancion actual es : " + str(self.song)
            else:
                if((self.song - 1) < 0):
                    self.song += 15
                    print "La cancion actual es : " + str(self.song)
                else:
                    self.song -= 1
                print "La cancion actual es : " + str(self.song)
        else:
            print "No puedo modificar, esta apagado"
#///////////////////////////////////////////////////////////////////////////////
class Curtains:

    def __init__(self):
        self.isOpen = False #Falso totalmente cerradas, True totalmente abiertas
        self.cant = 0 #0 es cerrada, 100 es totalmente abierta

    def get_state(self):
        return self.isOpen

    def get_cant(self):
        return self.cant

    def turn_open_closed(self, state):
        if(state):
            if(self.isOpen):
                print "Las cortinas ya estan abiertas."
            else:
                self.isOpen = True
                self.cant = 100
                print "Cortinas abiertas."
        else:
            if(not self.isOpen):
                print "Las cortinas ya estan cerradas."
            else:
                self.isOpen = False
                self.cant = 0
                print "Cortinas cerradaa."

    def up_down_cant(self, state):
        if(state):
            if(self.isOpen):
                print "Las cortinas ya estan totalmente abiertas"
            else:
                if(self.cant + 10 > 100):
                    self.cant = 100
                    print "Las cortinas ya estan totalmente abiertas"
                else:
                    self.cant += 10
                    print "Las cortinas estan abiertas en un " + str(self.cant)+"%"
        else:
            if(not self.isOpen):
                print "Las cortinas ya estan totalmente cerradas"
            else:
                if(self.cant - 10 < 0):
                    self.cant = 0
                    print "Las cortinas ya estan cerradas totalmente"
                else:
                    self.cant -= 10
                    print "Las cortinas estan abiertas en un " + str(self.cant)+"%"
 #///////////////////////////////////////////////////////////////////////////////
class Printer:

    def __init__(self):
        self.isOn = False
        self.sheets = 10 #Numero de hojas que tiene la impresora

    def get_state(self):
        return self.isOn

    def get_sheets(self):
        return self.sheets

    def put_sheets(self, sheets):
        self.sheets += sheets

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "La impresora ya esta encendida"
            else:
                print "Impresora encendida"
        else:
            if(not self.isOn):
                print "La impresora ya esta apagada"
            else:
                print "Impresora apagada"

    def print_out(self, pages, copies = 1):
        if(pages*copies <= self.sheets):
            self.sheets -= pages*copies
            print "Documentos impresos...","La impresora tiene ahora " + str(self.sheets) + " hoja(s) disponibles"
        else:
            print "Por favor ponga al menos " + str(pages*copies - self.sheets) + " hoja(s) en la impresora para poder imprimir su documento"
#/////////////////////////////////////////////////////////////////////////////////////////////

class Email:
    def __init__(self):
        self.inbox = ["hi, need help", "meeting saturday", "another mail"] #numero de corros sin leer
        self.to_read = len(self.inbox)

    def get_mesa(self):
        return self.to_read

    def without_read(self):
        print "Hay " + str(self.get_mesa()) + " mensajes sin leer"

    def list_mesa(self):
        if(self.to_read > 0):
            print "Todos los mensajes"
            for i in self.inbox:
                print i
        else:
            print "No hay mensajes por leer."

    def show_one_mesa(self, index):
        if(index <= self.to_read):
            print "Mesaje numero " + str(index)
            print self.inbox[index]
        else:
            print "No existe el mensaje solicitado"

    def show_last_mesa(self):
        if(self.to_read > 0):
            print self.inbox[self.to_read - 1]
        else:
            print "No hay mensajes por leer."

    def show_oldest_mesa(self):
        if(self.to_read > 0):
            print self.inbox[0]
        else:
            print "No hay mensajes por leer."

    def remove_mesa(self, index):#index debe venir index 1
        if(index <= self.to_read):
            print "mensaje eliminado:\n" + self.inbox.pop(index)
            self.to_read -= 1
        else:
            print "No existe el mensaje solicitado"

    def send_mesaje(self, string):
        print "Mensaje enviado:\n" + string
#//////////////////////////////////////////////////////////////////////////////

class Air:
    def __init__(self):
        self.isOn = False
        self.temp = 25 #grados centigrados

    def get_isOn(self):
        return self.isOn
    def get_temp(self):
        return self.temp

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "El aire acondicionado ya esta encendido"
            else:
                print "Aire acondicionado encendido"
                self.isOn = True
        else:
            if(not self.isOn):
                print "El aire acondicionado ya esta apagado"
            else:
                print "Aire acondicionado apagado"
                self.isOn = False

    def put_temp(self, temp):
        if(self.isOn):
            self.temp = temp
            print "La temperatura esta en " + str(self.temp) + " grados C"
        else:
            print "No puedo modifica la temperatura, el aire esta apagado"

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                self.temp += 1
            else:
                self.temp -= 1
            print "La temperatura esta en " + str(self.temp) + " grados C"
        else:
            print "No puedo modifica la temperatura, el aire esta apagado"

#////////////////////////////////////////////////////////////////////////////
#security alarm
class Alert:
    def __init__(self):
        self.isOn = False
        self.volume = 7 #max 10

    def get_isOn(self):
        return self.isOn
    def get_volume(self):
        return self.volume

    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "La alarma ya esta apagada"
            else:
                self.isOn = True
                print "Alarma encendida"
        else:
            if(not self.isOn):
                print "La alarma ya esta apagada"
            else:
                self.isOn = False
                print "Alarma apagada"

    def up_down_vol(self, state):
        if(self.isOn):
            if(state):
                if((self.volume + 1) > 10):
                    self.volume =  10
                    print "El volumen esta en su maximo valor: 10"
                else:
                    self.volume += 1
                    print "El volumen de la alarma es: " + str(self.volume)
            else:
                if((self.volume - 1) < 2):
                    self.volumen = 2
                    print "El volumen esta en su minimo valor: 2"
                else:
                    self.volume -= 1
                    print "El volumen de la alarma es: " + str(self.volume)
        else:
            print "No puedo modificar el volumen, la alarma esta apagada"
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
                print "La hornilla " + str(self.id) + " ya esta encendida"
            else:
                print "La hornilla " + str(self.id) + " esta encendida"
        else:
            if(not self.isOn):
                print "La hornilla " + str(self.id) + " ya esta apagada"
            else:
                print "La hornilla" + str(self.id) + " esta apagada"

    def change_intensity(self, state):
        if(state):
            self.isOn = True
            if(self.intensity + 2 > 10):
                self.intensity = 10
                print "La hornilla " + str(self.id) + " esta en su maximo intensidad"
            else:
                self.intensity += 2
                print "La hornilla " + str(self.id) + " es con una intensidad de " + str(self.intensity)
        else:
            if(self.intensity - 2 < 0):
                self.isOn = False
                self.intensity = 0
                print "La hornilla " + str(self.id) + " esta apagada"
            else:
                self.intensity -= 2
                print "La hornilla " + str(self.id) + " es con una intensidad de " + str(self.intensity)
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
            print "La hornilla especificada no es valida"
        else:
            return self.hornillas[id - 1]

    def turn_on_off(self, id, state):
        if(id <= 0 or id > 4):
            print "La hornilla especificada no es valida"
        else:
            self.hornillas[id - 1].turn_on_off(state)

    def change_intensity_hornilla(self, id, state):
        if(id <= 0 or id > 4):
            print "La hornilla especificada no es valida"
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
        print "Elementos en la nevera: "
        for i in self.elements:
            print i

    def rm_element(self, elem):
        if(self.no_elem > 0):
            if(elem in self.elements):
                self.elements.remove(elem)
                print "Elemento removido " + elem
            else:
                print "El elemento no se encuentra en la nevera"
        else:
            print "No hay elementos, es hora de comprar!"

    def add_elements(self, elem):
        self.elements.append(elem)
        print "Elemento agregado " + elem

    def up_down_temp(self, state):
        if(self.isOn):
            if(state):
                self.temp += 1
            else:
                self.temp -=1
        else:
            print "Nevera apagada"

    def put_temp(self, temp):
        if(self.isOn):
            self.temp = temp
        else:
            print "Nevera apagada"
#/////////////////////////////////////////////////////////////////////////////////

class Washer:
  def _init_(self):
      self.isOn = False
      self.time = 0
      self.index_state = 4
      self.state = ["Lana", "Delicado", "Sintetico", "Resistente", "Intensivo"]

  def get_Power(self):
      return self.isOn

  def get_time(self):
      return self.time

  def get_state(self):
      return self.state

  def change_time(self, minute):
      self.isOn = True
      self.time = minute
      print "El tiempo de lavado es de " + self.time + " minutos"

  def turn_on_off(self, state):
      if(state):
          if(self.isOn):
              print "La lavadora ya esta encendida"
          else:
              self.isOn = True
          print "Lavadora encendida"
      else:
          if(not self.isOn):
              print "La lavadora ya esta apagada"
          else:
              self.isOn = False
              print "La lavadora esta apagada"

  def change_state(self, state = "Delicado"):
      if(self.isOn):
          if(state in self.state):
              self.index_state = self.state.index(state)
              print "La estado actual es : " + self.state[self.index_state]
          else:
              print "El estado que desea no existe, se pondra el estado por defecto"
      else:
          print "No es posible ir a ese estado porque la lavadora esta apagada"

#//////////////////////////////////////////////////////////////////////////////

class Phone:
    def __init__(self):
        self.last_number = ""
        self.agenda = ["321456789", "789456123", "741258963", "369852147"]
        self.numbers = len(self.agenda)

    def llamar(self, num):
        print "Llamando a ... " + num

    def contesta(self):
        print "Hablando con"

    def add_agenda(self, num):
        self.agenda.append(num)
        print "Numero agradado " + num

    def remove_agenda(self, num):
        if(num in self.agenda):
            self.agenda.remove(num)
#///////////////////////////////////////////////////////////////////////////////
class Oven:
    def __init__(self):
        self.isOn = False
        self.temp = 0 #Centigrados
        self.time = 0 #Minutos
    
    def get_Power(self):
        return self.isOn
    
    def get_temp(self):
        return self.temp
    
    def get_time(self):
        return self.time
    
    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "El horno ya esta prendido"
            else:
                self.isOn = True
                print "El horno esta prendido"
        else:
            if(not self.isOn):
                print "El horno ya esta apagado"
            else:
                self.isOn = False
                print "El horno esta apagado"
    
    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        print "EL tiempo para de coccion sera de " + self.time + " minutos"
    
    def change_temp(self, temp):
        self.isOn = True
        self.temp = temp
        print "La temperatura para la coccion sera de " + self.temp + " C"
#///////////////////////////////////////////////////////////////////////////////    
class Dryer:
    def __init__(self):
        self.isOn = False
        self.time = 0
        self.index_state = 0
        self.state = ["Presecado", "Delicado", "Regular", "Mix"]
    
    def get_Power(self):
        return self.isOn
    
    def get_time(self):
        return self.time
        
    def get_state(self):
        return self.state
    
    def change_time(self, minute):
        self.isOn = True
        self.time = minute
        print "El tiempo de secado es de " + self.time + " minutos"
    
    def turn_on_off(self, state):
        if(state):
            if(self.isOn):
                print "La secadora ya esta encendida"
            else:
                self.isOn = True
                print "Secadora encendida"
        else:
            if(not self.isOn):
                print "La secadora ya esta apagada"
            else:
                self.isOn = False
                print "La secadora esta apagada"
    
    def change_state(self, state = "Regular"):
        if(self.isOn):
            if(state in self.state):
                self.index_state = self.state.index(state)
                print "La estado actual es : " + self.state[self.index_state]
            else:
                print "El estado que desea no existe, se pondra el estado por defecto"
        else:
            print "No es posible ir a ese estado porque la secadora esta apagada"
