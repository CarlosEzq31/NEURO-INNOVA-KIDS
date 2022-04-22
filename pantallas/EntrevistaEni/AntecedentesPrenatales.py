import tkinter as tk
from tkinter import *
from functools import partial
from pantallas.EntrevistaEni.AntecedentesNatales import *

class antecedentes_prenatales(tk.Frame):
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
                            text = "Antecedentes prenatales",
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
        
        # Formularios de la entrevista ENI
        forms = {}
        label = ['Producto de la gesta número', 'Embarazo deseado', 'Comentarios', 'Drogas en el embarazo', '¿Cuáles?']
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
            if form not in ['Embarazo deseado', 'Drogas en el embarazo']:
                canvas.create_image(int(screenwidth*0.775), int(screenheight*h), image = controller.barra_escribir, anchor = CENTER)
                forms[f"{form}_formulario"] = tk.Entry(self,
                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                        borderwidth = 0, 
                                        highlightthickness = 0,
                                        bg = 'white')
                forms.get(f"{form}_formulario").place(relx = 0.775, rely = h, anchor = CENTER)
            else:
                self.data[form] = ''
                tag = form.replace(' ','_').lower()
                canvas.create_image(int(screenwidth*0.725), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER,
                                    tags = f"{tag}_si")
                canvas.create_image(int(screenwidth*0.8), int(screenheight*h),
                                    image = controller.barra_seleccion,
                                    anchor = CENTER,
                                    tags = f"{tag}_no")
            h += 0.075
            
        # Funcion para resaltar selección
        def seleccion(opcion: str, valor: bool):
            if opcion == 'embarazo':
                if valor == True:
                    embarazo_si.config(bg = '#f6ddeb')
                    canvas.itemconfig('embarazo_deseado_si', image = controller.barra_seleccion_rellena)
                    embarazo_no.config(bg = 'white')
                    canvas.itemconfig('embarazo_deseado_no', image = controller.barra_seleccion)
                    self.data['Embarazo deseado'] = True
                else:
                    embarazo_si.config(bg = 'white')
                    canvas.itemconfig('embarazo_deseado_si', image = controller.barra_seleccion)
                    embarazo_no.config(bg = '#f6ddeb')
                    canvas.itemconfig('embarazo_deseado_no', image = controller.barra_seleccion_rellena)
                    self.data['Embarazo deseado'] = False
            elif opcion == 'drogas':
                if valor == True:
                    drogas_si.config(bg = '#f6ddeb')
                    canvas.itemconfig('drogas_en_el_embarazo_si', image = controller.barra_seleccion_rellena)
                    drogas_no.config(bg = 'white')
                    canvas.itemconfig('drogas_en_el_embarazo_no', image = controller.barra_seleccion)
                    self.data['Drogas en el embarazo'] = True
                else:
                    drogas_si.config(bg = 'white')
                    canvas.itemconfig('drogas_en_el_embarazo_si', image = controller.barra_seleccion)
                    drogas_no.config(bg = '#f6ddeb')
                    canvas.itemconfig('drogas_en_el_embarazo_no', image = controller.barra_seleccion_rellena)
                    self.data['Drogas en el embarazo'] = False
        
        # Botones de si y no
        embarazo_si = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                             highlightthickness = 0, padx=0, pady=0,
                             font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                             command = lambda: seleccion('embarazo', True))
        embarazo_si.place(relx = 0.725, rely = 0.475, anchor = CENTER)
        embarazo_no = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                             highlightthickness = 0, padx=0, pady=0,
                             font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                             command = lambda: seleccion('embarazo', False))
        embarazo_no.place(relx = 0.8, rely = 0.475, anchor = CENTER)
        drogas_si = Button(self,text = 'Si', borderwidth = 0, bg = 'white',
                             highlightthickness = 0, padx=0, pady=0,
                             font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                             command = lambda: seleccion('drogas', True))
        drogas_si.place(relx = 0.725, rely = 0.625, anchor = CENTER)
        drogas_no = Button(self,text = 'No', borderwidth = 0, bg = 'white',
                             highlightthickness = 0, padx=0, pady=0,
                             font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                             command = lambda: seleccion('drogas', False))
        drogas_no.place(relx = 0.8, rely = 0.625, anchor = CENTER)
        
                
        def printData():
            for form in label:
                if form not in ['Embarazo deseado', 'Drogas en el embarazo']:
                    self.data[f"{form}"] = forms.get(f"{form}_formulario").get()
            print(self.data)
            controller.mostrar_pantalla(self, antecedentes_prenatales2)
            
                    
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

class antecedentes_prenatales2(tk.Frame):
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
                            text = "Antecedentes prenatales",
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
        
        # Formularios de la entrevista ENI
        # label = ['Rubéola', 'Varicela', 'Edema', 'Traumatismo', 'Amenaza aborto', 'Sífilis', 'Toxoplasmosis', 'VIH', 'Hipertensión', 'Toxemia','Otros']
        label = ['Rubéola', 'Varicela', 'Edema', 'Traumatismo', 'Amenaza aborto', 'Sífilis', 'Toxoplasmosis']
        h = 0.4
        self.data = {}
        self.botones = {}
        
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
        
        for form in label:
            # Campo de la opción
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,  text = f"{form}", 
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
            controller.mostrar_pantalla(self, antecedentes_prenatales3)
            
                
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
        
class antecedentes_prenatales3(tk.Frame):
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
                            text = "Antecedentes prenatales",
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
        
        # Formularios de la entrevista ENI
        label = ['VIH', 'Hipertensión', 'Toxemia','Otros']
        h = 0.4
        self.data = {}
        self.botones = {}
        
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
        
        for form in label:
            # Campo de la opción
            canvas.create_image(int(screenwidth*0.55),int(screenheight*h),
                                image = controller.boton_rosa, anchor = CENTER)
            form_texto = tk.Label(self,  text = f"{form}", 
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
            controller.mostrar_pantalla(self, antecedentes_natales)
            
                
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command = printData,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')