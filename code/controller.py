# -*- coding: utf-8 -*-
import string
import re
import random
from elements import *

#//////////////////////////////////////////////////////////////////////
# Creando los objetos de la casa

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
        '''for i in range(0, len(self.keys)):
          match = self.keys[i].match(str)
          if match:
            resp = self.values[i]
            return resp[0](resp[1],resp[2])''' 

    def stateHouse(self): #Aca se dira el estado actual de la casa
        pass

gPats = [
  [r'.*',
  [ 
    #formato --> nombre de la funcion, lista de argumentos
    ]],
]