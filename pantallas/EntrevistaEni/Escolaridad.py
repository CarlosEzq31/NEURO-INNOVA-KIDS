from classes.mi_frame import *

class escolaridad(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad', 3, ANCHOR = NW)
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
        # ¿Asiste a la escuela?
        self.asiste_escuela = mi_seleccion(self.canvas, 0.548, 0.3, '¿Asiste a la escuela?', ['Si', 'No'],vacio = True)

        # ¿Por qué no asiste?
        self.no_asiste_escuela = mi_formulario(self.canvas, 0.775, 0.375, '¿Por qué no asiste a la escuela?', vacio = True)

        # Eduacación bilingüe
        self.bilingue = mi_seleccion(self.canvas, 0.548, 0.45, 'Eduacación bilingüe', ['Si', 'No'],vacio = True)

        # Segunda lengua
        self.segunda_lengua = mi_formulario(self.canvas, 0.775, 0.525, 'Segunda lengua', vacio = True)

        # Edad de inicio
        self.edad_inicio = mi_formulario(self.canvas, 0.775, 0.6, 'Edad de inicio', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad2')

class escolaridad2(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Problemas específicos)', 3, ANCHOR = NW)
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
        # Lectura
        self.lectura = mi_seleccion(self.canvas, 0.548, 0.3, 'Lectura', ['Si', 'No'], vacio = True)

        # Escritura
        self.escritura = mi_seleccion(self.canvas, 0.548, 0.375, 'Escritura', ['Si', 'No'], vacio = True)

        # Cálculo
        self.calculo = mi_seleccion(self.canvas, 0.548, 0.45, 'Cálculo', ['Si', 'No'], vacio = True)

        # Hiperactividad
        self.hiperactividad = mi_seleccion(self.canvas, 0.548, 0.525, 'Hiperactividad', ['Si', 'No'], vacio = True)

        # Atención
        self.atencion = mi_seleccion(self.canvas, 0.548, 0.6, 'Atención', ['Si', 'No'], vacio = True)

        # Otros
        self.otros = mi_formulario(self.canvas, 0.775, 0.675, 'Otros', vacio = True)

        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad3')

class escolaridad3(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Guardería)', 3, ANCHOR = NW)
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
        # Guardería
        self.guarderia = mi_seleccion(self.canvas, 0.548, 0.3, 'Guardería', ['Si', 'No'], vacio = True)

        # Edad de ingreso
        self.edad_ingreso = mi_formulario(self.canvas, 0.775, 0.375, 'Edad de ingreso', vacio = True)

        # ¿Cuántos años?
        self.anios = mi_formulario(self.canvas, 0.775, 0.45, '¿Cuántos años?', vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad4')

class escolaridad4(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Jardín de Niños)', 3, ANCHOR = NW)
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
        # Jardín de Niños
        self.jardin = mi_seleccion(self.canvas, 0.548, 0.3, 'Jardín de Niños', ['Si', 'No'], vacio = True)

        # Edad de ingreso
        self.edad_ingreso = mi_formulario(self.canvas, 0.775, 0.375, 'Edad de ingreso', vacio = True)

        # ¿Cuántos años?
        self.anios = mi_formulario(self.canvas, 0.775, 0.45, '¿Cuántos años?', vacio = True)

        # Rendimiento
        self.rendimiento = mi_seleccion(self.canvas, 0.548, 0.525, 'Rendimiento', ['Bueno', 'Malo', 'Regular'], vacio = True)

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad5')

# Primaria
class escolaridad5(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Primaría)', 3, ANCHOR = NW)
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
        # Edad de ingreso
        self.edad_ingreso = mi_formulario(self.canvas, 0.775, 0.3, 'Edad de ingreso', vacio = True)

        # ¿Cuántos años?
        self.anios = mi_formulario(self.canvas, 0.775, 0.375, '¿Cuántos años?', vacio = True)

        # Rendimiento
        self.rendimiento = mi_seleccion(self.canvas, 0.548, 0.45, 'Rendimiento', ['Bueno', 'Malo', 'Regular'], vacio = True)

        # Grados repetidos
        self.grados_repetidos = mi_formulario(self.canvas, 0.775, 0.525, 'Grados repetidos', vacio = True)

        # Clases particulares
        self.clases_particulares = mi_seleccion(self.canvas, 0.548, 0.6, 'Clases particulares', ['Si', 'No'], vacio = True)

        # Edad o grado escolar (clases particulares)
        self.edad_clases_particulares = mi_formulario(self.canvas, 0.775, 0.675, 'Edad o grado escolar', vacio = True)

        # Materias (clases particulares)
        self.materias = mi_formulario(self.canvas, 0.775, 0.75, 'Materias', vacio = True)

        # Terapias de apoyo (clases particulares)
        self.terapias = mi_seleccion(self.canvas, 0.548, 0.825, 'Terapias de apoyo', ['Si', 'No'], vacio = True)



    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad6')

class escolaridad6(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Primaría)', 3, ANCHOR = NW)
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
        # Edad o grado (terapias)
        self.edad_terapias = mi_formulario(self.canvas, 0.775, 0.3, 'Edad o grado (terap.)', vacio = True)

        # ¿Qué tipo?
        self.tipo = mi_formulario(self.canvas, 0.775, 0.375, '¿Qué tipo?', vacio = True)

        # ¿Cuánto tiempo?
        self.tiempo = mi_formulario(self.canvas, 0.775, 0.45, '¿Cuánto tiempo?', vacio = True)

        # Problemas específicos
        self.problemas_especificos = mi_seleccion(self.canvas, 0.548, 0.525, 'Problemas específicos', ['Si', 'No'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad7')

# Secundaria
class escolaridad7(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Secundaría)', 3, ANCHOR = NW)
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
        # Edad de ingreso
        self.edad_ingreso = mi_formulario(self.canvas, 0.775, 0.3, 'Edad de ingreso', vacio = True)

        # ¿Cuántos años?
        self.anios = mi_formulario(self.canvas, 0.775, 0.375, '¿Cuántos años?', vacio = True)

        # Rendimiento
        self.rendimiento = mi_seleccion(self.canvas, 0.548, 0.45, 'Rendimiento', ['Bueno', 'Malo', 'Regular'], vacio = True)

        # Grados repetidos
        self.grados_repetidos = mi_formulario(self.canvas, 0.775, 0.525, 'Grados repetidos', vacio = True)

        # Clases particulares
        self.clases_particulares = mi_seleccion(self.canvas, 0.548, 0.6, 'Clases particulares', ['Si', 'No'], vacio = True)

        # Edad o grado escolar (clases particulares)
        self.edad_clases_particulares = mi_formulario(self.canvas, 0.775, 0.675, 'Edad o grado escolar', vacio = True)

        # Materias (clases particulares)
        self.materias = mi_formulario(self.canvas, 0.775, 0.75, 'Materias', vacio = True)

        # Terapias de apoyo (clases particulares)
        self.terapias = mi_seleccion(self.canvas, 0.548, 0.825, 'Terapias de apoyo', ['Si', 'No'], vacio = True)



    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad8')

class escolaridad8(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Secundaría)', 3, ANCHOR = NW)
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
        # Edad o grado (terapias)
        self.edad_terapias = mi_formulario(self.canvas, 0.775, 0.3, 'Edad o grado (terap.)', vacio = True)

        # ¿Qué tipo?
        self.tipo = mi_formulario(self.canvas, 0.775, 0.375, '¿Qué tipo?', vacio = True)

        # ¿Cuánto tiempo?
        self.tiempo = mi_formulario(self.canvas, 0.775, 0.45, '¿Cuánto tiempo?', vacio = True)

        # Problemas específicos
        self.problemas_especificos = mi_seleccion(self.canvas, 0.548, 0.525, 'Problemas específicos', ['Si', 'No'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad9')

# Preparatoria
class escolaridad9(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Preparatoría)', 3, ANCHOR = NW)
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
        # Edad de ingreso
        self.edad_ingreso = mi_formulario(self.canvas, 0.775, 0.3, 'Edad de ingreso', vacio = True)

        # ¿Cuántos años?
        self.anios = mi_formulario(self.canvas, 0.775, 0.375, '¿Cuántos años?', vacio = True)

        # Rendimiento
        self.rendimiento = mi_seleccion(self.canvas, 0.548, 0.45, 'Rendimiento', ['Bueno', 'Malo', 'Regular'], vacio = True)

        # Grados repetidos
        self.grados_repetidos = mi_formulario(self.canvas, 0.775, 0.525, 'Grados repetidos', vacio = True)

        # Clases particulares
        self.clases_particulares = mi_seleccion(self.canvas, 0.548, 0.6, 'Clases particulares', ['Si', 'No'], vacio = True)

        # Edad o semestre (clases particulares)
        self.edad_clases_particulares = mi_formulario(self.canvas, 0.775, 0.675, 'Edad o semestre', vacio = True)

        # Materias (clases particulares)
        self.materias = mi_formulario(self.canvas, 0.775, 0.75, 'Materias', vacio = True)

        # Terapias de apoyo (clases particulares)
        self.terapias = mi_seleccion(self.canvas, 0.548, 0.825, 'Terapias de apoyo', ['Si', 'No'], vacio = True)



    def siguiente(self):
        if self.validar_formularios():
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad10')

class escolaridad10(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Preparatoria)', 3, ANCHOR = NW)
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
        # Edad o semestre (terapias)
        self.edad_terapias = mi_formulario(self.canvas, 0.775, 0.3, 'Edad o semestre (terap.)', vacio = True)

        # ¿Qué tipo?
        self.tipo = mi_formulario(self.canvas, 0.775, 0.375, '¿Qué tipo?', vacio = True)

        # ¿Cuánto tiempo?
        self.tiempo = mi_formulario(self.canvas, 0.775, 0.45, '¿Cuánto tiempo?', vacio = True)

        # Problemas específicos
        self.problemas_especificos = mi_seleccion(self.canvas, 0.548, 0.525, 'Problemas específicos', ['Si', 'No'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad11')

# Aptitudes e intereses
class escolaridad11(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Aptitudes e intereses)', 3, ANCHOR = NW)
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
        # Lectura
        self.lectura = mi_seleccion(self.canvas, 0.548, 0.3, 'Lectura', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Escritura
        self.escritura = mi_seleccion(self.canvas, 0.548, 0.375, 'Escritura', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Matemáticas
        self.matematicas = mi_seleccion(self.canvas, 0.548, 0.45, 'Matemáticas', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Deportes
        self.deportes = mi_seleccion(self.canvas, 0.548, 0.525, 'Deportes', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Dibujo
        self.dibujo = mi_seleccion(self.canvas, 0.548, 0.6, 'Dibujo', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Ciencias
        self.ciencias = mi_seleccion(self.canvas, 0.548, 0.675, 'Ciencias', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Ciencias sociales
        self.ciencias_sociales = mi_seleccion(self.canvas, 0.548, 0.75, 'Ciencias sociales', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            
            self.controller.entrevista_eni.agregar_datos(self.datos)
            self.controller.mostrar_pantalla(self, 'escolaridad12')

class escolaridad12(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Escolaridad\n(Aptitudes e intereses)', 3, ANCHOR = NW)
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
        # Música
        self.musica = mi_seleccion(self.canvas, 0.548, 0.3, 'Música', ['Mayor d.', 'Menor d.', 'Prefer.', 'No pref.'], vacio = True)

        # Otras
        self.otras = mi_formulario(self.canvas, 0.775, 0.375, 'Otras', vacio = True)

        # Comentarios
        self.comentarios = mi_formulario(self.canvas, 0.775, 0.45, 'Comentarios', vacio = True)

    def siguiente(self):
        if self.validar_formularios():
            self.controller.entrevista_eni.agregar_datos(self.datos)
            print(self.controller.entrevista_eni)
            # self.controller.mostrar_pantalla(self, 'pruebas')