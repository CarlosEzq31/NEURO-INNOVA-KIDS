import tkinter as tk
from tkinter import *
from test_sql import *

# set colors

bg_secondary_buttons = "#e8eab9"

class registro1(tk.Frame):
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
                            text = "Registro",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.registro_icono_grande, anchor = CENTER)
        
        # Boton de instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
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

        # Campos del formulario
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.4), image = controller.boton_rosa, anchor = CENTER)
        usuario_texto = tk.Label(self, 
                                text = "Usuario", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
        usuario_texto.place(relx = 0.55, rely = 0.4, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.4), image = controller.barra_escribir, anchor = CENTER)
        usuario_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        usuario_formulario.place(relx = 0.775, rely = 0.4, anchor = CENTER)


        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.475), image = controller.boton_rosa, anchor = CENTER)
        contraseña_texto = tk.Label(self, 
                                text = "Contraseña", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
        contraseña_texto.place(relx = 0.55, rely = 0.475, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.475), image = controller.barra_escribir, anchor = CENTER)
        contraseña_formulario = tk.Entry(self,
                                        font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                        show = "*",
                                        borderwidth = 0, 
                                        highlightthickness = 0,
                                        bg = 'white')
        contraseña_formulario.place(relx = 0.775, rely = 0.475, anchor = CENTER)


        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.55), image = controller.boton_rosa, anchor = CENTER)
        contraseña_texto2 = tk.Label(self, 
                                text = "Repetir contraseña", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
        contraseña_texto2.place(relx = 0.55, rely = 0.55, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.55), image = controller.barra_escribir, anchor = CENTER)
        contraseña2_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    show = "*",
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        contraseña2_formulario.place(relx = 0.775, rely = 0.55, anchor = CENTER)


        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.625), image = controller.boton_rosa, anchor = CENTER)
        nombre_texto = tk.Label(self, 
                                text = "Nombre del paciente", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                               **controller.estilo_rosa)
        
        nombre_texto.place(relx = 0.55, rely = 0.625, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.625), image = controller.barra_escribir, anchor = CENTER)
        nombre_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        nombre_formulario.place(relx = 0.775, rely = 0.625, anchor = CENTER)


        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.7), image = controller.boton_rosa, anchor = CENTER)
        contacto_texto = tk.Label(self, 
                                text = "Contacto", 
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                **controller.estilo_rosa)
        contacto_texto.place(relx = 0.55, rely = 0.7, anchor = CENTER)

        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.7), image = controller.barra_escribir, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.67), int(screenheight*0.69), 
                            text = "Nombre", 
                            font = ('Mukta Malar ExtraLight', int(button_font_size*0.8)), 
                            anchor = CENTER)
        contacto__nombre_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        contacto__nombre_formulario.place(relx = 0.775, rely = 0.7, anchor = CENTER)

        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.775), image = controller.barra_escribir, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.67), int(screenheight*0.765), 
                            text = "Número", 
                            font = ('Mukta Malar ExtraLight', int(button_font_size*0.8)), 
                            anchor = CENTER)
        contacto_tel_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        contacto_tel_formulario.place(relx = 0.775, rely = 0.775, anchor = CENTER)

        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.85), image = controller.barra_escribir, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.67), int(screenheight*0.84), 
                            text = "Parentesco", 
                            font = ('Mukta Malar ExtraLight', int(button_font_size*0.6)), 
                            anchor = CENTER)
        contacto_parent_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        contacto_parent_formulario.place(relx = 0.775, rely = 0.85, anchor = CENTER)
        
        
        paciente = {'tratamiento': 'Ninguno',
                'fecha_nacimiento': datetime.fromisoformat('2000-10-17'),
                'genero': 1,
                'lentes': 0,
                'lateralidad': 1,
                'suenio': 'Nada',
                'ayuno': 'No',
                'diagnostico_previo': 'Ninguno'}
        
        # Funcion que registra al nuevo usuario
        def save_data():
            data = {}
            for i in [usuario_formulario, contraseña_formulario, contraseña2_formulario, nombre_formulario, contacto__nombre_formulario, contacto_tel_formulario, contacto_parent_formulario]:
                texto = {usuario_formulario: 'usuario', contraseña_formulario: 'contraseña', contraseña2_formulario: 'repetir contraseña' , nombre_formulario: 'nombre', contacto__nombre_formulario: 'Contacto: Nombre', contacto_tel_formulario: 'Número de contacto', contacto_parent_formulario: 'Parentesco'}
                if i.get():
                    if contraseña_formulario.get() and contraseña2_formulario.get() and contraseña_formulario.get() != contraseña2_formulario.get():
                        texto_aviso(f"Los campos de contraseña deben contener lo mismo")
                        return None
                    if usuario_formulario.get():
                        if existe_usuario(usuario_formulario.get()):
                            texto_aviso(f"El usuario {usuario_formulario.get()} ya existe")
                            return None
                    data[f'{texto.get(i)}'] = i.get()
                else:
                    texto_aviso(f"El campo de {texto.get(i)} no debe estar vacío")
                    return None
                usuario = {'nombre': usuario_formulario.get(), 'contrasena': hashlib.new("sha256", f"{contraseña_formulario.get()}".encode()).hexdigest(), 'correo':f'{usuario_formulario.get()}@gmail.com' }
                contacto = {'nombre': contacto__nombre_formulario.get(), 'telefono': contacto_tel_formulario.get(), 'parentesco': contacto_parent_formulario.get()}
            data.pop('repetir contraseña')
            confirmation = insertar_nuevo_usuario(usuario, paciente, contacto)
            if confirmation:
                texto_aviso("Usuario registrado exitosamente")
            else:
                texto_aviso("Ocurrió un error, vuelve a intentarlo")
                
        # Funcion que pone un texto en pantalla
        def texto_aviso(texto):
            texto_error = canvas.create_text(int(screenwidth*0.5),int(screenheight*0.25), 
                            text = texto,
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
                            anchor = CENTER)
            controller.after(3000,lambda: canvas.delete(texto_error))

        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, tags = 'siguiente',anchor = CENTER)
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                # command = save_data,
                                command = lambda: controller.show_frame(self, registro2),
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')

class registro2(tk.Frame):
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
                            text = "Registro",
                            font = ('Mukta Malar ExtraLight', int(button_font_size*3)),
                            anchor = NW)
        canvas.create_image(int(screenwidth*0.21),int(screenheight*0.5), image = controller.registro_icono_grande, anchor = CENTER)
        
        # Boton de instrucciones
        canvas.create_image(int(screenwidth*0.9),int(screenheight*0.15), image = controller.boton_verde, anchor = CENTER, tags = 'instrucciones')
        canvas.create_image(int(screenwidth*0.84),int(screenheight*0.15), image = controller.signo_iterrogacion_chico, anchor = CENTER)
        instructions_button = tk.Button(self, 
                                        text = "Instrucciones", 
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

        # Campos del formulario

        # funcion para resaltar seleccion
        self.lentes = False
        self.mano = False
        def seleccion(canvas, boton1, boton2, imagen1, imagen2, atributo, valor):
            if valor == True:
                boton1.config(bg = '#f6ddeb')
                canvas.itemconfig(imagen1, image = controller.barra_seleccion_rellena)
                boton2.config(bg = 'white')
                canvas.itemconfig(imagen2, image = controller.barra_seleccion)
            else:
                boton2.config(bg = '#f6ddeb')
                canvas.itemconfig(imagen1, image = controller.barra_seleccion)
                boton1.config(bg = 'white')
                canvas.itemconfig(imagen2, image = controller.barra_seleccion_rellena)
            if  atributo == 'lentes':
                self.lentes = valor
            elif atributo == 'mano':
                self.mano = valor

        # lentes
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.4), image = controller.boton_rosa, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.55), int(screenheight*0.4),
                            text = 'Lentes',
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                            anchor = CENTER)
        canvas.create_image(int(screenwidth*0.725), int(screenheight*0.4), 
                            image = controller.barra_seleccion, 
                            anchor = CENTER,
                            tags = 'lentes_si')
        lentes_boton_si = tk.Button(self,
                                text = "Si",
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                command = lambda: seleccion(canvas, lentes_boton_si, lentes_boton_no, 
                                                            'lentes_si', 'lentes_no', 'lentes', True),
                                borderwidth = 0, 
                                bg = 'white', 
                                highlightthickness = 0,
                                padx=0, 
                                pady=0)
        lentes_boton_si.place(relx = 0.725, rely = 0.4, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.8), int(screenheight*0.4), 
                            image = controller.barra_seleccion, 
                            anchor = CENTER, 
                            tags = 'lentes_no')
        lentes_boton_no = tk.Button(self,
                                text = "No",
                                font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                                command = lambda: seleccion(canvas,lentes_boton_si, lentes_boton_no, 
                                                            'lentes_si', 'lentes_no', 'lentes', False),
                                borderwidth = 0, 
                                bg = 'white', 
                                highlightthickness = 0,
                                padx=0, 
                                pady=0)
        lentes_boton_no.place(relx = 0.8, rely = 0.4, anchor = CENTER)

        # mano dominante
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.475), 
                            image = controller.boton_rosa, 
                            anchor = CENTER,)
        canvas.create_text(int(screenwidth*0.55), int(screenheight*0.475),
                            text = 'Diesto/zurdo',
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                            anchor = CENTER)
        canvas.create_image(int(screenwidth*0.725), int(screenheight*0.475), 
                            image = controller.barra_seleccion, 
                            anchor = CENTER,
                            tags = 'mano_derecha')
        mano_izquierda_boton = tk.Button(self,
                                text = "Izquierda",
                                font = ('Mukta Malar ExtraLight', int(button_font_size*0.85)),
                                command = lambda: seleccion(canvas,mano_izquierda_boton, mano_derecha_boton,
                                                            'mano_derecha', 'mano_izquierda', 'mano', True),
                                borderwidth = 0, 
                                bg = 'white', 
                                highlightthickness = 0,
                                padx=0, 
                                pady=0)
        mano_izquierda_boton.place(relx = 0.725, rely = 0.475, anchor = CENTER)
        canvas.create_image(int(screenwidth*0.8), int(screenheight*0.475), 
                            image = controller.barra_seleccion, 
                            anchor = CENTER,
                            tags = 'mano_izquierda')
        mano_derecha_boton = tk.Button(self,
                                text = "Derecha",
                                font = ('Mukta Malar ExtraLight', int(button_font_size*0.85)),
                                command = lambda: seleccion(canvas,mano_izquierda_boton, mano_derecha_boton,
                                                            'mano_derecha', 'mano_izquierda', 'mano', False),
                                borderwidth = 0, 
                                bg = 'white', 
                                highlightthickness = 0,
                                padx=0, 
                                pady=0)
        mano_derecha_boton.place(relx = 0.8, rely = 0.475, anchor = CENTER)

        # diagnostico
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.55), image = controller.boton_rosa, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.55), int(screenheight*0.55),
                            text = 'Diagnóstico previo',
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                            anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.55), image = controller.barra_escribir, anchor = CENTER)
        diagnostico_texto = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    show = "*",
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        diagnostico_texto.place(relx = 0.775, rely = 0.55, anchor = CENTER)

        # medicamento
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.625), image = controller.boton_rosa, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.55), int(screenheight*0.625),
                            text = 'Medicamento',
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                            anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.625), image = controller.barra_escribir, anchor = CENTER)
        medicamento_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        medicamento_formulario.place(relx = 0.775, rely = 0.625, anchor = CENTER)

        # test de magallanes
        canvas.create_image(int(screenwidth*0.55),int(screenheight*0.7), image = controller.boton_rosa, anchor = CENTER)
        canvas.create_text(int(screenwidth*0.55), int(screenheight*0.7),
                            text = 'Test de Magallanes',
                            font = ('Mukta Malar ExtraLight', int(button_font_size*1)),
                            anchor = CENTER)
        canvas.create_image(int(screenwidth*0.775), int(screenheight*0.7), image = controller.barra_escribir, anchor = CENTER)
        test_magallanes_formulario = tk.Entry(self,
                                    font = ('Mukta Malar ExtraLight', int(button_font_size*1)), 
                                    borderwidth = 0, 
                                    highlightthickness = 0,
                                    bg = 'white')
        test_magallanes_formulario.place(relx = 0.775, rely = 0.7, anchor = CENTER)

        def texto_aviso(texto):
            texto_error = canvas.create_text(int(screenwidth*0.5),int(screenheight*0.25), 
                            text = texto,
                            font = ('Mukta Malar ExtraLight', int(button_font_size)),
                            anchor = CENTER)
            controller.after(3000,lambda: canvas.delete(texto_error))

        def aux():
            print('Valor de lentes', self.lentes)
            print('Valor de mano', self.mano)

        # Boton de siguiente
        canvas.create_image(int(screenwidth*0.15),int(screenheight*0.825), image = controller.boton_verde, anchor = CENTER, tags = 'siguiente')
        siguiente_boton = tk.Button(self, 
                                text = "Siguiente", 
                                command =  aux,
                                font = ('Mukta Malar ExtraLight', int(button_font_size)), 
                                **controller.estilo_verde)
        siguiente_boton.place(relx = 0.15, rely = 0.825, anchor = CENTER)
        controller.animacion_boton(siguiente_boton, canvas, 'siguiente', 'verde')
