import tkinter as tk
from tkinter import *
#from test_sql import *

class historial(tk.Frame):
    def __init__(self, parent, controller):

        screenwidth = controller.size['width']
        screenheight = controller.size['height']

        # Definimos el tamaño de la fuente
        button_font_size = controller.boton_tamanio
        
        tk.Frame.__init__(self, parent)
        # Definimos el tamaño de la fuente
        button_font_size = controller.boton_tamanio
        # creamos un lienzo
        canvas = tk.Canvas(self, width = screenwidth, height = screenheight, bg = 'white')
        canvas.pack(side = "top", fill = "both", expand = True)

        # colocamos el fondo de la pantalla
        canvas.create_image(0,0, image = controller.background, anchor = NW, tags = 'fondo')

        # colocar el logo
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el ícono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Historial de pruebas",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.35), 
                            text = "\t Pruebas realizadas anteriormente",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1.1)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.34),int(screenheight*0.55), image = controller.historial_icono_grande, anchor = CENTER)
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
        # Boton de instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda : controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                        **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')
        
        # Boton de atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
