import tkinter as tk
from tkinter import *
from functools import partial

class escolaridad(Frame):
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
                            text = "Escolaridad",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['¿Asiste el niño a la escuela?', '¿Por qué no asiste?', 'Educación Bilingue', 'Segunda Lengua', 'Edad de Inicio']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['¿Por qué no asiste?', 'Segunda Lengua', 'Edad de Inicio']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad2)
            
                    
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
        

class escolaridad2(Frame):
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
                            text = "Escolaridad (Problemas específicos)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Lectura', 'Escritura', 'Cálculo', 'Lenguaje', 'Hiperactvidad', 'Atención', 'Otros']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Otros']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad3)
            
                    
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
        
class escolaridad3(Frame):
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
                            text = "Escolaridad (Guardería)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Guardería', 'Edad de ingreso', '¿Cuántos años?']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad de ingreso', '¿Cuántos años?']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad4)
            
                    
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
        
class escolaridad4(Frame):
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
                            text = "Escolaridad (Jardín de Niños)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Jardín de niños', 'Edad de ingreso', '¿Cuántos años?', 'Rendimiento Bueno', 'Rendimiento Malo', 'Rendimiento Regular']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad de ingreso', '¿Cuántos años?']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad5)
            
                    
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
        
# Primaria
class escolaridad5(Frame):
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
                            text = "Escolaridad (Primaría)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Edad de ingreso', '¿Cuántos años?', 'Rendimiento', 'Grados repetidos', 'Clases Particulares', 'Edad o grado escolar', 'Materias', 'Terapias de apoyo']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad de ingreso', 'Rendimiento', '¿Cuántos años?', 'Grados repetidos', 'Edad o grado escolar', 'Materias']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad6)
            
                    
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

class escolaridad6(Frame):
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
                            text = "Escolaridad (Primaría)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Edad o grado escolar', '¿Qué tipo?', '¿Por cuánto tiempo?', 'Problemas específicos']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad o grado escolar', '¿Qué tipo?', '¿Por cuánto tiempo?', 'Problemas específicos']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad7)
            
                    
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
        
# Secundaria
class escolaridad7(Frame):
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
                            text = "Escolaridad (Secundaría)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Edad de ingreso', '¿Cuántos años?', 'Rendimiento', 'Grados repetidos', 'Clases Particulares', 'Edad o grado escolar', 'Materias', 'Terapias de apoyo']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad de ingreso', 'Rendimiento', '¿Cuántos años?', 'Grados repetidos', 'Edad o grado escolar', 'Materias']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad8)
            
                    
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

class escolaridad8(Frame):
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
                            text = "Escolaridad (Secundaría)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Edad o grado escolar', '¿Qué tipo?', '¿Por cuánto tiempo?', 'Problemas específicos']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad o grado escolar', '¿Qué tipo?', '¿Por cuánto tiempo?', 'Problemas específicos']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad9)
            
                    
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
 
# Preparatoria
class escolaridad9(Frame):
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
                            text = "Escolaridad (Preparatoría)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Edad de ingreso', '¿Cuántos años?', 'Rendimiento', 'Grados repetidos', 'Clases Particulares', 'Edad y semestre', 'Materias', 'Terapias de apoyo']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad de ingreso', 'Rendimiento', '¿Cuántos años?', 'Grados repetidos', 'Edad y semestre', 'Materias']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad10)
            
                    
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

class escolaridad10(Frame):
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
                            text = "Escolaridad (Preparatoria)",
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
            if valor == True:
                self.data[boton] = True
                self.botones.get(f'{boton}_si').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion_rellena)
                self.botones.get(f'{boton}_no').config(bg = 'white')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion)
            else:
                self.data[boton] = False
                self.botones.get(f'{boton}_si').config(bg = 'white')
                canvas.itemconfig(f'{boton}_si', image = controller.barra_seleccion)
                self.botones.get(f'{boton}_no').config(bg = '#f6ddeb')
                canvas.itemconfig(f'{boton}_no', image = controller.barra_seleccion_rellena)
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Edad y semestre', '¿Qué tipo?', '¿Por cuánto tiempo?', 'Problemas específicos']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,
                                  text = f"{form}",
                                  font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                  **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
            if form in ['Edad y semestre', '¿Qué tipo?', '¿Por cuánto tiempo?', 'Problemas específicos']:
                    canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                    forms[f"{form}_formulario"] = tk.Entry(self,
                                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                                        borderwidth = 0, 
                                                        highlightthickness = 0,
                                                        bg = 'white')
                    forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                # Boton opción si
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_si")
                self.botones[f'{tag}_si'] = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, True))
                self.botones.get(f'{tag}_si').place(relx = 0.725, rely = h, anchor = CENTER)
                # Boton opción no
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER, tags = f"{tag}_no")
                self.botones[f'{tag}_no'] = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                                                highlightthickness = 0, padx = 0, pady = 0,
                                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                                command = partial(seleccion, tag, False))
                self.botones.get(f'{tag}_no').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad11)
            
                    
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

# Aptitudes e intereses
class escolaridad11(tk.Frame):
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
                            text = "Escolaridad (Aptitudes e intereses)",
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
        label = ['Lectura', 'Escritura', 'Matemáticas', 'Deportes', 'Dibujo', 'Ciencias', 'Ciencias Sociales']
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
            # Boton opción Mayor desempeño
            canvas.create_image(int(screenwidth*0.575), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_mayor")
            self.botones[f'{tag}_mayor'] = Button(self,text = 'Mayor d.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 1))
            self.botones.get(f'{tag}_mayor').place(relx = 0.575, rely = h, anchor = CENTER)
            # Boton opción algunas veces
            canvas.create_image(int(screenwidth*0.65), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_menor")
            self.botones[f'{tag}_menor'] = Button(self,text = 'Menor d.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 2))
            self.botones.get(f'{tag}_menor').place(relx = 0.65, rely = h, anchor = CENTER)
            # Boton opción Muchas veces
            canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_preferencia")
            self.botones[f'{tag}_preferencia'] = Button(self,text = 'Prefer.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 3))
            self.botones.get(f'{tag}_preferencia').place(relx = 0.725, rely = h, anchor = CENTER)
            # Boton opción siempre
            canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_no_preferencia")
            self.botones[f'{tag}_no_preferencia'] = Button(self,text = 'No pref.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 4))
            self.botones.get(f'{tag}_no_preferencia').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            controller.mostrar_pantalla(self, escolaridad12)
            
                    
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
        
class escolaridad12(tk.Frame):
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
                            text = "Escolaridad (Aptitudes e intereses)",
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
        label = ['Música', 'Otras']
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
            # Boton opción Mayor desempeño
            canvas.create_image(int(screenwidth*0.575), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_mayor")
            self.botones[f'{tag}_mayor'] = Button(self,text = 'Mayor d.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 1))
            self.botones.get(f'{tag}_mayor').place(relx = 0.575, rely = h, anchor = CENTER)
            # Boton opción algunas veces
            canvas.create_image(int(screenwidth*0.65), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_menor")
            self.botones[f'{tag}_menor'] = Button(self,text = 'Menor d.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 2))
            self.botones.get(f'{tag}_menor').place(relx = 0.65, rely = h, anchor = CENTER)
            # Boton opción Muchas veces
            canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_preferencia")
            self.botones[f'{tag}_preferencia'] = Button(self,text = 'Prefer.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 3))
            self.botones.get(f'{tag}_preferencia').place(relx = 0.725, rely = h, anchor = CENTER)
            # Boton opción siempre
            canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                image = controller.barra_seleccion,
                                anchor = CENTER, tags = f"{tag}_no_preferencia")
            self.botones[f'{tag}_no_preferencia'] = Button(self,text = 'No pref.', borderwidth = 0, bg = 'white',
                                            highlightthickness = 0, padx = 0, pady = 0,
                                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                            command = partial(seleccion, tag, 4))
            self.botones.get(f'{tag}_no_preferencia').place(relx = 0.8, rely = h, anchor = CENTER)
            h += 0.075
                
        def printData():
            print(self.data)
            # controller.mostrar_pantalla(self, comportamiento12)
            
                    
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