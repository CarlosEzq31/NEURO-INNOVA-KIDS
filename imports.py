import tkinter as tk, pyglet, time, os, cv2, numpy as np
from tkinter import *
from PIL import Image as PImage, ImageTk as ImageTk, ImageGrab
from pantallas.Menu_principal import *
from pantallas.Ingreso import *
from pantallas.Pruebas import *
from pantallas.Lista_Pruebas import *
from pantallas.Splash import *
from pantallas.Instrucciones import *
from pantallas.Iniciar_sesion import *
from pantallas.Usuario import *
from pantallas.Historial import *
from pantallas.Entrevista import *
from pantallas.Paciente import *
from pantallas.RegistroUsuario import *
from pantallas.RegistroPaciente import *
from pantallas.Informacion_basica import *
from pantallas.InformacionBasica.Que_es import *
from pantallas.InformacionBasica.Resultados import *
from pantallas.InformacionBasica.Seguidor_ocular import *
from pantallas.InformacionBasica.Informacion_Pruebas import *
from pantallas.EntrevistaEni.AntecedentesPrenatales import *
from pantallas.EntrevistaEni.AntecedentesNatales import *
from pantallas.EntrevistaEni.AntecedentesPostnatales import *
from pantallas.EntrevistaEni.HistoriaClinica import *
from pantallas.EntrevistaEni.HistoriaFamiliar import *
from pantallas.EntrevistaEni.Comportamiento import *
from pantallas.EntrevistaEni.MetodoDisciplina import *
from pantallas.EntrevistaEni.Escolaridad import *

frames = [menu_principal, ingreso, lista_pruebas, informacion_basica, que_es, info_pruebas, inicio_paciente, seguidor_ocular, registro_usuario, registro_paciente, registro_paciente_2, 
                    instrucciones, iniciar_sesion, usuario_info, entrevista, pruebas, historial, resultados, historiaclinica, 
                    antecedentes_prenatales, antecedentes_prenatales2, antecedentes_prenatales3, antecedentes_prenatales4, 
                    historialfamiliar, historialfamiliar2, 
                    antecedentes_natales, antecedentes_natales2, 
                    antecedentes_postnatales, antecedentes_postnatales2, antecedentes_postnatales3, antecedentes_postnatales4, antecedentes_postnatales5, antecedentes_postnatales6, antecedentes_postnatales7, antecedentes_postnatales8, antecedentes_postnatales9, antecedentes_postnatales10, 
                    comportamiento, comportamiento2, comportamiento3, comportamiento4, comportamiento5, comportamiento6, comportamiento7, comportamiento8, comportamiento9, comportamiento10, comportamiento11, comportamiento12, 
                    disciplina, 
                    escolaridad, escolaridad2, escolaridad3, escolaridad4, escolaridad5, escolaridad6, escolaridad7, escolaridad8, escolaridad9, escolaridad10, escolaridad11, escolaridad12]

# obtener resolucion de pantalla
resolution = ImageGrab.grab()
screenwidth, screenheight = resolution.size
# screenwidth, screenheight = 1366, 768
del resolution

# obtenemos el directorio del programa
path = os.path.dirname(os.path.realpath(__file__))
path_ = os.path.dirname(os.path.realpath(__file__))

# importamos la fuente a utilizar
pyglet.font.add_file(f'{path}/src/fonts/Mukta_Malar/MuktaMalar-ExtraLight.ttf')

# importamos esta librería para que no afecte el reescalado de windows
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(2)