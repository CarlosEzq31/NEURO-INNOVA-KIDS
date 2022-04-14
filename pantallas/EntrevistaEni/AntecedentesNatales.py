import tkinter as tk
from tkinter import *
from pantallas.EntrevistaEni.HistoriaFamiliar import *

class antecedentes_natales(tk.Frame):
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
                            text = "Antecedentes Natales",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.registro_icono_grande, anchor = CENTER)
        
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
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Tipo de parto', 'Semanas de Gestación', 'Horas de parto', 'Tipo', 'Necesidades nacimiento', 'Sufrimiento Fetal', 'Peso', 'Talla']
        h = 0.4
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h), image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self, 
                                text = f"{form}", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
            forms[f"{form}_formulario"] = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
            forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            h += 0.075

        self.data = {}
        def printData():
            for form in label:
                self.data[f"{form}"] = forms.get(f"{form}_formulario").get()
            print(self.data)
            controller.show_frame(self, historialfamiliar)
            
                
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

# Padecimientos durante el emabarazo
class antecedentes_natales2(tk.Frame):
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
                            text = "Antecedentes Natales",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.registro_icono_grande, anchor = CENTER)
        
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
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Rubéola', 'Varicela', 'Edema', 'Traumatismo', 'Amenaza aborto', 'Sífilis', 'Toxoplasmosis', 'VIH', 'Hipertensión', 'Toxemia','Otros']
        h = 0.4
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h), image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self, 
                                text = f"{form}", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
            forms[f"{form}_formulario"] = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
            forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            h += 0.075

        self.data = {}
        def printData():
            for form in label:
                self.data[f"{form}"] = forms.get(f"{form}_formulario").get()
            print(self.data)
            controller.show_frame(self, historialfamiliar)
            
                
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
