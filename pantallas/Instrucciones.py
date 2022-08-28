from classes.mi_gif import *
from classes.mi_texto import *
from classes.mi_boton import *
from classes.mi_frame import *


class instrucciones(mi_frame):
    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla
        self.canvas.create_text(int(self.ancho*0.15), int(self.alto*0.25), 
                            text = "Instrucciones", 
                            font = ('Mukta Malar ExtraLight', int(self.controller.boton_tamanio*3)), 
                            anchor = NW)
        
        # Botón atrás
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)

        # Instrucción 1 
        self.texto_1 = mi_texto(self.canvas, 0.35, 0.375, '1', 4)
        self.instruccion_1 = mi_texto(self.canvas, 0.45, 0.39, 'Mantén la vista directamente \n    en el centro de la pantalla')
        self.gif_1_1 = mi_gif(self.canvas, 0.7, 0.325, controller.gif_instruccion1_a)
        self.gif_1_2 = mi_gif(self.canvas, 0.85, 0.325, controller.gif_instruccion1_b)


        # Instrucción 2
        self.texto_2 = mi_texto(self.canvas, 0.35, 0.55, '2', 4)
        self.instruccion_2 = mi_texto(self.canvas, 0.45, 0.55, 'Trata de parpadear \n  lo menos posible')
        self.gif_2_1 = mi_gif(self.canvas, 0.7, 0.555, controller.gif_instruccion1_a)
        self.gif_2_2 = mi_gif(self.canvas, 0.85, 0.555, controller.gif_instruccion2_b)


        # Instrucción 3
        self.texto_3 = mi_texto(self.canvas, 0.35, 0.785, '3', 4)
        self.instruccion_3 = mi_texto(self.canvas, 0.46, 0.8, 'No hables ni muevas la lengua o\n   movimiento con el rostro')
        self.gif_3_1 = mi_gif(self.canvas, 0.7, 0.8, controller.gif_instruccion1_a)
        self.gif_3_2 = mi_gif(self.canvas, 0.85, 0.8, controller.gif_instruccion3_b)
            
        self.bind("<Enter>", self.iniciar_gif)
        self.bind("<Leave>", self.detener_gif)

    def iniciar_gif(self, event = None):
        self.reproducir_gif()

    def detener_gif(self, event = None):
        for key, value in vars(self).items():
            if key.startswith('gif'):
                value.detener()
        self.after_cancel(self.after_id)

    def reproducir_gif(self):
        for key, value in vars(self).items():
            if key.startswith('gif'):
                value.animar()
        self.after_id = self.after(55, self.reproducir_gif)
        