# importamos las librerias necesarias
import textwrap
from classes.mi_frame import *

class que_es(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, '¿Qué es?', 3, ANCHOR = NW)
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

        # Texto de información
        texto_info = "NEURO INNOVA KIDS es una herramienta de evaluación, que ofrece un método no invasivo, a través de mediciones precisas durante tareas de demanda cognitiva, y que proveen una ventana a los sistemas cerebrales fundamentales para la atención.  El programa va a parametrizar el nivel de atención que tiene un niño. Con la finalidad de ser un apoyo para el especialista durante el diagnóstico y el seguimiento del paciente"
        self.texto_info = mi_texto(self.canvas, 0.65, 0.62, textwrap.fill(texto_info, width = 50), 1.25, ANCHOR = CENTER)