from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.mi_seleccion import *
from classes.mi_formulario import *

class antecedentes_prenatales(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.225, 'Antecedentes prenatales', 3, ANCHOR = NW)
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
        # Semanas de gestación
        self.semanas_gestacion = mi_formulario(self.canvas, 0.775, 0.35, 'Semanas gestación', vacio = True)
        
        # Embarazo deseado
        self.embarazo_deseado = mi_seleccion(self.canvas, self.semanas_gestacion.obtener_label_x(), 0.425, "Embarazo deseado", ["Si", "No"], vacio = True)

        # Comentarios 
        self.comentarios = mi_formulario(self.canvas, 0.775, 0.5, 'Comentarios', vacio = True)

        # Drogas en el embarazo
        self.drogas_embarazo = mi_seleccion(self.canvas, self.comentarios.obtener_label_x(), 0.575, "Drogras embarazo", ["Si", "No"], vacio = True)

        # ¿Cuales?
        self.cuales_embarazo = mi_formulario(self.canvas, 0.775, 0.65, '¿Cuales?', vacio = True)

        # Calidad de alimentacion 1-3
        self.calidad_alimentacion = mi_seleccion(self.canvas, self.cuales_embarazo.obtener_label_x(), 0.725, "Calidad aliment.", ["1", "2", "3"], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_prenatales2')

class antecedentes_prenatales2(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.225, 'Antecedentes prenatales', 3, ANCHOR = NW)
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
        # Rubéola
        self.rubeola = mi_seleccion(self.canvas, 0.548, 0.35, "Rubéola", ["Si", "No"], vacio = True)

        # Varicela
        self.varicela = mi_seleccion(self.canvas, 0.548, 0.425, "Varicela", ["Si", "No"], vacio = True)
        
        # Edema
        self.edema = mi_seleccion(self.canvas, 0.548, 0.5, "Edema", ["Si", "No"], vacio = True)

        # Traumatismos
        self.traumatismos = mi_seleccion(self.canvas, 0.548, 0.575, "Traumatismos", ["Si", "No"], vacio = True)

        # Amenaza aborto
        self.amenaza_aborto = mi_seleccion(self.canvas, 0.548, 0.65, "Amenaza aborto", ["Si", "No"], vacio = True)

        # Sífilis
        self.sifilis = mi_seleccion(self.canvas, 0.548, 0.725, "Sífilis", ["Si", "No"], vacio = True)

        # Toxoplasmosis
        self.toxoplasmosis = mi_seleccion(self.canvas, 0.548, 0.8, "Toxoplasmosis", ["Si", "No"], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_prenatales3')

class antecedentes_prenatales3(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.225, 'Antecedentes prenatales', 3, ANCHOR = NW)
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
        # VIH
        self.vih = mi_seleccion(self.canvas, 0.548, 0.35, "VIH", ["Si", "No"], vacio = True)

        # Hipertensión
        self.hipertension = mi_seleccion(self.canvas, 0.548, 0.425, "Hipertensión", ["Si", "No"], vacio = True)

        # Toxemia
        self.toxemia = mi_seleccion(self.canvas, 0.548, 0.5, "Toxemia", ["Si", "No"], vacio = True)

        # Otros
        self.otros = mi_seleccion(self.canvas, 0.548, 0.575, "Otros", ["Si", "No"], vacio = True)
        
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_prenatales4')

class antecedentes_prenatales4(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.225, 'Antecedentes prenatales\n(exposición)', 2, ANCHOR = NW)
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
        # ¿Cuáles vacunas?
        self.cuales_vacunas = mi_seleccion(self.canvas, 0.548, 0.3, "¿Cuáles vacunas?", ["Si", "No"], vacio = True)

        # ¿En que mes? (vacunas)
        self.en_que_mes_vacunas = mi_formulario(self.canvas, 0.775, 0.375, '¿En qué mes?', vacio = True)

        # Rayos X
        self.rayos_x = mi_seleccion(self.canvas, 0.548, 0.45, "Rayos X", ["Si", "No"], vacio = True)

        # ¿En que mes? (rayos x)
        self.en_que_mes_rayos_x = mi_formulario(self.canvas, 0.775, 0.525, '¿En qué mes?', vacio = True)

        # ¿Cuáles medicamentos?
        self.cuales_medicamentos = mi_formulario(self.canvas, 0.775, 0.6, '¿Cuáles medicamentos?', vacio = True)

        # ¿En que mes? (medicamentos)
        self.en_que_mes_medicamentos = mi_formulario(self.canvas, 0.775, 0.675, '¿En qué mes?', vacio = True)

        # Otros
        self.otros = mi_formulario(self.canvas, 0.775, 0.75, 'Otros', vacio = True)

        # ¿En que mes? (otros)
        self.en_que_mes_otros = mi_formulario(self.canvas, 0.775, 0.825, '¿En qué mes?', vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'antecedentes_natales')