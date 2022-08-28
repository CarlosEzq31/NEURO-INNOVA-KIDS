# importamos las librerias necesarias
import textwrap
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_ventanita import *

# pantalla de información básica
class info_pruebas(mi_frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.ancho = self.controller.ancho
        self.alto = self.controller.alto

        
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocamos el fondo de la pantalla
        self.canvas.create_image(0,0, image = controller.background, anchor = NW)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        #colocamos el titulo de la pantalla y el icono
        self.canvas.create_text(int(self.ancho*0.15),int(self.alto*0.25), 
                            text = "Pruebas",
                            font = ('Mukta Malar ExtraLight', int(self.controller.boton_tamanio*3)),
                            anchor = NW)
        self.canvas.create_image(int(self.ancho*0.21),int(self.alto*0.5), image = controller.play_icono_grande, anchor = CENTER)
        
        # Boton de menu principal
        self.boton_menu = mi_boton(self.canvas, 0.7, 0.15, 'Menú principal', 'verde',
                                    lambda x: controller.ir_menu_principal())

        # Boton de atras
        self.boton_atras = boton_atras(self.canvas, 0.15, 0.9)

        # Boton de instrucciones
        self.boton_instrucciones = mi_boton(self.canvas, 0.90, 0.15, 'Instrucciones', 'verde',
                                            lambda x: controller.ir_instrucciones(self),
                                            icono = controller.signo_iterrogacion_chico,
                                            icono_dentro = True)


        # Botones Figuras
        texto_figuras = "Se le mostrará una serie de dibujos sobrepuestos y otro grupo de dibujos que se hallan separados, el niño tendrá que seleccionar cuáles figuras se repiten en ambos grupos"
        self.boton_figuras = mi_boton(self.canvas, 0.7, 0.4, 'Figuras', 'rosa',
                                    lambda x: self.mensaje_informacion(controller, self.ancho, self.alto, 'Figuras Información', textwrap.fill(texto_figuras, width = 50),controller.figuras_img),
                                    grande = True)
                                    
        # Boton Cubos
        texto_cubos = "Se le mostrará una imagen de un cubo desplegados con figuras en cada uno de los lados, después una serie de imágenes de cubos en donde está el cubo de la imagen anterior. El paciente tendrá que escoger el cubo de la imagen anterior en la serie anterior"
        self.boton_cubos = mi_boton(self.canvas, 0.7, 0.525, 'Cubos', 'rosa',
                                    lambda x: self.mensaje_informacion(controller, self.ancho, self.alto, 'Cubos Información', textwrap.fill(texto_cubos, width = 50),controller.cubos_img),
                                    grande = True)

        # Boton Dominó
        texto_domino = "Se dará una secuencia numérica con ayuda de fichas de dominó y se le dará una serie de posibles respuestas  para seguir con la secuencia. El niño tendrá que escoger la respuesta correcta"
        self.boton_domino = mi_boton(self.canvas, 0.7, 0.65, 'Dominó', 'rosa',
                                    lambda x: self.mensaje_informacion(controller, self.ancho, self.alto, 'Dominó Información', textwrap.fill(texto_domino, width = 50),controller.domino_img),
                                    grande = True)
    
    def mensaje_informacion(self, controller,width: int, height: int, titulo: str, texto_: str, imagen):
        self.ventanita = ventana_emergente(self, controller, width, height, titulo, texto_, imagen)
        del self.ventanita