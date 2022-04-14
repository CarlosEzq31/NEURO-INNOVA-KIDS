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
                            text = "Instrucciones",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        

        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')

        # Instrucción 1 
        canvas.create_text(int(screenwidth*0.35),int(screenheight*0.475), 
                           text = '1', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*4.0)),
                           tags = '1',
                           anchor = CENTER)

        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.480), 
                           text = 'Mantén la vista directamente \n    en el centro de la pantalla', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'vista',
                           anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.475), 
                            image = controller.gifs[0], 
                            anchor = CENTER, 
                            tags = 'gif1')


        # Instrucción 2
        canvas.create_text(int(screenwidth*0.35),int(screenheight*0.610), 
                           text = '2', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*4.0)),
                           tags = '2',
                           anchor = CENTER)

        canvas.create_text(int(screenwidth*0.45),int(screenheight*0.615), 
                           text = 'Trata de parpadear \n  lo menos posible ', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'parpadeo',
                           anchor = CENTER)

        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.6),
                            image = controller.gifs[0],
                            anchor = CENTER,
                            tags = 'gif2')


        # Instrucción 3
        canvas.create_text(int(screenwidth*0.35),int(screenheight*0.745), 
                           text = '3', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size*4.0)),
                           tags = '3',
                           anchor = CENTER)

        canvas.create_text(int(screenwidth*0.46),int(screenheight*0.750), 
                           text = 'No hables ni muevas la lengua o\n   movimiento con el rostro', 
                           font = ('Mukta Malar ExtraLight', int(button_font_size)),
                           tags = 'movimiento',
                           anchor = CENTER)
        
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.725),
                            image = controller.gifs[0],
                            anchor = CENTER,
                            tags = 'gif3')
        
        
        # Funciones para animar gifs
        def animacion_gif(e):  
            self.after(0, actualizar, 0)
            
        def actualizar(ind):
            frame = controller.gifs[ind]
            # frame = frame.zoom(2,2)
            ind += 1
            if ind == len(controller.gifs):
                ind = 0
            canvas.itemconfig('gif1',image = frame)
            canvas.itemconfig('gif2',image = frame)
            canvas.itemconfig('gif3',image = frame)
            self.after(100, actualizar, ind)
            
        self.bind("<Enter>", animacion_gif)