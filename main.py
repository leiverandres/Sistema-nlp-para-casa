#-*- coding: utf-8 -*-
from controller import *
from elements import *

def interface():
    control = Controller_house()
    print "Elementos de la casa: "
    control.stateHouse()
    
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
        print "Casa: " + control.respond(s) + ", " + control.preguntas()


if __name__ == "__main__":
  interface()