import hashlib
# import mysql.connector
from datetime import date
from datetime import datetime
# db = mysql.connector.connect(host = 'localhost',
#                              user = 'root', 
#                              passwd = 'dabely2006', 
#                              auth_plugin = 'mysql_native_password',
#                              database = 'neuro_innova')


# Funcion para calcular la edad
def calcular_edad(nacimiento: str) -> int:
    nacimiento = datetime.strptime(nacimiento, '%d/%m/%Y')
    today = date.today()
    try: 
        birthday = nacimiento.replace(year = today.year)
    except ValueError:
        birthday = nacimiento.replace(year = today.year, month=nacimiento.month+1, day=1)
    if not birthday.year > today.year:
        return today.year - nacimiento.year - 1
    else:
        return today.year - nacimiento.year

# Función para crear un nuevo usuario y nuevo paciente que nos devuelve True si todo salió bien y False de lo contrario
def crear_nuevo_usuario(usuario: str, nombre: str, correo: str, contrasena: str, paciente: dict) -> bool:
    # Tenemos que ingresar un diccionario con el siguiente formato
    #   {'id_paciente': '',
    #     'tratamiento': 1,
    #     'fecha_nac': '20/04/2004',
    #     'genero': 0,
    #     'contacto': 'Yeni, 618107751, Madre',
    #     'lentes': 0,
    #     'lateralidad': 0,
    #     'sueno': 0,
    #     'ayuno': 0,
    #     'diagnosticoP': 'Nada'}
    mycursor = db.cursor()
    # Creamos el HASH para la contraseña
    contrasena = hashlib.new("sha256", f"{contrasena}".encode()).hexdigest()
    # Creamos el id de paciente
    id_paciente = usuario[0:2] + nombre[0:2] + str(datetime.now().strftime('%d%m%y'))
    paciente['id_paciente'] = id_paciente
    query = f"INSERT INTO `neuro_innova`.`usuario` (`id_usuario`, `nombre`, `correo`, `contrasena`, `id_paciente`) VALUES ('{usuario}','{nombre}', '{correo}', '{contrasena}', '{id_paciente}');"
    mycursor.execute(query)
    db.commit()
    # insertar el nuevo paciente
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in paciente.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in paciente.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('paciente', columns, values)
    mycursor.execute(query)
    db.commit()
    entrevista_sql(id_paciente)
    return True

# Función para agregar nueva entrevista o visita
def entrevista_sql(id_paciente):
    mycursor = db.cursor()
    data = {'id_ent': id_paciente + f"_{str(datetime.now().strftime('%d_%m_%y'))}",
            'id_paciente': id_paciente,
            'id_eni': id_paciente,
            'id_magallanes': id_paciente,
            'id_prueba': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('entrevista', columns, values)
    mycursor.execute(query)
    db.commit()

# Función para guardar información de las pruebas
def pruebas_sql(id_paciente, prueba, archivo):
    usuario = obtener_info_por_id(id_paciente).get('usuario')
    mycursor = db.cursor()
    data = {'id_prueba': id_paciente + f"{prueba}_{str(datetime.now().strftime('%d_%m_%Y %H_%M_%S'))}",
            'id_usuario': usuario,
            'id_paciente': id_paciente,
            'pruebas': f"{prueba}",
            'archivos_prueba': archivo.replace("\\","\\\\")}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('pruebas', columns, values)
    print(query)
    mycursor.execute(query)
    db.commit()


# Función para iniciar sesión que nos devuelve el id_paciente    
def iniciar_sesion_sql(usuario, contrasena):
    # cifrar contraseña
    contrasena = hashlib.new("sha256", f"{contrasena}".encode()).hexdigest()
    mycursor = db.cursor()
    query = f"""
    SELECT id_paciente FROM usuario WHERE id_usuario = '{usuario}' and contrasena = '{contrasena}'
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
        print('datos erroneos')

def obtener_info_por_id(id_paciente):
    mycursor = db.cursor()
    query = f"SELECT * FROM usuario WHERE id_paciente='{id_paciente}'"
    mycursor.execute(query)
    info = mycursor.fetchall()[0]
    data = {'usuario': info[0],
            'nombre': info[1],
            'correo': info[2]}
    query = f"SELECT * FROM paciente WHERE id_paciente='{id_paciente}'"
    mycursor.execute(query)
    info = mycursor.fetchall()[0]
    fecha_nac = info[2]
    data['edad'] = calcular_edad(fecha_nac)
    data['genero'] = 'Masculino' if int(info[3]) == 1 else 'Femenino'
    return data
    
# Actulizar algunos datos de la pantalla de historial clínica
def historia_clinica_sql(datos, id_paciente):
    mycursor = db.cursor()
    try:
        fecha_nac = datos.get('Fecha de Nacimiento').replace("-","/")
    except:
        fecha_nac = datos.get('Fecha de Nacimiento')
    query = f"UPDATE `paciente` SET `genero` = '{datos.get('Sexo')}', `fecha_nac` = '{fecha_nac}' WHERE (`id_paciente` = '{id_paciente}');"
    mycursor.execute(query)
    query = f"UPDATE `usuario` SET `nombre` = '{datos.get('Nombre')}' WHERE (`id_paciente` = '{id_paciente}');"
    mycursor.execute(query)
    db.commit()
    
# Insertar datos de la pantalla de historia familiar
def historia_familiar_sql(datos, id_paciente):
    datos = {'id_fam': id_paciente,
             'problema_lenguje': datos.get('Problema de lenguaje'),
             'deficiencia_sensorial': datos.get('Deficiencia sensorial'),
             'paralisis_sensorial': datos.get('Parálisis cerebral'),
             'epilsepsia': datos.get('Epilepsia'),
             'deficit_atencion': datos.get('Déficit de atención'),
             'problemas_coordinacion': datos.get('Prob Coord. Motriz'),
             'drogadiccion': datos.get('Drogadicción'),
             'alcoholismo': datos.get('Alcoholismo'),
             'enfermedad_psiquiatrica': datos.get('Enferm. Psiquiátrica'),
             'sindrome_down': datos.get('Sínd. Down'),
             'retardo_mental': datos.get('Retardo mental'),
             'problema_aprendizaje': datos.get('Prob. de aprendizaje'),
             'retraso_escolar': datos.get('Retraso escolar'),
             'otros': datos.get('Otros')}
    mycursor = db.cursor()
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in datos.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in datos.values())
    query = f"SELECT id_fam FROM familiar WHERE id_fam = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        datos.pop('id_fam')
        query = "UPDATE familiar SET {} WHERE id_fam = '{}'".format(', '.join("{}='{}'".format(k, datos[k]) for k in datos), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('familiar', columns, values)
    # print(query)
    mycursor.execute(query)
    db.commit()
    
# Insertar datos de la pantalla de antecendetes prenatales
def antecedentes_prenatales_sql(datos, id_paciente):
    data = {'id_pren': id_paciente,
             'embar_deseo': datos.get('Embarazo deseado'),
             'drogas_embar': datos.get('Drogas en el embarazo'),
             'prod_gesta': datos.get('Producto de la gesta número'),
             'alim_embar': datos.get('Calidad de Alimentación(1-3)'),
             'id_pad_emb': id_paciente,
             'id_exp_emb': id_paciente}
    mycursor = db.cursor()
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = f"SELECT id_pren FROM prenatal WHERE id_pren = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_pren')
        query = "UPDATE prenatal SET {} WHERE id_pren = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('prenatal', columns, values)
    mycursor.execute(query)
    db.commit()
    data = {'id_exp_emb': id_paciente,
            'rayos_x': datos.get('Rayos X'),
            'rayos_x_mes': datos.get('¿En qué mes? (rayos x)'),
            'vacunas': datos.get('¿Cuáles vacunas?'),
            'vacunas_mes': datos.get('¿En qué mes? (vacunas)'),
            'medicamentos': datos.get('¿Cuáles medicamentos?'),
            'medicamentos_mes': datos.get('¿En qué mes? (medicamentos)'),
            'otros': datos.get('Otros'),
            'otros_mes': datos.get('Otros (mes)')}
    mycursor = db.cursor()
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = f"SELECT id_exp_emb FROM expo_embarazo WHERE id_exp_emb = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_exp_emb')
        query = "UPDATE expo_embarazo SET {} WHERE id_exp_emb = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('expo_embarazo', columns, values)
    mycursor.execute(query)
    db.commit()
    data = {'id_pad_emb': id_paciente,
            'rubeola': datos.get('rubéola'),
            'varicela': datos.get('varicela'),
            'edema': datos.get('edema'),
            'traumatismo': datos.get('traumatismo'),
            'amenaza_aborto': datos.get('amenaza_aborto'),
            'sifilis': datos.get('sífilis'),
            'toxoplasmosis': datos.get('toxoplasmosis'),
            'vih': datos.get('vih'),
            'hipertension': datos.get('hipertensión'),
            'toxemia': datos.get('toxemia'),
            'otros': datos.get('otros')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = f"SELECT id_pad_emb FROM pade_embarazo WHERE id_pad_emb = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_pad_emb')
        query = "UPDATE pade_embarazo SET {} WHERE id_pad_emb = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('pade_embarazo', columns, values)
    mycursor.execute(query)
    db.commit()

# Funcion para informacion de antecedentes natales
def antecedentes_natales_sql(datos, id_paciente):
    # print(datos)
    mycursor = db.cursor()
    data = {'id_natal': id_paciente,
            'tipo_parto': datos.get('Tipo de parto'),
            'sem_gestacion': datos.get('Semanas de Gestación'),
            'duracion_parto': datos.get('Horas de parto'),
            'necesidades': datos.get('Al nacer el niño necesitó...'),
            'sufrimiento': datos.get('sufrimiento_nasal'),
            'id_datos_nac': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('natal', columns, values)
    query = f"SELECT id_natal FROM natal WHERE id_natal = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_natal')
        query = "UPDATE natal SET {} WHERE id_natal = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('natal', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_datos_nac': id_paciente,
            'apgar': datos.get('apgar'),
            'peso': datos.get('Semanas de Gestación'),
            'talla': datos.get('Horas de parto'),
            'cianosis_inicio': datos.get('Cianosis (día de inicio)'),
            'cianosis_duracion': datos.get('Cianosis (Duración)'),
            'ictericia_inicio': datos.get('Ictericia (día de inicio)'),
            'ictericia_duracion': datos.get('Ictericia (Duración)')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('datos_nacimiento', columns, values)
    query = f"SELECT id_datos_nac FROM datos_nacimiento WHERE id_datos_nac = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_datos_nac')
        query = "UPDATE datos_nacimiento SET {} WHERE id_datos_nac = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('datos_nacimiento', columns, values)
    mycursor.execute(query)
    db.commit()
    
    
# Funcion para informacion de antecedentes postnatales
def antecendentes_postnatales_sql(datos, id_paciente):
    # print(datos)
    mycursor = db.cursor()
    alimentacion  = ''
    if datos.get('alimentación_materna') == 1:
            alimentacion = 'materna,'
    if datos.get('alimentación_artificial') == 1:
            alimentacion = alimentacion + 'artifial,'
    if datos.get('alimentación_mixta') == 1:
            alimentacion = alimentacion + 'mixta'
    # print(alimentacion)
    data = {'id_postnat': id_paciente,
            'tipo_alim': alimentacion,
            'vomito': datos.get('vómitos'),
            'succion_pobre': datos.get('succión'),
            'actividad': datos.get('actividad_del_primer_año'),
            'id_motor': id_paciente,
            'id_leng': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('postnatal', columns, values)
    query = f"SELECT id_postnat FROM postnatal WHERE id_postnat = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_postnat')
        query = "UPDATE postnatal SET {} WHERE id_postnat = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('postnatal', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_motor': id_paciente,
            'gateo': datos.get('gateó'),
            'camino': datos.get('caminó_solo'),
            'control_esfinter': datos.get('control_de_esfínteres')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('desarrollo_motor', columns, values)
    query = f"SELECT id_motor FROM desarrollo_motor WHERE id_motor = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_motor')
        query = "UPDATE desarrollo_motor SET {} WHERE id_motor = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('desarrollo_motor', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_leng': id_paciente,
            'habla': datos.get('habla'),
            'edad_balbuceo': datos.get('balbuceo_(edad)'),
            'edad_2pal': datos.get('dijo_3_palabras'),
            'edad_3pal': datos.get('unió_2_palabras'),
            'edad_frases': datos.get('construyo_frases')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('desarrollo_leng', columns, values)
    query = f"SELECT id_leng FROM desarrollo_leng WHERE id_leng = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_leng')
        query = "UPDATE desarrollo_leng SET {} WHERE id_leng = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('desarrollo_leng', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_des_act': id_paciente,
            'id_vision': id_paciente,
            'id_audicion': id_paciente,
            'id_motriz': id_paciente,
            'id_leng2': id_paciente,
            'autosuficiente': datos.get('autosuficiente_en'),
            'deficiencias': datos.get('deficiente_en')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('des_actual', columns, values)
    query = f"SELECT id_des_act FROM des_actual WHERE id_des_act = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_des_act')
        query = "UPDATE des_actual SET {} WHERE id_des_act = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('des_actual', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_motriz': id_paciente,
            'correr': datos.get('corre'),
            'bicicleta': datos.get('anda_en_bicicleta'),
            'jugar': datos.get('juega'),
            'gusto_deport': datos.get('gusto_por_deportes'),
            'escribir': datos.get('escribe'),
            'dibujar': datos.get('dibuja'),
            'recortar': datos.get('recorta')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('motricidad', columns, values)
    query = f"SELECT id_motriz FROM motricidad WHERE id_motriz = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_motriz')
        query = "UPDATE motricidad SET {} WHERE id_motriz = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('motricidad', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_leng2': id_paciente,
            'todos_sonidos': datos.get('produce_sonidos_con_la_lengua'),
            'tartamudez': datos.get('tartamudea'),
            'dif_expresion': datos.get('dificultad_de_expresión'),
            'dif_comprension': datos.get('dificultad_de_comprensión'),
            'lengua1': datos.get('lengua_predominante'),
            'lengua2': datos.get('lengua_secuandaria')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('desarrollo_leng2', columns, values)
    query = f"SELECT id_leng2 FROM desarrollo_leng2 WHERE id_leng2 = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_leng2')
        query = "UPDATE desarrollo_leng2 SET {} WHERE id_leng2 = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('desarrollo_leng2', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_audicion': id_paciente,
            'normal': datos.get('audición_normal'),
            'audiometria': datos.get('audiometría'),
            'fecha': datos.get('fecha_de_audiometría'),
            'resultados': datos.get('resultado_audiometría')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('audicion', columns, values)
    query = f"SELECT id_audicion FROM audicion WHERE id_audicion = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_audicion')
        query = "UPDATE audicion SET {} WHERE id_audicion = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('audicion', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_vision': id_paciente,
            'normal': datos.get('visión_normal'),
            'examen': datos.get('examen'),
            'fecha': datos.get('fecha_de_examen'),
            'resultados': datos.get('resultado_examen'),
            'lentes': datos.get('lentes')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('vision', columns, values)
    query = f"SELECT id_vision FROM vision WHERE id_vision = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_vision')
        query = "UPDATE vision SET {} WHERE id_vision = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('vision', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_ant_pat': id_paciente,
            'id_trauma': id_paciente,
            'id_hosp': id_paciente,
            'id_convul': id_paciente,
            'id_alergias': id_paciente,
            'id_infecto_cont': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('ante_patologico', columns, values)
    query = f"SELECT id_ant_pat FROM ante_patologico WHERE id_ant_pat = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_ant_pat')
        query = "UPDATE ante_patologico SET {} WHERE id_ant_pat = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('ante_patologico', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_trauma': id_paciente,
            'fecha_tr': datos.get('fecha_de_traumatismo'),
            'duracion_tr': datos.get('duración') if datos.get('duración') != '' else 0}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('trauma', columns, values)
    query = f"SELECT id_trauma FROM trauma WHERE id_trauma = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_trauma')
        query = "UPDATE trauma SET {} WHERE id_trauma = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('trauma', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_hosp': id_paciente,
            'cirugias': datos.get('cirugías'),
            'motivo': datos.get('motivo')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('hospitalizaciones', columns, values)
    query = f"SELECT id_hosp FROM hospitalizaciones WHERE id_hosp = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_hosp')
        query = "UPDATE hospitalizaciones SET {} WHERE id_hosp = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('hospitalizaciones', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_convul': id_paciente,
            'edad_inicio': datos.get('edad_de_inicio') if datos.get('edad_de_inicio') != '' else 0,
            'tipo': datos.get('tipo'),
            'frecuencia': datos.get('frecuencia') if datos.get('frecuencia') != '' else 0,
            'fiebre': datos.get('con_fiebre'),
            'medicacion': datos.get('medicación')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('convulsiones', columns, values)
    query = f"SELECT id_convul FROM convulsiones WHERE id_convul = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_convul')
        query = "UPDATE convulsiones SET {} WHERE id_convul = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('convulsiones', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_alergias': id_paciente,
            'alergia': datos.get('¿a_qué_es_alérgic@?'),
            'manifesta': datos.get('manifestaciones'),
            'intoxicacion_plomo': datos.get('intoxicación_por_plomo'),
            'intoxicacion_medicamentos': datos.get('por_medicamentos'),
            'intoxicacion_otros': datos.get('otros')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('alergias', columns, values)
    query = f"SELECT id_alergias FROM alergias WHERE id_alergias = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_alergias')
        query = "UPDATE alergias SET {} WHERE id_alergias = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('alergias', columns, values)
    mycursor.execute(query)
    db.commit()
    
    
# Función para información de comportamiento
def comportamiento_sql(datos, id_paciente):
    # print(datos)
    mycursor = db.cursor()
    data = {'id_comp': id_paciente,
            'id_act': id_paciente,
            'id_aten': id_paciente,
            'id_crisis_col': id_paciente,
            'id_adapt': id_paciente,
            'id_lab_em': id_paciente,
            'id_rel_fam': id_paciente,
            'id_suenio': id_paciente,
            'id_comp_comer': id_paciente,
            'id_habit_alim': id_paciente,
            'id_tilibre': id_paciente,
            'id_social': id_paciente,
            'inteligencia': datos.get('inteligencia')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('comportamiento', columns, values)
    query = f"SELECT id_comp FROM comportamiento WHERE id_comp = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_comp')
        query = "UPDATE comportamiento SET {} WHERE id_comp = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('comportamiento', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_act': id_paciente,
            'hipoactivo': datos.get('hipoactivo'),
            'hiperactivo': datos.get('hiperactivo'),
            'destructivo': datos.get('destructivo'),
            'agresivo': datos.get('agresivo')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('actividad', columns, values)
    query = f"SELECT id_act FROM actividad WHERE id_act = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_act')
        query = "UPDATE actividad SET {} WHERE id_act = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('actividad', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_aten': id_paciente,
            'constante': datos.get('constante'),
            'corta': datos.get('corta'),
            'nula': datos.get('nula'),
            'variable': datos.get('variable')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('atencion', columns, values)
    query = f"SELECT id_aten FROM atencion WHERE id_aten = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_aten')
        query = "UPDATE atencion SET {} WHERE id_aten = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('atencion', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_crisis_col': id_paciente,
            'berrinches': datos.get('berrinches'),
            'arroja_c': datos.get('arroja_cosas_al_enojarse'),
            'arre_verb': datos.get('arremete_verbalemente'),
            'irascible': datos.get('variable')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('crisis', columns, values)
    query = f"SELECT id_crisis_col FROM crisis WHERE id_crisis_col = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_crisis_col')
        query = "UPDATE crisis SET {} WHERE id_crisis_col = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('crisis', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_adapt': id_paciente,
            'separa_pad': datos.get('se_separa_de_los_padres'),
            'adecua': datos.get('se_adecua_a_la_situación'),
            'reac_cat': datos.get('reacciones_catastróficas')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('adaptacion', columns, values)
    query = f"SELECT id_adapt FROM adaptacion WHERE id_adapt = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_adapt')
        query = "UPDATE adaptacion SET {} WHERE id_adapt = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('adaptacion', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_lab_em': id_paciente,
            'llora_facil': datos.get('llora_muy_facilmente'),
            'llanto_risa': datos.get('pasa_del_llanto_a_la_risa'),
            'emo_facil': datos.get('se_emociona_facilmente')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('labilidad_emo', columns, values)
    query = f"SELECT id_lab_em FROM labilidad_emo WHERE id_lab_em = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_lab_em')
        query = "UPDATE labilidad_emo SET {} WHERE id_lab_em = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('labilidad_emo', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_rel_fam': id_paciente,
            'dif_madre': datos.get('difícil_relación_con_papá'),
            'dif_padre': datos.get('difícil_relación_con_mamá'),
            'dif_hermanos': datos.get('difícil_relación_con_herm.')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('rel_fam', columns, values)
    query = f"SELECT id_rel_fam FROM rel_fam WHERE id_rel_fam = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_rel_fam')
        query = "UPDATE rel_fam SET {} WHERE id_rel_fam = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('rel_fam', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_suenio': id_paciente,
            'prom_horas': datos.get('promedio_de_horas_de_sueño') if datos.get('promedio_de_horas_de_sueño') != '' else 0,
            'sonam': datos.get('sonambulismo'),
            'siesta': datos.get('duerme_siesta'),
            'pesadillas': datos.get('pesadillas'),
            'dif_dormir': datos.get('dificultad_para_conciliar_sueño'),
            'dif_despertar': datos.get('dificil_despertar'),
            'suenio_cont': datos.get('sueño_continuo')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('suenio', columns, values)
    query = f"SELECT id_suenio FROM suenio WHERE id_suenio = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_suenio')
        query = "UPDATE suenio SET {} WHERE id_suenio = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('suenio', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_comp_comer': id_paciente,
            'sentado': datos.get('permanece_sentado'),
            'cubiertos': datos.get('juega_con_los_cubiertos'),
            'derrama': datos.get('derrama_los_alimentos'),
            'come_sin_d': datos.get('come_sin_distracción')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('comp_comer', columns, values)
    query = f"SELECT id_comp_comer FROM comp_comer WHERE id_comp_comer = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_comp_comer')
        query = "UPDATE comp_comer SET {} WHERE id_comp_comer = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('comp_comer', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_habit_alim': id_paciente,
            'c_comidas': datos.get('¿comidas_al_día?'),
            'selectivo': datos.get('¿es_selectivo_con_los_alimentos?')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('habit_alim', columns, values)
    query = f"SELECT id_habit_alim FROM habit_alim WHERE id_habit_alim = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_habit_alim')
        query = "UPDATE habit_alim SET {} WHERE id_habit_alim = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('habit_alim', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_tilibre': id_paciente,
            'tv': datos.get('tv'),
            'vjuegos': datos.get('videojuegos'),
            'compu': datos.get('computadora'),
            'j_aire': datos.get('juego_al_aire_libre'),
            'j_fantasia': datos.get('juego_de_fantasía'),
            't_lectura': datos.get('lectura'),
            'j_colectivos': datos.get('juegos_colectivos'),
            'j_construccion': datos.get('juegos_de_construcción')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('tiempo_libre', columns, values)
    query = f"SELECT id_tilibre FROM tiempo_libre WHERE id_tilibre = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_tilibre')
        query = "UPDATE tiempo_libre SET {} WHERE id_tilibre = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('tiempo_libre', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_social': id_paciente,
            'retraido': datos.get('retraído'),
            'abierto': datos.get('abierto'),
            'aislado': datos.get('aislado'),
            'facil_amigos': datos.get('facilidad_para_hacer_amigos'),
            'amigos_edad': datos.get('amigos_de_su_edad'),
            'amigos_grandes': datos.get('amigos_mayores'),
            'amigos_pequenos': datos.get('amigos_menores'),
            'amigos_otros': datos.get('otros_amigos')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('socializacion', columns, values)
    query = f"SELECT id_social FROM socializacion WHERE id_social = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_social')
        query = "UPDATE socializacion SET {} WHERE id_social = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('socializacion', columns, values)
    mycursor.execute(query)
    db.commit()
    
# Funcion para información de métodos de disciplina
def metodos_disciplina_sql(datos, id_paciente):
    # print(datos)
    mycursor = db.cursor()
    data = {'id_metod_dis': id_paciente,
            'reganio': datos.get('regaño'),
            'castigo_fis': datos.get('castigo_físico'),
            't_fuera': datos.get('tiempo_fuera'),
            'premio': datos.get('premio'),
            'convencimiento': datos.get('convencimiento'),
            'metod_otros': datos.get('otros')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('metod_dis', columns, values)
    query = f"SELECT id_metod_dis FROM metod_dis WHERE id_metod_dis = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_metod_dis')
        query = "UPDATE metod_dis SET {} WHERE id_metod_dis = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('metod_dis', columns, values)
    mycursor.execute(query)
    db.commit()
    
# Funcion para información de escolaridad
def escolaridad_sql(datos, id_paciente):
    # print(datos)
    problema = ''
    if datos.get('lectura_problemas') == 1:
            problema = 'lectura,'
    if datos.get('escritura_problemas') == 1:
            problema += 'escritura,'
    if datos.get('cálculo_problemas') == 1:
            problema += 'cálculo,'
    if datos.get('lenguaje_problemas') == 1:
            problema += 'lenguaje,'
    if datos.get('hiperactvidad_problemas') == 1:
            problema += 'hiperactvidad,'
    if datos.get('atención_problemas') == 1:
            problema += 'atención,'
    if datos.get('otros_problemas') == 1:
            problema += 'otros'
    mycursor = db.cursor()
    data = {'id_escil': id_paciente,
            'asiste': datos.get('¿asiste_el_niño_a_la_escuela?'),
            'id_bilingue': id_paciente,
            'prob_espec': problema,
            'id_guarderia': id_paciente,
            'id_jardin': id_paciente,
            'id_primaria': id_paciente,
            'id_secundaria': id_paciente,
            'id_prepa': id_paciente,
            'id_apt_inter': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('escolaridad', columns, values)
    query = f"SELECT id_escil FROM escolaridad WHERE id_escil = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_escil')
        query = "UPDATE escolaridad SET {} WHERE id_escil = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('escolaridad', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_bilingue': id_paciente,
            'educ_bilingue': datos.get('educación_bilingue'),
            'lengua': datos.get('segunda_lengua'),
            'lengua_inicio': datos.get('edad_de_inicio') if datos.get('edad_de_inicio') != '' else 0}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('bilingue', columns, values)
    query = f"SELECT id_bilingue FROM bilingue WHERE id_bilingue = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_bilingue')
        query = "UPDATE bilingue SET {} WHERE id_bilingue = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('bilingue', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_guarderia': id_paciente,
            'guarderia': datos.get('guardería_guarderia'),
            'g_ingreso': datos.get('edad_de_ingreso_guarderia') if datos.get('edad_de_ingreso_guarderia') != '' else 0,
            'g_duracion': datos.get('¿cuántos_años?_guarderia') if datos.get('¿cuántos_años?_guarderia') != '' else 0}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('guarderia', columns, values)
    query = f"SELECT id_guarderia FROM guarderia WHERE id_guarderia = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_guarderia')
        query = "UPDATE guarderia SET {} WHERE id_guarderia = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('guarderia', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    rendimiento = ''
    if datos.get('rendimiento_bueno_jardin') == 1:
        rendimiento = 2
    elif datos.get('rendimiento_malo_jardin') == 1:
        rendimiento = 0
    elif datos.get('rendimiento_regular_jardin') == 1:
        rendimiento = 1
    data = {'id_jardin': id_paciente,
            'jardin': datos.get('jardín_de_niños_jardin'),
            'j_ingreso': datos.get('edad_de_ingreso_jardin') if datos.get('edad_de_ingreso_jardin') != '' else 0,
            'j_duracion': datos.get('¿cuántos_años?_jardin') if datos.get('¿cuántos_años?_jardin') != '' else 0,
            'j_rendimiento': rendimiento}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('jardin', columns, values)
    query = f"SELECT id_jardin FROM jardin WHERE id_jardin = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_jardin')
        query = "UPDATE jardin SET {} WHERE id_jardin = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('jardin', columns, values)
    mycursor.execute(query)
    db.commit()
    if datos.get('rendimiento(bueno,_malo,_reg)_primaria').lower() == 'bueno':
        rendimiento = 2
    elif datos.get('rendimiento(bueno,_malo,_reg)_primaria').lower() == 'regular':
        rendimiento = 1
    else:
        rendimiento = 0
    mycursor = db.cursor()
    data = {'id_primaria': id_paciente,
            'p_ingreso': datos.get('edad_de_ingreso_primaria'),
            'p_tiempo': datos.get('¿cuántos_años?_primaria'),
            'p_rendimiento': rendimiento,
            'p_grad_repet': datos.get('grados_repetidos_primaria') if datos.get('grados_repetidos_primaria') != '' else 0,
            'id_pterap_clases': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('primaria', columns, values)
    query = f"SELECT id_primaria FROM primaria WHERE id_primaria = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_primaria')
        query = "UPDATE primaria SET {} WHERE id_primaria = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('primaria', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_pterap_clases': id_paciente,
            'p_clases': datos.get('clases_particulares_primaria'),
            'p_clases_edad': datos.get('edad_o_grado_escolar_primaria'),
            'p_clases_materia': datos.get('materias_primaria'),
            'p_terap': datos.get('terapias_de_apoyo_primaria'),
            'p_terap_edad': datos.get('edad_o_grado_escolar._primaria') if datos.get('edad_o_grado_escolar._primaria') != '' else 0,
            'p_terap_tipo': datos.get('¿qué_tipo?_primaria'),
            'p_terap_tiempo': datos.get('¿por_cuánto_tiempo?_primaria'),
            'p_terap_prob': datos.get('problemas_específicos_primaria')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('clases_terap', columns, values)
    query = f"SELECT id_pterap_clases FROM clases_terap WHERE id_pterap_clases = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_pterap_clases')
        query = "UPDATE clases_terap SET {} WHERE id_pterap_clases = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('clases_terap', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    if datos.get('rendimiento_secundaria').lower() == 'bueno':
        rendimiento = 2
    elif datos.get('rendimiento_secundaria').lower() == 'regular':
        rendimiento = 1
    else:
        rendimiento = 0
    data = {'id_secundaria': id_paciente,
            's_ingreso': datos.get('edad_de_ingreso_secundaria'),
            's_rendimiento': rendimiento,
            's_grad_repet': datos.get('grados_repetidos_secundaria') if datos.get('grados_repetidos_secundaria') != '' else 0,
            'id_sterap_clases': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('secundaria', columns, values)
    query = f"SELECT id_secundaria FROM secundaria WHERE id_secundaria = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_secundaria')
        query = "UPDATE secundaria SET {} WHERE id_secundaria = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('secundaria', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_sterap_clases': id_paciente,
            's_clases': datos.get('clases_particulares_secundaria'),
            's_clases_edad': datos.get('edad_o_grado_escolar_secundaria'),
            's_clases_materia': datos.get('materias_secundaria'),
            's_terap': datos.get('terapias_de_apoyo_secundaria'),
            's_terap_edad': datos.get('edad_o_grado_escolar._secundaria'),
            's_terap_tipo': datos.get('¿qué_tipo?_secundaria'),
            's_terap_tiempo': datos.get('¿por_cuánto_tiempo?_secundaria'),
            's_terap_prob': datos.get('problemas_específicos_secundaria')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('clases_terap2', columns, values)
    query = f"SELECT id_sterap_clases FROM clases_terap2 WHERE id_sterap_clases = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_sterap_clases')
        query = "UPDATE clases_terap2 SET {} WHERE id_sterap_clases = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('clases_terap2', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    if datos.get('rendimiento_prepa').lower() == 'bueno':
        rendimiento = 2
    elif datos.get('rendimiento_prepa').lower() == 'regular':
        rendimiento = 1
    else:
        rendimiento = 0
    data = {'id_prepa': id_paciente,
            'pre_ingreso': datos.get('edad_de_ingreso_prepa'),
            'pre_rendimiento': rendimiento,
            'pre_grad_repet': datos.get('grados_repetidos_prepa') if datos.get('grados_repetidos_prepa') != '' else 0,
            'id_preterap_clases': id_paciente}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('preparatoria', columns, values)
    query = f"SELECT id_prepa FROM preparatoria WHERE id_prepa = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_prepa')
        query = "UPDATE preparatoria SET {} WHERE id_prepa = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('preparatoria', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_preterap_clases': id_paciente,
            'pre_clases': datos.get('clases_particulares_prepa'),
            'pre_clases_edad': datos.get('edad_y_semestre_prepa'),
            'pre_clases_materia': datos.get('materias_prepa'),
            'pre_terap': datos.get('terapias_de_apoyo_prepa'),
            'pre_terap_edad': datos.get('edad_y_semestre._prepa'),
            'pre_terap_tipo': datos.get('¿qué_tipo?_prepa'),
            'pre_terap_tiempo': datos.get('¿por_cuánto_tiempo?_prepa'),
            'pre_terap_prob': datos.get('problemas_específicos_prepa')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('clases_terap3', columns, values)
    query = f"SELECT id_preterap_clases FROM clases_terap3 WHERE id_preterap_clases = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_preterap_clases')
        query = "UPDATE clases_terap3 SET {} WHERE id_preterap_clases = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('clases_terap3', columns, values)
    mycursor.execute(query)
    db.commit()
    mycursor = db.cursor()
    data = {'id_apt_inter': id_paciente,
            'apt_lectura': datos.get('lectura_intereses'),
            'apt_escritura': datos.get('escritura_intereses'),
            'apt_mate': datos.get('matemáticas_intereses'),
            'apt_deportes': datos.get('deportes_intereses'),
            'apt_dibujo': datos.get('dibujo_intereses'),
            'apt_ciencias': datos.get('ciencias_intereses'),
            'apt_csociales': datos.get('ciencias_sociales_intereses'),
            'apt_musica': datos.get('música'),
            'apt_otras': datos.get('otras'),
            'apt_coment': datos.get('comentarios')}
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    query = "INSERT INTO %s (%s ) VALUES (%s );" % ('apt_inter', columns, values)
    query = f"SELECT id_apt_inter FROM apt_inter WHERE id_apt_inter = '{id_paciente}'"
    mycursor.execute(query)
    try:
        info = mycursor.fetchall()[0]
    except:
        info = False
    if info != False:
        data.pop('id_apt_inter')
        query = "UPDATE apt_inter SET {} WHERE id_apt_inter = '{}'".format(', '.join("{}='{}'".format(k, data[k]) for k in data), id_paciente)
    else:
        query = "INSERT INTO %s (%s ) VALUES (%s );" % ('apt_inter', columns, values)
    mycursor.execute(query)
    db.commit()