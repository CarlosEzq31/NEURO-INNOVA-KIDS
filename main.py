from imports import *

class neuro_innova_app(tk.Tk):
    def __init__(self, *args, **kwargs):

        # función __init__ para la clase Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.ancho = screenwidth
        self.alto = screenheight
        self.geometry(f'{self.ancho}x{self.alto}')
        
        global tic
        tic = time.perf_counter()
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.withdraw()
        
        # Iniciamos la pantalla de carga
        self.splash = Splash(self)
        
        # creando un contenedor
        self.container = tk.Frame(self) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        # inicializando frames en un arreglo vacío
        self.frames = {}
        
        # Cargamos todas las imagenes a utilizar
        self.splash.actualizar_texto(text_ = f'Cargando media')
        self.crear_media()

        # Inicializamos el id
        self.id = 0

        # Comprobamos el directorio de salida de los archivos
        self.comprobar_directorio_salida()

        # Cargamos todos los frames a utilizar
        self.splash.actualizar_texto(text_ = f'Cargando pantallas')
        self.cargar_frames()
        
    
    # Función para cargar todos los frames a utilizar
    def cargar_frames(self):
        # Inicilizamos todos los frames en el arreglo frames
        # los añadimos a la ventana principal y mostramos un texto de carga en la pantalla de carga
        for F in frames:
            self.splash.actualizar_texto(text_ = f'Cargando pantallas .')
            frame = F(self.container,self)
            self.frames[f'{F.__name__}'] = frame
            self.splash.actualizar_texto(text_ = f'Cargando pantallas ..')
            frame.grid(row = 0, column = 0, sticky ="nsew")
            self.splash.actualizar_texto(text_ = f'Cargando pantallas ...')    

        # mostramos el frame del menu principal
        self.frame = self.frames['menu_principal']
        self.frame.tkraise()
        
        # actualizamos el texto en la pantal splash
        self.splash.actualizar_texto(text_ = f'Ya casi está listo')
        
        # colocar título de la ventana 
        self.title("NEURO INNOVA KIDS ®") 
        
        # colocar ícono
        self.iconphoto(False, PhotoImage(file = f'{path}/src/images/logo.png'))
        
        # mostrar programa en modo de pantalla completa
        self.wm_attributes('-fullscreen', 'True')

        # deshabilitar redimensionamiento de la ventana
        self.resizable(False, False)
        
        # cerrar la pantalla splash y eliminamos el objeto
        self.splash.destroy()

        # inicialización de la matriz del historial de los frames
        self.historial_frames = []
    
    # Funcion para mostrar un frame pasado como parámetro
    def mostrar_pantalla(self, current_frame, next_frame):
        self.historial_frames.append(str(current_frame)[9:])
        self.frame = self.frames[next_frame]
        self.frame.tkraise()

    # Funcion para ir al frame anterior
    def ir_atras(self):
        for i in self.frames:
            if str(self.historial_frames[-1]) == i:
                self.frame = self.frames[i]
                self.historial_frames.pop()
                self.frame.tkraise()
                break

    # Funcion para ir al menu principal
    def ir_menu_principal(self):
        self.historial_frames = ['menu_principal']
        self.frame = self.frames['menu_principal']
        self.frame.tkraise()
    
    # Funcion para ir a las instrucciones
    def ir_instrucciones(self, current_frame):
        self.mostrar_pantalla(current_frame, 'instrucciones')

    # Función que carga todas las imagenes para el programa
    def crear_media(self):
        # definimmos el tamaño de los botones
        self.boton_tamanio = int(self.alto * 0.018)
        
        # creacion de imagenes para el programa
        self.background = self.imagen_redimensionar(f"{path}/src/images/background.jpg", es_fondo = True)
        self.loguito = self.imagen_redimensionar(f"{path}/src/images/logo.png", ratio = 0.00002)
        self.logo = self.imagen_redimensionar(f"{path}/src/images/logo.png", ratio = 0.00007)
        self.boton_rosa_hover = self.imagen_redimensionar(f"{path}/src/images/image.png", ratio = 0.00035)
        self.boton_rosa = self.imagen_redimensionar(f"{path}/src/images/Boton rosa 12.png", ratio = 0.00035)
        self.boton_rosa_grande = self.imagen_redimensionar(f"{path}/src/images/Boton rosa 12.png", ratio = 0.0005)
        self.boton_rosa__hover_grande = self.imagen_redimensionar(f"{path}/src/images/image.png", ratio = 0.0005)
        self.back_ninios = self.imagen_redimensionar(f"{path}/src/images/fondo_ninios1.png", es_fondo = True)
        self.signo_iterrogacion_grande = self.imagen_redimensionar(f"{path}/src/images/Signo_de_interrogacion.png", ratio = 0.0003)
        self.signo_iterrogacion = self.imagen_redimensionar(f"{path}/src/images/Signo_de_interrogacion.png", ratio = 0.000075)
        self.signo_iterrogacion_chico = self.imagen_redimensionar(f"{path}/src/images/Signo_de_interrogacion.png", ratio = 0.00006)
        self.logo_bn = self.imagen_redimensionar(f"{path}/src/images/Logo B Y N.png", ratio = 0.000075)
        self.registro_icono = self.imagen_redimensionar(f"{path}/src/images/Usuarios.png", ratio = 0.00007)
        self.registro_icono_grande = self.imagen_redimensionar(f"{path}/src/images/Usuarios.png", ratio = 0.00018)
        self.play_icono = self.imagen_redimensionar(f"{path}/src/images/Play.png", ratio = 0.00007)
        self.play_icono_grande = self.imagen_redimensionar(f"{path}/src/images/Play.png", ratio = 0.0003)
        self.boton_verde = self.imagen_redimensionar(f"{path}/src/images/boton_verde.png", ratio = 0.00035)
        self.boton_verde_hover = self.imagen_redimensionar(f"{path}/src/images/verde_hover.png", ratio = 0.00035)
        self.historial_icono = self.imagen_redimensionar(f"{path}/src/images/Historial.png", ratio = 0.00007)
        self.historial_icono_grande = self.imagen_redimensionar(f"{path}/src/images/Historial.png", ratio = 0.0003)
        self.barra_escribir = self.imagen_redimensionar(f"{path}/src/images/barra_escribir1.png", ratio = 0.000525)
        self.barra_seleccion = self.imagen_redimensionar(f"{path}/src/images/barra_seleccion.png", ratio = 0.000125)
        self.barra_seleccion_hover = self.imagen_redimensionar(f"{path}/src/images/barra_seleccion_hover.png", ratio = 0.000125)
        self.barra_seleccion_rellena = self.imagen_redimensionar(f"{path}/src/images/barra_seleccion_rellena.png", ratio = 0.000125)
        self.fondo_splash = self.imagen_redimensionar(f"{path}/src/images/background.jpg", ratio = 0.000125)
        self.eyetracker_img = self.imagen_redimensionar(f"{path}/src/images/eyetracker.jpg", ratio = 0.00035)
        self.figuras_img = self.imagen_redimensionar(f"{path}/src/images/figuras_prueba.png", ratio = 0.00035)
        self.cubos_img = self.imagen_redimensionar(f"{path}/src/images/cubos_prueba.png", ratio = 0.00035)
        self.domino_img = self.imagen_redimensionar(f"{path}/src/images/domino_prueba.png", ratio = 0.00035)
        self.gif_instruccion1_a = self.gif_imagenes(f"{path}/src/images/instruccion1_a", 0.0002)
        self.gif_instruccion1_b = self.gif_imagenes(f"{path}/src/images/instruccion1_b", 0.000177)
        self.gif_instruccion2_b = self.gif_imagenes(f"{path}/src/images/instruccion2_b", 0.0002)
        self.gif_instruccion3_b = self.gif_imagenes(f"{path}/src/images/instruccion3_b", 0.0002)

    # Funcion para cargar las imagenes de los gifs
    def gif_imagenes(self, path, ratio) -> list:
        self.splash.actualizar_texto("Cargando gif.")
        lista = os.listdir(path)
        images = []
        self.splash.actualizar_texto("Cargando gif..")
        for i in range(len(lista)):
            if i%2 == 0:
                imagen = PImage.open(f"{path}/{lista[i]}").convert('RGBA')
                imagen = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGBA2BGRA)
                imagen_alto, imagen_ancho = imagen.shape[:2]
                ratio_ = screenwidth * ratio
                imagen = cv2.resize(imagen, (int(imagen_ancho*ratio_), int(imagen_alto*ratio_)), interpolation = cv2.INTER_AREA)
                imagen = cv2.cvtColor(imagen, cv2.COLOR_BGRA2RGBA)
                imagen = PImage.fromarray(imagen, "RGBA")
                imagen = ImageTk.PhotoImage(imagen)
                images.append(imagen)
                del imagen
        self.splash.actualizar_texto("Cargando gif...")
        return images
    
    # Funcion para cargar y redimensionar las imagenes
    def imagen_redimensionar(self, path: str, ratio: float = 1, es_fondo: bool = None) -> Image:
        self.splash.actualizar_texto("Cargando imagen.")
        path = path.replace(path_, "").replace('/', '\\')
        imagen = cv2.imread(f'.{path}', cv2.IMREAD_UNCHANGED)
        imagen_alto, imagen_ancho = imagen.shape[:2]
        ratio = ratio * screenwidth
        self.splash.actualizar_texto("Cargando imagen..")
        if es_fondo:
            imagen = cv2.resize(imagen, (screenwidth, screenheight))
        else:
            imagen = cv2.resize(imagen, (int(imagen_ancho*ratio), int(imagen_alto*ratio)), interpolation = cv2.INTER_AREA)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGRA2RGBA)
        imagen = PImage.fromarray(imagen, "RGBA")
        self.splash.actualizar_texto("Cargando imagen...")
        imagen = ImageTk.PhotoImage(imagen)
        return imagen
    
    # Función para comprobar el directorio de salida de los archivos
    def comprobar_directorio_salida(self, id_paciente = None):
        import os, ctypes.wintypes
        CSIDL_PERSONAL = 5       
        SHGFP_TYPE_CURRENT = 0   

        dir = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, dir)

        docs = str(dir.value)
        self.docs = str(dir.value)
        directory = docs + "\\NEURO INNOVA KIDS"

        # Si no existe el directorio, se crea
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Si no existe el directorio de los pacientes, se crea
        if not os.path.exists(directory + "\\PACIENTES"):
            os.makedirs(directory + "\\PACIENTES")
        
        if id_paciente:
            if not os.path.exists(directory + "\\PACIENTES" + f"\\{id_paciente}"):
                os.makedirs(directory + "\\PACIENTES" + f"\\{id_paciente}")

if __name__ == "__main__":
    app = neuro_innova_app()
    app.deiconify()
    toc = time.perf_counter()
    print(f'La carga del programa tomó {str(int(toc-tic)).strip()}s')
    del tic, toc
    app.mainloop()