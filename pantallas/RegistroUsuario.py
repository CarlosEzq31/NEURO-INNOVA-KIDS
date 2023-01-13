from classes.mi_frame import *

class registro_usuario(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
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
        self.nombre = mi_formulario(self.canvas, 0.775, 0.4, 'Nombre', focus = True)

        # nombre de usuario
        self.nombre_usuario = mi_formulario(self.canvas, 0.775, 0.475, 'Nombre de usuario')
        
        # contraseña
        self.contraseña = mi_formulario(self.canvas, 0.775, 0.55, 'Contraseña', contrasena = True)
        
        # confirmar contraseña
        self.confirmar_contraseña = mi_formulario(self.canvas, 0.775, 0.625, 'Confirmar contraseña',
                                                contrasena = True)
        # correo
        self.correo = mi_formulario(self.canvas, 0.775, 0.7, 'Correo', command = lambda x: self.registrar())

        # boton de siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.85, 0.9, 'Siguiente', 
                                'rosa', lambda x: self.registrar())
        

    def validar_formularios(self):
        self.datos = {}
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value):
                if value.datos() == '':
                    self.texto_aviso(0.5, 0.05, 'Todos los campos son obligatorios')
                    return False
                else:
                    self.datos[key] = value.datos()
        print(self.datos)
        return True

    def registrar(self):
        if self.validar_formularios():
            if self.datos['contraseña'] != self.datos['confirmar_contraseña']:
                self.texto_aviso(0.5, 0.05, 'Las contraseñas no coinciden')
                return False
            else:
                self.controller.usuario = Usuario(self.datos['nombre_usuario'], self.datos['contraseña'])
                try:
                    self.controller.usuario.registrar_usuario(self.datos['nombre'], self.datos['correo'])
                except:
                    self.texto_aviso(0.5, 0.05, 'El nombre de usuario ya existe')
                # crear boton de iniciar sesion
                self.boton_iniciar_sesion = mi_boton(self.canvas, 0.85, 0.825, 'Iniciar sesión', 'rosa',
                                                    lambda x: self.controller.mostrar_pantalla(self, 'iniciar_sesion'))

