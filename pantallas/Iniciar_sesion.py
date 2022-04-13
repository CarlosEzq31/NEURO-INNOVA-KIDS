import tkinter as tk
from tkinter import *
from test_sql import *
from pantallas.Pruebas import *

bg_primary_buttons = "#f6ddeb"
bg_secondary_buttons = "#e8eab9"


class iniciar_sesion(tk.Frame):
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
                            text = "Iniciar sesión",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        
        # Boton de menu principal
        canvas.create_image(int(screenwidth*0.7),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'menu')
        menu_button = tk.Button(self, 
                                text = "Menú principal", 
                                command = lambda : controller.ir_menu_principal(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        menu_button.place(relx = 0.7, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(menu_button, canvas, 'menu', 'verde')
        
        # Boton de instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
                                        command = lambda: controller.ir_instrucciones(self),
                                        font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                        **controller.estilo_verde)
        instructions_button.place(relx = 0.91, rely = 0.15, anchor = CENTER)
        controller.animacion_boton(instructions_button, canvas, 'instrucciones', 'verde')
        
        # Campos del formulario
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.725), image = controller.boton_rosa, anchor = CENTER)
        usuario_texto = tk.Label(self, 
                                text = "Usuario", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                borderwidth = 0, 
                                bg = bg_primary_buttons, 
                                highlightthickness = 0,
                                padx=0, 
                                pady=0)
        usuario_texto.place(relx = 0.55, rely = 0.725, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.725), image = controller.barra_escribir, anchor = CENTER)
        usuario_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        usuario_formulario.place(relx = 0.775, rely = 0.725, anchor = CENTER)


        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.8), image = controller.boton_rosa, anchor = CENTER)
        contraseña_texto = tk.Label(self, 
                                text = "Contraseña", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                borderwidth = 0, 
                                bg = bg_primary_buttons, 
                                highlightthickness = 0,
                                padx=0, 
                                pady=0)
        contraseña_texto.place(relx = 0.55, rely = 0.8, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.8), image = controller.barra_escribir, anchor = CENTER)
        contraseña_formulario = tk.Entry(self,
                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                        show = "*",
                                        borderwidth = 0, 
                                        highlightthickness = 0,
                                        bg = 'white')
        contraseña_formulario.place(relx = 0.775, rely = 0.8, anchor = CENTER)
        
        # Boton de atras
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.9), image = controller.boton_verde, anchor = CENTER, tags = 'atras')
        back_button = tk.Button(self, 
                                text = "Atrás", 
                                command = lambda : controller.previous_frame(),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        back_button.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(back_button, canvas, 'atras', 'verde')
        
        # funcion para iniciar sesion
        def iniciar_sesion_():
            usuario = usuario_formulario.get()
            passwd = contraseña_formulario.get()
            if usuario and passwd:
                id = iniciar_sesion_sql(nombre = usuario, passwd = passwd)
                if id:
                    controller.id = id
                    print(controller.id)
                    controller.show_frame(self, pruebas)
                else:
                    texto_aviso('Usuario o contraseña incorrectos')
            else:
                texto_aviso('Por favor, introduzca sus datos')
            # controller.show_frame(self, pruebas)
                    
        def texto_aviso(texto):
            texto_error = canvas.create_text(int(screenwidth*0.5),int(screenheight*0.25), 
                            text = texto,
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
                            anchor = CENTER)
            controller.after(3000,lambda: canvas.delete(texto_error))
            
        # Boton actualizar datos
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'actualizar',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Actualizar datos", 
                                # command = iniciar_sesion_,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'actualizar', 'verde')
        
        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.85),int(screenheight*0.9), image = controller.boton_rosa, tags = 'iniciar',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Iniciar sesión", 
                                command = iniciar_sesion_,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_rosa)
        siguiente_boton.place(relx = 0.85, rely = 0.9, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'iniciar', 'rosa')
        
        def aux(e):
            iniciar_sesion_()
        
        usuario_formulario.bind('<Return>', aux)
        contraseña_formulario.bind('<Return>', aux)