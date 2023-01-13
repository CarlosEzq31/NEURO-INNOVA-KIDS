from classes.mi_frame import *

class historialfamiliar(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Historial Familiar', 3, ANCHOR = NW)
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
        # Problema de lenguaje
        self.problema_lenguaje = mi_formulario(self.canvas, 0.775, 0.35, 'Problema de lenguaje', vacio = True)

        # Deficiencia sensorial
        self.deficiencia_sensorial = mi_formulario(self.canvas, 0.775, 0.425, 'Deficiencia sensorial', vacio = True)

        # Parálisis cerebral
        self.paralisis_cerebral = mi_formulario(self.canvas, 0.775, 0.5, 'Parálisis cerebral', vacio = True)

        # Epilepsia
        self.epilepsia = mi_formulario(self.canvas, 0.775, 0.575, 'Epilepsia', vacio = True)

        # Déficit de atención
        self.deficit_atención = mi_formulario(self.canvas, 0.775, 0.65, 'Déficit de atención', vacio = True)

        # Prob Coord. Motriz
        self.prob_coord_motriz = mi_formulario(self.canvas, 0.775, 0.725, 'Prob. Coord. Motriz', vacio = True)

        # Drogradiccion
        self.drogadiccion = mi_formulario(self.canvas, 0.775, 0.8, 'Drogadicción', vacio = True)


    def siguiente(self):
        if self.validar_formularios():    
            self.controller.entrevista_eni.agregar_datos('historia_familiar', self.datos)
            self.controller.mostrar_pantalla(self, 'historialfamiliar2')


class historialfamiliar2(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Historial Familiar', 3, ANCHOR = NW)
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
        # Alcoholismo
        self.alcoholismo = mi_formulario(self.canvas, 0.775, 0.35, 'Alcoholismo', vacio = True)

        # Enferm. Psiquiátrica
        self.enferm_psiquiatrica = mi_formulario(self.canvas, 0.775, 0.425, 'Enferm. Psiquiátrica', vacio = True)

        # Sínd. Down
        self.sind_down = mi_formulario(self.canvas, 0.775, 0.5, 'Sínd. Down', vacio = True)

        # Retardo mental
        self.retardo_mental = mi_formulario(self.canvas, 0.775, 0.575, 'Retardo mental', vacio = True)

        # Prob. aprendizaje
        self.prob_aprendizaje = mi_formulario(self.canvas, 0.775, 0.65, 'Prob. aprendizaje', vacio = True)

        # Retraso escolar
        self.retraso_escolar = mi_formulario(self.canvas, 0.775, 0.725, 'Retraso escolar', vacio = True)

        # Otros
        self.otros = mi_formulario(self.canvas, 0.775, 0.8, 'Otros', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            self.controller.entrevista_eni.agregar_datos('historia_familiar', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_prenatales')