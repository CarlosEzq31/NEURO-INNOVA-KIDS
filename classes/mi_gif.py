from tkinter import *
import tkinter as tk

class mi_gif():

    def __init__(self, canvas, x, y, gif, **kwargs):
        self.canvas = canvas
        self.frame = self.canvas.master
        self.controller = self.frame.controller
        self.alto = self.frame.alto
        self.ancho = self.frame.ancho
        self.x = x * self.ancho
        self.y = y * self.alto
        self.gif = gif
        self.gif_frame = 0
        self.dibujar()

    def dibujar(self):
        self.id_gif = self.canvas.create_image(self.x, self.y, image = self.gif[self.gif_frame], anchor = CENTER)

    def animar(self):
        self.canvas.itemconfig(self.id_gif, image = self.gif[self.gif_frame])
        self.gif_frame += 1
        if self.gif_frame == len(self.gif):
            self.gif_frame = 0

    def detener(self):
        self.canvas.itemconfig(self.id_gif, image = self.gif[self.gif_frame])
