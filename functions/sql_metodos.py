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
def crear_tabla(tabla):
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

def iniciar_sesion(nombre, passwd):
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
        print(x)
    except:
        print('datos erroneos')
