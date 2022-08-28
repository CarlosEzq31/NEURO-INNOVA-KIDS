import calendar
from datetime import date
import tkinter as tk
from tkinter import *

class mi_formulario():

    def __init__(self, canvas, x, y, texto, **kwargs):
        self.canvas = canvas
        self.frame = self.canvas.master
        self.controller = self.frame.controller
        self.alto = self.frame.alto
        self.ancho = self.frame.ancho
        self.x = x * self.ancho
        self.y = y * self.alto
        self.texto = texto
        self.vacio = kwargs.get('vacio', False)
        self.fecha = kwargs.get('fecha', False)
        self.focus = kwargs.get("focus", False)
        self.command = kwargs.get("command", None)
        self.contrasena = kwargs.get("contrasena", False)
        self.placeholder = kwargs.get("placeholder", None)
        self.por_defecto = None
        self.dibujar()

    def dibujar(self):
        self.id_form = self.canvas.create_image(self.x, self.y, image = self.controller.barra_escribir,
                                                anchor = CENTER)
        self.entry = Entry(self.canvas, 
                            font = ('Mukta Malar Extralight', int(self.controller.boton_tamanio)),
                            borderwidth = 0, 
                            highlightthickness = 0,
                            bg = 'white',
                            justify='center')
        if self.contrasena:
            self.entry.config(show = "*")
        bounds = self.canvas.bbox(self.id_form)
        width = bounds[2] - bounds[0]
        self.label_x = self.x* 1.045 - width
        self.window = self.canvas.create_window(self.x, self.y,
                                                window = self.entry,
                                                width = width * 0.9,
                                                anchor = CENTER)
        self.id_label = self.canvas.create_image(self.label_x, self.y, image = self.controller.boton_rosa, anchor = CENTER)
        self.id_texto = self.canvas.create_text(self.label_x, self.y,
                                                text = self.texto,
                                                font = ('Mukta Malar Extralight', int(self.controller.boton_tamanio)))

        self.animar()

    def animar(self): 
        self.canvas.tag_bind(self.id_form, '<Button-1>', lambda x: self.cambiar_focus())
        self.entry.bind('<Button-1>', lambda x: self.cambiar_focus())
        if self.command:
            self.entry.bind('<Return>', self.command)
        if self.focus:
            self.frame.frame_focus = self.entry
        if self.placeholder:
            self.colocar_placeholder()
            self.entry.bind('<FocusIn>', lambda x: self.limpiar())
            self.entry.bind('<FocusOut>', lambda x: self.colocar_placeholder())

    def datos(self):
        if self.fecha:
            dias, meses, anios = self.entry.get().split('/')
            dias = int(dias)
            meses = int(meses)
            anios = int(anios)
            if dias > 31 or dias < 1:
                self.frame.texto_aviso(0.5, 0.05, 'Día no válido')
                raise ValueError('Día inválido')
            if anios <= 1900 or anios > date.today().year:
                self.frame.texto_aviso(0.5, 0.05, 'Año no válido')
                raise ValueError('Año inválido')
            if meses == 2:
                if calendar.isleap(int(anios)):
                    if dias > 29:
                        self.frame.texto_aviso(0.5, 0.05, 'Día no válido')
                        raise ValueError('Día inválido')
                else:
                    if dias > 28:
                        self.frame.texto_aviso(0.5, 0.05, 'Día no válido')
                        raise ValueError('Día inválido')
            elif meses == 4 or meses == 6 or meses == 9 or meses == 11:
                if dias > 30:
                    self.frame.texto_aviso(0.5, 0.05, 'Día no válido')
                    raise ValueError('Día inválido')
            else:
                if dias > 31:
                    self.frame.texto_aviso(0.5, 0.05, 'Día no válido')
                    raise ValueError('Día inválido')
            if meses > 12 or meses < 1:
                self.frame.texto_aviso(0.5, 0.05, 'Mes no válido')
                raise ValueError('Mes inválido')
        if self.entry.get() == self.placeholder and not self.por_defecto:
            return ''
        return self.entry.get()

    def limpiar(self):
        if self.entry.get() == self.placeholder and not self.por_defecto:
            self.entry.delete(0, END)
            self.entry.config(fg = 'black')
        if self.frame.controller.frame != self.frame:
            self.colocar_placeholder()

    def cambiar_focus(self):
        self.entry.focus_set()
        self.frame.frame_focus = self.entry
        self.limpiar()
    
    def colocar_placeholder(self):
        if self.entry.get() == '' or self.frame.controller.frame != self.frame:
            if self.por_defecto:
                self.entry.config(fg = 'black')
            else:
                self.entry.config(fg = 'grey')
            self.entry.delete(0, END)
            if self.placeholder:
                self.entry.insert(0, self.placeholder)
    
    def obtener_label_x(self):
        return self.label_x / self.ancho

    def colocar_por_defecto(self, texto):
        self.por_defecto = texto
        self.placeholder = texto
        self.colocar_placeholder()
        self.entry.bind('<FocusIn>', lambda x: self.limpiar())
        self.entry.bind('<FocusOut>', lambda x: self.colocar_placeholder())
