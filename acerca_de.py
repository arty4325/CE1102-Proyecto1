"""
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores
Lenguaje: Python 3.9.9
Autores: Oscar Arturo Acuña Durán(2022049304)
Version: 4.1
Fecha de última modificación: Mayo 05/07/2022

"""
#Ya esta pestaña esta terminada

import tkinter as tk #Se importa para poder colocar mas elementos en el lienzo

from threading import Thread #Esto permite ejecutar varias funciones al mismo tiempo 
import time #Esto permite hacer que las funciones esperen antes de ejecutar la siguente instruccion

from PIL import Image, ImageTk #Esto permite importar y trabajar con imagenes rapidamente
import func_especiales #Aqui se tienen una serie de funciones que son muy utlizadas en la programacion

#mismas funciones de la ves pasada, mismo uso

def about(window, Inicio): #Se vuelve a poner como parametro window e inicio por que estos estan definidos en el archivo main
    """
            Instituto Tecnológico de Costa Rica
            Ingenieria en Computadores
    Lenguaje: Python 3.9.9
    Profesor: Ing: Milton Villegas Lemus
    Autor: Oscar Arturo Acuña Durán(2022049304)
    Version: 4.1
    Fecha de última modificación: Mayo 05/07/2022
    Entradas: Window, Inicio
    Restricciones: Window tiene que ser la definicion de la ventana y Inicio tiene que ser la definicion de un canvas
    Salidas: Dependiendo de los botones que se seleccionen en esta ventana, esta va a llevar o a la pantalla de inicio o bien va a cerrar 
    #El programa
    """
    Background = ImageTk.PhotoImage(file = "Imagenes/mainmenu.png") #Se define la imagen que aparece atras
    Inicio.create_image(0,0, image = Background, anchor = "nw") #Se coloca la imagen que aparece atras
    temp = [] #En esta lista se colocan los botones y los labels para que despues puedan ser todos borrados al mismo tiempo
    
    texto = open('infoabout.txt', 'r') #Se abre al informacion del about que esta en un archivo txt aparte
    LabelInfo = tk.Label(Inicio, text = texto.read(), font = ("Helvetica",20), background = "#4A1798", fg = "#FFFFFF")
    # Se crea un label que muestra lo que se lee del archivo infoabout, se le pone un background similar al color que aparece 
    # En la imagen de fondo 
    LabelInfo.place(x = 120, y = 326, anchor = "nw") #Se coloca la informacion
    
    temp.append(LabelInfo) #se pone en temp por que depsues se va a querrer borrar lo que aqui dice
    
    about_frames = func_especiales.cargarSprites("about/about-animation*") #Esto es para animar el titulo
    AB = Inicio.create_image(294, 193) #Se coloca el lugar en el cual ira el titulo
    
    def Movingtitle(i):
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
        if (i >= len(about_frames)): # Se revisa si el valor que se esta tomando esta dentro de la cantidad de sprites que existe 
            i = 0 #Si no esta este vuelve a ser 0
        Inicio.itemconfig(AB, image = about_frames[i]) #Configura la imagen AB para que el sprite que apareza es el que esta en la posicion i
        time.sleep(0.04) #Se espera un poco para seguie ejecutando la funcion 
        Thread(target = Movingtitle, args = (i + 1,)).start() #Se hace una llamada a la funcion con i + 1 en un hilo distinto
        
    Thread(target =Movingtitle, args = (0,)).start() # Se hace la llamada a la funcion comenzando por 0 en un hilo distinto 
        
    def botonreturn(): #este boton tiene como fin volver a la pantalla principal 
        Inicio.delete("all") #Se destruye todo lo que aparecia en la pantalla
        func_especiales.labelDest(temp) # Se destruyen todos los labels y botones
        from pantalla_inicio import PantallaInicio #se hace el import aqui para que no haya un problema con loop de imports
        PantallaInicio(window, Inicio) #Se ejecuta lo que debe de aparecer en la otra pantalla
        
        
    #Aqui se asigna la imagen y se termina de definir el boton de return
    ReturnButtonImage = ImageTk.PhotoImage(Image.open("Imagenes/about/returnbutton.png"))
    ReturnButton = tk.Button(Inicio, command = botonreturn, image = ReturnButtonImage)
    ReturnButton.image = ReturnButtonImage
    ReturnButton.place(x = 250, y = 679, anchor = "center")
    temp.append(ReturnButton)
    
    #Se pone la imagen del autor del proyecto :) 
    autor = ImageTk.PhotoImage(file = "Imagenes/about/fotoautor.png") 
    Inicio.create_image(970,479, image = autor, anchor = "center")
    
    
    
    window.mainloop() #para poder correr la funcion