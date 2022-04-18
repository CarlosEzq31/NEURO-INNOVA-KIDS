import tkinter as tk
from tkinter import *

class lista_pruebas(tk.Frame):
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
                            text = "Pruebas",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.play_icono_grande, anchor = CENTER)
        
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

        # boton atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # boton menu
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
        def iniciar_figuras():
            import os
            import subprocess
            import sys
            path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            python_path = path + "\python-3.76-venv\Scripts\python.exe"
            file = path + "\App-Tkinter\eye_tracker\Prueba_Figuras.py"
            subprocess.Popen(['powershell.exe', f"'{path}\python-3.76-venv\Scripts\Activate.ps1'"], stdout=sys.stdout)
            subprocess.Popen(['powershell.exe', f"& '{python_path}' '{file}'"], stdout=sys.stdout)
            texto_aviso("Cargando pruebas", 20*1000)

        # Botones con lista de pruebas
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.4), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'figuras')
        figuras_boton = tk.Button(self, 
                                    text = "Figuras", 
                                    command = iniciar_figuras,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                    **controller.estilo_rosa)
        figuras_boton.place(relx = 0.7, rely = 0.4, anchor = CENTER)
        controller.animacion_boton(figuras_boton, canvas, 'figuras', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.525), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'senderos')
        senderos_boton = tk.Button(self, 
                                text = "Senderos", 
                                command = lambda: controller.mostrar_pantalla(self, senderos),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        senderos_boton.place(relx = 0.7, rely = 0.525, anchor = CENTER)
        controller.animacion_boton(senderos_boton, canvas, 'senderos', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.65), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'domino')
        domino_boton = tk.Button(self, 
                                text = "Dominó", 
                                # command = lambda: controller.mostrar_pantalla(self,test_page)
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        domino_boton.place(relx = 0.7, rely = 0.65, anchor = CENTER)
        controller.animacion_boton(domino_boton, canvas, 'domino', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.775), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'colores')
        colores_boton = tk.Button(self, 
                                text = "Colores de Stroop", 
                                # command = lambda: controller.mostrar_pantalla(self,test_page)
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        colores_boton.place(relx = 0.7, rely = 0.775, anchor = CENTER)
        controller.animacion_boton(colores_boton, canvas, 'colores', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.9), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'cubos')
        cubos_boton = tk.Button(self, 
                                text = "Cubos de Kohs", 
                                # command = lambda: controller.mostrar_pantalla(self,test_page)
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        cubos_boton.place(relx = 0.7, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(cubos_boton, canvas, 'cubos', tamaño = 'grande')
        
        # Funcion que pone un texto en pantalla
        def texto_aviso(texto, tiempo = 3000,canvas = canvas, controller = controller):
            texto_error = canvas.create_text(int(screenwidth*0.5),int(screenheight*0.25), 
                            text = texto,
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
                            anchor = CENTER)
            controller.after(tiempo,lambda: canvas.delete(texto_error))
        
class figuras_superpuestas(tk.Frame):
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
        
        # colocamos el titulo de la pantalla
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Prueba de las figuras\nsuperpuestas",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1.2)),
                            anchor = NW)
        
        # colocamos el texto con las instrucciones
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.75), 
                            text = "en curso",
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
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

        # boton atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # boton menu
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
class senderos(tk.Frame):
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
        
        # colocamos el titulo de la pantalla
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Prueba de senderos",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1.2)),
                            anchor = NW)
        
        # colocamos el texto con las instrucciones
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.6), 
                            text = "Une los números haciendo click de\nforma consecutiva empezando en el\nnúmero que está indicado como\ninicio y terminando en el número \nmarcado como fin.",
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
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

        # boton atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # boton menu
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')