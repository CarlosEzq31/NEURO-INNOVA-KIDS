# importamos las librerias necesarias
import tkinter as tk
from tkinter import *

# estableciendo colores
bg_primary_buttons = "#f6ddeb"
bg_secondary_buttons = "#e8eab9"

# pantalla de información básica
class info_pruebas(tk.Frame):
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


        # Botones con lista de pruebas
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.4), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'figuras')
        figuras_boton = tk.Button(self, 
                                    text = "Figuras", 
                                    command = lambda: self.mensaje_informacion(controller, screenwidth, screenheight, 'Figuras Información','ESO es una prueba'),
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                    **controller.estilo_rosa)
        figuras_boton.place(relx = 0.7, rely = 0.4, anchor = CENTER)
        controller.animacion_boton(figuras_boton, canvas, 'figuras', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.525), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'senderos')
        senderos_boton = tk.Button(self, 
                                text = "Senderos", 
                                command = lambda: self.mensaje_informacion(controller, screenwidth, screenheight, 'Senderos Información','En la prueba...'),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        senderos_boton.place(relx = 0.7, rely = 0.525, anchor = CENTER)
        controller.animacion_boton(senderos_boton, canvas, 'senderos', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.65), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'domino')
        domino_boton = tk.Button(self, 
                                text = "Dominó", 
                                # command = lambda: controller.show_frame(self,test_page)
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        domino_boton.place(relx = 0.7, rely = 0.65, anchor = CENTER)
        controller.animacion_boton(domino_boton, canvas, 'domino', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.775), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'colores')
        colores_boton = tk.Button(self, 
                                text = "Colores de Stroop", 
                                # command = lambda: controller.show_frame(self,test_page)
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        colores_boton.place(relx = 0.7, rely = 0.775, anchor = CENTER)
        controller.animacion_boton(colores_boton, canvas, 'colores', tamaño = 'grande')

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.9), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'cubos')
        cubos_boton = tk.Button(self, 
                                text = "Cubos de Kohs", 
                                # command = lambda: controller.show_frame(self,test_page)
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        cubos_boton.place(relx = 0.7, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(cubos_boton, canvas, 'cubos', tamaño = 'grande')
    
    def mensaje_informacion(self, controller,width: int, height: int, titulo: str, texto_: str):
        mensaje_ventana = Splash(self, controller,width, height, titulo, texto_)
        
        
class Splash(tk.Toplevel):
    def __init__(self, parent, controller,screenwidth, screenheight, titulo, texto_):
        # Creamos la pantalla que muestra información de la prueba
        tk.Toplevel.__init__(self, parent)
        button_font_size = controller.boton_tamanio
        width, height = screenwidth*0.5, screenheight*0.5
        
        # Definimos el tamaño
        self.geometry(f"{int(width)}x{int(height)}+{int((screenwidth/2) - (width/2))}+{int((screenheight/2) - (height/2))}")
        canvas = tk.Canvas(self, width = width , height = height, bg = 'white')
        canvas.pack(side = "top", fill = "both", expand = True)
        
        # Colocamos el fondo de la pantalla
        canvas.create_image(0, 0, image = controller.fondo_splash, anchor = NW)
        
        # Colocamos el título de la ventana
        self.title(f"{titulo}")
        
        # Cargamos imágenes para el boton de salir
        self.boton_rosa_hover = controller.get_image_resized(f"{controller.path}/src/images/image.png", ratio = 0.00035)
        self.boton_rosa = controller.get_image_resized(f"{controller.path}/src/images/Boton rosa 12.png", ratio = 0.00035)
        
        # Colcamos la primer imagen
        canvas.create_image(int(width*0.8),int(height*0.1), image = self.boton_rosa, anchor = CENTER, tags = 'salir')
        cerrar_boton = Button(self, text = "Cerrar",
                              command = lambda: self.close(),
                              font = ('Mukta Malar ExtraLight', int(button_font_size*1.)),
                              **controller.estilo_rosa)
        cerrar_boton.place(relx = 0.8, rely = 0.1, anchor = CENTER)
        self.animacion_boton(cerrar_boton, canvas)
    
        canvas.create_text(int(width*0.5),int(height*0.5), 
                            text = texto_,
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
                            anchor = CENTER)
        self.attributes('-topmost', 'true')
        self.grab_set()
        self.wm_overrideredirect(True)

    def close(self):
        self.grab_release()
        self.destroy()
    
    # función para animar los botones
    def animacion_boton(self, button, canvas, tag = 'salir'):
        hightbg_hover = "#f692ca"
        hightbg_normal = "#f6ddeb"
        image_hover = self.boton_rosa_hover
        image_normal = self.boton_rosa
            
        def on_enter(e):
            button.config(highlightbackground = hightbg_hover, background = hightbg_hover, fg = 'white')
            canvas.itemconfig(tag, image = image_hover)

        def on_leave(e):
            button.config(highlightbackground = hightbg_normal,  background = hightbg_normal, fg = 'black')
            canvas.itemconfig(tag, image = image_normal)

        def on_click(e):
            button.config( fg = 'white')
            
        def on_unclick(e):
            button.config( fg = 'black')
        
        def on_enter_canvas(e):
            button.config(highlightbackground = hightbg_hover, background = hightbg_hover)
            canvas.itemconfig(tag, image = image_hover)

        def on_leave_canvas(e):
            button.config(highlightbackground = hightbg_normal, background = hightbg_normal)
            canvas.itemconfig(tag, image = image_normal)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_click)
        button.bind("<ButtonRelease-1>", on_unclick)
        canvas.tag_bind(tag, '<Enter>', on_enter_canvas)
        canvas.tag_bind(tag, "<Leave>", on_leave_canvas)