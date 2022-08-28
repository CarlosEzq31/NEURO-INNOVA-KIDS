import tkinter as tk
from PIL import Image as PImage, ImageTk as ImageTk
from tkinter import *
from PIL import ImageGrab
import cv2
import time

class Splash(tk.Toplevel):
    def __init__(self, parent, text_ : str = 'Cargando'):

        self.parent = parent
        self.alto = self.parent.alto
        self.ancho = self.parent.ancho
        tk.Toplevel.__init__(self, self.parent)
        self.geometry(f"600x400+{int((self.ancho/2) - (600/2))}+{int((self.alto/2) - (400/2))}")
        # set background color
        # self.config(bg = '#ffffff')
        self.title("Splash")
        label = Label(self,text = "")
        label.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        # set logo image
        self.logo = self.cargar_image()
        innova_button = Label(self, text="NEURO INNOVA KIDS", image = self.logo , borderwidth = 0)
        innova_button.place(relx = 0.5, rely = 0.5, anchor = CENTER) 
        self.texto_carga = Label(self, text = text_ , font=('Mukta Malar ExtraLight', 15))
        self.texto_carga.place(relx = 0.5, rely = 0.9, anchor = CENTER) 
        self.wm_overrideredirect(1)
        # actualizamos la pantalla de carga 
        self.update()
    
    def actualizar_texto(self, text_):
        self.texto_carga.config(text = text_)
        self.texto_carga.place(relx = 0.5, rely = 0.9, anchor = CENTER) 
        self.update()

    def cargar_image(self):
        image = cv2.imread(f".\\src\\images\\logo.png", cv2.IMREAD_UNCHANGED)
        img_width, img_height = image.shape[1], image.shape[0]
        image = cv2.resize(image, (int(img_width*self.ancho*0.00003), int(img_height*self.ancho*0.00003)), interpolation = cv2.INTER_AREA)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
        image = PImage.fromarray(image, "RGBA")
        image = ImageTk.PhotoImage(image)
        return image