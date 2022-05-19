import tkinter as tk
from tkinter import *


bg_primary_buttons = "#f6ddeb"
bg_secondary_buttons = "#e8eab9"


class instrucciones(tk.Frame):
    def __init__(self, parent, controller):

        screenwidth = controller.size['width']
        screenheight = controller.size['height']

        # Definimos el tamaño de la fuente
        button_font_size = controller.boton_tamanio
        
        # Incializamos el frame
        tk.Frame.__init__(self, parent)
        
        # Definimos el tamaño de la fuente
        button_font_size = controller.boton_tamanio
        
        # creamos un lienzo
        canvas = tk.Canvas(self, width = screenwidth, height = screenheight, bg = 'white')
        canvas.pack(side = "top", fill = "both", expand = True)

        # colocamos el fondo de la pantalla
        canvas.create_image(0, 0, image = controller.background,
                            anchor = NW)

        # colocar el logo
        canvas.create_image(int(screenwidth*0.1), int(screenheight*0.15),
                            image = controller.loguito,
                            anchor = CENTER)

        #colocamos el titulo de la pantalla
        canvas.create_text(int(screenwidth*0.15), int(screenheight*0.25), 
                            text = "Instrucciones", 
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)), 
                            anchor = NW)
        
        # colocamos el botón de atrás
        canvas.create_image(int(screenwidth*0.15), int(screenheight*0.9), 
                            image = controller.boton_verde, 
                            anchor = CENTER,
                            tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(), 
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')

        # Instrucción 1 
        canvas.create_text(int(screenwidth*0.35), int(screenheight*0.375), 
                           text = '1', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*4.0)), 
                           tags = '1', 
                           anchor = CENTER)

        canvas.create_text(int(screenwidth*0.45), int(screenheight*0.39), 
                           text = 'Mantén la vista directamente \n    en el centro de la pantalla', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                           tags = 'vista', 
                           anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.7), int(screenheight*0.325), 
                            image = controller.gif_instruccion1_a[0], 
                            anchor = CENTER, 
                            tags = 'gif1_1')
        canvas.create_image(int(screenwidth*0.85), int(screenheight*0.325), 
                            image = controller.gif_instruccion1_b[0], 
                            anchor = CENTER, 
                            tags = 'gif1_2')


        # Instrucción 2
        canvas.create_text(int(screenwidth*0.35), int(screenheight*0.550), 
                           text = '2', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*4.0)), 
                           tags = '2', 
                           anchor = CENTER)

        canvas.create_text(int(screenwidth*0.45), int(screenheight*0.555), 
                           text = 'Trata de parpadear \n  lo menos posible ', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                           tags = 'parpadeo', 
                           anchor = CENTER)

        canvas.create_image(int(screenwidth*0.7), int(screenheight*0.555), 
                            image = controller.gif_instruccion1_a[0], 
                            anchor = CENTER, 
                            tags = 'gif2_1')
        canvas.create_image(int(screenwidth*0.85), int(screenheight*0.555), 
                            image = controller.gif_instruccion2_b[0], 
                            anchor = CENTER, 
                            tags = 'gif1_2')


        # Instrucción 3
        canvas.create_text(int(screenwidth*0.35), int(screenheight*0.785), 
                           text = '3', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*4.0)), 
                           tags = '3', 
                           anchor = CENTER)

        canvas.create_text(int(screenwidth*0.46), int(screenheight*0.8), 
                           text = 'No hables ni muevas la lengua o\n   movimiento con el rostro', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                           tags = 'movimiento', 
                           anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.7), int(screenheight*0.8), 
                            image = controller.gif_instruccion1_a[0], 
                            anchor = CENTER, 
                            tags = 'gif3_1')
        canvas.create_image(int(screenwidth*0.85), int(screenheight*0.8), 
                            image = controller.gif_instruccion3_b[0], 
                            anchor = CENTER, 
                            tags = 'gif3_2')
     
        
        # función para animars gif
        def animacion_gif(e):  
            self.ind1a = 0
            self.ind1b = 0
            self.ind2a = 0
            self.ind2b = 0
            self.ind3a = 0
            self.ind3b = 0
            self.after(100, actualizar, self.ind1a, self.ind1b, self.ind2a, self.ind2b, self.ind3a, self.ind3a)
            
        def actualizar(ind1a, ind1b, ind2a, ind2b, ind3a, ind3b):
            frame1a = controller.gif_instruccion1_a[ind1a]
            frame1b = controller.gif_instruccion1_b[ind1b]
            frame2a = controller.gif_instruccion1_a[ind2a]
            frame2b = controller.gif_instruccion2_b[ind2b]
            frame3a = controller.gif_instruccion1_a[ind3a]
            frame3b = controller.gif_instruccion3_b[ind3b]
            self.ind1a += 1
            self.ind1b += 1
            self.ind2a += 1
            self.ind2b += 1
            self.ind3a += 1
            self.ind3b += 1
            if self.ind1a == len(controller.gif_instruccion1_a):
                self.ind1a = 0
            if self.ind1b == len(controller.gif_instruccion1_b):
                self.ind1b = 0
            if self.ind2a == len(controller.gif_instruccion1_a):
                self.ind2a = 0
            if self.ind2b == len(controller.gif_instruccion2_b):
                self.ind2b = 0
            if self.ind3a == len(controller.gif_instruccion1_a):
                self.ind3a = 0
            if self.ind3b == len(controller.gif_instruccion3_b):
                self.ind3b = 0
            canvas.itemconfig('gif1_1', image = frame1a)
            canvas.itemconfig('gif1_2', image = frame1b)
            canvas.itemconfig('gif2_1', image = frame2a)
            canvas.itemconfig('gif2_2', image = frame2b)
            canvas.itemconfig('gif3_1', image = frame3a)
            canvas.itemconfig('gif3_2', image = frame3b)
            self.after(100, actualizar, self.ind1a, self.ind1b, self.ind2a, self.ind2b, self.ind3a, self.ind3a)
            
        def detener_gif(e):
            canvas.itemconfig('gif1_1', image = controller.gif_instruccion1_a[0])
            canvas.itemconfig('gif1_2', image = controller.gif_instruccion1_b[0])
            canvas.itemconfig('gif2_1', image = controller.gif_instruccion1_a[0])
            canvas.itemconfig('gif2_2', image = controller.gif_instruccion2_b[0])
            canvas.itemconfig('gif3_1', image = controller.gif_instruccion1_a[0])
            canvas.itemconfig('gif3_2', image = controller.gif_instruccion3_b[0])
            self.ind = 0
            
            
        self.bind("<Enter>", animacion_gif)
        self.bind("<Leave>", detener_gif)