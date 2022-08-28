import hashlib
from datetime import datetime

class Prueba():
    def __init__(self, paciente, usuario, sueno, ayuno):
        self.paciente = paciente.id
        self.usuario = usuario.id
        self.id = self.generar_id()
        self.pruebas = []
        self.archivos = []
        self.sueno = 1 if sueno == "Si" else 0
        self.ayuno = 1 if ayuno == "Si" else 0
    
    def generar_id(self):
        return hashlib.sha256(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + self.paciente).encode('utf-8')).hexdigest()
    
    def __str__(self):
        string = "{"
        for key, value in vars(self).items():
            string += f"'{key}': {value}, "
        string  = string[:-2] + "}"
        return string