import os
from pathlib import Path
from PIL import ImageGrab

# Obtener resolucion de pantalla
resolution = ImageGrab.grab()
screenwidth, screenheight = resolution.size
del resolution

# Directorio del fichero actual
DIR = os.path.dirname(__file__)

# Directorio donde se almacenaran los datos
DATADIR = os.path.join(DIR, 'data')

# Directorio que contiene las imagenes
IMGDIR = os.path.join(DIR, 'img')
# IMGDIR = os.path.join(DIR, 'imgsn') #Carpeta pruebas para niños

# Directorio de la imagen de fondo
FONDODIR = f"{Path(__file__).parent.parent}\src\images\\"

# Escala de imagenes
IMGSCALE = (0.25/1080)*screenheight


# Directiorio del archivo de instrucciones
INSTFILE = os.path.join(DIR, 'instructions.txt')
FONTDIR = os.path.join(DIR, 'MuktaMalar-ExtraLight.ttf')
# Preguntar el nombre del participante para usarlo en los archivos de salida
# ask for the participant name, to use as the name for the logfile...
#LOGFILENAME = input("Participant name: ")
LOGFILENAME = "Sj"

# Directorio de los archivos de datos
LOGFILE = os.path.join(DATADIR, LOGFILENAME)

# Pantalla
SCREENNR = 1 # 1 Para monitores externos

# Para DISPTYPE, puedes escoger 'pygame' o 'psychopy';
# 'psychopy' si necesitas un tiempo de actualización de pantalla preciso en milisegundos
# 'pygame' si tiene problemas para usar PsychoPy
DISPTYPE = 'pygame'

# DISPSIZE es la resolcion de la pantalla
DISPSIZE = (screenwidth, screenheight) # DELL laptop
#DISPSIZE = (1536, 864)  # DELL external monitor
# DISPSIZE = (1920, 1080)  # DELL external monitor


# SCREENSIZE es el tamaño fisico de la pantalla
#SCREENSIZE = (34.5, 19.5)  # DELL laptop
#SCREENSIZE = (31.2, 18)
#SCREENSIZE = (47.6, 26.77)  # DELL external monitor
SCREENSIZE = (48, 28)  # Lenovo external monitor

# SCREENDIST es la distancia entre el usuario y la pantalla
SCREENDIST = 80.0

# FULLSCREEN, True para modo en pantalla completa, o False para modo ventana
FULLSCREEN = False

# BGC is for BackGroundColour, FGC for ForeGroundColour; both are RGB guns,
# which contain three values between 0 and 255, representing the intensity of
# Red, Green, and Blue respectively, e.g. (0,0,0) for black, (255,255,255) for
# white, or (255,0,0) for the brightest red
BGC = (0,0,0)
FGC = (255,255,255)
# the TEXTSIZE determines the size of the text in the experiment
TEXTSIZE = 24

# TIMING
# the TRIALTIME is the time each image is visible
TRIALTIME = 2500 # ms
# the intertrial interval (ITI) is the minimal amount of time between the
# presentation of two consecutive images
ITI = 500 # ms

# EYE TRACKING
# the TRACKERTYPE indicates the brand of eye tracker, and should be one of the
# following: 'eyelink', 'smi', 'tobii' 'dumbdummy', 'dummy'
TRACKERTYPE = 'eyetribe'
# TRACKERTYPE = 'opengaze'

# EyeTribe only
EYETRIBECALIBDUR = 1500
EYETRIBEPRECALIBDUR = 500  #ARMANDOLARA I CHANGED FROM 500 to 750

# the EYELINKCALBEEP constant determines whether a beep should be sounded on
# the appearance of every calibration target (EyeLink only)
#EYELINKCALBEEP = True

# set DUMMYMODE to True if no tracker is attached
DUMMYMODE = True

from pygaze.libscreen import Display, Screen
from pygaze.libinput import Keyboard, Mouse
from pygaze.eyetracker import EyeTracker
from pygaze.liblog import Logfile
import pygaze.libtime as timer
from PIL import Image as PImage


def tamanno_imagen(path: str, scale: float):
    imagen = PImage.open(path)
    x, y = imagen.size
    return x*IMGSCALE*scale,y*IMGSCALE*scale

def boton_presionado(x: float, y: float, pos_boton, tamanio_boton) -> bool:
    boton_x, boton_y = pos_boton
    boton_ancho, boton_alto = tamanio_boton
    return (x > boton_x - (boton_ancho/2) and  x < boton_x + (boton_ancho/2)) and (y > boton_y - (boton_alto/2) and  y < boton_y + (boton_alto/2))

def colocar_fondo(pantalla: Screen) -> None:
    pantalla.draw_image(image = FONDODIR + "background.jpg",scale = IMGSCALE)
    
def click_imagen(x,y, imagen):
    boton_x, boton_y = imagen.get("x"), imagen.get("y")
    boton_ancho, boton_alto = imagen.get("ancho"), imagen.get("alto")
    return (x > boton_x - (boton_ancho/2) and  x < boton_x + (boton_ancho/2)) and (y > boton_y - (boton_alto/2) and  y < boton_y + (boton_alto/2))

def colocarBoton(pantalla: Screen, imagen: str, ratio: float, x, y, text: str = None, ratioTexto: float = 1, color = (0,0,0)) : 
    pantalla.draw_image(image = imagen,
                        scale = IMGSCALE*ratio,
                        pos = (x,y))
    boton_ancho, boton_alto = tamanno_imagen(imagen, ratio)
    boton = {"x": x, "y": y, "ancho": boton_ancho, "alto": boton_alto}
    if text:
        pantalla.draw_text(text= text, 
                        fontsize=TEXTSIZE*ratioTexto, 
                        font='Mukta Malar ExtraLight',
                        colour = color,
                        pos = (x,y))
    return boton