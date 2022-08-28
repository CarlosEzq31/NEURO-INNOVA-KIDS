from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *
from classes.paciente import *

class usuario_info(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Datos del Paciente', 3, ANCHOR = NW)
        self.canvas.create_image(int(self.ancho*0.21),int(self.alto*0.5), image = controller.signo_iterrogacion_grande, anchor = CENTER)

        # boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)

        # boton atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9, command = lambda x: self.atras())
        
        # boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())
        
        # Mostrar los datos del paciente
        self.informacion = False
        self.bind('<Enter>', lambda x: self.mostrar_datos_paciente())
    
    def mostrar_datos_paciente(self):
        if not self.informacion:
            self.informacion = True
            self.paciente = self.controller.paciente
            
            # Datos del paciente
            
            # Nombre del paciente
            self.texto_nombre = mi_texto(self.canvas, 0.45, 0.52,
                                        'Nombre: ' + self.paciente.nombre, 1.5, ANCHOR = NW)
            
            # Fecha de registro
            self.texto_registro = mi_texto(self.canvas, 0.45, 0.57,
                                        'Fecha de registro: ' + self.paciente.fecha_reg, 1.5, ANCHOR = NW)
            
            # Sexo
            sexo = 'Masculino' if self.paciente.sexo == 'M' else 'Femenino' if self.paciente.sexo == 'F' else 'Otro'
            self.texto_sexo = mi_texto(self.canvas, 0.45, 0.62,
                                        'Sexo: ' + sexo, 1.5, ANCHOR = NW)

            # Edad
            self.texto_edad = mi_texto(self.canvas, 0.45, 0.67,
                                        'Edad: ' + str(self.paciente.edad), 1.5, ANCHOR = NW)

            # Diagnostico
            self.texto_diagnostico = mi_texto(self.canvas, 0.45, 0.72,
                                            'Diagnóstico : ' + self.paciente.diagnostico_previo, 1.5, ANCHOR = NW)
            
            # Domicilio
            self.texto_domicilio = mi_texto(self.canvas, 0.45, 0.77,
                                            'Domicilio: ' + self.paciente.domicilio, 1.5, ANCHOR = NW)
    
    def atras(self):
        self.informacion = False
        self.texto_nombre.destroy()
        self.texto_registro.destroy()
        self.texto_sexo.destroy()
        self.texto_edad.destroy()
        self.texto_diagnostico.destroy()
        self.texto_domicilio.destroy()
        self.controller.ir_atras()