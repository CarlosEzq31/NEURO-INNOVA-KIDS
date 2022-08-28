import hashlib, math
from classes.env import *
from datetime import datetime

class Paciente():
    def __init__(self, id = None):
        self.id = id
        if self.id:
            self.obtener_informacion()

    def __str__(self):
        string = "{"
        for key, value in vars(self).items():
            string += f"'{key}': {value}, "
        string  = string[:-2] + "}"
        return string
    
    def obtener_informacion(self):
        mycursor = db.cursor()
        query = f"""
        SELECT nombre, domicilio, fecha_reg, fecha_nac, sexo, contacto_datos, lentes, lateralidad, diagnosticoP, tratamiento FROM paciente WHERE id_paciente = '{self.id}'
        ;
        """
        # hacer peticion de la base de datos
        try:
            mycursor.execute(query)
        except:
            raise Exception("Error al obtener informacion")
        for x in mycursor:
            a = 0
        self.nombre = x[0]
        self.domicilio = x[1]
        self.fecha_reg = x[2]
        self.fecha_nacimiento = x[3]
        self.edad = self.calcular_edad()
        self.sexo = x[4]
        self.contacto_datos = x[5]
        self.lentes = x[6]
        self.lateralidad = x[7]
        self.diagnostico_previo = x[8]
        self.tratamiento = x[9]
    
    def datos_nuevos(self, args):
        for key, value in args.items():
            setattr(self, key, value)

    def datos(self):
        return vars(self)
    
    def registrar(self):
        mycursor = db.cursor()
        self.sexo_ = 'M' if self.sexo == 'Hombre' else 'F'
        self.lateralidad_ = 'I' if self.lateralidad == 'Izquierda' else 'D' if self.lateralidad == 'Derecha' 'D' else 'A'
        self.lentes_ = 1 if self.lentes == 'Si' else 0
        self.fecha_reg = datetime.now().strftime("%d/%m/%Y")
        self.id = hashlib.new("sha256", f"{self.nombre + self.fecha_nacimiento + self.fecha_reg}".encode()).hexdigest()
        query = f"""
        INSERT INTO paciente (id_paciente, nombre, domicilio, fecha_reg, fecha_nac, sexo, contacto_datos, lentes, lateralidad, diagnosticoP, tratamiento)
        VALUES ('{self.id}', '{self.nombre}', '{self.domicilio}', '{self.fecha_reg}', '{self.fecha_nacimiento}', '{self.sexo_}', '{self.datos_contacto}', '{self.lentes_}', '{self.lateralidad_}', '{self.diagnostico}', '{self.medicamentos}')
        ;
        """
        try:
            mycursor.execute(query)
            db.commit()
        except:
            raise Exception("Error al registrar")
        self.obtener_informacion()
    
    def calcular_edad(self):
        fecha_nac = datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y")
        hoy = datetime.strptime(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
        return math.floor((hoy - fecha_nac).days / 365)