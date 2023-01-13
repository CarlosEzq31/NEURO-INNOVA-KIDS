# importamos las librerias necesarias
from classes.mi_frame import *


# pantalla de información básica
class informacion_basica(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Información básica', 3, ANCHOR = NW)
        self.canvas.create_image(int(self.ancho*0.21),int(self.alto*0.5), image = controller.signo_iterrogacion_grande, anchor = CENTER)

        # boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)

        # boton atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)
        
        # boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())

        # boton que es
        self.boton_que_es = mi_boton(self.canvas, 0.7, 0.4, '¿Qué es?', 'rosa',
                                    lambda x: controller.mostrar_pantalla(self, 'que_es'),
                                    grande = True)

        # boton de pruebas
        self.boton_pruebas = mi_boton(self.canvas, 0.7, 0.525, 'Pruebas', 'rosa',
                                    lambda x: controller.mostrar_pantalla(self, 'info_pruebas'),
                                    grande = True)

        # boton de seguidor ocular
        self.boton_seguidor = mi_boton(self.canvas, 0.7, 0.65, 'Seguidor ocular', 'rosa',
                                        lambda x: controller.mostrar_pantalla(self, 'seguidor_ocular'),
                                        grande = True)

        # boton de resultados
        self.boton_resultados = mi_boton(self.canvas, 0.7, 0.775, 'Resultados', 'rosa',
                                        lambda x: controller.mostrar_pantalla(self, 'resultados'),
                                        grande = True)
