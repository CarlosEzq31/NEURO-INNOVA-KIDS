import os, subprocess
from classes.mi_boton import *
from classes.mi_frame import *
from classes.mi_texto import *

    
class lista_pruebas(mi_frame):

    def __init__(self, parent, controller):
        mi_frame.__init__(self, parent, controller, controller.background)

        # colocar el logo
        self.canvas.create_image(int(self.ancho*0.1),int(self.alto*0.15), image = controller.loguito, anchor = CENTER)

        # colocamos el titulo de la pantalla y el icono
        self.titulo_ventana = mi_texto(self.canvas, 0.15, 0.25, 'Paciente', 3, ANCHOR = NW)
        self.canvas.create_image(int(self.ancho*0.21),int(self.alto*0.5), image = controller.signo_iterrogacion_grande, anchor = CENTER)

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

        # boton de iniciar prueba de figuras
        self.boton_figuras = mi_boton(self.canvas, 0.7, 0.4, 'Figuras', 'rosa',
                                    lambda x: self.iniciar_figuras(),
                                    grande = True)

        # boton de iniciar prueba de cubos de kohs
        self.boton_cubos = mi_boton(self.canvas, 0.7, 0.525, 'Cubos de Kohs', 'rosa',
                                    lambda x: self.iniciar_cubos(),
                                    grande = True)
        
        # boton de iniciar prueba de domino
        self.boton_domino = mi_boton(self.canvas, 0.7, 0.65, 'Dómino', 'rosa',
                                    lambda x: self.iniciar_domino(),
                                    grande = True)
    
    def iniciar_figuras(self):
            path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            python_path = path + "\eyetracking_env\Scripts\python.exe"
            file = path + "\App-Tkinter\eye_tracker\Prueba_Figuras.py"
            try:
                subprocess.Popen(['powershell.exe', f"'{path}\eyetracking_env\Scripts\Activate.ps1'"])
                subprocess.Popen(['powershell.exe', f"& '{python_path}' '{file}' {self.controller.id}"])
            except:
                pass
            self.texto_aviso(0.5, 0.05,"Cargando pruebas", tiempo = 20)
            
            
    def iniciar_cubos(self):
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        python_path = path + "\eyetracking_env\Scripts\python.exe"
        file = path + "\App-Tkinter\eye_tracker\Cubos.py"
        try:
            subprocess.Popen(['powershell.exe', f"'{path}\eyetracking_env\Scripts\Activate.ps1'"])
            subprocess.Popen(['powershell.exe', f"& '{python_path}' '{file}' {self.controller.id}"])
        except:
            pass
        self.texto_aviso(0.5, 0.05,"Cargando pruebas", tiempo = 20)
            
    def iniciar_domino(self):
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        python_path = path + "\eyetracking_env\Scripts\python.exe"
        file = path + "\App-Tkinter\eye_tracker\Prueba_Domino.py"
        try:
            subprocess.Popen(['powershell.exe', f"'{path}\eyetracking_env\Scripts\Activate.ps1'"])
            subprocess.Popen(['powershell.exe', f"& '{python_path}' '{file}' {self.controller.id}"])
        except:
            pass
        self.texto_aviso(0.5, 0.05,"Cargando pruebas", tiempo = 20)