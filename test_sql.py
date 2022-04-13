import hashlib
import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dabely2006',
    auth_plugin='mysql_native_password',
    database = 'tdah'
)

def main():
    # contacto = {'nombre': 'Paola Rodriguez',
    #             'telefono': '6181870061',
    #             'parentesco': 'Madre'}
    # paciente = {'tratamiento': 'Ninguno',
    #             'fecha_nacimiento': datetime.fromisoformat('2000-10-17'),
    #             'genero': 1,
    #             'lentes': 0,
    #             'lateralidad': 1,
    #             'suenio': 'Nada',
    #             'ayuno': 'No',
    #             'diagnostico_previo': 'Ninguno'}
    # usuario = {'nombre': 'Alejandro Roblez',
    #            'correo': 'alex@gmail.com',
    #            'contrasena': hashlib.new("sha256", b"12345678").hexdigest()}
    # insertar_nuevo_usuario(usuario, paciente, contacto)
    # obtener_parentesco()
    # iniciar_sesion('Alejandro Roblez', '12345678')
    # datos = {'nombre':'Abel','contrasena': 'abel'}
    # actualizar_datos(2,datos,'usuarios')
    # obtener_info_por_id(1, 'hola')
    print(existe_usuario('asdasdsa'))
    # nombre = 'dane'
    # print(hashlib.new("sha256", f"{nombre}".encode()).hexdigest())

def crear_basedatos():
    mycursor = db.cursor()
    query = """CREATE DATABASE IF NOT EXISTS tdah"""
    mycursor.execute(query)

def crear_tabla(tabla: str):
    mycursor = db.cursor()
    if tabla == 'contactos':
        query = """CREATE TABLE `contactos`
                (
                `id`         integer NOT NULL AUTO_INCREMENT ,
                `nombre`     varchar(100) NOT NULL ,
                `telefono`   varchar(40) NOT NULL ,
                `parentesco` varchar(45) NOT NULL ,

                PRIMARY KEY (`id`)
                );"""
        mycursor.execute(query)
    elif tabla == 'pacientes':
        query = """CREATE TABLE `pacientes`
                    (
                    `id`                 integer NOT NULL AUTO_INCREMENT ,
                    `tratamiento`        varchar(100) NULL ,
                    `id_contacto`        integer NOT NULL ,
                    `fecha_nacimiento`   date NOT NULL ,
                    `genero`             integer NOT NULL ,
                    `lentes`             integer NOT NULL ,
                    `lateralidad`        integer NOT NULL ,
                    `suenio`             varchar(100) NOT NULL ,
                    `ayuno`              varchar(100) NOT NULL ,
                    `diagnostico_previo` varchar(100) NOT NULL ,

                    PRIMARY KEY (`id`),
                    KEY `FK_37` (`id_contacto`),
                    CONSTRAINT `FK_35` FOREIGN KEY `FK_37` (`id_contacto`) REFERENCES `contactos` (`id`)
                    );"""
        mycursor.execute(query)
    elif tabla == 'usuarios':
        query = """CREATE TABLE `usuarios`
                (
                `id`          integer NOT NULL AUTO_INCREMENT ,
                `nombre`      varchar(100) NOT NULL ,
                `id_paciente` integer NOT NULL ,
                `correo`      varchar(255) NOT NULL ,
                `contrasena`  varchar(64) NOT NULL ,

                PRIMARY KEY (`id`),
                KEY `FK_64` (`id_paciente`),
                CONSTRAINT `FK_62` FOREIGN KEY `FK_64` (`id_paciente`) REFERENCES `pacientes` (`id`)
                );"""
        mycursor.execute(query)

def insertar_nuevo_usuario(usuario: dict, paciente: dict, contacto: dict):
    mycursor = db.cursor()
    # insertar el nuevo contacto
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in contacto.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in contacto.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('contactos', columns, values)
    mycursor.execute(query)
    db.commit()
    # print(query)
    id = mycursor.lastrowid
    # insertar el nuevo paciente
    paciente['id_contacto'] = id
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in paciente.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in paciente.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('pacientes', columns, values)
    mycursor.execute(query)
    db.commit()
    # insertar el nuevo usuario
    id = mycursor.lastrowid
    usuario['id_paciente'] = id
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in usuario.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in usuario.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('usuarios', columns, values)
    mycursor.execute(query)
    db.commit()
    
def obtener_parentesco():
    mycursor = db.cursor()
    query = """
    SELECT id_paciente FROM usuarios WHERE nombre = 'Danely Santillán'
    ;
    """
    mycursor.execute(query)
    for x in mycursor:
        print(x)
    id = x[0]
    query = f"""
    SELECT id_contacto FROM pacientes WHERE id = {id}
    ;
    """
    mycursor.execute(query)
    for x in mycursor:
        print(x)
    id_contacto = x[0]
    query = f"""
    SELECT parentesco FROM contactos WHERE id = {id_contacto}
    ;
    """
    x = mycursor.execute(query)
    for x in mycursor:
        print(x)
        
def iniciar_sesion_sql(nombre, passwd):
    # cifrar contraseña
    passwd = hashlib.new("sha256", f"{passwd}".encode()).hexdigest()
    mycursor = db.cursor()
    query = f"""
    SELECT id FROM usuarios WHERE nombre = '{nombre}' and contrasena = '{passwd}'
    ;
    """
    # hacer peticion de la base de datos
    mycursor.execute(query)
    for x in mycursor:
        a = 0
    # intentar acceder
    try:
        return x[0]
    except:
        return False

def obtener_info_por_id(id: int, tabla: str):
    mycursor = db.cursor()
    query = f"""
    # --sql
    SELECT id_paciente,nombre FROM usuarios WHERE id = {id}
    ;
    """
    mycursor.execute(query)
    id, nombre = mycursor.fetchall()[0]
    query = f"""
    # --sql
    SELECT genero FROM pacientes WHERE id = {id}
    ;
    """
    mycursor.execute(query)
    genero = mycursor.fetchall()[0][0]
    if genero == 1:
        genero = 'Masculino'
    else:
        genero = 'Femenino'
    return {'genero': genero, 'nombre': nombre}

def actualizar_datos(id: int, datos: dict, tabla: str):
    mycursor = db.cursor()
    if 'contrasena' in datos.keys():
        datos['contrasena'] = hashlib.new("sha256", f"{datos.get('contrasena')}".encode()).hexdigest()
    query = f"UPDATE `tdah`.`{tabla}` SET "
    for k,v in datos.items():
        query += "`%s` = '%s', " %(k,v)
    query = query[:-2]+f" WHERE (`id` = '{id}');"
    print(query)
    mycursor.execute(query)
    db.commit()

def existe_usuario(nombre: str) -> bool:
    mycursor = db.cursor()
    query = f"""
    SELECT id_paciente FROM usuarios WHERE nombre = '{nombre}'
    ;
    """
    mycursor.execute(query)
    for x in mycursor:
        print(x)
    try:
        id = x[0]
        return True
    except:
        return False


if __name__ == '__main__':
    main()