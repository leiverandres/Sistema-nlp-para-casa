#-*- coding: utf-8 -*-


import string
import re
import random
from control import *


data = Namespace()

data.object = ('ventanasala', 'ventanacuarto', 'ventanacomedor', 
              'puertappal', 'puertacuarto', 'puertabano', 'nevera', 
              'tvsala', 'tvcuarto', 'hornilla1', 'hornilla2', 'hornilla3',
              'lavadora', 'sonido','computador', 'luzsala', 'luzcuarto', 'luzcocina', 
              'luzbano', 'luzpatio', 'luzcomedor')

data.ventanasala = 0
data.ventanacuarto = 0
data.ventanacomedor = 0
data.puertappal = 0
data.puertacuarto = 0
data.puertabano = 0
data.nevera = 0
data.tvsala = 0
data.tvcuarto = 0
data.hornilla1 = 0
data.hornilla2 = 0
data.hornilla3 = 0
data.lavadora = 0
data.sonido = 0
data.computador = 0
data.luzsala = 0
data.luzcuarto = 0
data.luzcocina = 0
data.luzbano = 0
data.luzpatio = 0
data.luzcomedor = 0



class Casa(object):

  def __init__(self):
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
    self.values = map(lambda x:x[1],gPats)

  def respond(self,str):
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = self.values[i]
        return resp[0](resp[1],resp[2]) 

  def preguntas(self):
    a = ["Estoy preparado para una nueva orden.", "Que otra orden deseas darme?", "Puedo irme a descansar?", "Te sientes a gusto con lo que hago?"]
    resp = random.choice(a)
    return resp

  def estadoCasa(self):
    for i in range(0,len(data.object)):
      resp = data.estado(data.object[i], "a")
      print  resp


gPats = [
  [r'(.*)(abrir|abra)(.*)ventana(.*)sala(.*)',
  [ 
    data.controlVentana1, data.object[0], 1
    ]],

  [r'(.*)(cerrar|cierre)(.*)ventana(.*)sala(.*)',
  [ 
    data.controlVentana1,data.object[0], 0
    ]],

  [r'(.*)estado(.*)ventana(.*)sala(.*)',
  [ 
    data.estado, data.object[0], 1
    ]],

  [r'(.*)(abrir|abra)(.*)ventana(.*)cuarto(.*)',
  [ 
    data.controlVentana2,data.object[1], 1
    ]], 
 
  [r'(.*)(cerrar|cierre)(.*)ventana(.*)cuarto(.*)',
  [ 
    data.controlVentana2, data.object[1], 0
    ]],  

  [r'(.*)estado(.*)ventana(.*)cuarto(.*)',
  [ 
    data.estado, data.object[1], 0
    ]],

  [r'(.*)(abrir|abra)(.*)ventana(.*)comedor(.*)',
  [ 
    data.controlVentana3, data.object[2], 1
    ]], 
 
  [r'(.*)(cerrar|cierre)(.*)ventana(.*)comedor(.*)',
  [ 
    data.controlVentana3, data.object[2], 0
    ]],
  
  [r'(.*)estado(.*)ventana(.*)comedor(.*)',
  [ 
    data.estado, data.object[2], 0
    ]],
  
  [r'(.*)(abrir|abra)(.*)ventanas(.*)',
  [ 
    data.controlVentanas, [data.object[0], data.object[1],data.object[2]], 1
    ]],
    

  [r'(.*)(cerrar|cierre)(.*)ventanas(.*)',
  [ 
    data.controlVentanas, [data.object[0], data.object[1],data.object[2]], 0
    ]],

  [r'(.*)(estado|estados)(.*)ventanas(.*)',
  [ 
    data.controlEstados, [data.object[0], data.object[1],data.object[2]], 0
    ]],

  [r'(.*)(abrir|abra)(.*)puerta(.*)principal(.*)',
  [ 
    data.controlPuertappal, data.object[3], 1
    ]], 
 
  [r'(.*)(cerrar|cierre)(.*)puerta(.*)principal(.*)',
  [ 
    data.controlPuertappal, data.object[3], 0
    ]],

  [r'(.*)estado(.*)puerta(.*)principal(.*)',
  [ 
    data.estado, data.object[3], 0
    ]],

  [r'(.*)(abrir|abra)(.*)puerta(.*)cuarto(.*)',
  [ 
    data.controlPuertacuarto, data.object[4], 1
    ]], 
 
  [r'(.*)(cerrar|cierre)(.*)puerta(.*)cuarto(.*)',
  [ 
    data.controlPuertacuarto, data.object[4], 0
    ]], 

  [r'(.*)estado(.*)puerta(.*)cuarto(.*)',
  [ 
    data.estado, data.object[4], 0
    ]],   

  [r'(.*)(abrir|abra)(.*)puerta(.*)baño(.*)',
  [ 
    data.controlPuertabano, data.object[5], 1
    ]], 
 
  [r'(.*)(cerrar|cierre)(.*)puerta(.*)baño(.*)',
  [ 
    data.controlPuertabano, data.object[5], 0
    ]],

  [r'(.*)estado(.*)puerta(.*)baño(.*)',
  [ 
    data.estado, data.object[5], 0
    ]],

  [r'(.*)(abrir|abra)(.*)puertas(.*)',
  [ 
    data.controlPuertas, [data.object[3], data.object[4],data.object[5]], 1
    ]],
    

  [r'(.*)(cerrar|cierre)(.*)puertas(.*)',
  [ 
    data.controlPuertas, [data.object[3], data.object[4],data.object[5]], 0
    ]],
  
  [r'(.*)(estado|estados)(.*)puertas(.*)',
  [ 
    data.controlEstados, [data.object[3], data.object[4],data.object[5]], 0
    ]],

  [r'(.*)(abrir|abra)(.*)(nevera|refrijerador)(.*)',
  [ 
    data.controlNevera, data.object[6], 1
    ]], 
 
  [r'(.*)(cerrar|cierre)(.*)(nevera|refrijerador)(.*)',
  [ 
    data.controlNevera, data.object[6], 0
    ]],

  [r'(.*)estado(.*)(nevera|refrijerador)(.*)',
  [ 
    data.estado, data.object[6], 0
    ]],
  [r'(.*)(encender|encienda|prender|prenda)(.*)(televisor|tv)(.*)(sala)(.*)',
  [ 
    data.controlTvsala, data.object[7], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(televisor|tv)(.*)(sala)(.*)',
  [ 
    data.controlTvsala, data.object[7], 0
    ]],

  [r'(.*)estado(.*)(televisor|tv)(.*)(sala)(.*)',
  [ 
    data.estado, data.object[7], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(televisor|tv)(.*)(cuarto)(.*)',
  [ 
    data.controlTvcuarto, data.object[8], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(televisor|tv)(.*)(cuarto)(.*)',
  [ 
    data.controlTvcuarto, data.object[8], 0
    ]],

  [r'(.*)estado(.*)(televisor|tv)(.*)(cuarto)(.*)',
  [ 
    data.estado, data.object[8], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(televisores|tvs)(.*)',
  [ 
    data.controlTelevisores, [data.object[7],data.object[8]], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(televisores|tvs)(.*)',
  [ 
    data.controlTelevisores, [data.object[7],data.object[8]], 0
    ]],

  [r'(.*)(estado|estados)(.*)(televisores|tvs)(.*)',
  [ 
    data.controlEstados, [data.object[7],data.object[8]], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(primera|primer)?(.*)(hornilla)(.*)(uno|1)?(.*)',
  [ 
    data.controlHornilla1, data.object[9], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(primera|primer)?(.*)(hornilla)(.*)(uno|1)?(.*)',
  [ 
    data.controlHornilla1, data.object[9], 0
    ]],

  [r'(.*)estado(.*)(primera|primer)?(.*)(hornilla)(.*)(uno|1)?(.*)',
  [ 
    data.estado, data.object[9], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(segunda)?(.*)(hornilla)(.*)(dos|2)?(.*)',
  [ 
    data.controlHornilla2, data.object[10], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(segunda)?(.*)(hornilla)(.*)(dos|2)?(.*)',
  [ 
    data.controlHornilla2, data.object[10], 0
    ]],

  [r'(.*)estado(.*)(segunda)?(.*)(hornilla)(.*)(dos|2)?(.*)',
  [ 
    data.estado, data.object[10], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(tercera|tercer)?(.*)(hornilla)(.*)(tres|3)?(.*)',
  [ 
    data.controlHornilla3, data.object[11], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(tercera|tercer)?(.*)(hornilla)(.*)(tres|3)?(.*)',
  [ 
    data.controlHornilla3, data.object[11], 0
    ]],

  [r'(.*)estado(.*)(tercera|tercer)?(.*)(hornilla)(.*)(tres|3)?(.*)',
  [ 
    data.estado, data.object[11], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(hornillas|estufa)(.*)',
  [ 
    data.controlEstufa, [data.object[9], data.object[10],data.object[11]], 1
    ]],
    
  [r'(.*)(apagar|apague)(.*)(hornillas|estufa)(.*)',
  [ 
    data.controlEstufa, [data.object[9], data.object[10],data.object[11]], 0
    ]],

  [r'(.*)(estado|estados)(.*)(hornillas|estufa)(.*)',
  [ 
    data.controlEstados, [data.object[9], data.object[10],data.object[11]], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)lavadora(.*)',
  [ 
    data.controlLavadora, data.object[12], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)lavadora(.*)',
  [ 
    data.controlLavadora, data.object[12], 0
    ]],  
 
  [r'(.*)estado(.*)lavadora(.*)',
  [ 
    data.estado, data.object[12], 0
    ]],  

  [r'(.*)(encender|encienda|prender|prenda)(.*)sonido(.*)',
  [ 
    data.controlSonido, data.object[13], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)sonido(.*)',
  [ 
    data.controlSonido, data.object[13], 0
    ]],  

  [r'(.*)estado(.*)sonido(.*)',
  [ 
    data.estado, data.object[13], 0
    ]],  

  [r'(.*)(encender|encienda|prender|prenda)(.*)(computador|pc)(.*)',
  [ 
    data.controlPC, data.object[14], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(computador|pc)(.*)',
  [ 
    data.controlPC, data.object[14], 0
    ]],
 
  [r'(.*)estado(.*)(computador|pc)(.*)',
  [ 
    data.estado, data.object[14], 0
    ]],
  [r'(.*)(encender|encienda|prender|prenda)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)sala(.*)',
  [ 
    data.controlLuzSala, data.object[15], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)sala(.*)',
  [ 
    data.controlLuzSala, data.object[15], 0
    ]], 

  [r'(.*)estado(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)sala(.*)',
  [ 
    data.estado, data.object[15], 0
    ]], 

  [r'(.*)(encender|encienda|prender|prenda)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)cuarto(.*)',
  [ 
    data.controlLuzCuarto, data.object[16], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)cuarto(.*)',
  [ 
    data.controlLuzCuarto, data.object[16], 0
    ]], 

  [r'(.*)estado(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)cuarto(.*)',
  [ 
    data.estado, data.object[16], 0
    ]],     

  [r'(.*)(encender|encienda|prender|prenda)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)cocina(.*)',
  [ 
    data.controlLuzCocina, data.object[17], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)cocina(.*)',
  [ 
    data.controlLuzCocina, data.object[17], 0
    ]], 

  [r'(.*)estado(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)cocina(.*)',
  [ 
    data.estado, data.object[17], 0
    ]], 

  [r'(.*)(encender|encienda|prender|prenda)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)Bano(.*)',
  [ 
    data.controlLuzBano, data.object[18], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)Bano(.*)',
  [ 
    data.controlLuzBano, data.object[18], 0
    ]],

  [r'(.*)estado(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)Bano(.*)',
  [ 
    data.estado, data.object[18], 0
    ]],

  [r'(.*)(encender|encienda|prender|prenda)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)patio(.*)',
  [ 
    data.controlLuzPatio, data.object[19], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)patio(.*)',
  [ 
    data.controlLuzPatio, data.object[19], 0
    ]],

  [r'(.*)estado(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)patio(.*)',
  [ 
    data.estado, data.object[19], 0
    ]],
  [r'(.*)(encender|encienda|prender|prenda)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)comedor(.*)',
  [ 
    data.controlLuzComedor, data.object[20], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)comedor(.*)',
  [ 
    data.controlLuzComedor, data.object[20], 0
    ]],

  [r'(.*)estado(.*)(luz|bombillas|bombillo|lampara|lamparas|luces)(.*)comedor(.*)',
  [ 
    data.estado, data.object[20], 0
    ]],  

  [r'(.*)(encender|encienda|prender|prenda)(.*)(bombillas|lamparas|luces)(.*)',
  [ 
    data.controlLuces, [data.object[15],data.object[16],data.object[17],data.object[18],data.object[19],data.object[20]], 1
    ]], 
 
  [r'(.*)(apagar|apague)(.*)(bombillas|lamparas|luces)(.*)',
  [ 
    data.controlLuces, [data.object[15],data.object[16],data.object[17],data.object[18],data.object[19],data.object[20]], 0
    ]],

  [r'(.*)(estado|estados)(.*)(bombillas|lamparas|luces)(.*)',
  [ 
    data.controlEstados, [data.object[15],data.object[16],data.object[17],data.object[18],data.object[19],data.object[20]], 0
    ]],

  [r'(.*)(si|bien)(.*)',
  [ 
    data.bien, "Que bueno", "."
    ]],

  [r'(.*)(no|mal|triste|preocupado)(.*)',
  [ 
    data.mal, "Luces muy seguro", "."
    ]],

  [r'(.*)salir(.*)',
  [ 
    data.salir, "Hasta pronto!", "adios"
    ]],

  [r'(.*)',
  [ data.garbage, "intentelo de nuevo, orden irreconocible", "."]]

  ]
  

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------



def command_interface():
  control = Casa();
  print "Elementos de la casa: "
  control.estadoCasa()
  print 'Para salir escribe "Salir"'
  print '='*72
  print "Casa: Hola, que deseas hacer"
  s = ""
  while s.lower() != 'salir':
    try:
      s = raw_input("TÚ: ")
    except EOFError:
      s = "salir"
      print s
    while s[-1] in "!.": s = s[:-1]
    print "Casa: " + control.respond(s) + ", " +control.preguntas()


if __name__ == "__main__":
  command_interface()