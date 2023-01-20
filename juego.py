"""
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores
Lenguaje: Python 3.9.9
Autores: Oscar Arturo Acuña Durán(2022049304)
Version: 4.1
Fecha de última modificación: Mayo 05/07/2022

"""
# Tengo que hacer un plan de como hacer el juego antes de comenzar a programarlo

# Redactarlo en la tablet
import tkinter as tk

#Esto se importa para poder engañar a la recursividad y hacer una recursividad infinita
from threading import Thread
import time
import func_especiales
#Lo sigiuente se importa para poder usar .png como botones
from PIL import ImageTk
import random 

import keyboard #Este modulo se tiene que instalar 
# En el pdf de la documentacion se explica por que se intalo esto

import pygame



def Juego(window, Inicio, jugador, dificulty):
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Lenguaje: Python 3.9.9
    Profesor: Ing Milton Villegas Lemus
    Autor: Oscar Arturo Acuña Duran (2022049304)
    Version: 4.1
    Fecha de última modificación: Mayo 05/07/2022
    Entradas: Las entradas son 
    window: Definicion de la ventana
    Inicio: Creacion del lienzo 
    jugador: String con el nombre del juador
    dificulty: Nivel de dificultad
    Restricciones: jugador tiene que ser un string con una longitud mayor a 0 y menor que 10 
    dificulty tiene que ser un string y entre sus opciones solo esta Easy, Medium y Hard
    Salidas: Ejecuta el juego en el lienzo que se definio en main 
    """
    
    global MovingX #Cantidad de sprites que se mueve el carro del jugador en el eje x
    MovingX = 0
    global EnemyVelocity # Tiempo en el que se ejecuta la funcion que anima al enemigo 
    EnemyVelocity = 0.008
    global SpritesMoving # Cantidad de sprites que se esta moviendo el enemigo en el eje y en cada intervalo de tiempo 
    SpritesMoving = 4
    global HaveCollided # Esta variable revisa si ya paso una colison
    HaveCollided = False
    global TimePlayed #Esta variable cuenta el tiempo jugado en segundos
    TimePlayed = 0
    global CarRide #Esta variable muestra la marcha del carro en ese momento 
    CarRide = 1
    global Lives #Esta variable define la cantidad de vidas que le quedan al jugador 
    global IsRunning #Esta variable define si el juego se tiene que seguir ejecutando 
    IsRunning = True 
    global HaveLost #Esta variable define si el jugador ya perdio 
    HaveLost = False
    global DfTime  #Definicion del tiempo que se tiene para cambiar de marcha
    global CarsPassed  # Se crea una variable para contar la cantidad de carros que se les ha sobrepasado 
    CarsPassed = 0
    global HowManyExist #Cuantos enemigos hay en la pantalla en este momento 
    HowManyExist = 0
    global ListCars #Esta lista dice cual enemigo es el que existe
    ListCars = [False,False,False]
    global CoordsBlue #Se definen las coordenadas iniciales del enemigo azul 
    CoordsBlue = [390, -150]
    global CoordsGreen #Se definen las coordenadas iniciales del enemigo verde
    CoordsGreen = [220, -150]
    global CoordsRedEnemy #Se definen las coordenadas iniciales del enemigo rojo 
    CoordsRedEnemy = [560, -150]
    global KmTravelled  #quiero hacer el contador de Kilometros recorridos
    KmTravelled = 0
    global IfAccelerating #Esto establece si el carro esta acelerando en ese momento 
    IfAccelerating = False
    global ChangingCarRide #Esto lo que establece es si el usuario ejecuto el cambio de marcha 
    ChangingCarRide = False
    global AllowingAccelerating #Esto lo que establece es si el carro tiene el permiso de acelerar en ese momento 
    AllowingAccelerating = True 
    global Stopping  #Esto lo que establece es si el carro esta frenando en ese momento 
    Stopping = False
    global CarAccelerating #Establece si el carro esta activamenet acelerando 
    CarAccelerating = False
    #Se van a programar ciertos parametros que tienen que ver con la dificultad del juego
     
    if dificulty == "Easy":# En este caso si se juega en facil son 3 vidas y se tienen 3 segundos para cambiar de marcha
        DfTime = 3
        Lives = 3
    elif dificulty == "Medium":# En este caso si se juega en medio son 2 vidas y se tienen dos segundos para cambiar de marcha
        DfTime = 2
        Lives = 2
    elif dificulty == "Hard": # En este caso si se juega en dificil es 1 vidas y se tiene un segundo para cambiar de marcha
        DfTime = 1
        Lives = 1
   
    
    

    
    pygame.mixer.init() #Se inicia el mixer para poder correr la musica
    #pygame.mixer.music.load("Aceleracion.mp3")
    #pygame.mixer.music.play(-1)
    
    
    #Definir el menu de abajo aqui arriba 
    #Primero se cargan los sprites 
    MenuBackground = func_especiales.cargarSprites("juego/Menu/CuttedSprites/PossibleSprites*") #Se crea la imagen de la animacion que 
    #Aparece atras del volante en la pantalla
    MBackground = Inicio.create_image(0,725, anchor = "nw") #se le da un label 

    Inicio.create_rectangle(880,0,1176,966, fill = "#007890", outline = 'black') #Se crea un rectangulo al lado en donde aparecen los labels 
    
    #Se crea un label que despliega el nombre del jugador
    LabNombArch = tk.Label(Inicio, text = "Nombre del Jugador: " + jugador, font = ("Arial", 15), background = "#007890")
    LabNombArch.place(x = 890, y = 160, anchor = "nw")
    
    #Se coloca la acera de la izquierda     
    AceraIzq = ImageTk.PhotoImage(file = "Imagenes/juego/ladoizq.png")
    Inicio.create_image(0,0, image = AceraIzq, anchor = "nw")
    
    #Se coloca la Acera de la derecha
    AceraDer = ImageTk.PhotoImage(file = "Imagenes/juego/ladoder.png")
    Inicio.create_image(735,0, image = AceraDer, anchor = "nw")
    
    #Se coloca el carro 
    MenuCar = ImageTk.PhotoImage(file = "Imagenes/juego/FinalCars/FinalDisplayCar.png")
    Inicio.create_image(0, 816, image = MenuCar, anchor = "nw")
    
    #Se van a poner las luces verdes y rojas que se tienen que poner, van a ser globales para poder editarlas dentro del codigo
    global GreenLight
    
    GreenLight = ImageTk.PhotoImage(file = "Imagenes/juego/Lights/LuzVerdeApagada.png")
    
    
    global DarkGreenLight
    DarkGreenLight = ImageTk.PhotoImage(file = "Imagenes/juego/Lights/LuzVerdeEncendida.png")
    
    
    #Ahora se les da la posicion 
    FirstGreen = Inicio.create_image(490, 896, image = GreenLight, anchor = "nw")
    SecondGreen = Inicio.create_image(510, 906, image = GreenLight, anchor = "nw")
    ThirdGreen = Inicio.create_image(530, 916, image = GreenLight, anchor = "nw")
    FourthGreen = Inicio.create_image(550, 926, image = GreenLight, anchor = "nw")
    
    
    global RedLight 
    RedLight = ImageTk.PhotoImage(file = "Imagenes/juego/Lights/LuzRojaApagada.png")
    
    global DarkRedLight 
    DarkRedLight = ImageTk.PhotoImage(file = "Imagenes/juego/Lights/LuzRojaPrendida.png")
    
    ThirdRed = Inicio.create_image(380, 896, image = RedLight, anchor = "nw")
    SecondRed = Inicio.create_image(355, 906, image = RedLight, anchor = "nw")
    FirstRed = Inicio.create_image(330, 916, image = RedLight, anchor = "nw")
    
    
    #Frames de la animacion de la victoria
    Victory_Frames = func_especiales.cargarSprites("juego/YouWin/VictorySprites*")
    VictoryImage = Inicio.create_image(260, 363, anchor ="nw")
    
    
    #Se va a cargar la animacion de la calle y de la acera que se tiene
    background_frames = func_especiales.cargarSprites("juego/street*")
    BF = Inicio.create_image(147,0, anchor = "nw")
    
    #Se crea el cactus y se le da un lugar en la pantalla
    #El cactus es el equivalente al arbusto que se solicita en la especificacion 
    ReferenceCactus = ImageTk.PhotoImage(file = "Imagenes/juego/Cactus/CactusSprite.png")
    RCactus = Inicio.create_image(770, 50, image = ReferenceCactus, anchor = "nw")
    
    #Se van a cargar los sprites del carro rojo
    RedCar_frames = func_especiales.cargarSprites("juego/FinalCars/RedCar*")
    RedCar = Inicio.create_image(390,490, anchor = "nw")
    
    #Se van a cargar los sprites de la explosion
    Explosion_frames = func_especiales.cargarSprites("juego/Explosion/BUM*")
    
    
    
    
    # Se uso https://www.imgonline.com.ua/eng/replace-color.php para cambiar el color de los sprites 
    #Citar https://www.remove.bg/
    
    #Se va a cargar el carro Azul 
    BlueCarCenter_Frames = ImageTk.PhotoImage(file = "Imagenes/juego/Formula1/CarroAzul.png")
    BlueCarCenter = Inicio.create_image(390,-150,image = BlueCarCenter_Frames, anchor = "nw")
    
    GreenCarLeft_Frames = ImageTk.PhotoImage(file = "Imagenes/juego/Formula1/CarroVerde.png")
    GreenCarLeft = Inicio.create_image(220, -150, image = GreenCarLeft_Frames, anchor = "nw")
    
    RedCarRight_Frames = ImageTk.PhotoImage(file = "Imagenes/juego/Formula1/CarroEnemigoRojo.png")
    RedCarRight = Inicio.create_image(560, -150, image = RedCarRight_Frames, anchor = "nw")
    
    
    def BackToMov():
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Oscar Arturo Acuña Duran (2022049304)
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: No posee
        Restricciones: No posee
        Salidas: No posee
        """
        global Lives, SpritesMoving, Stopping, AllowingAccelerating, ChangingCarRide, IfAccelerating, ListCars, HowManyExist, HaveCollided
        global HaveLost
        #Se imortan las variables globales 
        
        if Lives > 0:
            Lives = Lives - 1 #Se le quita una vida al personaje 
            #Se reestablecen las coordenadas de los enemigos 
            Inicio.coords(BlueCarCenter, 390, -150) 
            Inicio.coords(GreenCarLeft, 220, -150)
            Inicio.coords(RedCarRight, 560, -150)
            #Recordar quitar puntos del puntaje (10 % tal ves)
            
            #Se redefine el valor de ciertas variables para evitar bugs 
            IfAccelerating = False
            ChangingCarRide = False
            HaveCollided = False
            AllowingAccelerating = True
            Stopping = False
            
            #El carro vuelve al centro
            Inicio.coords(RedCar, 390, 490)
            
            #Se vuelven a poner todas las luces verdes en apagado
            Inicio.itemconfig(FirstGreen, image = GreenLight)
            Inicio.itemconfig(SecondGreen, image = GreenLight)
            Inicio.itemconfig(ThirdGreen, image = GreenLight)
            Inicio.itemconfig(FourthGreen, image = GreenLight)
            
            
            
            #Vuelve a la velocidad minima 
            SpritesMoving = 4

        if Lives == 0 and HaveLost == False: #Perdio el jugador 
            window.update()
            HaveLost = True
            time.sleep(3)
            window.destroy() #Se cierra la ventana del juego en estos casos

    
    
    
    def EnemySpawner():
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Oscar Arturo Acuña Duran (2022049304)
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: No posee
        Restricciones: No posee
        Salidas: No posee
        Descripcion: Esta funcion randomiza y ejecuta la aparicion de enemigos den la pantalla 
        Se encarga que los enemigos aparezcan bajo las condiciones que se establecieron en la especificacion del proyecto
        """
        #Esta leyendo en el momento en el cual el valor se hace negativo entonces no encuentra nada en la lista
        global HowManyExist, ListCars, HaveLost 
        TempList = [0,1,2] #Esta lista se usa para ver cual es el carro que se va a colocar 
        if HowManyExist == 0:
            NoCarsTime = random.randint(0,2) 
            #https://pynative.com/python-random-randrange/
            time.sleep(NoCarsTime) #Se hace random la cantidad de tiempo que tomara en que aparezca el carro
            #https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
            WhichCar = random.choice(TempList) #Se escoge un carro 
            if WhichCar == 0:
                Thread(target = MovingGreen, args = ()).start() #Esta Thread hace que el carro verde aparezca 
                HowManyExist = HowManyExist + 1 # Se tiene que establecer que existe ahora un carro
            elif WhichCar == 1:
                Thread(target = MovingBlue, args = ()).start() #Este Thread hace que el carro azul aparezca
                HowManyExist = HowManyExist + 1 # Se tiene que establecer que existe ahora un carro 
            elif WhichCar == 2:
                Thread(target = MovingRed, args = ()).start() #Este Thread hace que el carro rojo enemigo aparezca
                HowManyExist = HowManyExist + 1 #Se tiene que establecer que ahora existe un carro 
        
 
        elif HowManyExist == 1: #Si existe solo un carro (Por que no se permite que aparezcan mas de dos)
            if True in ListCars: #Se quiere ver cual es el que existe 
                WhatCar = ListCars.index(True) #Se ve cual es la posicion en whatcar en la que esta el carro 
                if WhatCar == 0: #Si el que existe el el de la izquierda 
                    if CoordsGreen[1] <= 240: # Esto se hace para uqe no aparezcan a la par en el eje y
                        time.sleep(0.1) 
                    else:
                        Choice = random.choice([True, False, False, False, False, False]) #Se ve si se va a hacer otro o no 
                        if Choice == True: # Si si se quiere hacer otro 
                            SecondCar = random.choice([1,2]) #Se randomiza cual sera (Fijese que se hace de esta manera para que
                            # No aparezca en el mismo carril 
                            if SecondCar == 1: # Si es el uno 
                                Thread(target = MovingBlue, args = ()).start() #Se ejecuta este Thread y el carro aparece 
                                HowManyExist = HowManyExist + 1 #Se tiene que Establecer que aparecio otro carro para que no aparezcan mas 
                            else:
                                Thread(target = MovingRed, args = ()).start() # Se ejecuta el otro carro 
                                HowManyExist = HowManyExist + 1 #Se tiene que establecer que aparecio otro carro para que no aparezcan mas 
                elif WhatCar == 1: #Si el carro que estaba era el del centro 
                    if CoordsBlue[1] <= 240: #Esto es para que no aparezcan a la par en el eje y 
                        time.sleep(0.1)
                    else:
                        Choice = random.choice([True, False, False, False, False]) #Se escoge a ver cual va a aparecer 
                        if Choice == True: 
                            SecondCar = random.choice([0,2]) #Se toma la desicion random 
                            if SecondCar == 0:
                                Thread(target = MovingGreen, args = ()).start() #Se ejecuta el otro carro 
                                HowManyExist = HowManyExist + 1 #Hay que establecer que aparecio otro carro 
                            else:
                                Thread(target = MovingRed, args = ()).start() #Se ejecuta el otro carro 
                                HowManyExist = HowManyExist + 1 #Hay que establecer que aparecio otro carro 
                            
                elif WhatCar == 2: #Si el carro que estaba era el de la derecha 
                    if CoordsRedEnemy[1] <= 240: #Esto para que el segundo carro no aparezca igual en el eje y
                        time.sleep(0.1)
                    else: # Se ejecuta otro carro 
                        Choice = random.choice([True, False, False, False]) #Se toma la desicion de si se va a ejecutar 
                        if Choice == True:
                            SecondCar = random.choice([0,1]) #Se escoje entre las opciones que hay 
                            if SecondCar == 0:
                                Thread(target = MovingGreen, args = ()).start() #Se ejecuta el otro carro 
                                HowManyExist = HowManyExist + 1 #Se establece que hay un nuevo carro 
                            else:
                                Thread(target = MovingBlue, args = ()).start() #Se ejecuta otro carro 
                                HowManyExist = HowManyExist + 1 #Se establece que hay otro carro 
        if HaveLost == False: #se hace la llamada recursiva si no se ha perdido         
            Thread(target = EnemySpawner, args = ()).start() 
    Thread(target = EnemySpawner, args = ()).start()  #Estos threads permiten tener una recursividad invinita 
    

    def MovingRedCar():
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Oscar Arturo Acuña Duran (2022049304)
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: No Posee
        Restricciones: No posee
        Salidas: No posee
        Descripcion: Esta funcionse encarga de ejecutar el movimiento del carro en el eje x
        Ademas de eso en esta funcion se programa lo que ocurre cuando se cambia de marcha
        y cuando se colisiona. 
        """
        global MovingX, EnemyVelocity, CoordsBlue, CoordsGreen, CoordsRedEnemy, SpritesMoving, HaveCollided, IsRunning, HaveLost
            
        if IsRunning and HaveCollided == False and HaveLost == False:  #Si esos parametros se cumplen entonces se puede ejecutar la funcion
            CoordsCar = Inicio.coords(RedCar) #Se establece una variable local para las coordenadas del programa 
            Inicio.coords(RedCar, CoordsCar[0] - MovingX, CoordsCar[1]) #Se mueven las coordenadas en el eje x
            
            if keyboard.is_pressed("a") and CoordsCar[0] != 220 and SpritesMoving != 0: #Si se estripa la tecla a y las condiciones se cumplen 
            #El movimiento en el eje x sera de 10 pixeles 
                if SpritesMoving != 0:
                    MovingX = 10
            if keyboard.is_pressed("d") and CoordsCar[0] != 560 and SpritesMoving != 0: #Si se estripa la tecla d y las condiciones se cumplen
            #El movimiento en el eje x sera de -10 pixeles
                if SpritesMoving != 0:
                    MovingX = -10
    
            if ((CoordsCar[0]) - MovingX) == 220: #Se establece condicion de finalizacion para cuando llega al carril de la izquierda 
                MovingX = 0
            elif ((CoordsCar[0]) - MovingX) == 560: #Se establece condicion de finalizacion para cuando llega al carril de la derecha 
                MovingX = 0
            elif ((CoordsCar[0]) - MovingX) == 390: #Se establece condicion de finalizacion para cuando llega al carril del centro 
                MovingX = 0
                
            #Aqui es en donde se va a definir el choque 
            if abs(CoordsGreen[0] - CoordsCar[0]) <= 20 and abs(CoordsGreen[1] - CoordsCar[1]) <= 120: #Si esto ocurre entonces choco 
                SpritesMoving = 0
                HaveCollided = True
            elif abs(CoordsRedEnemy[0] - CoordsCar[0]) <= 20 and abs(CoordsRedEnemy[1] - CoordsCar[1]) <= 120: #Si esto ocurre entonces choco
                SpritesMoving = 0
                HaveCollided = True
            elif abs(CoordsBlue[0] - CoordsCar[0]) <= 20 and abs(CoordsBlue[1] - CoordsCar[1]) <= 120: #Si esto ocurre entonces choco
                SpritesMoving = 0
                HaveCollided = True
            
        if HaveCollided == True: #Esto se ejecutara solo si el carro ha chocado 
            Thread(target = BackToMov, args = ()).start()
        def RecursiveCall(): #Se hace la llamada recusiva de esta funcion 
            MovingRedCar()
        window.after(5, RecursiveCall)
    Thread(target = MovingRedCar, args = ()).start() #Se llama a la funcion MovingRedCar en otro hilo

    
    def MovingVictory(i):
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Marcelo Truque Montero
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: Un numero entero mayor o igual a 0 que indica cual sprite se esta llamando
        Restricciones: i es entero y es mayor o igual a 0
        Salidas: Carga y coloca la animacion de la funcion

        """
        if (i >= len(Victory_Frames) - 1): #Si i esta afuera del rango permitido pasa a ser 0 de nuevo 
            i = 0
         
        if IsRunning: 
            Inicio.itemconfig(VictoryImage, image = Victory_Frames[i]) #Anima la victoria 
        def RecursiveCall(): #Funcion que llama a la recursividad 
            MovingVictory(i + 1)
        window.after(100, RecursiveCall) #Se espera antes de volver a llamar a la funcion 
    
    


     
    def MovingAnimations(i, k, w):
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Oscar Arturo Acuña Duran (2022049304)
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: i, k, w
        Restricciones: i, k y w tienen que ser numeros enteros positivos y tienen que ser menores a la longitud de background_frames
        RedCar_frames y de MenuBackground respectivamente
        Salidas: Crea la animacion del background, del menu background y del background del menu que aparece en parte inferior de la pantalla
        """
        global HaveCollided, SpritesMoving, IsRunning, HaveLost 

        if (i >= len(background_frames) - 1): #Se revisa si el indice esta en el rango adecuado 
            i = 0
        else:
            i = i + 1
        if (k >= len(RedCar_frames) - 1):#Se revisa si el indice esta en el rango adecuado 
            k = 0
        else:
            k = k + 1
        if (w >= len(MenuBackground) - 1):#Se revisa si el indice esta en el rango adecuado 
            w = 0
            
        if IsRunning and HaveLost == False:
            Inicio.itemconfig(BF, image = background_frames[i]) #Se cambia el frame de BF
            Inicio.itemconfig(RedCar, image = RedCar_frames[k]) #Se cambia el frame de RedCar
            Inicio.itemconfig(MBackground, image = MenuBackground[i]) #Se cambia el frame de MBackground 
        def RecursiveCall(): #Se define la funcion qeu hace la llamada recursiva 
            MovingAnimations(i + 1, k + 1, w + 1) #Se hace la llamada recursiva
        window.after(100, RecursiveCall) #Se establece cuanto tiempo se va a esperar
    Thread(target = MovingAnimations, args = (0, 0, 0,)).start() #Se llama la funcion en otro hilo 

    
    def flech_pressed(event):
        global HaveCollided
        global ChangingCarRide

        if keyboard.is_pressed(" ") and HaveCollided == False: #se detecta si se estripo el espacio 
            ChangingCarRide = True # Si este se estripo entoces se ejecuta la funcion qeu indica que se esta cambiando de marcha 
        
    window.bind("<Key>", flech_pressed)
    
    

    def TurningRedLights(Which): #Esta funcion decide cual luz roja es la que se va a prender en ese momento 
        if Which == "Second": #Si se selecciona la segunda 
            Inicio.itemconfig(SecondRed, image = DarkRedLight) #Se prende 
            time.sleep(2) #Se espera dos segundos 
            Inicio.itemconfig(SecondRed, image = RedLight) #Se apaga
            
        elif Which == "Third": #Si se selecciona la tercera 
            Inicio.itemconfig(ThirdRed, image = DarkRedLight) #Se prende 
            time.sleep(2) #Se espera dos segundos  
            Inicio.itemconfig(ThirdRed, image = RedLight) #Se apaga 

    def PseudoFunction():
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Oscar Arturo Acuña Duran (2022049304)
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: No Posee
        Restricciones: No posee
        Salidas: No posee
        Descripcion: Esta funcion se encarga de todo lo que tiene que ver con las marchas, ella le solicita al usuario que cambie de marcha
        Ella para el juego si el usuario cambia de marcha muy tarde
        Ademas la funcion se encarga de prender las luces verdes y rojas que se redactan en la especificacion
        """
        global SpritesMoving, CarRide, ChangingCarRide, IfAccelerating, AllowingAccelerating, Stopping, HaveCollided, IsRunning, DfTime, HaveLost
        global GreenLight, DarkGreenLight

        # https://www.codegrepper.com/code-examples/python/python+read+all+keypress

        
        if ChangingCarRide and AllowingAccelerating: #Esto es lo que se ejecuta cuando se estripa espacio antes de tiempo 
            if CarRide == 1:
                SpritesMoving = 5
            elif CarRide == 2:
                SpritesMoving = 7
            elif CarRide == 3:
                SpritesMoving = 19
            elif CarRide == 4:
                SpritesMoving = 29
            
            
            #Quitarle velocidad al carro 
        
        if keyboard.is_pressed(" ") and SpritesMoving != 0: # Esto detecta si se estripo el espacio 
            ChangingCarRide = True #Se establece que se esta haciendo el cambio de marcha 
            
            
        if Stopping and SpritesMoving != 4: #Esta funcion ejecuta el frenado 
                if SpritesMoving != 4:
                    Stopping = False
                    SpritesMoving = SpritesMoving - 1 #Le quita un sprite a la cantidad de sprites a la que se estan moviendo los enemigos 
                    time.sleep(1/30) #Se espera esta cantidad de tiempo para seguir 
                if SpritesMoving == 4: #Si llega a cuatro tiene que parar 
                    Stopping = False # El carro  no puede ir a una velocidad menor a la minima 
                    Thread(target = TurningRedLights, args = ("Third",)).start() #Se cambia el color de la luz roja 
                if SpritesMoving < 4: #Se hace esto para evitar un bug
                    SpritesMoving = 4
        
        if 6 > SpritesMoving >= 4 and AllowingAccelerating: #En ese intervalo el carro esta en la primera marcha 
            CarRide = 1
        elif 18 > SpritesMoving >= 6 and AllowingAccelerating: #En ese intervalo el carro esta en la segunda marcha 
            CarRide = 2 
        elif 28 > SpritesMoving >= 18 and AllowingAccelerating: #En ese intervalo el carro esta en la tercera marcha 
            CarRide = 3
        elif 32 > SpritesMoving >= 28 and AllowingAccelerating: #En ese intervalo el carro esta en la cuarta marcha 
            CarRide = 4

        
        #Se van a definir las condiciones en las cuales el usuario debe de cambiar de Marcha
        if (SpritesMoving == 6 or SpritesMoving == 18 or SpritesMoving == 28) and not(keyboard.is_pressed("s")):
            AllowingAccelerating = False
            #Ahora suena la alarma 
            pygame.mixer.music.load("Alarma.mp3")
            pygame.mixer.music.play() #Esta alarma le debe de indicar al jugador que debe de cambiar de marcha 
            if ChangingCarRide == False: #Si no se ha cambiado de marcha 
                time.sleep(0.5*DfTime) #Se espera el 50% del tiempo 
                Inicio.itemconfig(ThirdGreen, image = DarkGreenLight) #Se prende la luz verde
            if ChangingCarRide == False: #Si no se ha cambiado de marcha 
                time.sleep(0.3*DfTime)
                Inicio.itemconfig(ThirdGreen, image = GreenLight) #Se apaga la luz verde
                Inicio.itemconfig(SecondGreen, image = DarkGreenLight) #Se prende la luz verde 
            if ChangingCarRide == False: #Si no se ha cambiado de marcha 
                time.sleep(0.2*DfTime) #Se espera hasta el 80% del tiempo 
                Inicio.itemconfig(SecondGreen, image = GreenLight) #Se apaga la luz verde
                Inicio.itemconfig(FirstGreen, image = DarkGreenLight) # Se prende la luz verde 
                time.sleep(0.2*DfTime) #Lo que se espera segun la especificacion  
            if ChangingCarRide == False: #Si no se ha cambiado de marcha 
                Inicio.itemconfig(FirstGreen, image = DarkGreenLight) #Se prende la luz verde
            if ChangingCarRide == True: #Si ya cambio de marcha 
                Inicio.itemconfig(FirstGreen, image = GreenLight) #Se apagan las luces verdes
                Inicio.itemconfig(SecondGreen, image = GreenLight)
                Inicio.itemconfig(ThirdGreen, image = GreenLight)
                AllowingAccelerating = True #Vuelve a dejaar al usuario acelerar
                ChangingCarRide = False #Le dije al juego que ya no se esta cambiando de marcha 
                #Tengo que moverme a la siguiente aceleracion
                if CarRide == 1: #Establece a cual marcha va a cambiar despues de la ejecucion 
                    CarRide = 2
                elif CarRide == 2:
                    CarRide = 3
                elif CarRide == 3:
                    CarRide = 4
                
            elif ChangingCarRide == False: #Si no cambio de marcha
                #SpritesMoving = 0 
                AllowingAccelerating = False
                Thread(target = BackToMov, args = ()).start() #Se ejecuta BackToMov y se le quita una vida al carro 
        if HaveLost == False: #Si no ha perdido esto se sigue ejecutando 
            Thread(target = PseudoFunction, args = ()).start()
    Thread(target = PseudoFunction, args = ()).start()   

  

    def ExcAcceleration():
        """
        Instituto Tecnológico de Costa Rica
        Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Profesor: Ing Milton Villegas Lemus
        Autor: Oscar Arturo Acuña Duran (2022049304)
        Version: 4.1
        Fecha de última modificación: Mayo 05/07/2022
        Entradas: No Posee
        Restricciones: No posee
        Salidas: No posee
        Descripcion: Esta funcion ejecuta la aceleracion y el frenado del carro 
        """
        global AllowingAccelerating, IfAccelerating, SpritesMoving, CarRide, Stopping, HaveLost 

        if keyboard.is_pressed('w') and AllowingAccelerating and HaveLost == False: #Si se presiona w, se puede acelerar y no ha perdido 
            IfAccelerating = True #Esta acelerando 
            Inicio.itemconfig(FourthGreen, image = DarkGreenLight)  #Se prende la luz verde
        else: #En otro caso 
            Inicio.itemconfig(FourthGreen, image = GreenLight) #Se apaga la luz verde 
      
            
        
        if keyboard.is_pressed('s') and HaveLost == False: #Si se estripa la desaceleracion y no ha perdido
            if SpritesMoving != 4:
                Stopping = True #Se establece que esta frenando 
                
            if SpritesMoving <= 4: #Si llegara a ser menor o igual que cuatro 
                Stopping = False #ya no esta frenando 
            
        if Stopping and HaveLost == False: #Si esta parando 
            Inicio.itemconfig(FirstRed, image = DarkRedLight) #Prender la luz verde
        elif HaveLost == False: #Si perdio 
            Inicio.itemconfig(FirstRed, image = RedLight) #Apagar la luz 
        
        if IfAccelerating and HaveLost == False: #Si esta acelerando y no ha perdido
            if CarRide == 1: #Si esta en la primera marcha 
                IfAccelerating = False
                SpritesMoving = SpritesMoving + 1 #Aumenta los sprites
                time.sleep(2.5/5) #Segun la especificacion del proyecto 
            if CarRide == 2: #Si esta en la segunda marcha 
                IfAccelerating = False 
                SpritesMoving = SpritesMoving + 1 #aumenta los sprites
                time.sleep(2.5/30) #Segun la especificacion del proyecto 
            if CarRide == 3: #Si esta en la tercera marcha 
                SpritesMoving = SpritesMoving + 1 #aumenta los sprites 
                IfAccelerating = False
                time.sleep(2.5/25) #Segun la especificacion del proyecto 
        
        if HaveLost == False:  #Si no ha perdido ejecute el thread 
            Thread(target = ExcAcceleration, args = ()).start()
    Thread(target = ExcAcceleration, args = ()).start()

   
    def CompleteName(Name): #Esta funcion completa un sprite para que tenga 10 caracteres
        if len(Name) ==  10:
            return Name
        else:
            return CompleteName(Name + " ")
        
    
    def CountingKilometers(): 
        global SpritesMoving, KmTravelled, EnemyVelocity, SpritesMoving, Lives, HaveLost 
        
        CoordsCactus = Inicio.coords(RCactus) #Se establece el cactus 
        KmTravelled = KmTravelled + (1/180000)*SpritesMoving #Se calcula cuanto se ha movido 
        #Proceso matematico detras de el calculo de las velocidades 
        time.sleep(EnemyVelocity)
        MovingCactus = int(KmTravelled*(10**2)) #Se establece en que coordenada en y tiene que estar el cactus 
        if CoordsCactus[1] <= 650:
            Inicio.coords(RCactus, CoordsCactus[0], 50 + 6*MovingCactus) #Se coloca el cactus en esa coordenada 
        else:
            Inicio.coords(RCactus, CoordsCactus[0], 50) #En otro caso se vuelve a poner el cactus en el inicio
        
        if KmTravelled < 0.5 and HaveLost == False: #Si se quiere cambiar la distancia de la carrera cambiar esto 
            Thread(target = CountingKilometers, args = ()).start() #Ejecuta el conteo de kilometros a menos de que haya ganado 
        else: #En otro caso 
            Thread(target = MovingVictory, args = (0,)).start() #Anima la victoria 
            UsersAndRanking = open("usersandranking.txt", 'a') #Se usa la a para append los resultados
            User = CompleteName(jugador) #Se da el nombre del usuario 
            if dificulty == "Easy": #si es dificultad facil
                Ranking = (CarsPassed*1)/TimePlayed #Se multiplica el restulado por 1
            elif dificulty == "Medium": #Si es media 
                Ranking = (CarsPassed*1.5)/TimePlayed #Se multiplica por 1.5
            elif dificulty == "Hard": #Si es dificil 
                Ranking = (CarsPassed*2)/TimePlayed #Se multiplica por 2
            
            UsersAndRanking.write(User + str(Ranking) + "\n") #Se escriben los resultados en el documento .txt
            UsersAndRanking.close() #Se cierra el documento 
            time.sleep(2)
            window.destroy() #Se cierra el juego      
    Thread(target = CountingKilometers, args = ()).start() #Thread que llama al conteo de kilometros
    
    
    def UpdatingLabels():
        global SpritesMoving, KmTravelled, EnemyVelocity, TimePlayed, CarsPassed, Lives, CarRide
      
        #Se coloca la informacion del tiempo jugado  
        TimeLabel = tk.Label(Inicio, text = "Tiempo Jugado " + str(TimePlayed), font = ("Arial", 15), background = "#007890")
        TimeLabel.place(x = 890, y = 480, anchor = "nw")
        
        #Se coloca la informacion de la marcha 
        CarRideL = tk.Label(Inicio, text = "Marcha: " + str(CarRide), font = ("Arial", 15))
        CarRideL.place(x = 415, y = 866, anchor = "nw")
        
        #Se coloca la informacion de a cuantos carros se les ha sobrepasado 
        CPassedLabel = tk.Label(Inicio, text = "Carros Sobrepasados" + str(CarsPassed), font = ("Arial", 15), background = "#007890")
        CPassedLabel.place(x = 890, y = 640, anchor = "nw")    
        
        #Se coloca la informacion de la cantidad de kilometros recorridos 
        KmLabel = tk.Label(Inicio, text = "Kilometros Recorridos: " + str(round(KmTravelled, 4)), font = ("Arial", 15), background = "#007890")
        KmLabel.place(x =890, y = 320, anchor = "nw")
        
        #Se coloca la informacion de la velocidad a la que va el carro 
        Velocity = tk.Label(Inicio, text = str(SpritesMoving*2.5), font = ("Arial", 15))
        Velocity.place(x = 435, y = 896, anchor = "nw")
        
        #Se coloca la informacion de la catidad de vidas que se tiene 
        LabelLives = tk.Label(Inicio, text = "Vidas: " + str(Lives), font = ("Arial", 15), background = "#007890")
        LabelLives.place(x = 890, y = 800, anchor = "nw")
        
        #Se cuenta el tiempo 
        if SpritesMoving != 0:
            time.sleep(1)
            TimePlayed = TimePlayed + 1
        if HaveLost == False: #Si se perdio se deja de ejecutar esto 
            Thread(target = UpdatingLabels, args = ()).start()
    Thread(target = UpdatingLabels, args = ()).start()
    def MovingRed():
        global CarsPassed, EnemyVelocity, HowManyExist, CoordsRedEnemy, ListCars, SpritesMoving 
        CoordsRedEnemy = Inicio.coords(RedCarRight)
        if CoordsRedEnemy[1] < 650 and HaveLost == False:
            ListCars[2] = True
            Inicio.coords(RedCarRight, CoordsRedEnemy[0], CoordsRedEnemy[1] + SpritesMoving)
            time.sleep(EnemyVelocity)
            MovingRed()
        elif HaveLost == False:
            CarsPassed = CarsPassed + 1
            ListCars[2] = False
            HowManyExist = HowManyExist - 1
            Inicio.coords(RedCarRight, 560, -150)
            
    def MovingBlue():
        global CarsPassed, HowManyExist, CoordsBlue, EnemyVelocity, ListCars, SpritesMoving, HaveLost 
        CoordsBlue = Inicio.coords(BlueCarCenter)
        if CoordsBlue[1] < 650 and HaveLost == False:
            ListCars[1] = True
            Inicio.coords(BlueCarCenter, CoordsBlue[0], CoordsBlue[1] + SpritesMoving)
            time.sleep(EnemyVelocity)
            MovingBlue()

        elif HaveLost == False:
            CarsPassed = CarsPassed + 1
            ListCars[1] = False
            HowManyExist = HowManyExist - 1
            Inicio.coords(BlueCarCenter, 390, -150)

    def MovingGreen():
        global CarsPassed, HowManyExist, CoordsGreen, EnemyVelocity, ListCars, SpritesMoving, HaveLost
        CoordsGreen = Inicio.coords(GreenCarLeft)
        if CoordsGreen[1] < 650 and HaveLost == False:
            ListCars[0] = True
            Inicio.coords(GreenCarLeft, CoordsGreen[0], CoordsGreen[1] + SpritesMoving)
            time.sleep(EnemyVelocity)
            MovingGreen()
        elif HaveLost == False:
            CarsPassed = CarsPassed + 1
            ListCars[0] = False
            HowManyExist = HowManyExist - 1
            Inicio.coords(GreenCarLeft, 220, -150)
    

    
    def CloseTheGame():
        #Esta funcion se encarga de cerrar el juego 
        global IsRunning
        IsRunning = False
        Inicio.destroy()
        return
    

    window.protocol("WM_DELETE_WINDOW", CloseTheGame)
    window.mainloop()



    