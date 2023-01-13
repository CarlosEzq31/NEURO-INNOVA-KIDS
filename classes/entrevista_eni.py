import hashlib, datetime
from classes.env import *

class EntrevistaEni():
    def __init__(self, paciente):
        self.paciente = paciente
        self.id = hashlib.new("sha256", f"{self.paciente.id}".encode()).hexdigest()
        self.datos = {}

    def agregar_datos(self, seccion: str, datos: dict):
        """
        Agrega los datos de la entrevista a la base de datos

        Parametros
        ----------
        seccion: str
            Seccion de la entrevista
        datos: dict
            Datos de la seccion de la entrevista
        """
        # Cambiar Si's y No's por 1's y 0's
        for key, value in datos.items():
            if value == "Si":
                datos[key] = 1
            elif value == "No":
                datos[key] = 0
        if seccion in self.datos:
            self.datos[seccion].update(datos)
        else:
            self.datos[seccion] = datos
    
    
    def __str__(self):
        string = "{"
        for key, value in vars(self).items():
            string += f"'{key}': {value}, "
        string  = string[:-2] + "}"
        return string
    
    def __repr__(self):
        return self.__str__()

    def registrar_entrevista(self):
        """
        Registra la entrevista en la base de datos mysql y retorna True si se registro correctamente
        """
        # Historial familiar
        datos = self.datos["historia_familiar"]
        query = """
        INSERT INTO familiar (`id_fam`, `problema_lenguaje`, `deficiencia_sensorial`, `paralisis_sensorial`, `epilepsia`, `deficit_atencion`, `problemas_coordinacion`, `drogadiccion`, `alcoholismo`, `enfermedad_psiquiatrica`, `sindrome_down`, `retardo_mental`, `problema_aprendizaje`, `retraso_escolar`, `otros`)  values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["problema_lenguaje"], datos["deficiencia_sensorial"], datos["paralisis_sensorial"], datos["epilepsia"], datos["deficit_atención"], datos["prob_coord_motriz"], datos["drogadiccion"], datos["alcoholismo"], datos["enferm_psiquiatrica"], datos["sind_down"], datos["retardo_mental"], datos["prob_aprendizaje"], datos["retraso_escolar"], datos["otros"])

        # Antecedentes prenatales
        datos = self.datos["antecedentes_prenatales"]
        query += """
        INSERT INTO prenatales (`id_pren`, `prod_gesta`, `embar_deseo`, `drogas_embar`, `alim_embar`, `id_pad_emb`, `id_exp_emb`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["semanas_gestacion"], datos["embarazo_deseado"], datos["cuales_embarazo"], datos["calidad_alimentacion"], datos["id_pad_emb"], datos["id_exp_emb"])
        query += """
        INSERT INTO expo_embarazo (`id_exp_emb`, `rayos_x`, `rayos_x_mes`, `vacunas`, `vacunas_mes`, `medicamentos`, `medicamentos_mes`, `otros`, `otros_mes`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["rayos_x"], datos["en_que_mes_rayos_x"], datos["cuales_vacunas"], datos["en_que_mes_vacunas"], datos["cuales_medicamentos"], datos["en_que_mes_medicamentos"], datos["otros_expo"], datos["en_que_mes_otros"])
        query += """
        INSERT INTO padE_emb (`id_pad_emb`, `rubeola`, `varicela`, `edema`, `traumatismo`, `amenaza_aborto`, `sifilis`, `toxoplasmosis`, `vih`, `hipertension`, `toxemia`, `otros`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["rubeola"], datos["varicela"], datos["edema"], datos["traumatismo"], datos["amenaza_aborto"], datos["sifilis"], datos["toxoplasmosis"], datos["vih"], datos["hipertension"], datos["toxemia"], datos["otros"])

        # Antecedentes natales
        datos = self.datos["antecedentes_natales"]
        query += """
        INSERT INTO natales (`id_natal`, `tipo_parto`, `sem_gestacion`, `duracion_parto`, `necesidades`, `sufrimiento`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["parto"], datos["semanas"], datos["horas"], datos["nino_necesito"], datos["sufrimiento_nasal"])
        query += """
        INSERT INTO datos_nacimiento (`id_datos_nac`, `apgar`, `peso`, `talla`, `cianosis_inicio`, `cianosis_duracion`, `ictericia_inicio`, `ictericia_duracion`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["apgar"], datos["peso"], datos["talla"], datos["cianosis"], datos["cianosis_duracion"], datos["ictericia"], datos["ictericia_duracion"])

        # Antecedentes postnatales
        datos = self.datos["antecedentes_postnatales"]
        datos['tipo_alimentacion'] = 0 if datos['alimentacion_materna'] == 'Si' else 1 if datos['alimentacion_artificial'] == 'No' else 2
        "id_postnat, tipo_alim, vomito, succion_pobre, actividad, id_motor, id_leng"
        query += """
        INSERT INTO postnatales (`id_postnat`, `tipo_alim`, `vomito`, `succion_pobre`, `actividad`, `id_motor`, `id_leng`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["tipo_alimentacion"], datos["vomito"],  datos["succion"], datos["actividad_primer_ano"], self.id, self.id)
        query += """
        INSERT INTO desarrollo_motor (`id_motor`, `gateo`, `camino`, `control_esfinter`) values (`%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["gateo"], datos["camino_solo"], datos["control_esfinteres"])
        query += """
        INSERT INTO desarrollo_leng (`id_leng`, `habla`, `edad_balbuceo`, `edad_2pal`, `edad_3pal`, `edad_frases`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["habla"], datos["'balbuceo_edad"], datos["unio_2_palabras_edad"], datos["dijo_3_palabras_edad"], datos["construyo_frases_edad"])
        query += """
        INSERT INTO des_actual (`id_des_act`, `id_vision`, `id_audicion`, `autosuficiente`, `deficiencias`, `id_motriz`, `id_leng2`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, self.id, self.id, datos["autosuficiente_en"], datos["deficiente_en"], self.id, self.id)
        query += """
        INSERT INTO motricidad (`id_motriz`, `correr`, `bicicleta`, `jugar`, `gusto_deport`, `escribir`, `dibujar`, `recortar`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["corre"], datos["anda_en_bicicleta"], datos["juega"], datos["gusto_por_los_deportes"], datos["escribe"], datos["dibuja"], datos["recorta"])
        query += """
        INSERT INTO desarrollo_leng2 (`id_leng2`, `todos_sonidos`, `tartamudez`, `dif_expresion`, `dif_comprension`, `lengua1`, `lengua2`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["produce_sonidos_con_la_lengua"], datos["tartamudea"], datos["dificultad_de_expresion"], datos["dificultad_de_comprension"], datos["lengua_predominante"], datos["lengua_secundaria"])
        query += """
        INSERT INTO audicion (`id_audicion`, `normal`, `audiometria`, `fecha`, `resultados`) values (`%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["audicion_normal"], datos["audiometria"], datos["fecha_audiometria"], datos["resultados_audiometria"])
        query += """
        INSERT INTO vision (`id_vision`, `normal`, `examen`, `fecha`, `resultados`, `lentes`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["vision_normal"], datos["examen"], datos["fecha_examen"], datos["resultado_examen"], datos["lentes"])
        "id_ant_pat, id_trauma, id_hosp, id_convul, id_infecto_cont, id_alergias"
        query += """
        INSERT INTO ante_patologicos(`id_ant_pat`, `id_trauma`, `id_hosp`, `id_convul`, `id_infecto_cont`, `id_alergias`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, self.id, self.id, self.id, self.id, self.id)
        "id_trauma, fecha_tr, duracion_tr"
        query += """
        INSERT INTO trauma (`id_trauma`, `fecha_tr`, `duracion_tr`) values (`%s`, `%s`, `%s`)
        ; """ % (self.id, datos["fecha_traumatismo"], datos["duracion_traumatismo"])
        "id_hosp, cirugias, motivo"
        query += """
        INSERT INTO hospitalizaciones (`id_hosp`, `cirugias`, `motivo`) values (`%s`, `%s`, `%s`)
        ; """ % (self.id, datos["cirugias"], datos["motivo_cirugia"])
        "id_convul, edad_inicio, tipo, frecuencia, fiebre, medicacion"
        query += """
        INSERT INTO convulsiones (`id_convul`, `edad_inicio`, `tipo`, `frecuencia`, `fiebre`, `medicacion`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["edad_inicio"], datos["tipo_convulsiones"], datos["frecuencia_convulsiones"], datos["con_fiebre"], datos["medicacion"])
        "id_alergias, alergia, manifesta, intoxicacion_plomo, intoxicacion_medicamentos, intoxicacion_otros"
        query += """
        INSERT INTO alergias (`id_alergias`, `alergia`, `manifesta`, `intoxicacion_plomo`, `intoxicacion_medicamentos`, `intoxicacion_otros`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, datos["alergia"], datos["manifestaciones"], datos["intoxicacion_plomo"], datos["por_medicamentos"], datos["otros"])

        # Comportamiento
        "id_comp, id_act, id_aten, id_crisis_col, id_adapt, id_lab_em, id_rel_fam, id_suenio, id_comp_comer, id_habit_alim, id_tilibre, id_social, inteligencia"
        query += """
        INSERT INTO comportamiento (`id_comp`, `id_act`, `id_aten`, `id_crisis_col`, `id_adapt`, `id_lab_em`, `id_rel_fam`, `id_suenio`, `id_comp_comer`, `id_habit_alim`, `id_tilibre`, `id_social`, `inteligencia`) values (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`)
        ; """ % (self.id, self.id, self.id, self.id, self.id, self.id, self.id, self.id, self.id, self.id, self.id, self.id, self.id)
        