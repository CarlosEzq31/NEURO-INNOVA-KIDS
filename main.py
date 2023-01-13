from imports import *
tic = time.perf_counter()

class neuro_innova_app(Tk):
    """
        Clase de la aplicación NEURO INNOVA KIDS ®
    """
    def __init__(self, *args, **kwargs):
        """
        Clase de la aplicación NEURO INNOVA KIDS ®
        """
        # función __init__ para la clase Tk
        Tk.__init__(self, *args, **kwargs)
        self.ancho = screenwidth
        self.alto = screenheight
        self.geometry(f'{self.ancho}x{self.alto}')
        
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.withdraw()
        
        # Iniciamos la pantalla de carga
        self.pantalla_carga = pantalla_carga(self)
        
        # creando un contenedor
        self.container = tk.Frame(self) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        # inicializando frames en un arreglo vacío
        self.frames = {}
        
        # Cargamos todas las imagenes a utilizar
        self.pantalla_carga.actualizar_texto(text_ = f'Cargando media')
        self.crear_media()

        # Comprobamos el directorio de salida de los archivos
        self.comprobar_directorio_salida()

        # Cargamos todos los frames a utilizar
        self.pantalla_carga.actualizar_texto(text_ = f'Cargando pantallas')
        self.cargar_frames()

        # Mostramos la ventana principal
        self.frame = self.frames['menu_principal']
        self.frame.tkraise()

        # Actualizamos el texto en la pantal pantalla_carga
        self.pantalla_carga.actualizar_texto(text_ = f'Ya casi está listo')
        
        # Colocar título de la ventana 
        self.title("NEURO INNOVA KIDS ®") 
        
        # Colocar ícono
        self.iconphoto(False, PhotoImage(file = f'{path}/src/images/logo.png'))
        
        # Mostrar programa en modo de pantalla completa
        self.wm_attributes('-fullscreen', 'True')

        # Deshabilitar redimensionamiento de la ventana
        self.resizable(False, False)
        
        # Cerrar la pantalla pantalla_carga y eliminamos el objeto
        self.pantalla_carga.destroy()

        # Inicialización de la matriz del historial de los frames
        self.historial_frames = []
        
    
    # Función para cargar todos los frames a utilizar
    def cargar_frames(self) -> None:
        """
        Función para cargar todos los frames a utilizar
        """
        # Inicilizamos todos los frames en el arreglo frames
        # los añadimos a la ventana principal y mostramos un texto de carga en la pantalla de carga
        for F in frames:
            self.pantalla_carga.actualizar_texto(text_ = f'Cargando pantallas .')
            frame = F(self.container, self)
            self.frames[f'{F.__name__}'] = frame
            self.pantalla_carga.actualizar_texto(text_ = f'Cargando pantallas ..')
            frame.grid(row = 0, column = 0, sticky ="nsew")
            self.pantalla_carga.actualizar_texto(text_ = f'Cargando pantallas ...')    
    
    # Funcion para mostrar un frame pasado como parámetro
    def mostrar_pantalla(self, pantalla_actual: Frame, siguiente_pantalla: str) -> None:
        """
        Función para mostrar un frame pasado como parámetro
        
        Parámetros:
        ----------
        pantalla_actual: mi_frame
            Frame actual
        siguiente_pantalla: str
            Nombre del frame a mostrar
        """
        self.historial_frames.append(str(pantalla_actual)[9:])
        self.frame = self.frames[siguiente_pantalla]
        self.frame.tkraise()

    # Funcion para ir al frame anterior
    def ir_atras(self):
        """
        Función para ir al frame anterior
        """
        for i in self.frames:
            if str(self.historial_frames[-1]) == i:
                self.frame = self.frames[i]
                self.historial_frames.pop()
                self.frame.tkraise()
                break

    # Funcion para ir al menu principal
    def ir_menu_principal(self):
        """
        Función para ir al menu principal
        """
        self.historial_frames = ['menu_principal']
        self.frame = self.frames['menu_principal']
        self.frame.tkraise()
    
    # Funcion para ir a las instrucciones
    def ir_instrucciones(self, frame_actual: Frame):
        """
        Función para ir a las instrucciones

        Parámetros:
        ----------
        frame_actual: mi_frame
            Frame actual
        """
        self.mostrar_pantalla(frame_actual, 'instrucciones')

    # Función que carga todas las imagenes para el programa
    def crear_media(self):
        """
        Función que carga todas las imagenes para el programa
        """
        # definimmos el tamaño de los botones
        self.boton_tamanio = int(self.alto * 0.018)
        
        # creacion de imagenes para el programa usando multitreading
        self.background = self.imagen_redimensionar(f"./src/images/background.jpg", es_fondo = True)
        self.loguito = self.imagen_redimensionar(f"./src/images/logo.png", ratio = 0.00002)
        self.logo = self.imagen_redimensionar(f"./src/images/logo.png", ratio = 0.00007)
        self.boton_rosa_hover = self.imagen_redimensionar(f"./src/images/image.png", ratio = 0.00035)
        self.boton_rosa = self.imagen_redimensionar(f"./src/images/Boton rosa 12.png", ratio = 0.00035)
        self.boton_rosa_grande = self.imagen_redimensionar(f"./src/images/Boton rosa 12.png", ratio = 0.0005)
        self.boton_rosa__hover_grande = self.imagen_redimensionar(f"./src/images/image.png", ratio = 0.0005)
        self.back_ninios = self.imagen_redimensionar(f"./src/images/fondo_ninios1.png", es_fondo = True)
        self.signo_iterrogacion_grande = self.imagen_redimensionar(f"./src/images/Signo_de_interrogacion.png", ratio = 0.0003)
        self.signo_iterrogacion = self.imagen_redimensionar(f"./src/images/Signo_de_interrogacion.png", ratio = 0.000075)
        self.signo_iterrogacion_chico = self.imagen_redimensionar(f"./src/images/Signo_de_interrogacion.png", ratio = 0.00006)
        self.logo_bn = self.imagen_redimensionar(f"./src/images/Logo B Y N.png", ratio = 0.000075)
        self.registro_icono = self.imagen_redimensionar(f"./src/images/Usuarios.png", ratio = 0.00007)
        self.registro_icono_grande = self.imagen_redimensionar(f"./src/images/Usuarios.png", ratio = 0.00018)
        self.play_icono = self.imagen_redimensionar(f"./src/images/Play.png", ratio = 0.00007)
        self.play_icono_grande = self.imagen_redimensionar(f"./src/images/Play.png", ratio = 0.0003)
        self.boton_verde = self.imagen_redimensionar(f"./src/images/boton_verde.png", ratio = 0.00035)
        self.boton_verde_hover = self.imagen_redimensionar(f"./src/images/verde_hover.png", ratio = 0.00035)
        self.historial_icono = self.imagen_redimensionar(f"./src/images/Historial.png", ratio = 0.00007)
        self.historial_icono_grande = self.imagen_redimensionar(f"./src/images/Historial.png", ratio = 0.0003)
        self.barra_escribir = self.imagen_redimensionar(f"./src/images/barra_escribir1.png", ratio = 0.000525)
        self.barra_seleccion = self.imagen_redimensionar(f"./src/images/barra_seleccion.png", ratio = 0.000125)
        self.barra_seleccion_hover = self.imagen_redimensionar(f"./src/images/barra_seleccion_hover.png", ratio = 0.000125)
        self.barra_seleccion_rellena = self.imagen_redimensionar(f"./src/images/barra_seleccion_rellena.png", ratio = 0.000125)
        self.fondo_pantalla_carga = self.imagen_redimensionar(f"./src/images/background.jpg", ratio = 0.000125)
        self.eyetracker_img = self.imagen_redimensionar(f"./src/images/eyetracker.jpg", ratio = 0.00035)
        self.figuras_img = self.imagen_redimensionar(f"./src/images/figuras_prueba.png", ratio = 0.00035)
        self.cubos_img = self.imagen_redimensionar(f"./src/images/cubos_prueba.png", ratio = 0.00035)
        self.domino_img = self.imagen_redimensionar(f"./src/images/domino_prueba.png", ratio = 0.00035)
        self.gif_instruccion1_a = self.gif_imagenes(f"{path}/src/images/instruccion1_a", 0.0002)
        self.gif_instruccion1_b = self.gif_imagenes(f"{path}/src/images/instruccion1_b", 0.000177)
        self.gif_instruccion2_b = self.gif_imagenes(f"{path}/src/images/instruccion2_b", 0.0002)
        self.gif_instruccion3_b = self.gif_imagenes(f"{path}/src/images/instruccion3_b", 0.0002)

    # Funcion para cargar las imagenes de los gifs
    def gif_imagenes(self, path: str, ratio: float) -> list:
        """
        Funcion para cargar las imagenes de los gifs

        Parámetros:
        ----------
        path: str
            ruta de la carpeta donde se encuentran las imagenes
        ratio: float
            ratio de redimensionamiento de las imagenes
        """
        self.pantalla_carga.actualizar_texto("Cargando gif.")
        # Lista donde están las imagenes del gif
        lista = os.listdir(path)
        # Creamos un diccionario para ordenar las imagenes
        self.gifs_images = {}
        # Creamos una lista donde estaran los hilos
        threads = []
        # Obtenemos el ratio de redimensionamiento
        ratio = screenwidth * ratio
        self.pantalla_carga.actualizar_texto("Cargando gif..")
        # Recorremos la lista de imagenes
        for i in range(len(lista)):
            # Solo cargamos la mitad de las imagenes
            if i%2 == 0:
                # Creamos un hilo para cargar la imagen
                t = threads.append(threading.Thread(target=self.gif_redimensionar, args=(f"{path}/{lista[i]}", ratio, i)))
                # Iniciamos el hilo
                threads[-1].start()
        # Esperamos a que terminen los hilos
        [t.join() for t in threads]
        # Ordenamos el diccionario
        images = dict(sorted(self.gifs_images.items()))
        # Creamos una lista donde estaran las imagenes
        images = [ImageTk.PhotoImage(images[i]) for i in images]
        self.pantalla_carga.actualizar_texto("Cargando gif...")
        # Retornamos la lista de imagenes
        return images
    
    # Funcion para redimensionar las imagenes del gif
    def gif_redimensionar(self, gif: str, ratio: float, index: int) -> list:
        """
        Funcion para redimensionar las imagenes del gif

        Parámetros:
        ----------
        gif: list
            lista de imagenes del gif
        ratio: float
            ratio de redimensionamiento de las imagenes
        images: list
            lista de imagenes del gif redimensionadas de salida
        """
        imagen = PImage.open(gif).convert('RGBA')
        imagen = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGBA2BGRA)
        imagen = cv2.resize(imagen, (0, 0), fx = ratio, fy = ratio, interpolation = cv2.INTER_AREA)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGRA2RGBA)
        imagen = PImage.fromarray(imagen, "RGBA")
        self.gifs_images[index] = imagen
    
    # Funcion para cargar y redimensionar las imagenes
    def imagen_redimensionar(self, path: str, ratio: float = 1, es_fondo: bool = None) -> PhotoImage:
        """
        Funcion para cargar y redimensionar las imagenes

        Parámetros:
        ----------
        path: str
            ruta de la imagen
        ratio: float
            ratio de redimensionamiento de la imagen
        es_fondo: bool
            si la imagen es un fondo
        """
        self.pantalla_carga.actualizar_texto("Cargando imagen.")
        path = path.replace('/', '\\')
        imagen = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        ratio *= screenwidth
        self.pantalla_carga.actualizar_texto("Cargando imagen..")
        if es_fondo:
            imagen = cv2.resize(imagen, (screenwidth, screenheight))
        else:
            imagen = cv2.resize(imagen, (0, 0), fx = ratio, fy = ratio, interpolation = cv2.INTER_AREA)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGRA2RGBA)
        imagen = PImage.fromarray(imagen, "RGBA")
        self.pantalla_carga.actualizar_texto("Cargando imagen...")
        imagen = ImageTk.PhotoImage(imagen)
        return imagen
    
    # Función para comprobar el directorio de salida de los archivos
    def comprobar_directorio_salida(self):
        """
        Función para comprobar el directorio de salida de los archivos
        """
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
    
    def deiconify(self) -> None:
        """
        Funcion para desiconificar la ventana
        """
        return super().wm_deiconify()
    
    def mainloop(self) -> None:
        """
        Funcion para iniciar el bucle principal de la ventana
        """
        return super().mainloop()

if __name__ == "__main__":
    app = neuro_innova_app()
    app.deiconify()
    toc = time.perf_counter()
    print(f"Tiempo de carga: {toc - tic:0.4f} segundos")
    app.mainloop()