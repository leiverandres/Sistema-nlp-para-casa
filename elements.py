class TV:
    def __init__(self):
        self.isOn = False
        self.channel = 1#max 100
        self.volume = 10

#///////////////////// getters ////////////////////
    def get_state(self):
        return self.isOn;
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume
#//////////////////// /////////////////////////////

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

class Light:
    def __init__ (self):
        self.isOn = False
        self.intensity = 0

#/////////// getters //////////////////////
    def get_state(self):
        return self.isOn;
    def get_intensity(self):
        return self.intensity
#/////////////////////////////////////////

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

    def up_down_inten(self, state):
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

# class Shower:
#     def __init__(self):
#         self.isOn = False
#         self.temp = 0 #temperatura
#
