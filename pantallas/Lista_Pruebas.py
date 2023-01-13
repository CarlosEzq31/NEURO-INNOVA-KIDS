from classes.mi_frame import *
import os, subprocess, time
    
class lista_pruebas(mi_frame):

    def __init__(self, parent: Frame, controller: neuro_innova_app):
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
        
        # boton para registrar la prueba
        self.boton_registrar = mi_boton(self.canvas, 0.825, 0.9, 'Registrar pruebas', 'verde',
                                        lambda x: self.registrar_prueba())

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

        self.prueba_ = False
        self.bind("<Leave>", lambda x: self.texto_espera())
    
    def iniciar_figuras(self):
        self.texto_carga = mi_texto(self.canvas, 0.5, 0.05, "Cargando prueba figuras", 2)
        self.prueba = 'Prueba_Figuras'
        self.iniciar_prueba(self.prueba)
            
            
    def iniciar_cubos(self):
        self.texto_carga = mi_texto(self.canvas, 0.5, 0.05, "Cargando prueba de cubos", 2)
        self.prueba = 'Cubos'
        self.iniciar_prueba(self.prueba)
            
    def iniciar_domino(self):
        self.texto_carga = mi_texto(self.canvas, 0.5, 0.05, "Cargando prueba domino", 2)
        self.prueba = 'Prueba_Domino'
        self.iniciar_prueba(self.prueba)
    
    def iniciar_prueba(self, prueba):
        for key, value in vars(self).items():
            if isinstance(value, mi_boton):
                value.deshabilitar()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        python_path = path + "\eyetracking_env\Scripts\python.exe"
        file = path + f"\App-Tkinter\eye_tracker\{prueba}.py"
        self.salida = open('.\\temp.temp', 'w')
        subprocess.Popen(['powershell.exe', f"'{path}\eyetracking_env\Scripts\Activate.ps1'"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        self.s1 = subprocess.Popen(['powershell.exe', f"& '{python_path}' '{file}' {self.controller.paciente.id}"], stdout=self.salida)
    
    def texto_espera(self):
        if self.s1.poll() is None:
            self.texto_carga.destroy()
            self.prueba_ = True
            self.texto_carga = mi_texto(self.canvas, 0.5, 0.05, "Prueba en curso", 2)
            self.after(1000, lambda: self.texto_espera())
            return
        elif self.prueba_ and self.s1.poll() is not None:
            self.texto_carga.destroy()
            self.prueba_ = False
            self.texto_carga = mi_texto(self.canvas, 0.5, 0.05, "Prueba finalizada", 2)
            self.after(3000, lambda: self.texto_carga.destroy())
            self.salida.close()
            try:
                with open('.\salida.txt', 'r') as self.salida:
                    for linea in self.salida:
                        if ".json" in linea:
                            archivo = linea.replace("\n", "")
                            print(archivo)
                    self.controller.prueba.agregar_prueba(self.prueba, archivo)
                os.remove('.\salida.txt')
                os.remove(".\\temp.temp")
            except:
                pass
            self.prueba = ''
            time.sleep(1)
            for key, value in vars(self).items():
                if isinstance(value, mi_boton):
                    value.habilitar()
            return
    
    def registrar_prueba(self):
        print(self.controller.prueba)
        self.controller.prueba.registrar_prueba()
        self.controller.mostrar_pantalla(self, 'pruebas')