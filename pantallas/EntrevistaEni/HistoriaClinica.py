from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.mi_seleccion import *
from classes.mi_formulario import *

class historiaclinica(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Paciente', 3, ANCHOR = NW)
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
        
        # Formulario de datos
        # Nombre
        self.nombre = mi_formulario(self.canvas, 0.775, 0.4, 'Nombre')

        # Fecha de nacimiento
        self.fecha_nacimiento = mi_formulario(self.canvas, 0.775, 0.5, 'Fecha de nacimiento', fecha = True)

        # Sexo
        self.sexo = mi_seleccion(self.canvas, self.fecha_nacimiento.obtener_label_x(), 0.6, 'Sexo', ['Mascul.', 'Femen.'])

        # Grado escolar
        self.grado_escolar = mi_formulario(self.canvas, 0.775, 0.7, 'Grado escolar')

        # Boton de siguiente
        self.boton_siguiente = mi_boton(self.canvas, 0.825, 0.9, 'Siguiente', 'verde',
                                        lambda x: self.siguiente())
        
        # Colocar valores por defecto al iniciar la pantalla
        self.bind('<Enter>', lambda x: self.colocar_valores_por_defecto())

    def siguiente(self):
        if self.validar_formularios():
            print(self.datos)
            self.controller.mostrar_pantalla(self, 'historialfamiliar')

    def colocar_valores_por_defecto(self):
        self.nombre.colocar_por_defecto(self.controller.paciente.nombre)
        self.fecha_nacimiento.colocar_por_defecto(self.controller.paciente.fecha_nacimiento)