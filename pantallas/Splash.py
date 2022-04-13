import tkinter as tk
from PIL import Image as PImage, ImageTk as ImageTk
from tkinter import *
try:
    from PIL import ImageGrab
except:
    import pyscreenshot as ImageGrab

class Splash(tk.Toplevel):
    def __init__(self, parent, text_ : str = 'Cargando'):
        # obtener resolucion de pantalla
        resolution = ImageGrab.grab()
        screenwidth, screenheight = resolution.size
        del resolution
        tk.Toplevel.__init__(self, parent)
        self.geometry(f"600x400+{int((screenwidth/2) - (600/2))}+{int((screenheight/2) - (400/2))}")
        self.title("Splash")
        label = Label(self,text = "")
        label.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        # set logo image
        self.logo = PImage.open(f"{parent.path}/src/images/logo.png")
        logo_width, logo_height = self.logo.size
        self.logo = self.logo.resize((int(logo_width*screenwidth*0.00003), int(logo_height*screenwidth*0.00003)), PImage.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        innova_button = Label(self, text="NEURO INNOVA KIDS", image = self.logo , borderwidth = 0)
        innova_button.place(relx = 0.5, rely = 0.5, anchor = CENTER) 
        self.texto_carga = Label(self, text = text_ , font=('Mukta Malar ExtraLight', 15))
        self.texto_carga.place(relx = 0.5, rely = 0.9, anchor = CENTER) 
        self.wm_overrideredirect(True)
        # actualizamos la pantalla de carga 
        self.update()
    
    def actualizar_texto(self, text_):
        self.texto_carga.config(text = text_)
        self.texto_carga.place(relx = 0.5, rely = 0.9, anchor = CENTER) 
        self.update()
