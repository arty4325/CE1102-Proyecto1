"""
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores
Lenguaje: Python 3.9.9
Autores: Oscar Arturo Acuña Durán(2022049304)
Version: 4.1
Fecha de última modificación: Mayo 05/07/2022

"""

import tkinter as tk

from PIL import Image, ImageTk

import func_especiales

#mismas funciones de la ves pasada, mismo uso
def Ranking(window, Inicio): #Se vuelve a poner como parametro window e inicio por que estos estan definidos en main
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
    Background = ImageTk.PhotoImage(file = "Imagenes/mainmenu.png")
    Inicio.create_image(0,0, image = Background, anchor = "nw")
    temp = [] #para poder borrar los botones despues 
    UsersAndRanking = open("usersandranking.txt", 'r')
    
    #Aqui se va a ejecutar el algoritmo de ordenamiento 
    ListUsersAndRanking = UsersAndRanking.readlines()
    
    #Despues me encargo de hacer las funciones que borran los items que son iguales
    def TupleGenerator(ListUsersAndRanking, Ret): #Esta funcion genera una tupla en donde los indices pares son los nombres de usuario 
    #Y los impares el puntaje que obtuvieron 
        if ListUsersAndRanking == []: #Conicion finalizacion 
            return Ret
        else:
            Ret += [ListUsersAndRanking[0][0:10], float(ListUsersAndRanking[0][10:-1])] #Lo que hace es ayudarse que ya se sabe la longitud del nombre
            return TupleGenerator(ListUsersAndRanking[1:], Ret)
      
    def ListGenerator(ListUsersAndRanking, Ret): #Esto genera una lista con los puntajes obtenidos 
        if ListUsersAndRanking == []: #Condicion finalizacion 
            return Ret
        else:
            Ret += [float(ListUsersAndRanking[0][10:-1])]
            return ListGenerator(ListUsersAndRanking[1:], Ret)
    
    def OnlyNames(ListUsersAndRanking, Ret): #Esto genera una lista con el nombre de los jugadores en orden a como jugaron 
        if ListUsersAndRanking == []: #Condicion finalizacion 
            return Ret 
        else:
            Ret += [ListUsersAndRanking[0][0:10]]
            return OnlyNames(ListUsersAndRanking[1:], Ret)
        
        
    NamesAndRanking = TupleGenerator(ListUsersAndRanking, [])
    
    OnlyNames = OnlyNames(ListUsersAndRanking, [])
    OnlyNumbers = ListGenerator(ListUsersAndRanking, [])
    
    EditableNames = OnlyNames[:]
    EditableNumbers = OnlyNumbers[:]
  
    
    def bubble_sort(EditableNumbers): #Sorting Burguja 
      
        if len(EditableNumbers) <= 1: #Condicion de finalizacion 
            return EditableNumbers
        if len(EditableNumbers) == 2: #Condicion de finalizacoin 
            return EditableNumbers if EditableNumbers[0] < EditableNumbers[1] else [EditableNumbers[1], EditableNumbers[0]] #se revisa 
            #Si se quieren rotar los numeros 
        a, b = EditableNumbers[0], EditableNumbers[1] #Se seleccionan los primeros dos 
        bs = EditableNumbers[2:] #Se hace slicing
        res = []
        if a < b: #Se revisa si el primero es mayor al segundo 
            res = [a] + bubble_sort([b] + bs) #Se conserva orden 
        else: #Si el segundo es mayor al primero 
            res = [b] + bubble_sort([a] + bs) #Se invierte el orden 
        return bubble_sort(res[:-1]) + res[-1:] #Devuelve las listas
     
     
    SortedRanking = bubble_sort(EditableNumbers) #ordena el ranking 
    
    def SortingNames(Names, SortedRanking, Res):
        #Esta funcion quiere ordenar los nombres a como se ordeno el ranking 
        if Names ==[]: #Condicion de finalizacion 
            return Res
        else:
            i = Names.index(SortedRanking[0]) #Se consigue el inidice de algun elemento 
            Res += [Names[i - 1]] #Se busca en la lista y se le suma al resutlado en cola 
            del Names[i] #Lo borra de la listade nombres
            del Names[i - 1] #Lo borra de la listade nombres 
            return SortingNames(Names, SortedRanking[1:], Res) #Llamada recursiva 
    
        
    #Y esto deberia de dar el nombre de los jugadores en la manera correcta
    SortedName = SortingNames(NamesAndRanking, SortedRanking, []) 
    
    
    
    # Place the labels
    # Ahora se va a proceder a pones los labels
    if len(SortedName) >= 1:
        FirstPlace = tk.Label(Inicio, text = SortedName[0] + str(SortedRanking[0]), font = ("Arial", 30), background = "#4A1798")
        FirstPlace.place(x = 588, y = 583, anchor = "nw")
    
    if len(SortedName) >= 2:
        SecondPlace = tk.Label(Inicio, text = SortedName[1] + str(SortedRanking[1]), font = ("Arial", 30), background = "#4A1798")
        SecondPlace.place(x = 588, y = 533, anchor = "nw")
    if len(SortedName) >= 3:
        ThirdPlace = tk.Label(Inicio, text = SortedName[2] + str(SortedRanking[2]), font = ("Arial", 30), background = "#4A1798")
        ThirdPlace.place(x = 588, y = 483, anchor = "nw")
        
    if len(SortedName) >= 4:
        FourthPlace = tk.Label(Inicio, text = SortedName[3] + str(SortedRanking[3]), font = ("Arial", 30), background = "#4A1798")
        FourthPlace.place(x = 588, y = 433, anchor = "nw")
        
    if len(SortedName) >= 5:
        FifthPlace = tk.Label(Inicio, text = SortedName[4] + str(SortedRanking[4]), font = ("Arial", 30), background = "#4A1798")
        FifthPlace.place(x = 588, y = 383, anchor = "nw")
    
    if len(SortedName) >= 6:
        SixthPlace = tk.Label(Inicio, text = SortedName[5] + str(SortedRanking[5]), font = ("Arial", 30), background = "#4A1798")
        SixthPlace.place(x = 588, y = 333, anchor = "nw")
        
    if len(SortedName) >= 7:
        SeventhPlace = tk.Label(Inicio, text = SortedName[6] + str(SortedRanking[6]), font = ("Arial", 30), background = "#4A1798")
        SeventhPlace.place(x = 588, y = 283)
        
    temp.append(FirstPlace)
    temp.append(SecondPlace)
    temp.append(ThirdPlace)
    temp.append(FourthPlace)
    temp.append(FifthPlace)
    temp.append(SixthPlace)
    temp.append(SeventhPlace)
    
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
    
    
    window.mainloop()
