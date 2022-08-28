import hashlib
from classes.env import *
from datetime import datetime

class Usuario():

    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = hashlib.new("sha256", f"{contrasena}".encode()).hexdigest()
        hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = hashlib.new("sha256", f"{self.usuario + self.contrasena + hoy}".encode()).hexdigest()
    
    def registrar_usuario(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        mycursor = db.cursor()
        query = f"INSERT INTO `neuro_innova`.`usuario` (`id_usuario`, `nombre`, `usuario`, `correo`, `contrasena`) VALUES ('{self.id}','{self.nombre}','{self.usuario}', '{self.correo}', '{self.contrasena}');"
        try:
            mycursor.execute(query)
            db.commit()
            return True
        except:
            self.id = None
            print("Error al registrar usuario")
            raise Exception("Error al registrar usuario")
    
    def iniciar_sesion(self):
        mycursor = db.cursor()
        query = f"""
        SELECT id_usuario FROM usuario WHERE usuario = '{self.usuario}' and contrasena = '{self.contrasena}'
        ;
        """
        # hacer peticion de la base de datos
        mycursor.execute(query)
        for x in mycursor:
            a = 0
        try:
            self.id = x[0]
            return x[0]
        except:
            raise Exception("Usuario o contraseña incorrectos")
    
    def obtener_pacientes(self):
        pacientes = []
        mycursor = db.cursor()
        query = f"""
        SELECT id_paciente, nombre FROM neuro_innova.paciente
        ;
        """
        # hacer peticion de la base de datos
        mycursor.execute(query)
        for x in mycursor:
            a = 0
            pacientes.append({'id': x[0], 'nombre': x[1]})
        return pacientes

        