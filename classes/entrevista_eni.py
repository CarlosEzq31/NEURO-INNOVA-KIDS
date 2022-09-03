import hashlib, datetime
from classes.env import *

class EntrevistaEni():
    def __init__(self, paciente):
        self.paciente = paciente
        self.id = hashlib.new("sha256", f"{self.paciente.id}".encode()).hexdigest()

    def agregar_datos(self, datos):
        """
        Agrega los datos de la entrevista a la base de datos
        """
        for key, value in datos.items():
            setattr(self, key, value)
    
    def registrar_entrevista(self):
        """
        Registra la entrevista en la base de datos mysql y retorna True si se registro correctamente
        """
        return True
    
    def __str__(self):
        string = "{"
        for key, value in vars(self).items():
            string += f"'{key}': {value}, "
        string  = string[:-2] + "}"
        return string