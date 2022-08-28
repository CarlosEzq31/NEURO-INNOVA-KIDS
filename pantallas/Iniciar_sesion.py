from classes.mi_boton import *
from classes.mi_formulario import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.usuario import *

class iniciar_sesion(mi_frame):
    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocamos el fondo de la pantalla
        self.canvas.create_image(0,0, image = controller.background, anchor = NW)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Iniciar sesión', 3, ANCHOR = NW)
        
        # Boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())
        
        # Boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)
        # Boton de atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)
        
        # Formulario para el usuario
        self.usuario_form = mi_formulario(self.canvas, 0.775, 0.725, 'Usuario', focus = True,
                                        command = lambda x: self.iniciar_sesion(), placeholder = 'Alguien')

        # Formulario para la contraseña
        self.contrasena_form = mi_formulario(self.canvas, 0.775, 0.8,
                                            'Contraseña', contrasena = True,
                                            command = lambda x: self.iniciar_sesion())
        
            
        # Boton actualizar datos
        self.boton_actulizar_datos = mi_boton(self.canvas, 0.15, 0.825, 'Actulizar datos',
                                            'verde', lambda x: None)
        
        # Boton de siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.85, 0.9, 'Iniciar sesión', 
                                'rosa', lambda x: self.iniciar_sesion())


    def iniciar_sesion(self):
        if self.validar_formularios():
            self.controller.usuario = Usuario(self.datos['usuario_form'], self.datos['contrasena_form'])
            try:
                self.controller.usuario.iniciar_sesion()
                self.controller.mostrar_pantalla(self, 'inicio_paciente')
                self.limpiar_formularios()
            except Exception as e:
                print(e)
                self.texto_aviso(0.5, 0.05, 'Usuario o contraseña incorrectos')
    
    def validar_formularios(self):
        self.datos = {}
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value):
                if value.datos() == '':
                    self.texto_aviso(0.5, 0.05, 'Todos los campos son obligatorios')
                    return False
                else:
                    self.datos[key] = value.datos()
        return True
    
    def limpiar_formularios(self):
        for key, value in vars(self).items():
            if 'mi_formulario' in str(value):
                value.limpiar()