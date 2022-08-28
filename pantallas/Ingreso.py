# importamos las librerias necesarias
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_boton import *


# pantalla de información básica
class ingreso(mi_frame):
    def __init__(self, parent, controller):
        # inicializamos el frame
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.25),int(self.alto*0.4), image = self.controller.logo, anchor = CENTER)
        
        # boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)

        # boton de atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)
        
        # boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())


        # boton de iniciar sesion
        self.boton_iniciar_sesion = mi_boton(self.canvas, 0.6, 0.7, 'Iniciar sesión', 'rosa',
                                            lambda x: self.controller.mostrar_pantalla(self, 'iniciar_sesion'),
                                            grande = True)
        # boton de registro
        self.boton_registro = mi_boton(self.canvas, 0.6, 0.825, 'Registro', 'rosa',
                                        lambda x: self.controller.mostrar_pantalla(self, 'registro_usuario'),
                                        grande = True)