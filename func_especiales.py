"""
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores
Lenguaje: Python 3.9.9
Autores: Oscar Arturo Acuña Durán(2022049304)
Version: 4.1
Fecha de última modificación: Mayo 05/07/2022

"""
import tkinter as tk
import glob 

def cargarimgs(input, listaResultado):
    """
            Instituto Tecnológico de Costa Rica
            Ingenieria en Computadores
    Lenguaje: Python 3.9.9
    Profesor: Ing Milton Villegas Lemus
    Autor: Marcelo Truque Montero
    Version: 4.1
    Fecha de última modificación: Mayo 05/07/2022
    Entradas: La lista de imagenes
    Restricciones: Tiene que ser una lista que corresponda a las imagenes
    Salidas: Carga las imagenes en una lista
    """
    
   
    if(input == []): #Se establece la condicion de finalizacion
        return listaResultado
    else:
        listaResultado.append(tk.PhotoImage(file = input[0])) #Se van poniendo las imagenes en una lista 
        return cargarimgs(input[1:], listaResultado) #Se hace un slicing de la lista y se continua
    
def cargarSprites(patron):
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Lenguaje: Python 3.9.9
    Profesor: Ing Milton Villegas Lemus
    Autor: Marcelo Truque Montero
    Version: 4.1
    Fecha de última modificación: Mayo 05/07/2022
    Entradas: El nombre de los sprites que se quieren cargar con un * al final
    Restricciones: Lo que se ingresa tiene que ser el nombre de sprites que existen
    Salidas: Carga los sprites

    """
    x = glob.glob("Imagenes/" + patron) #Se buscan los sprites en la memoria con glob.glob
    x.sort() #Se ordenan para que aparezcan en el orden correcto cuando se desplieguen 
    return cargarimgs(x, []) #Se retorna la lista ordenada


def labelDest(List):
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Lenguaje: Python 3.9.9
    Profesor: Ing Milton Villegas Lemus
    Autor: Oscar Arturo Acuña Duran (2022049304)
    Version: 4.1
    Fecha de última modificación: Mayo 05/07/2022
    Entradas: Tiene que ser una listq que contiene unicamente nombres de labels y botones que existen
    Restricciones: Los elementos tienen que ser tipo string
    Salidas: Destruye los labels y botones
    """
    if List == []:
        return [] #Condicion de finalizacion 
    else:
        (List[0]).destroy() #Se destruyen los elementos 
        labelDest(List[1:]) #Se hace un slicing
    
