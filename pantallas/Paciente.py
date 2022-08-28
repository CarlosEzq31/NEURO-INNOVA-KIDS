from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.mi_lista import *
from classes.paciente import *


class inicio_paciente(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Paciente', 3, ANCHOR = NW)
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

        # Boton de crear paciente
        self.boton_crear_paciente = mi_boton(self.canvas, 0.7, 0.4, 'Crear paciente nuevo', 'rosa',
                                            lambda x: self.registrar_paciente(),
                                            grande = True)

        # Lista de pacientes la mostramos cuando entremos en la pantalla
        self.lista_dibujada = False
        self.bind('<Enter>', lambda x: self.mostrar_pacientes())

        # Boton de siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.85, 0.9, 'Siguiente', 
                                'rosa', lambda x: self.iniciar_paciente())

    def iniciar_paciente(self):
        id = [paciente['id'] for paciente in self.controller.pacientes if paciente['nombre'] == self.lista_pacientes.datos()][0]
        self.controller.paciente = Paciente(id)
        self.controller.mostrar_pantalla(self, 'pruebas')
        self.lista_dibujada = False
    
    def mostrar_pacientes(self):
        if not self.lista_dibujada:
            self.lista_dibujada = True
            self.controller.pacientes = self.controller.usuario.obtener_pacientes()
            self.lista_nombres = sorted([paciente['nombre'] for paciente in self.controller.pacientes])
            self.lista_pacientes = mi_lista(self.canvas, 0.7, 0.525, 'Seleccionar paciente', self.lista_nombres)
    
    def registrar_paciente(self):
        self.controller.mostrar_pantalla(self, 'registro_paciente')
        self.lista_dibujada = False
        self.lista_pacientes.destroy()