from tkinter import *
import tkinter as tk

class mi_frame(tk.Frame):

    def __init__(self, parent, controller, fondo):
        self.controller = controller
        self.parent = parent
        self.ancho = self.controller.ancho
        self.alto = self.controller.alto
        self.frame_focus = None
        
        tk.Frame.__init__(self, self.parent)

        # creamos un lienzo
        self.canvas = tk.Canvas(self, width = self.ancho, height = self.alto, bg = 'white')
        self.canvas.pack(side = "top", fill = "both", expand = True)

        # colocamos el fondo de la pantalla
        self.canvas.create_image(0,0, image = fondo, anchor = NW)
        
        self.bind('<Enter>', lambda x: self.focus_())

    
    def texto_aviso(self, x, y, texto, **kwargs):
        """Muestra un texto en la pantalla"""
        tiempo = kwargs.get('tiempo', 3000)
        tamano = kwargs.get('tamano', 2)
        self.texto_aviso_id = self.canvas.create_text(int(self.ancho * x),int(self.alto * y), 
                            text = texto,
                            font = ('Mukta Malar ExtraLight', int(self.controller.boton_tamanio * tamano)),
                            anchor = CENTER)
        self.controller.after(tiempo, lambda: self.canvas.delete(self.texto_aviso_id))
    
    def focus_(self):
        """Coloca el foco en el último formulario que se haya seleccionado"""
        if self.frame_focus:
            self.frame_focus.focus_set()
    

    def validar_formularios(self):
        """Valida que los formularios no estén vacíos
        y crea un atributo con el valor de cada formulario"""
        self.datos = {}
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value) or 'mi_seleccion' in str(value):
                if value.datos() == '' and value.vacio == False:
                    self.texto_aviso(0.5, 0.05, 'Todos los campos son obligatorios')
                    return False
                else:
                    self.datos[key] = value.datos()
        return True