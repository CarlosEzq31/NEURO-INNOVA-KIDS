import tkinter as tk
from tkinter import *
from pantallas.Ingreso import *
from pantallas.Informacion_basica import *


class menu_principal(tk.Frame):
    def __init__(self, parent, controller):
        ancho_pantalla = controller.size['width']
        alto_pantalla = controller.size['height']

        # Definimos el tamaño de la fuente
        button_font_size = controller.boton_tamanio

        tk.Frame.__init__(self, parent)
        # creamos un lienzo
        canvas = tk.Canvas(self, width = ancho_pantalla, height = alto_pantalla, bg = 'white')
        canvas.pack(side = "top", fill = "both", expand = True)

        # colocamos el fondo de la pantalla
        canvas.create_image(0,0, image = controller.back_ninios, anchor = NW)
        # colocar el logo
        canvas.create_image(int(ancho_pantalla*0.25),int(alto_pantalla*0.4), image = controller.logo, anchor = CENTER)
        
        # crear y colocar el boton de informacion
        canvas.create_image(int(ancho_pantalla*0.875),int(alto_pantalla*0.7), image = controller.boton_rosa, tags = 'informacion',anchor = CENTER)
        canvas.create_image(int(ancho_pantalla*0.75),int(alto_pantalla*0.7), image = controller.signo_iterrogacion, anchor = CENTER)
        about_button = tk.Button(self, text = "Información básica",
                                command = lambda : controller.show_frame(self,informacion_basica), 
                                font = ('Mukta Malar ExtraLight', button_font_size), 
                                **controller.estilo_rosa)
        about_button.place(relx = 0.875, rely = 0.7, anchor = CENTER)
        controller.animacion_boton(about_button, canvas, 'informacion')
        
        # crear y colocar el boton para entrar al programa
        canvas.create_image(int(ancho_pantalla*0.875),int(alto_pantalla*0.8), image = controller.boton_rosa,tags = 'neuro', anchor = CENTER)
        canvas.create_image(int(ancho_pantalla*0.75),int(alto_pantalla*0.8), image = controller.logo_bn, anchor = CENTER)
        neuro_boton = tk.Button(self, text = "NEURO INNOVA KIDS®",
                                font = ('Mukta Malar ExtraLight', button_font_size), 
                                command = lambda : controller.show_frame(self, ingreso),
                                **controller.estilo_rosa)
        neuro_boton.place(relx = 0.875, rely = 0.8, anchor = CENTER)
        controller.animacion_boton(neuro_boton, canvas, 'neuro')

        # crear y colocar el boton para salir del programa
        canvas.create_image(int(ancho_pantalla*0.875),int(alto_pantalla*0.9), image = controller.boton_rosa, tags = 'salir',anchor = CENTER)
        salir_boton = tk.Button(self, text = "Salir",
                                command = lambda : controller.destroy(),
                                font = ('Mukta Malar ExtraLight', button_font_size), 
                                **controller.estilo_rosa)
        salir_boton.place(relx = 0.875, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(salir_boton, canvas, 'salir')