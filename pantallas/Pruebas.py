from classes.mi_frame import *

class pruebas(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
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

        # boton de usuario
        self.boton_usuario = mi_boton(self.canvas, 0.625, 0.525, 'Paciente', 'rosa',
                                    lambda x: controller.mostrar_pantalla(self, 'usuario_info'),
                                    grande = True,
                                    icono = controller.registro_icono,
                                    icono_dentro = True)
        
        # boton de iniciar prueba
        self.boton_entrevista = mi_boton(self.canvas, 0.625, 0.65, 'Entrevista nueva', 'rosa',
                                    lambda x: self.ir_a_entrevista(),
                                    tamano_letra = 1.2,
                                    grande = True,
                                    icono = controller.play_icono,
                                    icono_dentro = True)
        
        # boton de historial
        self.boton_historial = mi_boton(self.canvas, 0.625, 0.775, 'Historial de pruebas', 'rosa',
                                        lambda x: controller.mostrar_pantalla(self, 'historial'),
                                        tamano_letra = 1.2,
                                        grande = True,
                                        icono = controller.historial_icono,
                                        icono_dentro = True)

        # boton de entrevista eni
        self.boton_entrevista_eni = mi_boton(self.canvas, 0.625, 0.9, 'Entrevista ENI', 'rosa',
                                            lambda x: controller.mostrar_pantalla(self, 'historiaclinica'),
                                            tamano_letra = 1.2,
                                            grande = True,
                                            icono = controller.historial_icono,
                                            icono_dentro = True)

    
    def ir_a_entrevista(self):
        self.controller.entrevista = Entrevista(self.controller.usuario.id, self.controller.paciente.id)
        self.controller.mostrar_pantalla(self, 'entrevista')
        # print(self.controller.entrevista)