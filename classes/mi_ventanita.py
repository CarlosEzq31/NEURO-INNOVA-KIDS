from tkinter import *
import tkinter as tk, math
from classes.mi_boton import *

class ventana_emergente(tk.Toplevel):
    def __init__(self, parent, controller, ancho, alto, titulo, texto_, imagen):
        self.parent = parent
        self.controller = controller
        self.ancho_pantalla = controller.ancho
        self.alto_pantalla = controller.alto
        self.ancho = ancho * 0.8
        self.alto = alto * 0.8
        self.titulo = titulo
        self.texto_ = texto_
        self.imagen = imagen
        self.controller.boton_tamanio = controller.boton_tamanio
        tk.Toplevel.__init__(self, self.parent)

        # Definimos el tamaño de la ventana
        self.geometry(f"{int(self.ancho)}x{int(self.alto)}+{int((self.ancho_pantalla/2) - (self.alto_pantalla/2))}+{int((self.ancho/2) - (self.alto/2))}")
        
        # Creamos el canvas
        self.canvas = tk.Canvas(self, width = self.ancho, height = self.alto, bg = 'white')
        self.canvas.pack(side = 'top', fill = 'both', expand = True)

        # Colocamos el fondo de la pantalla
        self.canvas.create_image(self.ancho / 2, self.alto / 2, image = controller.fondo_pantalla_carga, anchor = CENTER)

        # Titulo de la pantalla
        self.title(self.titulo)

        # Colocamos la ventana en frente de todas las demás
        self.attributes('-topmost', True)

        # Desactivamos el redimensionamiento de la ventana
        self.resizable(False, False)

        # Texto de la pantalla
        self.texto = self.canvas.create_text(self.ancho * 0.45, self.alto * 0.45, text = self.texto_,
                                            font = ('Mukta Malar ExtraLight', int(self.controller.boton_tamanio)),
                                            anchor = CENTER)

        # Imagen de la pantalla
        self.canvas.create_image(int(self.ancho*0.45),int(self.alto*0.45),
                            image = imagen,
                            anchor = CENTER)

        # Boton de atras
        self.boton_atras = mi_boton(self.canvas, 0.8, 0.1, 'Atrás', 'verde', lambda x: self.animacion_salida())
        
        # Atributos de la ventana
        self.grab_set()
        self.wm_overrideredirect(True)
        self.animacion_entrada()

        
    def animacion_entrada(self, t = 0):
        """Animación de entrada de la ventana"""
        y = self.alto * 2 * math.exp(-0.008*t)
        s = f"{int(self.ancho)}x{int(self.alto)}+{int((self.ancho_pantalla/2) - (self.ancho/2))}+" + str(int(y))
        self.geometry(s)
        self.deiconify()

        if y > int((self.alto_pantalla/2) - (self.alto/2)):
            self.after(1, lambda y = y: self.animacion_entrada(t + 1))
        else:
            self.geometry(f"{int(self.ancho)}x{int(self.alto)}+{int((self.ancho_pantalla/2) - (self.ancho/2))}+{int((self.alto_pantalla/2) - (self.alto/2))}")
        
            
    def animacion_salida(self, t = 0):
        """Animación de salida de la ventana"""
        y = (self.alto * 2 - self.alto * 2 * math.exp(-0.008*t)) + self.alto_pantalla/2
        s = f"{int(self.ancho)}x{int(self.alto)}+{int((self.ancho_pantalla/2) - (self.ancho/2))}+" + str(int(y))
        self.geometry(s)
        self.deiconify()

        if y >= self.alto_pantalla/2 and y < self.alto_pantalla*2:
            self.after(1, lambda y = y: self.animacion_salida(t + 1))
        else: 
            self.grab_release()
            self.destroy()