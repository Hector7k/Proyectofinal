import random 
import os
from getpass import getpass
#funcion para limpiar la terminal y que no se mescle todo
def limpiar_terminal():
  os.system("cls")

#Funcion que almacena los datos del menu de juego
def menu_juego():
      print("-------Lista-------")
      print("|🪨|Piedra"        )
      print("|📄|Papel "        )
      print("|✂️|Tijera"        )
      print("|<<| Volver")
      print("-------Salir-------") 
while True:
#Menu de modo de juego
    print("Hola Bienvanido selecciona el modo de juego")
    print("1 ) Jugar contra la computadora")
    print("2 ) Modo multijugador")
    print("3 ) Salir") 
    #Eleccion del jugador 
    modo_juego = input("Introduce el modo de juego que deseas: ")
    limpiar_terminal()
    if modo_juego not in ("1", "2", "3"):
      print("Opcion incorrecta introduce la Opcion 1, 2, 3")
      continue

    if modo_juego == "3":
        
      print("Gracias por jugar")
      exit()
#Modo de juego 1) Contra la computadora
    elif modo_juego == "1":
     nombre = input("Hola intruduce un usuario para empezar a jugar: ")
#Almacenamiento de victorias y empates
     Comp_puntos = 0
     Juga_puntos = 0
     modo1_empate = 0
     while True:
    #Se usa un fString para incluir dentro del print una variable que en este caso use la variable
    #que almacena un nombre 
      print(f"Bienvenido al juego \nPiedra🪨 Papel📄 O Tijera✂️  {nombre}")
      menu_juego()
      opciones = ['piedra', 'papel', 'tijera']
      Jugador = input(f"Hora de juga {nombre} selecciona tu jugada: ").lower()
      limpiar_terminal()
      #La computadora selecciona su jugada
      computadora = random.choice(opciones)
      #Se realiza la validacion de la seleccion del jugador 
      if Jugador == "salir":#si se cumple la condicion y cierra el juego
        print("Saliendo gracias por jugar :D")
        exit()
      if Jugador == "volver":#si cumple la condicion vuelve al menu principal
        limpiar_terminal()
        print("Volviendo al menu principal")
        break
      if Jugador not in ("piedra", "papel", "tijera",):#si cumple la condicion imprime opcion no valida y pide la opcion de nuevo
        limpiar_terminal()
        print("opcion no valida vuelve a ingresar")
        continue

      elif Jugador == computadora:#si cumple la funcion imprime "Empate"
        print(f"la computadora elijio {computadora} y el Jugador {Jugador}")
        print("Empate")
        modo1_empate += 1

      elif (computadora == "tijera" and Jugador == "papel") or \
           (computadora == "piedra" and Jugador == "tijera") or \
           (computadora == "papel" and Jugador == "piedra"):#Si cumple la funcion imprime "Gana computadora"
        print(f"la computadora selecciono {computadora} y el Jugador {Jugador}")
        print("Gana Computadora")
        Comp_puntos += 1

      else:#Si cumple la funcion imprime gana el jugador 
        print(f"la computadora selecciono {computadora} y el Jugador {Jugador}")
        print("Gana jugador")
        Juga_puntos += 1
      #Imprime las estadisticas actualizadas con la ultima victoria
      print(f"La computadora tiene {Comp_puntos} Victorias")
      print(f"El jugador tiene {Juga_puntos} Victorias")
      print(f"y existen {modo1_empate} empates")
      #se crea un bucle para la seleccion si desea seguir jugando o no
      while True:
         volver = input("¿Quieres volver a jugar? (si/no): ").lower()
         if volver == "si":
          print(f"Vamos a jugar de nuevo {nombre} \n ")
          limpiar_terminal()
          break  # sale de este while y vuelve al juego         
         elif volver == "no":
          print(f"Gracias por jugar {nombre}")
          if Juga_puntos == Comp_puntos: #Al culminar el juego imprime si quedaron empate
            print("Quedaron Empate")
            exit()
          
          if Comp_puntos > Juga_puntos: #Al culminar el juego imprime si gano la computadora
            print(f"Perdon {nombre} la computadora te gano esta vez con {Comp_puntos} VICTORIAS")
            exit()
          
          elif Juga_puntos > Comp_puntos:
            print(F"FELICIDADES {nombre} superaste a la computadora ganaste {Juga_puntos} partidas en total")
            exit()
           # termina todo el programa
          else:
           print("Opción no válida")

#Modo Multijugador
    elif modo_juego == "2":
      #Imprime la bienvenida al modo de juego 2 
      print("Bienvenidos al modo Multijugador")
      print("Intruduscan sus nombres:")
      nombre1 = input("Jugador 1: ")
      nombre2 = input("Jugador 2: ")
      #Almacena las victorias y empates del modo multijugador
      Pm_jugador1 = 0
      Pm_jugador2 = 0
      Pm_empate = 0
      while True:
        print(f"Bienvenidos al juego \nPiedra🪨 Papel📄 O Tijera✂️  {nombre1} y {nombre2}")
        menu_juego() #ejecuta la funcion que imprime el menu de juego
        Jugador1 = getpass(f"{nombre1} selecciona tu jugada: ").lower() #Ingreso de jugada getpass(No permite ver lo escrito)
        if Jugador1 == "salir":#Termina el juego
          print("Gracias por jugar")
          exit()
        if Jugador1 == "volver":#vuelve al menu principal
          print("Volviendo al menu principal")
          limpiar_terminal()#limpia la terminal
          break
        if Jugador1 not in ("piedra", "papel", "tijera",):#devuelve un error si la opcion no es correcta
          print(f"{nombre1} Tu opcion no es valida intenta de nuevo")
          continue
        Jugador2 = getpass(f"{nombre2} selecciona tu jugada: ").lower()#Ingreso de jugada getpass(No permite ver lo escrito)

        if Jugador2 == "salir":#Termina el juego
          print(F"Gracias por jugar")
          exit()

        if Jugador2 == "volver":#vuelve al menu principal
          print("Volviendo al menu principal")
          limpiar_terminal()#limpia la terminal
          break

        if Jugador2 not in ("piedra", "papel", "tijera",):#devuelve un error si la opcion no es correcta
          print(f"{nombre2} Tu opcion no es valida intenta de nuevo")
          continue
        #Define si las jugadas son iguales y imprime que fue un empate
        if Jugador1 == Jugador2:
          print(f"{nombre1} selecciono {Jugador1} y {nombre2} selecciono {Jugador2} ")
          limpiar_terminal()
          print("Empate")
          Pm_empate += 1
        #define con que jugadas gana el jugador 1 
        elif (Jugador1 == "papel" and Jugador2 == "piedra") or \
            (Jugador1 == "tijera" and Jugador2 == "papel") or \
            (Jugador1 == "piedra" and Jugador2 == "tijera"):
          print(f"{nombre1} selecciono {Jugador1} y {nombre2} selecciono {Jugador2} ")
          Pm_jugador1 += 1
          print(f"Gana {nombre1}")
        #Define que si ninguna de las anteriores es correcta imrpime que gano el jugador 
        else:
          print(f"{nombre1} selecciono {Jugador1} y {nombre2} selecciono {Jugador2} ")
          Pm_jugador2 += 1
          print(f"Gana {nombre2}")
        #Imprime las estadisticas de el juego 
        print("-------Estadisticas-------")
        print(f"{nombre1} Tiene {Pm_jugador1} partidas ganadas")
        print(f"{nombre2} Tiene {Pm_jugador2} partidas ganadas")
        print(f"y existen {Pm_empate} Empates")
        print("--------------------")
        #crea un bucle para la seleccion de fin de juego 
        while True:
            volver_multi = input("Quieres volver a jugar si/no: ").lower()
            if volver_multi == "si":#regresa al menu de juego
              limpiar_terminal()
              print("vamos a jugar de nuevo")
              break#sale del bucle
            elif volver_multi == "no": #sale del juego y imrpime los resultados de la ultima partida
                print("Gracias por")
                if Pm_jugador1 > Pm_jugador2:
                  print(f"Felicitaciones {nombre1} ganaste {Pm_jugador1} partidas {Pm_jugador1 - Pm_jugador2} mas que {nombre2}")
                  exit() 
                elif Pm_jugador1 < Pm_jugador2:
                    print(F"Felicitaciones {nombre2} ganaste {Pm_jugador2} partidas {Pm_jugador1 - Pm_jugador2} mas que {nombre1}")
                    exit()
                else:# si no selecciona una opcion valida imprime "opcion no valida" y pide la eleccion de nuevo
                  print("opcion no valida")
                  continue
            

      



