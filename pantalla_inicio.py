"""
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores
Lenguaje: Python 3.9.9
Autores: Oscar Arturo Acuña Durán(2022049304)
Version: 4.1
Fecha de última modificación: Mayo 05/07/2022

"""

import tkinter as tk

#Esto se importa para poder engañar a la recursividad y hacer una recursividad infinita
from threading import Thread
import time

#Lo sigiuente se importa para poder usar .png como botones
from PIL import Image, ImageTk

#Se impotran las funciones especiales y la otra pantalla
import func_especiales
import acerca_de
import juego
import ranking

# Se quiere importar la musica y que se pueda usar en tkinter
# https://youtu.be/djDcVWbEYoE Citar a este maje 
# Lo bueno de esto es que sirve en cualquier sistema operativo 
# Se puede hacer con pygame 
# Marcelo nos dio permiso de hacer esto entonces no estoy haciendo nada ilegalisimo 
# Recordar mencionar que PyGame se installa desde la vara de comandos

import pygame 



#Se define la pantalla de inicio que se ejecuta en main
def PantallaInicio(window, Inicio): #Observe como se pone window e Inicio como parametros ya que estan definidos en main
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Lenguaje: Python 3.9.9
    Profesor: Ing Milton Villegas Lemus
    Autor: Oscar Arturo Acuña Duran (2022049304)
    Version: 4.1
    Fecha de última modificación: Mayo 05/07/2022
    Entradas: Window, Inicio
    Restricciones: Las entradas tienen que ser el window y el inicio que se establecio en el archivo main 
    Salidas: Carga y coloca la pantalla de incio 
    """
    global IsRunning
    IsRunning = True
    #Se tiene que activar Pygame 
    # https://onlymp3.to/en10/
    # https://github.com/pygame/pygame/issues/2785
    # https://nerdparadise.com/programming/pygame/part3
    
    # Cancion https://www.youtube.com/watch?v=wmin5WkOuPw
    #Se carga Pygame para la musica 
    pygame.mixer.init()
    
    #Se carga la musica
    pygame.mixer.music.load("Sonidos/TheProdigyFirestarter.mp3")
    
    #Ahora se corre
    pygame.mixer.music.play(loops = -1)
    
  
    temp = [] #Esta lista se crea para meter aqui los botones y luego destruirlos cunando haya que salirse de esta funcion
    Background = ImageTk.PhotoImage(file = "Imagenes/mainmenu.png")
    
    #Ahora se tiene que colocar el background en el canvas
    Inicio.create_image(0, 0, image = Background, anchor = "nw")
    
    #Ahora se usa la funcion que esta en func_especiales para cargar los sprites
    Title = func_especiales.cargarSprites("/Titulo/titulo-*")
    TM = Inicio.create_image(588, 193)
    
    #Ahora se hace una funcion qeu permite animar el titulo
    
    def Movingtitle(i):
        #Autoria: Marcelo Truque Montero 
        global IsRunning
        if (i >= len(Title)):
            i = 0 
        if IsRunning:
            Inicio.itemconfig(TM, image = Title[i])
        def CallRec():
            Movingtitle(i + 1)
        window.after(40, CallRec)

    
    def Close(): 
        #Autoria: Jose Fernando Morales Vargas 
        global IsRunning
        IsRunning = False
        time.sleep(0.5)
        window.destroy()
        return
        
    
    def botonrank():
        #Se destruye todo lo lo que esta en esta pantalla y despues se llama al raking 
        Inicio.delete("all") 
        func_especiales.labelDest(temp) 
        ranking.Ranking(window, Inicio)
    
    def botonabout():
        #Se destruye todo lo que esta en esta pantalla y luego se llama al about 
        Inicio.delete("all")
        func_especiales.labelDest(temp)
        acerca_de.about(window, Inicio)
    
    def botonexit():
        #Se destruye la ventana 
        window.destroy()
    
    def LogReturn():
        #Esta funcion retorna a la pantalla de inicio 
        Inicio.delete("all")
        func_especiales.labelDest(temp)
        PantallaInicio(window, Inicio)
        
    def botonlogin():
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
        Descripcion: Esta funcion permite al usuario poner su nombre y despues elejir el nivel de dificultad para asi comenzar a jugar 
        """
        def EntryPlay():
            
            nonlocal UserEntry  
            User = UserEntry.get()

            if len(User) < 1 or len(User) > 10: #Se revisa que si este dentro del parametro de lo establecido 
                ErrorLabel = tk.Label(Inicio, text = "Por favor introduzca un nombre de usuario con diez o \n menos caracteres", font = ("Helvetica", 20), background = "#4A1798", fg = "#FFFFFF")
                ErrorLabel.place(x = 784, y = 700, anchor = "center")
                temp.append(ErrorLabel)
                
            elif 1 <= len(User) <= 10: #Se revisa que si este dentro del parametro de lo establecido 
                func_especiales.labelDest(temp) 
                Inicio.create_image(588, 387, image = DifTitle, anchor = "center")
                
                #Se tienen que crear las funciones primero
                def EasyGame(): #ejecuta el juego facil 
                    Inicio.delete("all")
                    func_especiales.labelDest(temp)
                    #Cuando se ejecute el juego se tiene que poner entre los parametros el user
                    pygame.mixer.music.stop()
                    juego.Juego(window, Inicio, User, "Easy")
                    Close()
                    
                def MediumGame(): #Ejecuta el juego en su mediana complejidad
                    Inicio.delete("all")
                    func_especiales.labelDest(temp)
                    #Cuando se ejecute el juego se tiene que poner entre los parametros el user
                    pygame.mixer.music.stop()
                    juego.Juego(window, Inicio, User, "Medium")
                    Close()
                    
                def HardGame(): #Ejecuta el juego en su complejidad mas alta 
                    Inicio.delete("all")
                    func_especiales.labelDest(temp)
                    #Cuando se ejecute el juego se tiene que poner entre los parametros el user
                    pygame.mixer.music.stop()
                    juego.Juego(window, Inicio, User, "Hard")
                    Close()
                
                
                #Se colocan los botones para hard, medium y easy 
                easybuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/easybutton.png"))
                mediumbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/mediumbutton.png"))
                hardbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/hardbutton.png"))

                EasyButton = tk.Button(Inicio, command = EasyGame, image = easybuttonimage)
                EasyButton.image = easybuttonimage
                EasyButton.place(x = 294, y = 580, anchor = "center")        
                temp.append(EasyButton)
        
                MediumButton = tk.Button(Inicio, command = MediumGame, image = mediumbuttonimage)
                MediumButton.image = mediumbuttonimage
                MediumButton.place(x = 588, y = 580, anchor = "center")
                temp.append(MediumButton)
        
                HardButton = tk.Button(Inicio, command = HardGame, image = hardbuttonimage)
                HardButton.image = hardbuttonimage
                HardButton.place(x = 882, y = 580, anchor = "center")
                temp.append(HardButton)

                
        
                
        #Se crean botones 
        UserButton = tk.Button(Inicio, command = EntryPlay, image = usernamebuttonimage) 
        UserButton.image = usernamebuttonimage
        temp.append(UserButton)
    
        LoginButton.destroy()
        RankingButton.destroy()
        AboutButton.destroy()
        
        #Se crean entrys
        UserEntry.place(x = 784, y = 386, anchor = "center")
        UserButton.place(x = 392, y = 386, anchor = "center")
        LogReturnButton.place(x = 160, y = 729, anchor = 'center')
        #Esta es la informacion que se despliega en el inicio de sesion 
        information = open('infologin.txt', 'r')
        LabelInfo = tk.Label(Inicio, text = information.read(), font = ("Helvetica",20), background = "#4A1798", fg = "#FFFFFF")
        LabelInfo.place(x = 784, y = 580, anchor = "center")
        temp.append(LabelInfo) #aqui se arreglo bug (Apuntar en documento)
        

    UserEntry = tk.Entry(Inicio, width = 10, font = ("Helvetica", 53))
    temp.append(UserEntry)

    #Se definen las imagenes de los botones
    rankingbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/rankingbutton.png"))
    aboutbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/aboutbutton.png"))
    salirbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/exitbutton.png"))
    loginbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/loginbutton.png"))
    usernamebuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/usernamebutton.png"))
    returnbuttonimage = ImageTk.PhotoImage(Image.open("Imagenes/Titulo/returnbutton.png"))
    
    DifTitle = ImageTk.PhotoImage(file = "Imagenes/Titulo/dificultyleveltitle.png")
    
    
    #Se definen los botones
    

    
    #Se hace un boton para volver a lo de antes cuando se estaba en el login
    LogReturnButton = tk.Button(Inicio, command = LogReturn, image = returnbuttonimage)
    LogReturnButton.image = returnbuttonimage
    temp.append(LogReturnButton)
    
    # Para iniciar sesion 
    LoginButton = tk.Button(Inicio, command = botonlogin, image = loginbuttonimage)
    LoginButton.image = loginbuttonimage
    LoginButton.place(x = 588, y = 386, anchor = "center")
    temp.append(LoginButton)
    
    # para ir al ranking 
    RankingButton = tk.Button(Inicio, command = botonrank, image = rankingbuttonimage)
    RankingButton.image = rankingbuttonimage
    RankingButton.place(x = 588, y = 580, anchor = "center")
    temp.append(RankingButton)
    
    #Para ir al about 
    AboutButton = tk.Button(Inicio, command = botonabout, image = aboutbuttonimage)
    AboutButton.image = aboutbuttonimage
    AboutButton.place(x = 588, y = 773, anchor = "center")
    temp.append(AboutButton)
    
    #Para salir 
    ExitButton = tk.Button(Inicio, command = botonexit, image = salirbuttonimage)
    ExitButton.image = salirbuttonimage
    ExitButton.place(x = 160, y = 889, anchor = 'center')
    temp.append(ExitButton)
    
    
    
    
    
    
    
    window.protocol("WM_DELETE_WINDOW", Close)
    Thread(target = Movingtitle, args = (0,)).start() #Esto se hace para animar el titulo
    
    window.mainloop() #Esto se hace para poder correr todo lo anterior
    
            
        