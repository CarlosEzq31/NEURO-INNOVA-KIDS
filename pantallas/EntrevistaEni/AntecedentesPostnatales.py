import tkinter as tk
from tkinter import *
from functools import partial
from pantallas.EntrevistaEni.Comportamiento import *

# Alimentación
class antecedentes_postnatales(tk.Frame):
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
                            text = "Antecedentes Postnatales",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.registro_icono_grande, anchor = CENTER)
        
        # Boton de instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda : controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                        **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')

        # Boton de atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
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
        label = ['Alimentación Materna', 'Alimentación Artificial','Alimentación Mixta', 'Vómitos', 'Succión']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h), image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self, 
                                text = f"{form}", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
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
            controller.mostrar_pantalla(self, antecedentes_postnatales2)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
# Condiciones durante el primer año
class antecedentes_postnatales2(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
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
        label = ['Actividad del primer año', 'Gateó','Caminó solo', 'Control de esfínteres', 'Habla', 'Balbuceo (edad)']
        h = 0.4
        self.botones = {}
        self.data = {}        
        
        for form in label:
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h), image = controller.boton_rosa, anchor = CENTER)
            form_texto = Label(self, 
                                text = f"{form}", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
            form_texto.place(relx = 0.55, rely = h, anchor = CENTER)
            tag = form.replace(' ','_').lower()
            self.data[tag] = ''
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
            controller.mostrar_pantalla(self, antecedentes_postnatales3)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')        

# Condiciones durante el primer año
class antecedentes_postnatales3(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        label = ['Dijo 3 palabras', 'Unió 2 palabras', 'Construyo frases']
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
            controller.mostrar_pantalla(self, antecedentes_postnatales4)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
                
# Desarrollo actual
class antecedentes_postnatales4(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        label = ['Autosuficiente en', 'Deficiente en', 'Corre', 'Anda en bicicleta', 'Juega', 'Gusto por deportes', 'Escribe', 'Dibuja']
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
            if form in ['Autosuficiente en', 'Deficiente en']:
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
            controller.mostrar_pantalla(self, antecedentes_postnatales5)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

# Desarrollo actual
class antecedentes_postnatales5(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        label = ['Recorta', 'Produce sonidos con la lengua', 'Tartamudea', 'Dificultad de expresión',
                 'Dificultad de comprensión', 'Lengua predominante', 'Lengua Secuandaria']
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
            if form in ['Autosuficiente en', 'Deficiente en', 'Lengua predominante', 'Lengua Secuandaria']:
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
            controller.mostrar_pantalla(self, antecedentes_postnatales6)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

# Antecedentes patológicos
class antecedentes_postnatales6(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        label = ['Traumatismos', 'Fecha', 'Duración', 'Cirugías', 'Motivo', 'Convulsiones', 'Edad de Inicio']
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
            if form in ['Fecha', 'Duración', 'Motivo', 'Edad de Inicio']:
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
            controller.mostrar_pantalla(self, antecedentes_postnatales7)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class antecedentes_postnatales7(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        label = ['Tipo', 'Frecuencia', 'Con Fiebre', 'Sarampión', 'Meningitis', 'Encefalítis', 'Otras']
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
            if form in ['Tipo', 'Frecuencia', 'Otras', '¿A qué?', 'Manifestaciones', 'Otros']:
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
            controller.mostrar_pantalla(self, antecedentes_postnatales8)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')


class antecedentes_postnatales8(tk.Frame):
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
                            text = "Antecedentes Postnatales",
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
        label = ['Alergias', '¿A que?', 'Manifestaciones', 'Intoxicación por plomo', 'Por medicamentos', 'Otros']
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
            if form in ['¿A qué?', 'Manifestaciones', 'Otros']:
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
            controller.mostrar_pantalla(self, comportamiento)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self,
                                    text = "Siguiente",
                                    command = printData,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size)),
                                    **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')