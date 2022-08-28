import subprocess, os, ctypes.wintypes
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *

class historial(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Historial de pruebas', 3, ANCHOR = NW)
        self.canvas.create_image(int(self.ancho*0.21),int(self.alto*0.5), image = controller.historial_icono_grande, anchor = CENTER)

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
        self.boton_siguient = mi_boton(self.canvas, 0.85, 0.9, 'Obtener resultados', 'rosa',
                                        lambda x: self.abrir_resultados())
        
    def abrir_resultados(self):
        CSIDL_PERSONAL = 5       # My Documents
        SHGFP_TYPE_CURRENT = 0   # Get current, not default value

        dir = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, dir)

        docs = str(dir.value)
        directory = docs + "\\NEURO INNOVA KIDS"
        ruta = os.path.join(directory, 'DATA')
        print(ruta)
        subprocess.Popen(f'explorer "{ruta}\\"')