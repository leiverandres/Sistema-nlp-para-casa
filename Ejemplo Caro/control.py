
class Namespace(dict):

  def __getattr__(self,attr):
    return self[attr]

  def __setattr__(self,attr, value):
    self[attr] = value

  def controlVentana1(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    #print str(attr) + "  " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La ventana fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La ventana ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La ventana ya estaba abierta"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La ventana fue cerrada"

  def controlVentana2(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    
    ##print "estabado2 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La ventana fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La ventana ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La ventana ya estaba abierta"
    else:
      self[attr] = 0
      return "La ventana fue cerrada"

  def controlVentana3(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La ventana fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La ventana ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La ventana ya estaba abierta"
    else:
      self[attr] = 0
      return "La ventana fue cerrada"


  def controlVentanas(self, attr1, valor):
    ventanas = []
      # 1 abierto, 0 cerrado, valor indica 1 para abrir, 0 para cerrar.=
    for x in xrange(0,len(attr1)):
      if(self[attr1[x]] == 0 and valor == 1):
        self[attr1[x]] = 1
        ventanas.append(attr1[x] + " fue abierta")
      elif (self[attr1[x]] == 1 and valor == 0):
        self[attr1[x]] = 0
        ventanas.append(attr1[x] +  " fue cerrada")
    return str(ventanas)

      

  def controlPuertappal(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    
    #print "estabado1 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La puerta fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La puerta ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La puerta ya estaba abierta"
    else:
      self[attr] = 0
      return "La puerta fue cerrada"

  def controlPuertacuarto(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    
    #print "estabado2 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La puerta fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La puerta ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La puerta ya estaba abierta"
    else:
      self[attr] = 0
      return "La puerta fue cerrada"

  def controlPuertabano(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La puerta fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La puerta ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La puerta ya estaba abierta"
    else:
      self[attr] = 0
      return "La puerta fue cerrada"


  def controlPuertas(self, attr1, valor):
    puertas = []
      # 1 abierto, 0 cerrado, valor indica 1 para abrir, 0 para cerrar.=
    for x in xrange(0,len(attr1)):
      if(self[attr1[x]] == 0 and valor == 1):
        self[attr1[x]] = 1
        puertas.append (attr1[x]  + "fue abierta")
      elif (self[attr1[x]] == 1 and valor == 0):
        self[attr1[x]] = 0
        puertas.append(attr1[x] + " fue cerrada")
    return str(puertas)

  def controlNevera(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La nevera fue abierta"
    elif(self[attr] == 0 and value == 0):
      return "La nevera ya estaba cerrada"
    elif(self[attr] == 1 and value == 1):
      return "La nevera ya estaba abierta"
    else:
      self[attr] = 0
      return "La nevera fue cerrada"

  def controlTvsala(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "El televisor fue encendido"
    elif(self[attr] == 0 and value == 0):
      return "El televisor ya estaba apagado"
    elif(self[attr] == 1 and value == 1):
      return "El televisor ya estaba encendido"
    else:
      self[attr] = 0
      return "El televisor fue apagado"

  def controlTvcuarto(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "El televisor fue encendido"
    elif(self[attr] == 0 and value == 0):
      return "El televisor ya estaba apagado"
    elif(self[attr] == 1 and value == 1):
      return "El televisor ya estaba encendido"
    else:
      self[attr] = 0
      return "El televisor fue apagado"

  def controlTelevisores(self, attr1, valor):
    televisores = []
      # 1 abierto, 0 cerrado, valor indica 1 para abrir, 0 para cerrar.=
    for x in xrange(0,len(attr1)):
      if(self[attr1[x]] == 0 and valor == 1):
        self[attr1[x]] = 1
        televisores.append(attr1[x] + " fue encendido")
      elif (self[attr1[x]] == 1 and valor == 0):
        self[attr1[x]] = 0
        televisores.append(attr1[x] + " fue apagado")
    return str(televisores)

  def controlHornilla1(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La hornilla uno  fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La hornilla uno  ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La hornilla uno ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La hornilla uno fue apagada"

  def controlHornilla2(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La hornilla dos  fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La hornilla dos  ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La hornilla dos ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La hornilla dos fue apagada"

  def controlHornilla3(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    ##print "estabado3 :" + str(self[attr]) + "  valor: " + str(value)
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La hornilla tres  fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La hornilla tres  ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La hornilla tres ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La hornilla tres fue apagada"

  def controlEstufa(self, attr1, valor):
    estufa = []
      # 1 abierto, 0 cerrado, valor indica 1 para abrir, 0 para cerrar.=
    for x in xrange(0,len(attr1)):
      if(self[attr1[x]] == 0 and valor == 1):
        self[attr1[x]] = 1
        estufa.append(attr1[x]+ " fue encendida")
      elif (self[attr1[x]] == 1 and valor == 0):
        self[attr1[x]] = 0
        estufa.append(attr1[x] + " fue apagada")
    return str(estufa)

  def controlLavadora(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La lavadora fue encendida"
    elif(self[attr] == 0 and value == 0):
      return "La lavadora ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La lavadora ya estababa encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La lavadora fue apagada"

  def controlSonido(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "El sonido fue encendido"
    elif(self[attr] == 0 and value == 0):
      return "El sonido ya estaba apagado"
    elif(self[attr] == 1 and value == 1):
      return "El sonido ya estaba encendido"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "El sonido fue apagado"

  def controlPC(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "El computador fue encendido y esta listo para su uso."
    elif(self[attr] == 0 and value == 0):
      return "El computador ya estaba apagado"
    elif(self[attr] == 1 and value == 1):
      return "El computador ya estaba encendido"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "El computador fue apagado"

  def controlLuzSala(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La luz de la sala fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La luz de la sala ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La luz de la sala ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La luz de la sala fue apagada"

  def controlLuzCuarto(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La luz del cuarto fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La luz del cuarto ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La luz del cuarto ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La luz del cuarto fue apagada"
  
  def controlLuzCocina(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La luz de la cocina fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La luz de la cocina ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La luz de la cocina ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La luz de la cocina fue apagada"
 
  def controlLuzBano(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La luz del bano fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La luz del bano ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La luz del bano ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La luz del bano fue apagada"
  
  def controlLuzPatio(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La luz del patio fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La luz del patio ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La luz del patio ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La luz del patio fue apagada"
  
  def controlLuzComedor(self, attr, value):
  # 1 abierto, 0 cerrado, value indica 1 para abrir, 0 para cerrar.=
    if(self[attr] == 0 and value == 1):
      self[attr] = 1
      return "La luz del comedor fue encendida."
    elif(self[attr] == 0 and value == 0):
      return "La luz del comedor ya estaba apagada"
    elif(self[attr] == 1 and value == 1):
      return "La luz del comedor ya estaba encendida"
    elif(self[attr] == 1 and value == 0):
      self[attr] = 0
      return "La luz del comedor fue apagada"
  
  def controlLuces(self, attr1, valor):
    luces= []
    # 1 abierto, 0 cerrado, valor indica 1 para abrir, 0 para cerrar.=
    for x in xrange(0,len(attr1)):
      if(self[attr1[x]] == 0 and valor == 1):
        self[attr1[x]] = 1
        luces.append(attr1[x] + " fue encendida")
      elif (self[attr1[x]] == 1 and valor == 0):
        self[attr1[x]] = 0
        luces.append(attr1[x] + " fue apagada")
    return str(luces)   

  def controlEstados(self, attr1, valor):
    estados = []
      # 1 abierto, 0 cerrado, valor indica 1 para abrir, 0 para cerrar.=
    for x in xrange(0,len(attr1)):
      if(self[attr1[x]] == 0):
        estados.append(attr1[x] + " se encuentra apagado o cerrado")
      elif (self[attr1[x]] == 1 ):
        estados.append(attr1[x] + " se encuentra encendido o abierto")  
    return str (estados) 

  def estado(self, attr, attr1):
    if(self[attr] == 0):
      return attr + " se encuentra apagado o cerrado"
    elif (self[attr] == 1):
      return attr + " se encuentra encendido o abierto"

  def salir(self, attr, attr1):
    return attr

  def garbage(self, attr, attr1):
    return attr

  def bien(self, attr, attr1):
    return attr

  def mal(self, attr, attr1):
    return attr

