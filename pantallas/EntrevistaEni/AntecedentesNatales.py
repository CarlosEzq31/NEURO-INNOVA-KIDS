from classes.mi_frame import *

class antecedentes_natales(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.225, 'Antecedentes Natales', 3, ANCHOR = NW)
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
        # Tipo de parto
        self.parto = mi_formulario(self.canvas, 0.775, 0.35, 'Tipo de parto', vacio = True)

        # Semanas de gestación
        self.semanas = mi_formulario(self.canvas, 0.775, 0.425, 'Semanas de gestación', vacio = True)

        # Horas de parto
        self.horas = mi_formulario(self.canvas, 0.775, 0.5, 'Horas de parto', vacio = True)

        # Al nacer el niño necesitó...
        self.nino_necesito = mi_formulario(self.canvas, 0.775, 0.575, 'Al nacer el niño necesitó...', vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            self.controller.entrevista_eni.agregar_datos('antecedentes_natales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_natales2')


class antecedentes_natales2(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.225, 'Antecedentes Natales', 2, ANCHOR = NW)
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
        # Cianosis (día de inicio)
        self.cianosis = mi_formulario(self.canvas, 0.775, 0.3, 'Cianosis (día de inicio)', vacio = True)

        # Cianosis (duración)
        self.cianosis_duracion = mi_formulario(self.canvas, 0.775, 0.375, 'Cianosis (duración)', vacio = True)

        # Ictericia (día de inicio)
        self.ictericia = mi_formulario(self.canvas, 0.775, 0.45, 'Ictericia (día de inicio)', vacio = True)

        # Ictericia (duración)
        self.ictericia_duracion = mi_formulario(self.canvas, 0.775, 0.525, 'Ictericia (duración)', vacio = True)

        # Sufrimiento nasal
        self.sufrimiento_nasal = mi_seleccion(self.canvas, self.ictericia_duracion.obtener_label_x(), 0.6, 'Sufrimiento nasal', ["Si", "No"],vacio = True)

        # Apgar
        self.apgar = mi_seleccion(self.canvas, self.ictericia_duracion.obtener_label_x(), 0.675, 'Apgar', ["Si", "No"], vacio = True)

        # Peso
        self.peso = mi_formulario(self.canvas, 0.775, 0.75, 'Peso', vacio = True)

        # Talla
        self.talla = mi_formulario(self.canvas, 0.775, 0.825, 'Talla', vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            self.controller.entrevista_eni.agregar_datos('antecedentes_natales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales')