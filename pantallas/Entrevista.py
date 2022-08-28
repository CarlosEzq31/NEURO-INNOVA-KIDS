from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.paciente import *
from classes.mi_prueba import *
from classes.mi_seleccion import *


class entrevista(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Entrevista', 3, ANCHOR = NW)
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
        
        # Formularios para la nueva entrevista
        # Ayuno
        self.ayuno = mi_seleccion(self.canvas, 0.5, 0.4, '¿Ayuno? (Horas)', ['4 o menos', '4 - 6', '6 - 8', '8 o más'])

        # Sueño
        # self.sueno = mi_formulario(self.canvas, 0.7, 0.5, 'Horas de sueño')
        self.sueno = mi_seleccion(self.canvas, 0.5, 0.5, '¿Sueño? (Horas)', ['4 o menos', '4 - 6', '6 - 8', '8 o más'])


        # Boton de siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.85, 0.9, 'Siguiente', 'verde',
                                            lambda x: self.siguiente())

        
    def siguiente(self):
        if self.validar_formularios():
            self.controller.prueba = Prueba(self.controller.paciente, self.controller.usuario, self.datos['sueno'], self.datos['ayuno'])
            self.controller.entrevista.agregar_prueba(self.controller.prueba)
            print(self.controller.prueba)
            print(self.controller.entrevista)