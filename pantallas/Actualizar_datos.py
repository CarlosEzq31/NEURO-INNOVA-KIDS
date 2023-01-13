from classes.mi_frame import *

class actualizar_datos(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocamos el fondo de la pantalla
        self.canvas.create_image(0,0, image = controller.background, anchor = NW)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Actulizar datos', 3, ANCHOR = NW)
        
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
        self.usuario = mi_formulario(self.canvas, 0.775, 0.35, 'Usuario', focus = True)

        # Formulario para la contraseña antigua
        self.contrasena_antigua = mi_formulario(self.canvas, 0.775, 0.425, 'Contraseña antigua', contrasena = True)

        # Formulario para la contraseña nueva
        self.contrasena_nueva = mi_formulario(self.canvas, 0.775, 0.5, 'Contraseña nueva', contrasena = True)
    
        # Formulario para la confirmacion de la contraseña nueva
        self.confirmacion_contrasena = mi_formulario(self.canvas, 0.775, 0.575, 'Confirmar contraseña', contrasena = True)

        # Boton de actualizar
        self.boton_actualizar = mi_boton(self.canvas, 0.85, 0.9, 'Actualizar', 'verde', lambda x: self.actualizar())
    
    def actualizar(self):
        if self.validar_formularios():
            self.controller.usuario = Usuario(self.datos['usuario'], self.datos['contrasena_antigua'])
            if not self.controller.usuario.revisar_usuario_disponible(self.datos['usuario']):
                self.texto_aviso('El usuario ya existe')
            else:
                self.controller.usuario.actualizar_datos(self.datos['usuario'], self.datos['contrasena_nueva'])
                self.texto_aviso('Datos actualizados')
                self.limpiar_formularios()