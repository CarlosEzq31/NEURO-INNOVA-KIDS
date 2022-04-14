import tkinter as tk
from tkinter import *
from pantallas.Ingreso import *
from pantallas.Pruebas import *
from pantallas.Instrucciones import *


bg_primary_buttons = "#f6ddeb"
bg_secondary_buttons = "#e8eab9"

# second window frame page1
class inicio(tk.Frame):
    def __init__(self, parent, controller):
        screenwidth = controller.size['width']
        screenheight = controller.size['height']

        # Definimos el tamaño de la fuente
        button_font_size = controller.boton_tamanio
        
        tk.Frame.__init__(self, parent)
        # creamos un lienzo
        canvas = tk.Canvas(self, width = screenwidth, height = screenheight, bg = 'white')
        canvas.pack(side = "top", fill = "both", expand = True)
        # colocamos el fondo de la pantalla
        canvas.create_image(0,0, image = controller.background, anchor = NW)

        # colocar el logo
        canvas.create_image(int(screenwidth*0.25),int(screenheight*0.4), image = controller.logo, anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, tags = "instrucciones",anchor = CENTER)
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda : controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                        **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')

        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, tags = 'atras',anchor = CENTER)
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, tags = "menu", anchor = CENTER)
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                command = lambda : controller.ir_menu_principal(),
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')


        canvas.create_image(int(screenwidth*0.6),int(screenheight*0.7), image = controller.boton_rosa_grande, tags = 'registro',anchor = CENTER)
        canvas.create_image(int(screenwidth*0.57),int(screenheight*0.7), image = controller.registro_icono, anchor = CENTER)
        register_button = tk.Button(self, 
                                    text = "Registro", 
                                    command = lambda : controller.show_frame(self, ingreso),
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                    **controller.estilo_rosa)
        register_button.place(relx = 0.626, rely = 0.7, anchor = CENTER)
        controller.animacion_boton(register_button, canvas, 'registro',tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.6),int(screenheight*0.825), image = controller.boton_rosa_grande, tags = 'pruebas',anchor = CENTER)
        canvas.create_image(int(screenwidth*0.57),int(screenheight*0.825), image = controller.play_icono, anchor = CENTER)
        test_button = tk.Button(self, 
                                text = "Pruebas", 
                                command = lambda: controller.show_frame(self,pruebas),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        test_button.place(relx = 0.625, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(test_button, canvas, 'pruebas', tamaño = 'grande')