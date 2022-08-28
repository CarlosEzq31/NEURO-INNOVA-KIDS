from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.mi_seleccion import *
from classes.mi_formulario import *

class disciplina(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Método de disciplina', 3, ANCHOR = NW)
        self.canvas.create_image(int(self.ancho*0.21),int(self.alto*0.5), image = controller.registro_icono_grande, anchor = CENTER)

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

        # Boton de siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.825, 0.9, 'Siguiente', 'verde',
                                        lambda x: self.siguiente())
        
        # Formulario de datos
        # Regaño
        self.regano = mi_seleccion(self.canvas, 0.548, 0.3, 'Regaño', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Castigo físico
        self.castigo_fisico = mi_seleccion(self.canvas, 0.548, 0.375, 'Castigo físico', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Tiempo fuera
        self.tiempo_fuera = mi_seleccion(self.canvas, 0.548, 0.45, 'Tiempo fuera', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Premio
        self.premio = mi_seleccion(self.canvas, 0.548, 0.525, 'Premio', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Convencimiento
        self.convencimiento = mi_seleccion(self.canvas, 0.548, 0.6, 'Convencimiento', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Otros
        self.otros = mi_formulario(self.canvas, 0.775, 0.675, 'Otros', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad')