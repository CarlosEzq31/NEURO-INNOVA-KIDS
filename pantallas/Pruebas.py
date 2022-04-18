import tkinter as tk
from tkinter import *
from pantallas.Lista_Pruebas import *
from pantallas.Usuario import *
from pantallas.Historial import *
from pantallas.EntrevistaEni.HistoriaClinica import *

class pruebas(tk.Frame):
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
        canvas.create_image(0,0, image = controller.background, anchor = NW)

        # colocar el logo
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Pruebas",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        
        # boton instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda : controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                       **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')
        
        # boton menu
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                command = lambda : controller.ir_menu_principal(),
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')

        # boton usuario
        canvas.create_image(int(screenwidth*0.6),int(screenheight*0.65), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'usuario')
        canvas.create_image(int(screenwidth*0.57),int(screenheight*0.65), image = controller.registro_icono, anchor = CENTER)
        register_button = tk.Button(self, 
                                    text = "Usuario", 
                                    command = lambda : controller.mostrar_pantalla(self, usuario_info),
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                    **controller.estilo_rosa)
        register_button.place(relx = 0.625, rely = 0.65, anchor = CENTER)
        controller.animacion_boton(register_button, canvas, 'usuario', tamaño = 'grande')

        # boton iniciar prueba
        canvas.create_image(int(screenwidth*0.6),int(screenheight*0.775), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'prueba')
        canvas.create_image(int(screenwidth*0.52),int(screenheight*0.775), image = controller.play_icono, anchor = CENTER)
        test_button = tk.Button(self, 
                                text = "Iniciar prueba nueva", 
                                command = lambda: controller.mostrar_pantalla(self, lista_pruebas),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.2)), 
                                **controller.estilo_rosa)
        test_button.place(relx = 0.625, rely = 0.775, anchor = CENTER)
        controller.animacion_boton(test_button, canvas, 'prueba', tamaño = 'grande')

        # boton historial 
        canvas.create_image(int(screenwidth*0.6),int(screenheight*0.9), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'historial')
        canvas.create_image(int(screenwidth*0.52),int(screenheight*0.9), image = controller.historial_icono, anchor = CENTER)
        historial_boton = tk.Button(self, 
                                text = "Historial de pruebas", 
                                command = lambda: controller.mostrar_pantalla(self, historial),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.2)), 
                                **controller.estilo_rosa)
        historial_boton.place(relx = 0.625, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(historial_boton, canvas, 'historial', tamaño = 'grande')
        
        # boton de entrevista eni
        canvas.create_image(int(screenwidth*0.6),int(screenheight*0.525), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'eni')
        canvas.create_image(int(screenwidth*0.52),int(screenheight*0.525), image = controller.historial_icono, anchor = CENTER)
        eni_boton = tk.Button(self, 
                                text = "Entrevista ENI", 
                                command = lambda: controller.mostrar_pantalla(self, historiaclinica),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.2)), 
                                **controller.estilo_rosa)
        eni_boton.place(relx = 0.625, rely = 0.525, anchor = CENTER)
        controller.animacion_boton(eni_boton, canvas, 'eni', tamaño = 'grande')
        
        def salir():
            self.i = False
            controller.id = 0
            controller.previous_frame()
            
        # boton atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : salir(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')