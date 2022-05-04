import tkinter as tk
from tkinter import *
from functions.sql_metodos import *

class usuario_info(tk.Frame):
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

        #colocamos el titulo de la pantalla
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Usuario",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        
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
        
        
        # Datos del paciente
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.475), 
                           text = 'Datos del paciente', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*1.5)),
                           tags = 'datos',
                           anchor = NW)
        # id
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.525), 
                           text = 'id', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'id',
                           anchor = NW)
        
        # Fecha de registro
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.575), 
                           text = 'Fecha de registro: 1/08/2020', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'fecha',
                           anchor = NW)
        
        # Nombre del aplicador
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.61), 
                           text = 'Nombre del aplicador: Carmen cabrera', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'aplicador',
                           anchor = NW)
        # Sexo
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.645), 
                           text = 'Sexo: Femenino', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'sexo',
                           anchor = NW)
        # Edad
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.68), 
                           text = 'Edad: 11 años', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'edad',
                           anchor = NW)
        # Estatura
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.715), 
                           text = 'Estatura : 1.30 m', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'estatura',
                           anchor = NW)
        # Diagnostico
        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.75), 
                           text = 'Diagnóstico : TDAH', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'diagnostico',
                           anchor = NW)
        
        # Obtenemos los datos del usuario mediante el id
        self.i = True
        def mostrar_datos(e):
            while self.i == True and controller.id != 0:
                datos = obtener_info_por_id(controller.id)
                print(datos)
                canvas.itemconfig('id', text = datos.get('usuario'))
                canvas.itemconfig('datos', text = str('Nombre: ' + datos.get('nombre')))
                canvas.itemconfig('sexo', text = str('Genero: ' + datos.get('genero')))
                self.i = False
        
        
        self.bind('<Enter>', mostrar_datos)
        
        def salir():
            self.i = True
            controller.previous_frame()
            
        # Boton de atras
        canvas.create_image(int(screenwidth*0.15), int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : salir(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')