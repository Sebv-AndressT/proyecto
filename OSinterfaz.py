from tkinter import *

class OSInterfaz:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('OsornoSprings')
        self.ventana.geometry('800x800')

        #entrada de datos
        self.nombre = Label(self.ventana, text='Nombre:')
        self.nombre.pack()

        self.entrada = Entry(self.ventana)
        self.entrada.pack()

        #espacios de estacionamiento 
        self.opcion_estacionamiento = StringVar(value="desocupado")

        Radiobutton(self.ventana, text='Puesto 1')