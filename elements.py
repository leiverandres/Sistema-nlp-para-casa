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
        if(isOn):
            if (state):
                self.channel = (self.channel + 1) % 120
                print "Canal next: " + str(elf.channel)
            else:
                if(self.channel - 1 <= 0):
                    self.set_channel(120);
                    print "Canal prev: " + str(sel.channel)
                else:
                    self.chennel -= 1
                    print "Canal prev: " + str(elf.channel)
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
///////////////////////////////////////////////////////////////////////////////

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
///////////////////////////////////////////////////////////////////////////////
class Shower:
    def __init__(self):
        self.isOn = False
        self.temp = 25 #temperatura
        self.flow = 0

    def get_state(self):
        return self.isOn
    def get_state(self):
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
            if(not self, isOn):
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
///////////////////////////////////////////////////////////////////////////////
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
///////////////////////////////////////////////////////////////////////////////

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
