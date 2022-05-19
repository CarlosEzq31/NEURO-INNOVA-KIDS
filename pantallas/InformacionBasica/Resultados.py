# importamos las librerias necesarias
import tkinter as tk
import textwrap
from tkinter import *

# estableciendo colores
bg_primary_buttons = "#f6ddeb"
bg_secondary_buttons = "#e8eab9"

# pantalla de información básica
class resultados(tk.Frame):
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
                            text = "Seguidor ocular",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.signo_iterrogacion_grande, anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Resultados", 
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
        
        # Texto de información
        texto_info = "Una vez realizada las pruebas el programa dará la opción para imprimir, descargar y acceder a los resultados. Éstos serán una serie de gráficas que revelan el desempeño del niño durante las pruebas, ayudarán a medir el nivel de atención y realizar el seguimiento de cualquier situación de estrés o trauma que pueda tener el paciente. Los datos recopilados serán manejados según lo establecido en la Ley Federal de Protección de Datos Personales en Posesión de los particulares(LFPDPPP) para asegurar que la información sea protegida, tratada de manera legítima, informada y controlada, así mismo se les proporcionará un convenio de confidencialidad y consentimiento para estos fines."
        canvas.create_text(int(screenwidth*0.65),int(screenheight*0.62), 
                           text = textwrap.fill(texto_info, width = 50), 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*1.25)),
                           tags = 'vista',
                           anchor = CENTER)