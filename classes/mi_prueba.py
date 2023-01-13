import hashlib
from datetime import datetime
from classes.env import *

class Prueba():
    def __init__(self, paciente, usuario, sueno, ayuno):
        self.paciente = paciente.id
        self.usuario = usuario.id
        self.id = self.generar_id()
        self.pruebas = []
        self.archivos = []
        self.sueno = sueno
        self.ayuno = ayuno
    
    def generar_id(self):
        return hashlib.sha256(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + self.paciente).encode('utf-8')).hexdigest()
    
    def __str__(self):
        string = "{"
        for key, value in vars(self).items():
            string += f"'{key}': {value}, "
        string  = string[:-2] + "}"
        return string
    
    def agregar_prueba(self, prueba, archivo):
        """
        Agrega una prueba a la lista de pruebas
        
        Parámetros
        ----------
        prueba : str
            id de la prueba
        archivo : str
            ruta del archivo de la prueba
        """
        self.pruebas.append(prueba)
        self.archivos.append(archivo)
    
    def registrar_prueba(self):
        """
        Registra la prueba en la base de datos
        """
        opciones = ['4 o menos', '4 - 6', '6 - 8', '8 o más']
        for i in range(len(opciones)):
            if self.sueno == opciones[i]:
                self.sueno = i
            if self.ayuno == opciones[i]:
                self.ayuno = i
        pruebas = ''
        for prueba in self.pruebas:
            pruebas += prueba + ', '
        pruebas = pruebas[:-2]
        archivos = ''
        for archivo in self.archivos:
            archivos += archivo + ', '
        archivos = archivos[:-2]
        mycursor = db.cursor()
        query = f"""
        INSERT INTO `neuro_innova`.`pruebas` (id_prueba, id_usuario, id_paciente, pruebas, archivos_prueba, sueno, ayuno) VALUES ('{self.id}','{self.paciente}','{self.usuario}', '{pruebas}', '{archivos}', '{self.sueno}', '{self.ayuno}');
        """
        try:
            mycursor.execute(query)
            db.commit()
            return True
        except Exception as e:
            print("Error al registrar entrevista")
            print(e)
            raise Exception("Error al registrar entrevista")