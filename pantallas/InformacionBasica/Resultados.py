# importamos las librerias necesarias
import textwrap
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *

class resultados(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Resultados', 3, ANCHOR = NW)
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
        texto_info = "Una vez realizada las pruebas el programa dará la opción para imprimir, descargar y acceder a los resultados. Éstos serán una serie de gráficas que revelan el desempeño del niño durante las pruebas, ayudarán a medir el nivel de atención y realizar el seguimiento de cualquier situación de estrés o trauma que pueda tener el paciente. Los datos recopilados serán manejados según lo establecido en la Ley Federal de Protección de Datos Personales en Posesión de los particulares(LFPDPPP) para asegurar que la información sea protegida, tratada de manera legítima, informada y controlada, así mismo se les proporcionará un convenio de confidencialidad y consentimiento para estos fines."
        self.texto_info = mi_texto(self.canvas, 0.65, 0.62, textwrap.fill(texto_info, width = 50), 1.25, ANCHOR = CENTER)