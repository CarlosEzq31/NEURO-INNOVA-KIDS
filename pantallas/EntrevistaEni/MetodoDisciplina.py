import tkinter as tk
from tkinter import *
from functools import partial
from functions.sql_metodos import *
from pantallas.EntrevistaEni.Escolaridad import *

class disciplina(Frame):
    def __init__(self, parent, controller):
        
        # Obtenemos el tamaño de la pantalla
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Método de disciplina",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), 
                            image = controller.registro_icono_grande, anchor = CENTER)
        
        # Boton de instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15),
                            image = controller.boton_verde, anchor = CENTER,
                            tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15),
                            image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda : controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                        **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')

        # Boton de atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9),
                            image = controller.boton_verde, anchor = CENTER,
                            tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15),
                            image = controller.boton_verde, anchor = CENTER,
                            tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
        def seleccion(boton, valor):
            if valor == 1:
                self.data[boton] = 1
                self.botones.get(f'{boton}_nunca').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_nunca', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_algunas').config(bg = 'white')
                canvas.itemconfig(f'{boton}_algunas', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_muchas').config(bg = 'white')
                canvas.itemconfig(f'{boton}_muchas', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_siempre').config(bg = 'white')
                canvas.itemconfig(f'{boton}_siempre', image = controller.barra_seleccion)
            elif valor == 2:
                self.data[boton] = 2
                self.botones.get(f'{boton}_nunca').config(bg = 'white')
                canvas.itemconfig(f'{boton}_nunca', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_algunas').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_algunas', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_muchas').config(bg = 'white')
                canvas.itemconfig(f'{boton}_muchas', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_siempre').config(bg = 'white')
                canvas.itemconfig(f'{boton}_siempre', image = controller.barra_seleccion)
            elif valor == 3:
                self.data[boton] = 3
                self.botones.get(f'{boton}_nunca').config(bg = 'white')
                canvas.itemconfig(f'{boton}_nunca', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_algunas').config(bg = 'white')
                canvas.itemconfig(f'{boton}_algunas', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_muchas').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_muchas', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_siempre').config(bg = 'white')
                canvas.itemconfig(f'{boton}_siempre', image = controller.barra_seleccion)
            elif valor == 4:
                self.data[boton] = 3
                self.botones.get(f'{boton}_nunca').config(bg = 'white')
                canvas.itemconfig(f'{boton}_nunca', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_algunas').config(bg = 'white')
                canvas.itemconfig(f'{boton}_algunas', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_muchas').config(bg = 'white')
                canvas.itemconfig(f'{boton}_muchas', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_siempre').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_siempre', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Regaño', 'Castigo físico', 'Tiempo fuera', 'Premio', 'Convencimiento', 'Otros']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.45),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.45, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            # Boton opción Nunca
            canvas.create_image(int(screenwidth*0.575), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_nunca")
            self.botones[f'{tag}_nunca'] = Button(self,text = 'Nunca', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 1))
            self.botones.get(f'{tag}_nunca').place(relx = 0.575, rely = h, anchor = CENTER)
            # Boton opción algunas veces
            canvas.create_image(int(screenwidth*0.65), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_algunas")
            self.botones[f'{tag}_algunas'] = Button(self,text = 'Algunas v.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 2))
            self.botones.get(f'{tag}_algunas').place(relx = 0.65, rely = h, anchor = CENTER)
            # Boton opción Muchas veces
            canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_muchas")
            self.botones[f'{tag}_muchas'] = Button(self,text = 'Muchas v.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 3))
            self.botones.get(f'{tag}_muchas').place(relx = 0.725, rely = h, anchor = CENTER)
            # Boton opción siempre
            canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_siempre")
            self.botones[f'{tag}_siempre'] = Button(self,text = 'Siempre', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 4))
            self.botones.get(f'{tag}_siempre').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            if controller.comprobar_formularios(self.data, canvas):
                metodos_disciplina_sql(self.data, controller.id)
                controller.mostrar_pantalla(self, escolaridad)
        
        
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), 
                            image = controller.boton_verde, tags = 'siguiente',
                            anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')