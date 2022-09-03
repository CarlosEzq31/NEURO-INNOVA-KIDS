import hashlib
from classes.env import *

class Entrevista():
    def __init__(self, id_usuario, id_paciente):
        self.id_usuario = id_usuario
        self.id_paciente = id_paciente
        self.id = hashlib.new("sha256", f"{self.id_usuario + self.id_paciente}".encode()).hexdigest()
        self.prueba = None
        self.entrevista_eni = None
    
    def __str__(self):
        string = "{"
        for key, value in vars(self).items():
            string += f"'{key}': {value}, "
        string  = string[:-2] + "}"
        return string

    def agregar_prueba(self, prueba):
        """
        Agrega una prueba a la entrevista
        
        Parámetros
        ----------
        prueba : Prueba
            Prueba a agregar a la entrevista"""
        if not self.prueba:
            self.prueba = prueba.id
            return True

    def agregar_entrevista_eni(self, entrevista_eni):
        """
        Agrega una entrevista eni a la entrevista

        Parámetros
        ----------
        entrevista_eni : EntrevistaEni"""
        if not self.entrevista_eni:
            self.entrevista_eni = entrevista_eni
            return True
        
    def registrar_entrevista(self):
        """
        Registra la entrevista en la base de datos"""
        if self.prueba and self.entrevista_eni:
            mycursor = db.cursor()
            query = f"INSERT INTO `neuro_innova`.`entrevista` (id_ent, id_paciente, id_eni, id_magallanes, id_prueba) VALUES ('{self.id}','{self.id_paciente}','{self.id_usuario}', '{self.eni.id}', '{self.magallanes}', '{self.prueba.id}');"
            try:
                mycursor.execute(query)
                db.commit()
                return True
            except:
                print("Error al registrar entrevista")
                raise Exception("Error al registrar entrevista")