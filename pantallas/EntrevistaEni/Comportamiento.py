import tkinter as tk
from tkinter import *
from functools import partial
from functions.sql_metodos import comportamiento_sql
from pantallas.EntrevistaEni.Comportamiento import *
from pantallas.EntrevistaEni.MetodoDisciplina import disciplina

class comportamiento(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (actividad)",
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
                self.data[boton] = 4
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
        label = ['Hipoactivo', 'Hiperactivo', 'Destructivo', 'Agresivo']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                global data 
                data = self.data
                controller.mostrar_pantalla(self, comportamiento2)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

class comportamiento2(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (atención)",
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
                self.data[boton] = 4
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
        label = ['Constante', 'Corta', 'Nula', 'Variable']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento3)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class comportamiento3(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Crísis Coléricas)",
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
                self.data[boton] = 4
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
        label = ['Berrinches', 'Arroja cosas al enojarse', 'Arremete verbalemente', 'Irascible']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento4)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class comportamiento4(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Adaptación)",
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
                self.data[boton] = 4
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
        label = ['Se separa de los padres', 'Se adecua a la situación', 'Reacciones catastróficas']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento5)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class comportamiento5(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Labilidad emocional)",
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
                self.data[boton] = 4
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
        label = ['Llora muy facilmente', 'Pasa del llanto a la risa', 'Se emociona facilmente']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento6)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

class comportamiento6(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Relaciones familiares)",
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
                self.data[boton] = 4
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
        label = ['Difícil relación con papá', 'Difícil relación con mamá', 'Difícil relación con herm.']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento7)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class comportamiento7(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Sueño)",
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
                self.data[boton] = 4
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
        label = ['Sonambulismo', 'Promedio de horas de sueño','Duerme siesta', 'Pesadillas', 'Dificultad para conciliar sueño', 'Dificil despertar', 'Sueño continuo']
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
            if form in ['Promedio de horas de sueño']:
                canvas.create_image(int(screenwidth*0.675), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                forms[f"{form}_formulario"] = tk.Entry(self,
                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                        borderwidth = 0, 
                                        highlightthickness = 0,
                                        bg = 'white')
                forms.get(f"{form}_formulario").place(relx = 0.675, rely = h, anchor = CENTER)
            else:
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
            for form in label:
                if form == 'Promedio de horas de sueño':
                    tag = form.replace(' ','_').lower()
                    self.data[f"{tag}"] = forms.get(f"{form}_formulario").get()
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento8)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class comportamiento8(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Comportamiento a la hora de comer)",
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
                self.data[boton] = 4
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
        label = ['Permanece sentado', 'Juega con los cubiertos', 'Derrama los alimentos', 'Come sin distracción']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento9)
            
                    
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
        
class comportamiento9(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Hábitos alimenticios)",
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
                self.data[boton] = 4
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
        label = ['¿Comidas al día?','¿Es selectivo con los alimentos?']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento10)
            
                    
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
        
class comportamiento10(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Tiempo libre)",
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
                self.data[boton] = 4
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
        label = ['TV', 'Videojuegos', 'Computadora', 'Juego al aire libre', 'Juego de fantasía', 'Lectura', 'Juegos colectivos', 'Juegos de construcción']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento11)
            
                    
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
        
class comportamiento11(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Socialización)",
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
                self.data[boton] = 4
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
        label = ['Retraído', 'Abierto', 'Aislado', 'Facilidad para hacer amigos', 'Amigos de su edad', 'Amigos mayores', 'Amigos menores', 'Otros amigos']
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
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                controller.mostrar_pantalla(self, comportamiento12)
            
                    
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
        
class comportamiento12(tk.Frame):
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
        canvas.create_image(int(screenwidth*0.1),int(screenheight*0.15),
                            image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        canvas.create_text(int(screenwidth*0.15),int(screenheight*0.25), 
                            text = "Comportamiento (Inteligencia)",
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
                self.botones.get(f'{boton}_esperada').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_esperada', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_mayor').config(bg = 'white')
                canvas.itemconfig(f'{boton}_mayor', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_menor').config(bg = 'white')
                canvas.itemconfig(f'{boton}_menor', image = controller.barra_seleccion)
            elif valor == 2:
                self.data[boton] = 2
                self.botones.get(f'{boton}_esperada').config(bg = 'white')
                canvas.itemconfig(f'{boton}_esperada', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_mayor').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_mayor', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_menor').config(bg = 'white')
                canvas.itemconfig(f'{boton}_menor', image = controller.barra_seleccion)
            elif valor == 3:
                self.data[boton] = 3
                self.botones.get(f'{boton}_esperada').config(bg = 'white')
                canvas.itemconfig(f'{boton}_esperada', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_mayor').config(bg = 'white')
                canvas.itemconfig(f'{boton}_mayor', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_menor').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_menor', image = controller.barra_seleccion_rellena)
                
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Inteligencia']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.45),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form} para la edad",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.45, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            # Boton opción Nunca
            canvas.create_image(int(screenwidth*0.575), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_esperada")
            self.botones[f'{tag}_esperada'] = Button(self,text = 'Esperada', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 1))
            self.botones.get(f'{tag}_esperada').place(relx = 0.575, rely = h, anchor = CENTER)
            # Boton opción algunas veces
            canvas.create_image(int(screenwidth*0.65), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_mayor")
            self.botones[f'{tag}_mayor'] = Button(self,text = 'Mayor', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 2))
            self.botones.get(f'{tag}_mayor').place(relx = 0.65, rely = h, anchor = CENTER)
            # Boton opción Muchas veces
            canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_menor")
            self.botones[f'{tag}_menor'] = Button(self,text = 'Menor', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 3))
            self.botones.get(f'{tag}_menor').place(relx = 0.725, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            # print(self.data)
            if controller.comprobar_formularios(self.data, canvas):
                data.update(self.data)
                # print(data)
                comportamiento_sql(data, controller.id)
                controller.mostrar_pantalla(self, disciplina)
            
                    
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