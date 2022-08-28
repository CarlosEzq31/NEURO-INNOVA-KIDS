import tkinter as tk
from tkinter import *

class mi_texto():
    def __init__(self, canvas, x, y, texto, tamano = 1,**kwargs):
        self.canvas = canvas
        self.frame = self.canvas.master
        self.controller = self.frame.controller
        self.alto = self.frame.alto
        self.ancho = self.frame.ancho
        self.x = x * self.ancho
        self.y = y * self.alto
        self.texto = texto
        self.tamano = tamano
        self.anchor = kwargs.get('ANCHOR', CENTER)
        self.dibujar()

    def dibujar(self):
        self.id_texto = self.canvas.create_text(self.x, self.y, text = self.texto, 
                                                font = ('Mukta Malar ExtraLight', int(self.controller.boton_tamanio * self.tamano)),
                                                anchor = self.anchor)
    
    def destroy(self):
        self.canvas.delete(self.id_texto)