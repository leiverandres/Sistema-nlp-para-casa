#-*- coding: utf-8 -*-
from controller import *
from elements import *

def interface():
    control = Controller_house()
    exit = ["salir", "adios", "hasta luego", "hasta pronto", "chao"]
    
    print print_all()
    print 'Para salir puedes escribir una de estas opciones:'
    print exit
    print '='*72
    print "Casa: Hola, que deseas hacer"
    s = ""
    
    while (s not in exit):
        try:
          s = raw_input("TÚ: ")
          s = s.lower()
        except EOFError:
          s = "salir"
          print s
        while s[-1] in "!.": s = s[:-1]
        print "Casa: " + control.respond(s) + "\n" + control.questions()

if __name__ == "__main__":
  interface()