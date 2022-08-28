from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.mi_seleccion import *
from classes.mi_formulario import *

class comportamiento(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Comportamiento\n(actividad)', 3, ANCHOR = NW)
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
        # Hipoactivo
        self.hipoactivo = mi_seleccion(self.canvas, 0.548, 0.3, 'Hipoactivo', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Hiperactivo
        self.hiperactivo = mi_seleccion(self.canvas, 0.548, 0.375, 'Hiperactivo', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Destructivo
        self.destructivo = mi_seleccion(self.canvas, 0.548, 0.45, 'Destructivo', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Agresivo
        self.agresivo = mi_seleccion(self.canvas, 0.548, 0.525, 'Agresivo', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento2')

class comportamiento2(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.225, 'Comportamiento\n(atención)', 3, ANCHOR = NW)
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
        # Constante
        self.constante = mi_seleccion(self.canvas, 0.548, 0.3, 'Constante', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Corta
        self.corta = mi_seleccion(self.canvas, 0.548, 0.375, 'Corta', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Nula
        self.nula = mi_seleccion(self.canvas, 0.548, 0.45, 'Nula', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Variable
        self.variable = mi_seleccion(self.canvas, 0.548, 0.525, 'Variable', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento3')

class comportamiento3(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Crísis Coléricas)', 3, ANCHOR = NW)
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
        # Berrinches
        self.berrinches = mi_seleccion(self.canvas, 0.548, 0.3, 'Berrinches', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Arroja cosas al enojarse
        self.arroja = mi_seleccion(self.canvas, 0.548, 0.375, 'Arroja cosas al enojarse', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Arremete verbalmente
        self.arremete = mi_seleccion(self.canvas, 0.548, 0.45, 'Arremete verbalmente', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Irascible
        self.irascible = mi_seleccion(self.canvas, 0.548, 0.525, 'Irascible', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento4')

class comportamiento4(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Adaptación)', 3, ANCHOR = NW)
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
        # Se separa de los padres
        self.separa = mi_seleccion(self.canvas, 0.548, 0.3, 'Se separa de los padres', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Se adecua a la situación
        self.adecuacion = mi_seleccion(self.canvas, 0.548, 0.375, 'Se adecua a la situación', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Reacciones catastróficas
        self.reacciones = mi_seleccion(self.canvas, 0.548, 0.45, 'Reacciones catastróficas', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento5')

class comportamiento5(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Labilidad emocional)', 3, ANCHOR = NW)
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
        # Llora muy facilmente
        self.llorar = mi_seleccion(self.canvas, 0.548, 0.3, 'Llora muy facilmente', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Pasa del llanto a la risa
        self.risa = mi_seleccion(self.canvas, 0.548, 0.375, 'Pasa del llanto a la risa', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Se emociona fácilmente
        self.emocion = mi_seleccion(self.canvas, 0.548, 0.45, 'Se emociona fácilmente', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento6')

class comportamiento6(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Relaciones familiares)', 3, ANCHOR = NW)
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
        # Difícil relación con papá
        self.papa = mi_seleccion(self.canvas, 0.548, 0.3, 'Difícil relación con papá', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Difícil relación con mamá
        self.mama = mi_seleccion(self.canvas, 0.548, 0.375, 'Difícil relación con mamá', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Difícil relación con hermanos
        self.hermanos = mi_seleccion(self.canvas, 0.548, 0.45, 'Difícil relación con herm.', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)
        


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento7')

class comportamiento7(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Sueño)', 3, ANCHOR = NW)
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
        # Sonambulismo
        self.sonambulismo = mi_seleccion(self.canvas, 0.548, 0.3, 'Sonambulismo', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Promedio de horas de sueño
        self.sueno = mi_formulario(self.canvas, 0.775, 0.375, 'Promedio de horas de sueño', vacio = True)

        # Duerme siesta
        self.siesta = mi_seleccion(self.canvas, 0.548, 0.45, 'Duerme siesta', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Pesadillas
        self.pesadillas = mi_seleccion(self.canvas, 0.548, 0.525, 'Pesadillas', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Dificultad para conciliar el sueño
        self.conciliar = mi_seleccion(self.canvas, 0.548, 0.6, 'Dificultad para conciliar el sueño', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Dificultad para despertar
        self.despertar = mi_seleccion(self.canvas, 0.548, 0.675, 'Dificultad para despertar', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Sueño continuo
        self.continuo = mi_seleccion(self.canvas, 0.548, 0.75, 'Sueño continuo', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento8')

class comportamiento8(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(A la hora de comer)', 3, ANCHOR = NW)
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
        # Permanece sentado
        self.sentado = mi_seleccion(self.canvas, 0.548, 0.3, 'Permanece sentado', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Juega con los cubiertos
        self.cubiertos = mi_seleccion(self.canvas, 0.548, 0.375, 'Juega con los cubiertos', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Derrama alimentos
        self.alimentos = mi_seleccion(self.canvas, 0.548, 0.45, 'Derrama alimentos', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Come sin distracción
        self.sin_dist = mi_seleccion(self.canvas, 0.548, 0.525, 'Come sin distracción', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)


    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento9')

class comportamiento9(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Hábitos alimenticios)', 3, ANCHOR = NW)
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
        # ¿Comidas al día?
        self.comidas = mi_seleccion(self.canvas, 0.548, 0.3, '¿Comidas al día?', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # ¿Selectivo con los alimentos?
        self.selectivo = mi_seleccion(self.canvas, 0.548, 0.375, '¿Selectivo con los alimentos?', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento10')

class comportamiento10(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Tiempo libre)', 3, ANCHOR = NW)
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
        # TV
        self.tv = mi_seleccion(self.canvas, 0.548, 0.3, 'TV', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Videojuegos
        self.videojuegos = mi_seleccion(self.canvas, 0.548, 0.375, 'Videojuegos', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Computadora
        self.computadora = mi_seleccion(self.canvas, 0.548, 0.45, 'Computadora', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Juego al aire libre
        self.juego_al_aire_libre = mi_seleccion(self.canvas, 0.548, 0.525, 'Juego al aire libre', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Juego de fantasía
        self.juego_fantasia = mi_seleccion(self.canvas, 0.548, 0.6, 'Juego de fantasía', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Lectura
        self.lectura = mi_seleccion(self.canvas, 0.548, 0.675, 'Lectura', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Juegos colectivos
        self.juegos_colectivos = mi_seleccion(self.canvas, 0.548, 0.75, 'Juegos colectivos', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Juegos de construcción
        self.juegos_construccion = mi_seleccion(self.canvas, 0.548, 0.825, 'Juegos de construcción', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento11')

class comportamiento11(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Socialización)', 3, ANCHOR = NW)
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
        # Retraído
        self.retraido = mi_seleccion(self.canvas, 0.548, 0.3, 'Retraído', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Abierto
        self.abierto = mi_seleccion(self.canvas, 0.548, 0.375, 'Abierto', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Aislado
        self.aislado = mi_seleccion(self.canvas, 0.548, 0.45, 'Aislado', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Facilidad para hacer amigos
        self.facilidad_amigos = mi_seleccion(self.canvas, 0.548, 0.525, 'Facilidad para hacer amigos', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Amigos de su edad
        self.amigos_edad = mi_seleccion(self.canvas, 0.548, 0.6, 'Amigos de su edad', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Amigos mayores
        self.amigos_mayores = mi_seleccion(self.canvas, 0.548, 0.675, 'Amigos mayores', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Amigos menores
        self.amigos_menores = mi_seleccion(self.canvas, 0.548, 0.75, 'Amigos menores', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)

        # Otros amigos
        self.otros_amigos = mi_seleccion(self.canvas, 0.548, 0.825, 'Otros amigos', ['Casi nunca', 'Algunas v.', 'Muchas v.', 'Siempre'], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'comportamiento12')

class comportamiento12(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.045, 0.224, 'Comportamiento\n(Inteligencia)', 3, ANCHOR = NW)
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
        # Inteligencia (Esperada, mayor, menor)
        self.inteligencia = mi_seleccion(self.canvas, 0.548, 0.3, 'Inteligencia', ['Esperada', 'Mayor', 'Menor'], vacio = True)
        

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'disciplina')