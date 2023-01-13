# Importar librerias necesarias
from classes.mi_frame import *

class menu_principal(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.back_ninios)

        # colocar el logo
        self.canvas.create_image(int(self.ancho * 0.25), int(self.alto * 0.4), image = self.controller.logo, anchor = CENTER)

        # boton de informacion
        self.boton_info = mi_boton(self.canvas, 0.875, 0.7, 'Información básica', 'rosa', 
                                    lambda x: self.controller.mostrar_pantalla(self, 'informacion_basica'),
                                    icono = self.controller.signo_iterrogacion,
                                    icono_x = -0.5)

        # boton de neuro innova kids
        self.boton_neuro = mi_boton(self.canvas, 0.875, 0.8, 'NEURO INNOVA KIDS®', 'rosa', 
                                    lambda x: self.controller.mostrar_pantalla(self, 'ingreso'),
                                    icono = self.controller.logo_bn)

        # Boton para salir del programa
        self.boton_salir = mi_boton(self.canvas, 0.875, 0.9, 'Salir', 'rosa', 
                                    lambda x: self.controller.destroy())