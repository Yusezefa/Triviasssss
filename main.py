import time

#colores
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
RESET = '\033[39m'

#Puntaje
puntaje = 0

#Intentos
iniciar_trivia = True  
intentos = 0  



# Texto inicio
print(ROJO+"¿Crees estar listo para postular a la UNMSM?"+RESET)
time.sleep(1)
print(AZUL+"Pondremos a prueba tus conocimientos e ingenio ;)"+RESET)
time.sleep(1)
print("Tienes", puntaje, "puntos")

# Personalización

nombre = input("Ingresa tu nombre: \n")

# Saludo personalizado
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)
time.sleep(1)

while iniciar_trivia == True: 
  
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  confirmacion1 = input("¿Estamos listos para empezar?\n")
  while confirmacion1 not in ("si", "no"):
  	confirmacion1 = input(
  	    "Debes responder si o no. Ingresa nuevamente tu respuesta: ")
  if confirmacion1 == "si":
  	print("¡Comencemos", nombre, "!")
  else:
  	print("Ya estamos aquí ;)")
  
  time.sleep(2)
  	# Pregunta 1
  print(VERDE+"\n1) Mientras que Juan pone al fuego la sartén, ingresa una llamada telefónica que atiende por varios minutos. Al percatarse de que la sartén sigue en el fuego, intenta retirarla, pero se quema y la suelta bruscamente. Esta respuesta es producida gracias a una función del sistema:"+RESET)
  time.sleep(1)
  print("   a) Normal")
  print("   b) Autónomo")
  print("   c) Periférico")
  print("   d) Central")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  
  #Condicionamos la respuesta correcta
  
  while respuesta_1 not in ("a", "b", "c", "d"):
  	respuesta_1 = input(
  	    "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "b":
    puntaje += 10
    print(AZUL+"\nRespuesta correcta ¡Sigue asi", nombre, "!"+RESET)
  else:
    puntaje -= 10
    print(AZUL+"\nRespuesta incorrecta. Seguiremos practicando,", nombre+RESET)
  # Siguiente
  print(ROJO+"\nTienes", puntaje, "puntos"+RESET)
  print("\nContinuemos...")
  
  time.sleep(2)
  
  # Pregunta 2
  print(VERDE+"\n2) Para aglomerar los sólidos en suspensión durante el tratamiento de aguas industriales, se añade un compuesto iónico como el Fe2(SO4)3. Identifique la nomenclatura tradicional de la sustancia que se usa."+RESET)
  print("   a) Sulfato ferroso")
  print("   b) Tetraóxido de hierro")
  print("   c) Sulfato ferrico")
  print("   d) Sulfato hipoferroso")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  
  #Condicionamos la respuesta correcta
  
  while respuesta_2 not in ("a", "b", "c", "d"):
  	respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "c":
    puntaje += 10
    print(AZUL+"\nRespuesta correcta ¡Sigue asi", nombre, "!"+RESET)
  else:
    puntaje -= 10
    print(AZUL+"\nRespuesta incorrecta. Seguiremos practicando,", nombre+RESET)
  
    # Continuemos
  print(ROJO+"\nTienes", puntaje, "puntos"+RESET)
  print("\nContinuemos...")
  
    
  time.sleep(2)
  
  #Pregunta 3
  print(VERDE+"\n3) Considerando que, en el texto escrito, la coma permite poner en evidencia determinadas relaciones entre los constituyentes sintácticos, señale la opción en la que las reglas de uso de este signo se han aplicado correctamente:"+RESET)
  
  print("   a) Sinceramente, Luis, deseo lo mejor para ti.")
  print("   b) Todos los chicos que salieron, no volvieron.")
  print("   c) Han plantado geranios, pero, no los riegan.")
  print("   d) A ellos que se jubilaron, no les han pagado.")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  
  #Condicionamos la respuesta correcta
  
  while respuesta_3 not in ("a", "b", "c", "d"):
  	respuesta_3 = input(
  	    "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    puntaje += 10
    print(AZUL+"\nRespuesta correcta ¡Sigue asi", nombre, "!"+RESET)
  else:
    puntaje -= 10
    print(AZUL+"\nRespuesta incorrecta. Seguiremos practicando,", nombre+RESET)
  
  
  #Continuamos
  print(ROJO+"\nTienes", puntaje, "puntos"+RESET)
  print("\nContinuemos...")
  
  
  time.sleep(2)
  
  # Pregunta 4
  print(VERDE+
      "\n4) En un torneo de tenis organizado por la Municipalidad de Jesús María, 39 personas de la categoríasingles se inscriben para damas senior y todas ellas participarán desde la primera fase. Las fases son eliminatorias y, en cada una de ellas, si el número de tenistas es impar, se elige por sorteo a una que pasa directamente a la siguiente fase. ¿Cuántos partidos se jugarán para determinar a la campeona de la categoría?"+RESET
  )
  print("   a) 39 partidos")
  print("   b) 28 partidos")
  print("   c) 38 partidos")
  print("   d) 33 partidos")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input("\nTu respuesta: ")
  
  #Condicionamos la respuesta correcta
  
  while respuesta_4 not in ("a", "b", "c", "d"):
  	respuesta_4 = input(
  	    "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_4 == "c":
    puntaje += 10
    print(AZUL+"\nRespuesta correcta ¡Sigue asi", nombre, "!"+RESET)
  else:
    puntaje -= 10
    print(AZUL+"\nRespuesta incorrecta. Seguiremos practicando,", nombre+RESET)
  
    
  
  print(ROJO+"\nTienes", puntaje, "puntos"+RESET)
  print("\nContinuemos")
  
  time.sleep(2)
  
  #Pregunta 5
  print(VERDE+"\n5) ¿Cual de estos animales NO pone huevos?"+RESET)
  print("   a) Avestruz")
  print("   b) Jirafa")
  print("   c) Ornitorrinco")
  print("   d) Caimán")
  
  # Respuesta 5
  respuesta_5 = input("\nTu respuesta: ")
  
  while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Acierto o error
  if respuesta_5 == "a":
    puntaje -= 10
    print(AZUL+"Incorrecto!", nombre, "El avestruz es un ave y sí pone huevos"+RESET)
  elif respuesta_5 == "c":
    puntaje -= 10
    print(AZUL+"Incorrecto!", nombre, "El ornitorrinco sí pone huevos"+RESET)
  elif respuesta_5 == "d":
    puntaje -= 10
    print(AZUL+"Incorrecto!", nombre, "El caimán es un reptio y sí pone huevos"+RESET)
  else:
    puntaje += 10
    print("Respuesta correcta", nombre, "!")
  
  
  #Continuemos
  print(ROJO+"\nTienes", puntaje, "puntos"+RESET)
  print("\nAhora la última pregunta!")
  
  time.sleep(2)
  
  # Pregunta 6 (Es pregunta "broma" o capciosa)
  print(ROJO+"\n6) Dime -la respuesta correcta-"+RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_6"
  respuesta_6 = input("\nTu respuesta: ")
  
  #Condicionamos la respuesta correcta
  
  while respuesta_6 not in ("la respuesta correcta", "gfgfgbfvvxv323"):
  	respuesta_6 = input(AZUL+"Sigue intentando, sé que sabes ;) Ingresa nuevamente tu respuesta:"+RESET)
  if respuesta_6 == "la respuesta correcta":
    puntaje += 10
    print(AZUL+"\nRespuesta correcta ¡Estamos listos,", nombre, "!\n"+RESET)	
  
  print(ROJO+"\nTienes", puntaje, "puntos"+RESET)
  
  
  time.sleep(2)
  
  #Mensaje pregunta 7 (análisis personal)
    
  print (VERDE+nombre, ", ahora piensa en ti y en razones para lograr todas tus metas y planes"+RESET)
  #Respuesta 7
  respuesta7 = input (AMARILLO+"\nDime una razón para lograr tus metas:\n"+RESET)
  
  time.sleep(2)
  
  #Despedida
  print(ROJO+"\n¡Qué bien!", nombre, "lograste", puntaje, "puntos. Espero te haya gustado este pequeño test y te sirva para aumentar tu confianza. Continua tu preparación. ¡Suerte!"+RESET)

  #Nuevo intento 
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o presiona enter para finalizar: ").lower()
  
  if repetir_trivia != "si": 
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  