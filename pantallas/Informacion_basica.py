# importamos las librerias necesarias
import tkinter as tk
from tkinter import *
from pantallas.Resultados import *
from pantallas.InformacionBasica.Que_es import *
from pantallas.InformacionBasica.Informacion_Pruebas import *
from pantallas.InformacionBasica.Seguidor_ocular import *

# estableciendo colores
bg_primary_buttons = "#f6ddeb"
bg_secondary_buttons = "#e8eab9"

# pantalla de información básica
class informacion_basica(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Información básica",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.signo_iterrogacion_grande, anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda : controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                        **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')

        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self,
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')

        # Botones con lista de pruebas
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.4), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'que_es')
        register_button = tk.Button(self, 
                                    text = "¿Qué es?", 
                                    command = lambda : controller.mostrar_pantalla(self, que_es),
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                    **controller.estilo_rosa)
        register_button.place(relx = 0.7, rely = 0.4, anchor = CENTER)
        controller.animacion_boton(register_button, canvas, 'que_es', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.525), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'pruebas')
        test_button = tk.Button(self,
                                text = "Pruebas", 
                                command = lambda: controller.mostrar_pantalla(self,info_pruebas),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        test_button.place(relx = 0.7, rely = 0.525, anchor = CENTER)
        controller.animacion_boton(test_button, canvas, 'pruebas', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.65), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'seguidor_ocular')
        seguidor_boton = tk.Button(self, 
                                text = "Seguidor ocular", 
                                command = lambda: controller.mostrar_pantalla(self, seguidor_ocular),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        seguidor_boton.place(relx = 0.7, rely = 0.65, anchor = CENTER)
        controller.animacion_boton(seguidor_boton, canvas, 'seguidor_ocular', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.775), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'resultados')
        resultados_boton = tk.Button(self, 
                                text = "Resultados", 
                                command = lambda: controller.mostrar_pantalla(self, resultados),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        resultados_boton.place(relx = 0.7, rely = 0.775, anchor = CENTER)
        controller.animacion_boton(resultados_boton, canvas, 'resultados', tamaño = 'grande')
