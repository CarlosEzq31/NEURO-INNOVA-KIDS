# importamos las librerias necesarias
import tkinter as tk
import math
import textwrap
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


        # Botones con lista de pruebas
        texto_figuras = "Se le mostrará una serie de dibujos sobrepuestos y otro grupo de dibujos que se hallan separados, el niño tendrá que seleccionar cuáles figuras se repiten en ambos grupos"
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.4), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'figuras')
        figuras_boton = tk.Button(self, 
                                    text = "Figuras", 
                                    command = lambda: self.mensaje_informacion(controller, screenwidth, screenheight, 
                                                                               'Figuras Información', textwrap.fill(texto_figuras, width = 50),
                                                                               controller.figuras_img),
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                    **controller.estilo_rosa)
        figuras_boton.place(relx = 0.7, rely = 0.4, anchor = CENTER)
        controller.animacion_boton(figuras_boton, canvas, 'figuras', tamaño = 'grande')

        texto_cubos = "Se le mostrará una imagen de un cubo desplegados con figuras en cada uno de los lados, después una serie de imágenes de cubos en donde está el cubo de la imagen anterior. El paciente tendrá que escoger el cubo de la imagen anterior en la serie anterior"
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.525), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'senderos')
        cubos_boton = tk.Button(self, 
                                text = "Cubos de Kohs", 
                                command = lambda: self.mensaje_informacion(controller, screenwidth, screenheight, 
                                                                           'Senderos Información', textwrap.fill(texto_cubos, width = 50),
                                                                           controller.cubos_img),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        cubos_boton.place(relx = 0.7, rely = 0.525, anchor = CENTER)
        controller.animacion_boton(cubos_boton, canvas, 'senderos', tamaño = 'grande')


        texto_domino = "Se dará una secuencia numérica con ayuda de fichas de dominó y se le dará una serie de posibles respuestas  para seguir con la secuencia. El niño tendrá que escoger la respuesta correcta"
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.65), image = controller.boton_rosa_grande, anchor = CENTER, tags = 'domino')
        domino_boton = tk.Button(self, 
                                text = "Dominó", 
                                command = lambda: self.mensaje_informacion(controller, screenwidth, screenheight, 
                                                                           'Senderos Información', textwrap.fill(texto_domino, width = 50),
                                                                           controller.domino_img),
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1.45)), 
                                **controller.estilo_rosa)
        domino_boton.place(relx = 0.7, rely = 0.65, anchor = CENTER)
        controller.animacion_boton(domino_boton, canvas, 'domino', tamaño = 'grande')
    
    def mensaje_informacion(self, controller,width: int, height: int, titulo: str, texto_: str, imagen):
        mensaje_ventana = Splash(self, controller,width, height, titulo, texto_, imagen)
        
        
class Splash(tk.Toplevel):
    def __init__(self, parent, controller,screenwidth, screenheight, titulo, texto_, imagen):
        # Creamos la pantalla que muestra información de la prueba
        tk.Toplevel.__init__(self, parent)
        button_font_size = controller.boton_tamanio
        self.ratio = 0.75
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.width, self.height = screenwidth*self.ratio, screenheight*self.ratio
        
        # Definimos el tamaño
        self.geometry(f"{int(self.width)}x{int(self.height)}+{int((self.screenwidth/2) - (self.width/2))}+{int((self.screenheight/2) - (self.height/2))}")
        canvas = tk.Canvas(self, width = self.width , height = self.height, bg = 'white')
        canvas.pack(side = "top", fill = "both", expand = True)
        
        # Colocamos el fondo de la pantalla
        # canvas.create_image(self.width/2, self.height/2, image = controller.fondo_splash, anchor = CENTER)
        
        # Colocamos el título de la ventana
        self.title(f"{titulo}")
        
        # Cargamos imágenes para el boton de salir
        self.boton_rosa_hover = controller.imagen_redimensionar(f"{controller.path}/src/images/image.png", ratio = 0.00035)
        self.boton_rosa = controller.imagen_redimensionar(f"{controller.path}/src/images/Boton rosa 12.png", ratio = 0.00035)
        
        # Colcamos la primer imagen
        canvas.create_image(int(self.width*0.8),int(self.height*0.1), image = self.boton_rosa, anchor = CENTER, tags = 'salir')
        cerrar_boton = Button(self, text = "Cerrar",
                              command = lambda: self.close(),
                              font = ('Mukta Malar ExtraLight', int(button_font_size*1.)),
                              **controller.estilo_rosa)
        cerrar_boton.place(relx = 0.8, rely = 0.1, anchor = CENTER)
        self.animacion_boton(cerrar_boton, canvas)
        
        # Colocamos el texto de la información de la prueba
        canvas.create_text(int(self.width*0.45),int(self.height*0.2), 
                            text = texto_,
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
                            anchor = CENTER)
        
        # Colocamos el screenshot de la prueba
        canvas.create_image(int(screenwidth*0.45),int(screenheight*0.45),
                            image = imagen,
                            anchor = CENTER)
        
        # Atributos
        self.attributes('-topmost', 'true')
        self.grab_set()
        self.wm_overrideredirect(True)
        self.animacion_entrada()

    # funcion para cerrar la ventana emergente y habilitar click en la ventana principal
    def close(self):
        self.animacion_salida()
        
    def animacion_entrada(self, t = 0):
        y = self.height*2*math.exp(-0.018*t)
        s = f"{int(self.width)}x{int(self.height)}+{int((self.screenwidth/2) - (self.width/2))}+" + str(int(y))
        self.geometry(s)
        self.deiconify()

        if y > int((self.screenheight/2) - (self.height/2)):
            self.after(1, lambda y = y: self.animacion_entrada(t + 1))
        else:
            # self.geometry(f"{int(width)}x{int(height)}+{int((screenwidth/2) - (width/2))}+{int((screenheight/2) - (height/2))}")
            self.geometry(f"{int(self.width)}x{int(self.height)}+{int((self.screenwidth/2) - (self.width/2))}+{int((self.screenheight/2) - (self.height/2))}")
            
    def animacion_salida(self, t = 0):
        y = (self.height*2 - self.height*2*math.exp(-0.028*t)) + self.height/2
        s = f"{int(self.width)}x{int(self.height)}+{int((self.screenwidth/2) - (self.width/2))}+" + str(int(y))
        self.geometry(s)
        self.deiconify()

        if y >= self.height/2 and y < self.height*2:
            self.after(1, lambda y = y: self.animacion_salida(t + 1))
        else: 
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