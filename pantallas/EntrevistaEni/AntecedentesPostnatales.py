from classes.mi_frame import *

# Alimentación
class antecedentes_postnatales(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Alimentación Materna
        self.alimentacion_materna = mi_seleccion(self.canvas, 0.548, 0.3, 'Alimentación Materna', ["Si", "No"], vacio = True)

        # Alimentación artificial
        self.alimentacion_artificial = mi_seleccion(self.canvas, 0.548, 0.375, 'Alimentación Artificial', ["Si", "No"], vacio = True)

        # Alimentación mixta
        self.alimentacion_mixta = mi_seleccion(self.canvas, 0.548, 0.45, 'Alimentación Mixta', ["Si", "No"], vacio = True)

        # Vómitos
        self.vomitos = mi_seleccion(self.canvas, 0.548, 0.525, 'Vómitos', ["Si", "No"], vacio = True)

        # Succión
        self.succion = mi_seleccion(self.canvas, 0.548, 0.6, 'Succión pobre', ["Si", "No"], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales2')

# Condiciones durante el primer año
class antecedentes_postnatales2(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Actividad del primer año
        self.actividad_primer_ano = mi_formulario(self.canvas, 0.775, 0.3, 'Actividad del primer año', vacio = True)

        # ¿Gateó?
        self.gateo = mi_seleccion(self.canvas, self.actividad_primer_ano.obtener_label_x(), 0.375, '¿Gateó?', ["Si", "No"], vacio = True)

        # ¿Caminó solo?
        self.camino_solo = mi_seleccion(self.canvas, self.actividad_primer_ano.obtener_label_x(), 0.45, '¿Caminó solo?', ["Si", "No"], vacio = True)

        # ¿Control de esfínteres?
        self.control_esfinteres = mi_seleccion(self.canvas, self.actividad_primer_ano.obtener_label_x(), 0.525, '¿Control de esfínteres?', ["Si", "No"], vacio = True)

        # ¿Habla?
        self.habla = mi_seleccion(self.canvas, self.actividad_primer_ano.obtener_label_x(), 0.6, '¿Habla?', ["Si", "No"], vacio = True)

        # Balbuceo (edad)
        self.balbuceo_edad = mi_formulario(self.canvas, 0.775, 0.675, 'Balbuceo (edad)', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales3')

# Condiciones
class antecedentes_postnatales3(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Dijo 3 palabras (edad)
        self.dijo_3_palabras_edad = mi_formulario(self.canvas, 0.775, 0.3, 'Dijo 3 palabras (edad)', vacio = True)

        # Unió 2 palabras (edad)
        self.unio_2_palabras_edad = mi_formulario(self.canvas, 0.775, 0.375, 'Unió 2 palabras (edad)', vacio = True)

        # Construyo frases (edad)
        self.construyo_frases_edad = mi_formulario(self.canvas, 0.775, 0.45, 'Construyo frases (edad)', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales4')


class antecedentes_postnatales4(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Autosuficiente en
        self.autosuficiente_en = mi_formulario(self.canvas, 0.775, 0.3, 'Autosuficiente en', vacio = True)

        # Deficiente en
        self.deficiente_en = mi_formulario(self.canvas, 0.775, 0.375, 'Deficiente en', vacio = True)

        # ¿Corre?
        self.corre = mi_seleccion(self.canvas, self.deficiente_en.obtener_label_x(), 0.45, '¿Corre?', ["Si", "No"], vacio = True) 

        # ¿Anda en bicicleta?
        self.anda_en_bicicleta = mi_seleccion(self.canvas, self.deficiente_en.obtener_label_x(), 0.525, '¿Anda en bicicleta?', ["Si", "No"], vacio = True)

        # ¿Juega?
        self.juega = mi_seleccion(self.canvas, self.deficiente_en.obtener_label_x(), 0.6, '¿Juega?', ["Si", "No"], vacio = True)

        # Gusto por los deportes
        self.gusto_por_los_deportes = mi_seleccion(self.canvas, self.deficiente_en.obtener_label_x(), 0.675, 'Gusto por los deportes', ["Si", "No"], vacio = True)

        # ¿Escribe?
        self.escribe = mi_seleccion(self.canvas, self.deficiente_en.obtener_label_x(), 0.75, '¿Escribe?', ["Si", "No"], vacio = True)

        # ¿Dibuja?
        self.dibuja = mi_seleccion(self.canvas, self.deficiente_en.obtener_label_x(), 0.825, '¿Dibuja?', ["Si", "No"], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales5')

# Desarrollo actual
class antecedentes_postnatales5(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Recorta
        self.recorta = mi_seleccion(self.canvas, 0.548, 0.3, 'Recorta', ["Si", "No"], vacio = True)

        # Produce sonidos con la lengua
        self.produce_sonidos_con_la_lengua = mi_seleccion(self.canvas, 0.548, 0.375, 'Produce sonidos con la lengua', ["Si", "No"], vacio = True)

        # Tartamudea
        self.tartamudea = mi_seleccion(self.canvas, 0.548, 0.45, 'Tartamudea', ["Si", "No"], vacio = True)

        # Dificultad de expresión
        self.dificultad_de_expresion = mi_seleccion(self.canvas, 0.548, 0.525, 'Dificultad de expresión', ["Si", "No"], vacio = True)

        # Dificultad de comprensión
        self.dificultad_de_comprension = mi_seleccion(self.canvas, 0.548, 0.6, 'Dificultad de comprensión', ["Si", "No"], vacio = True)

        # Lengua predominante
        self.lengua_predominante = mi_formulario(self.canvas, 0.775, 0.675, 'Lengua predominante', vacio = True)

        # Lengua secundaria
        self.lengua_secundaria = mi_formulario(self.canvas, 0.775, 0.75, 'Lengua secundaria', vacio = True)
        
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales6')

# Antecedentes patológicos
class antecedentes_postnatales6(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Traumatismos
        self.traumatismos = mi_seleccion(self.canvas, 0.548, 0.3, 'Traumatismos', ["Si", "No"], vacio = True)

        # Fecha de traumatismo
        self.fecha_traumatismo = mi_formulario(self.canvas, 0.775, 0.375, 'Fecha de traumatismo', vacio = True)

        # Duración de traumatismo
        self.duracion_traumatismo = mi_formulario(self.canvas, 0.775, 0.45, 'Duración de traumatismo', vacio = True)

        # Cirugías
        self.cirugias = mi_seleccion(self.canvas, 0.548, 0.525, 'Cirugías', ["Si", "No"], vacio = True)

        # Motivo de cirugía
        self.motivo_cirugia = mi_formulario(self.canvas, 0.775, 0.6, 'Motivo de cirugía', vacio = True)

        # Convulsiones
        self.convulsiones = mi_formulario(self.canvas, 0.775, 0.675, 'Convulsiones', vacio = True)

        # Edad de Inicio
        self.edad_inicio = mi_formulario(self.canvas, 0.775, 0.75, 'Edad de Inicio', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales7')


class antecedentes_postnatales7(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Tipo de traumatismos
        self.tipo_convulsiones = mi_formulario(self.canvas, 0.775, 0.3, 'Tipo de convulsiones', vacio = True)

        # Frecuencia (traumatismos)
        self.frecuencia_convulsiones = mi_formulario(self.canvas, 0.775, 0.375, 'Frecuencia', vacio = True)

        # Con Fiebre
        self.con_fiebre = mi_seleccion(self.canvas, 0.548, 0.45, 'Con fiebre', ["Si", "No"], vacio = True)

        # Medicación
        self.medicacion = mi_formulario(self.canvas, 0.775, 0.525, 'Medicación', vacio = True)

        # Sarampión
        self.sarampion = mi_seleccion(self.canvas, 0.548, 0.6, 'Sarampión', ["Si", "No"], vacio = True)

        # Meningitis
        self.meningitis = mi_seleccion(self.canvas, 0.548, 0.675, 'Meningitis', ["Si", "No"], vacio = True)

        # Encefalítis
        self.encefalitis = mi_seleccion(self.canvas, 0.548, 0.75, 'Encefalítis', ["Si", "No"], vacio = True)

        # Otras
        self.otras = mi_formulario(self.canvas, 0.775, 0.825, 'Otras', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales8')


class antecedentes_postnatales8(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # ¿A qué es alergic@?
        self.alergias = mi_formulario(self.canvas, 0.775, 0.3, '¿A qué es alergic@?', vacio = True)

        # Manifestaciones
        self.manifestaciones = mi_formulario(self.canvas, 0.775, 0.375, 'Manifestaciones', vacio = True)

        # Intoxicación por plomo
        self.intoxicacion_plomo = mi_seleccion(self.canvas, 0.548, 0.45, 'Intoxicación por plomo', ["Si", "No"], vacio = True)

        # Por medicamentos
        self.por_medicamentos = mi_seleccion(self.canvas, 0.548, 0.6, 'Por medicamentos', ["Si", "No"], vacio = True)

        # Otros
        self.otros = mi_formulario(self.canvas, 0.775, 0.525, 'Otros', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales9')


class antecedentes_postnatales9(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Audición normal
        self.audicion_normal = mi_seleccion(self.canvas, 0.548, 0.3, 'Audición normal', ["Si", "No"], vacio = True)

        # Audometría
        self.audometria = mi_seleccion(self.canvas, 0.548, 0.375, 'Audometría', ["Si", "No"], vacio = True)

        # Fecha de audiometría
        self.fecha_audiometria = mi_formulario(self.canvas, 0.775, 0.45, 'Fecha de audiometría', vacio = True)

        # Resulatdo de audiometría
        self.resultado_audiometria = mi_formulario(self.canvas, 0.775, 0.525, 'Resultado de audiometría', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_postnatales10')


class antecedentes_postnatales10(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Antecedentes Postnatales', 3, ANCHOR = NW)
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
        # Visión normal
        self.vision_normal = mi_seleccion(self.canvas, 0.548, 0.3, 'Visión normal', ["Si", "No"], vacio = True)

        # Examen
        self.examen = mi_seleccion(self.canvas, 0.548, 0.375, 'Examen', ["Si", "No"], vacio = True)

        # Fecha de examen
        self.fecha_examen = mi_formulario(self.canvas, 0.775, 0.45, 'Fecha de examen', vacio = True)

        # Resulatdo de examen
        self.resultado_examen = mi_formulario(self.canvas, 0.775, 0.525, 'Resultado de examen', vacio = True)

        # Lentes
        self.lentes = mi_seleccion(self.canvas, 0.548, 0.6, 'Lentes', ["Si", "No"], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            self.controller.entrevista_eni.agregar_datos('antecedentes_postnatales', self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento')
            print(self.controller.entrevista_eni.datos['antecedentes_postnatales'])