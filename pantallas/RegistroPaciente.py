from classes.paciente import *
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.mi_seleccion import *
from classes.mi_formulario import *

class registro_paciente(mi_frame):

    def __init__(self, parent, controller):
        # inicializamos el frame
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.25),int(self.alto*0.4), image = self.controller.logo, anchor = CENTER)
        
        # boton de atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)
        
        # boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())

        # boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)

        # formulario de registro
        # nombre
        self.nombre = mi_formulario(self.canvas, 0.775, 0.3, 'Nombre', focus = True)

        # domicilio
        self.domicilio = mi_formulario(self.canvas, 0.775, 0.4, 'Domicilio')

        # fecha de nacimiento
        self.fecha_nacimiento = mi_formulario(self.canvas, 0.775, 0.5, 'Fecha de nacimiento', placeholder = '04/04/2022', fecha = True)

        # sexo
        self.sexo = mi_seleccion(self.canvas, self.fecha_nacimiento.obtener_label_x(), 0.6, 'Sexo', ['Hombre', 'Mujer'])

        # boton siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.85, 0.9, 'Siguiente', 
                                        'rosa', lambda x: self.siguiente())

    def siguiente(self):
        if self.validar_formularios():
            self.controller.paciente = Paciente()
            self.controller.paciente.datos_nuevos(self.datos)
            self.controller.mostrar_pantalla(self, 'registro_paciente_2')

    def validar_formularios(self):
        self.datos = {}
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value) or 'mi_seleccion' in str(value):
                if value.datos() == '':
                    self.texto_aviso(0.5, 0.05, 'Debes rellenar todos los campos')
                    return False
                else:
                    self.datos[key] = value.datos()
        return True

    def limpiar_formularios(self):
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value) or 'mi_seleccion' in str(value):
                value.limpiar()

class registro_paciente_2(mi_frame):

    def __init__(self, parent, controller):
        # inicializamos el frame
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.25),int(self.alto*0.4), image = self.controller.logo, anchor = CENTER)
        
        # boton de atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)
        
        # boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())

        # boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)

        # formulario de registro

        # Datos de contacto
        self.datos_contacto = mi_formulario(self.canvas, 0.775, 0.3, 'Datos de contacto',
                                            placeholder = 'ej. Nombre: Alicia, Teléfono: 123456789, Parentesco: Madre')

        # Lentes
        self.lentes = mi_seleccion(self.canvas, self.datos_contacto.obtener_label_x(), 0.4, '¿Usa lentes?', ['Si', 'No'])

        # Lateralidad
        self.lateralidad = mi_seleccion(self.canvas, self.datos_contacto.obtener_label_x(), 0.5, 'Lateralidad', ['Derecha', 'Izquierda', 'Ambas'])

        # Diagnóstico previo
        self.diagnostico = mi_formulario(self.canvas, 0.775, 0.6, 'Diagnóstico previo', placeholder = 'ej. Diabetes, Hipertensión, etc.', vacio = True)

        # Medicamentos
        self.medicamentos = mi_formulario(self.canvas, 0.775, 0.7, 'Medicamentos', placeholder = 'ej. Paracetamol, etc.', vacio = True)

        # boton siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.85, 0.9, 'Registrar paciente', 
                                        'rosa', lambda x: self.siguiente())

    def siguiente(self):
        if self.validar_formularios():
            self.controller.paciente.datos_nuevos(self.datos)
            self.controller.paciente.datos()
            self.controller.paciente.registrar()
            self.texto_aviso(0.5, 0.05, 'Paciente registrado')
            self.boton_pruebas = mi_boton(self.canvas, 0.85, 0.8, 'Ir a Pruebas',
                                            'rosa', lambda x: self.controller.mostrar_pantalla(self, 'pruebas'))

    def validar_formularios(self):
        self.datos = {}
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value) or 'mi_seleccion' in str(value):
                if value.datos() == '' and value.vacio == False:
                    self.texto_aviso(0.5, 0.05, 'Debes rellenar todos los campos')
                    return False
                else:
                    self.datos[key] = value.datos()
        return True

    def limpiar_formularios(self):
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value) or 'mi_seleccion' in str(value):
                value.limpiar()
