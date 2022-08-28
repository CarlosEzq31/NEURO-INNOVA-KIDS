# importamos las librerias necesarias
import textwrap
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *

class seguidor_ocular(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Seguidor ocular', 3, ANCHOR = NW)
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
        texto_info = "NEURO INNOVA KIDS funciona a través de seguidor ocular, el cual nos brindará información del niño mientras efectúa tareas de carga cognitiva. El seguidor ocular es un dispositivo de luz infrarroja  que procesa el punto donde se fija la mirada (donde estamos mirando), o el movimiento del ojo en relación con la cabeza en la pantalla del servidor.Este método es un proceso no invasivo por lo que  el niño no sufrirá riesgos. Y solo grabará la mirada del niño, por lo que su rostro no será registrado ni aparecerá en la base de datos"
        self.texto_info = mi_texto(self.canvas, 0.65, 0.62, textwrap.fill(texto_info, width = 50), 1.25, ANCHOR = CENTER)

        # Imagen del eyetracker
        self.canvas.create_image(int(self.ancho*0.3),int(self.alto*0.725), image = self.controller.eyetracker_img, anchor = CENTER)