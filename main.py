"""
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores
Lenguaje: Python 3.9.9
Autores: Oscar Arturo Acuña Durán(2022049304)
Version: 4.1
Fecha de última modificación: Mayo 05/07/2022

"""
#La idea de este archivo es llevar una version mucho mas ordenada de lo que se esta realizando 

#En el archivo Main lo que se quiere hacer es llamar a la ventana y al canvas
#De esta manera, cuando se abre otra pestaña se pueden poner mas cosas al canvas sin necesidad de abrir mas ventanas

import tkinter as tk # Se importa el tkinter para poder realizar la interfaz grafica

import pantalla_inicio #para poder ejecutar la pantalla desde aqui

#Primero se crea una ventana con las dimenciones en las cuales se hara el juego 
window = tk.Tk() #Define una ventana
window.title("Brick Game") #Le da un titlulo a la ventana 
window.minsize(1176,966) #Se le da un tamaño a la ventana 
window.resizable(False, False) #Se establece que esta ventana no se puede ni expandir ni reducir

#Se crea el linezo
Inicio = tk.Canvas(window, width = 1176, height = 966)
Inicio.place(x = 0, y = 0)
#Se llama la pantalla de inicio, en esta pantalla esta definido el window.mainloop()
pantalla_inicio.PantallaInicio(window, Inicio)
