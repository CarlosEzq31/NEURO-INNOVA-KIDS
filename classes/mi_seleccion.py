import tkinter as tk
from tkinter import *
from functools import partial

class mi_seleccion():

    def __init__(self, canvas, x, y, texto, opciones,**kwargs):
        self.canvas = canvas
        self.frame = self.canvas.master
        self.controller = self.frame.controller
        self.alto = self.frame.alto
        self.ancho = self.frame.ancho
        self.x = x * self.ancho
        self.y = y * self.alto
        self.seleccion = ''
        self.opciones = opciones
        self.texto = texto
        self.focus = kwargs.get("focus", False)
        self.vacio = kwargs.get("vacio", False)
        self.dibujar()

    def dibujar(self):
        """Dibuja la barra de seleccion"""
        self.id_label = self.canvas.create_image(self.x , self.y, image = self.controller.boton_rosa, anchor = CENTER)
        self.id_texto = self.canvas.create_text(self.x , self.y,
                                                text = self.texto,
                                                font = ('Mukta Malar Extralight', int(self.controller.boton_tamanio)))
        
        bounds = self.canvas.bbox(self.id_label)
        width = bounds[2] - bounds[0]

        self.opciones_img_id = {}
        self.opciones_texto_id = {}
        i = 1.075
        for opcion in self.opciones:
            x_pos = self.x * i + (width / 2)
            self.opciones_img_id[f'{opcion}_img_id'] = self.canvas.create_image(x_pos, self.y, image = self.controller.barra_seleccion, anchor = CENTER)
            self.opciones_texto_id[f'{opcion}_texto_id'] = self.canvas.create_text(x_pos, self.y, text = opcion, font = ('Mukta Malar Extralight', int(self.controller.boton_tamanio)))
            i += 0.15

        self.animar()
    
    def animar(self):
        """Animacion de la barra de seleccion"""
        for opcion in self.opciones:
            self.canvas.tag_bind(self.opciones_img_id[f'{opcion}_img_id'], '<Enter>', partial(self.hover, opcion))
            self.canvas.tag_bind(self.opciones_img_id[f'{opcion}_img_id'], '<Leave>', partial(self.leave, opcion))
            self.canvas.tag_bind(self.opciones_texto_id[f'{opcion}_texto_id'], '<Enter>', partial(self.hover_texto, opcion))
            self.canvas.tag_bind(self.opciones_texto_id[f'{opcion}_texto_id'], '<Leave>', partial(self.leave_texto, opcion))
            self.canvas.tag_bind(self.opciones_img_id[f'{opcion}_img_id'], '<Button-1>', partial(self.seleccionar, opcion))
            self.canvas.tag_bind(self.opciones_texto_id[f'{opcion}_texto_id'], '<Button-1>', partial(self.seleccionar, opcion))
    
    def hover(self, opcion, event):
        """Resalta la opcion seleccionada"""
        self.canvas.itemconfig(self.opciones_img_id[f'{opcion}_img_id'], image = self.controller.barra_seleccion_hover)

    def leave(self, opcion, event):
        """Deja de resaltar la opcion seleccionada"""
        if self.seleccion != opcion:
            self.canvas.itemconfig(self.opciones_img_id[f'{opcion}_img_id'], image = self.controller.barra_seleccion)
        else:
            self.canvas.itemconfig(self.opciones_img_id[f'{opcion}_img_id'], image = self.controller.barra_seleccion_rellena)

    def hover_texto(self, opcion, event):
        """Resalta la opcion seleccionada"""
        self.canvas.itemconfig(self.opciones_img_id[f'{opcion}_img_id'], image = self.controller.barra_seleccion_hover)
        self.canvas.itemconfig(self.opciones_texto_id[f'{opcion}_texto_id'], fill = 'white')


    def leave_texto(self, opcion, event):
        """Deja de resaltar la opcion seleccionada"""
        self.canvas.itemconfig(self.opciones_texto_id[f'{opcion}_texto_id'], fill = 'black')
    
    def seleccionar(self, opcion, event):
        """Selecciona la opcion"""
        if self.seleccion != opcion:
            for opcion_ in self.opciones:
                self.canvas.itemconfig(self.opciones_img_id[f'{opcion_}_img_id'], image = self.controller.barra_seleccion)
                self.canvas.itemconfig(self.opciones_texto_id[f'{opcion_}_texto_id'], fill = 'black')
            self.canvas.itemconfig(self.opciones_img_id[f'{opcion}_img_id'], image = self.controller.barra_seleccion_rellena)
            self.seleccion = opcion
        else:
            self.limpiar()
    
    def datos(self) -> str:
        """Devuelve los datos de la barra de seleccion"""
        return self.seleccion

    def limpiar(self):
        """Limpia la barra de seleccion"""
        self.seleccion = ''
        for opcion in self.opciones:
            self.canvas.itemconfig(self.opciones_img_id[f'{opcion}_img_id'], image = self.controller.barra_seleccion)
            self.canvas.itemconfig(self.opciones_texto_id[f'{opcion}_texto_id'], fill = 'black')