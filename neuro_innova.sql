-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-04-2022 a las 20:25:03
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
USE `neuro_innova`;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `neuro_innova`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `id_act` varchar(10) NOT NULL,
  `hipoactivo` int(1) NOT NULL,
  `hiperactivo` int(1) NOT NULL,
  `destructivo` int(1) NOT NULL,
  `agresivo` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adaptacion`
--

CREATE TABLE `adaptacion` (
  `id_adapt` varchar(10) NOT NULL,
  `separa_pad` int(1) NOT NULL,
  `adecua` int(1) NOT NULL,
  `reac_cat` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alergias`
--

CREATE TABLE `alergias` (
  `id_alergias` varchar(10) NOT NULL,
  `alergia` varchar(30) NOT NULL,
  `manifesta` varchar(30) NOT NULL,
  `intoxicacion_plomo` int(1) NOT NULL,
  `intoxicacion_medicamentos` int(1) NOT NULL,
  `intoxicacion_otros` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ante_patologico`
--

CREATE TABLE `ante_patologico` (
  `id_ant_pat` varchar(10) NOT NULL,
  `id_trauma` varchar(10) NOT NULL,
  `id_hosp` varchar(10) NOT NULL,
  `id_convul` varchar(10) NOT NULL,
  `id_infecto_cont` varchar(10) NOT NULL,
  `id_alergias` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `apt_inter`
--

CREATE TABLE `apt_inter` (
  `id_apt_inter` varchar(10) NOT NULL,
  `apt_lectura` int(1) NOT NULL,
  `apt_escritura` int(1) NOT NULL,
  `apt_mate` int(1) NOT NULL,
  `apt_deportes` int(1) NOT NULL,
  `apt_dibujo` int(1) NOT NULL,
  `apt_ciencias` int(1) NOT NULL,
  `apt_csociales` int(1) NOT NULL,
  `apt_musica` int(1) NOT NULL,
  `apt_otras` varchar(50) NOT NULL,
  `apt_coment` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atencion`
--

CREATE TABLE `atencion` (
  `id_aten` varchar(10) NOT NULL,
  `constante` int(1) NOT NULL,
  `corta` int(1) NOT NULL,
  `nula` int(1) NOT NULL,
  `variable` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `audicion`
--

CREATE TABLE `audicion` (
  `id_audicion` varchar(10) NOT NULL,
  `normal` int(1) NOT NULL,
  `audiometria` int(1) NOT NULL,
  `fecha` varchar(9) NOT NULL,
  `resultados` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bilingue`
--

CREATE TABLE `bilingue` (
  `id_bilingue` varchar(10) NOT NULL,
  `educ_bilingue` int(1) NOT NULL,
  `lengua` varchar(30) NOT NULL,
  `lengua_inicio` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clases_terap`
--

CREATE TABLE `clases_terap` (
  `id_pterap_clases` varchar(10) NOT NULL,
  `p_clases` int(1) NOT NULL,
  `p_clases_edad` int(2) NOT NULL,
  `p_clases_materia` varchar(25) NOT NULL,
  `p_terap` int(1) NOT NULL,
  `p_terap_edad` int(2) NOT NULL,
  `p_terap_tipo` varchar(30) NOT NULL,
  `p_terap_tiempo` varchar(20) NOT NULL,
  `p_terap_prob` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clases_terap2`
--

CREATE TABLE `clases_terap2` (
  `id_sterap_clases` varchar(10) NOT NULL,
  `s_clases` int(1) NOT NULL,
  `s_clases_edad` int(2) NOT NULL,
  `s_clases_materia` varchar(15) NOT NULL,
  `s_terap` int(1) NOT NULL,
  `s_terap_edad` int(2) NOT NULL,
  `s_terap_tipo` varchar(30) NOT NULL,
  `s_terap_tiempo` varchar(20) NOT NULL,
  `s_terap_prob` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clases_terap3`
--

CREATE TABLE `clases_terap3` (
  `id_preterap_clases` varchar(10) NOT NULL,
  `pre_clases` int(1) NOT NULL,
  `pre_clases_edad` int(2) NOT NULL,
  `pre_clases_materia` varchar(15) NOT NULL,
  `pre_terap` int(1) NOT NULL,
  `pre_terap_edad` int(2) NOT NULL,
  `pre_terap_tipo` varchar(30) NOT NULL,
  `pre_terap_tiempo` varchar(20) NOT NULL,
  `pre_terap_prob` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comportamiento`
--

CREATE TABLE `comportamiento` (
  `id_comp` varchar(10) NOT NULL,
  `id_act` varchar(10) NOT NULL,
  `id_aten` varchar(10) NOT NULL,
  `id_crisis_col` varchar(10) NOT NULL,
  `id_adapt` varchar(10) NOT NULL,
  `id_lab_em` varchar(10) NOT NULL,
  `id_rel_fam` varchar(10) NOT NULL,
  `id_suenio` varchar(10) NOT NULL,
  `id_comp_comer` varchar(10) NOT NULL,
  `id_habit_alim` varchar(10) NOT NULL,
  `id_tilibre` varchar(10) NOT NULL,
  `id_social` varchar(10) NOT NULL,
  `inteligencia` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comp_comer`
--

CREATE TABLE `comp_comer` (
  `id_comp_comer` varchar(10) NOT NULL,
  `sentado` int(1) NOT NULL,
  `cubiertos` int(1) NOT NULL,
  `derrama` int(1) NOT NULL,
  `come_sin_d` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `convulsiones`
--

CREATE TABLE `convulsiones` (
  `id_convul` varchar(10) NOT NULL,
  `edad_inicio` int(3) NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `frecuencia` int(3) NOT NULL,
  `fiebre` int(1) NOT NULL,
  `medicacion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `crisis`
--

CREATE TABLE `crisis` (
  `id_crisis_col` varchar(10) NOT NULL,
  `berrinches` int(1) NOT NULL,
  `arroja_c` int(1) NOT NULL,
  `arre_verb` int(1) NOT NULL,
  `irascible` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_nacimiento`
--

CREATE TABLE `datos_nacimiento` (
  `id_datos_nac` varchar(30) NOT NULL,
  `apgar` int(1) NOT NULL,
  `peso` float NOT NULL,
  `talla` float NOT NULL,
  `cianosis_inicio` int(3) NOT NULL,
  `cianosis_duracion` int(3) NOT NULL,
  `ictericia_inicio` int(3) NOT NULL,
  `ictericia_duracion` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desarrollo_leng`
--

CREATE TABLE `desarrollo_leng` (
  `id_leng` varchar(10) NOT NULL,
  `habla` int(1) NOT NULL,
  `edad_balbuceo` int(2) NOT NULL,
  `edad_2pal` int(2) NOT NULL,
  `edad_3pal` int(2) NOT NULL,
  `edad_frases` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desarrollo_leng2`
--

CREATE TABLE `desarrollo_leng2` (
  `id_leng2` varchar(10) NOT NULL,
  `todos_sonidos` int(1) NOT NULL,
  `tartamudez` int(1) NOT NULL,
  `dif_expresion` int(1) NOT NULL,
  `dif_comprension` int(1) NOT NULL,
  `lengua1` varchar(20) NOT NULL,
  `lengua2` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desarrollo_motor`
--

CREATE TABLE `desarrollo_motor` (
  `id_motor` varchar(10) NOT NULL,
  `gateo` int(1) NOT NULL,
  `camino` int(1) NOT NULL,
  `control_esfinter` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `des_actual`
--

CREATE TABLE `des_actual` (
  `id_des_act` varchar(10) NOT NULL,
  `id_vision` varchar(10) NOT NULL,
  `id_audicion` varchar(10) NOT NULL,
  `autosuficiente` varchar(30) NOT NULL,
  `deficiencias` varchar(30) NOT NULL,
  `id_motriz` varchar(10) NOT NULL,
  `id_leng2` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eni`
--

CREATE TABLE `eni` (
  `id_eni` varchar(10) NOT NULL,
  `id_ent` varchar(10) NOT NULL,
  `id_fam` varchar(10) NOT NULL,
  `id_pren` varchar(10) NOT NULL,
  `id_natal` varchar(10) NOT NULL,
  `id_postnat` varchar(10) NOT NULL,
  `id_des_act` varchar(10) NOT NULL,
  `id_ant_pat` varchar(10) NOT NULL,
  `id_comp` varchar(10) NOT NULL,
  `id_metod_dis` varchar(10) NOT NULL,
  `id_escol` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermedades_contag`
--

CREATE TABLE `enfermedades_contag` (
  `id_infecto_cont` varchar(10) NOT NULL,
  `sarampion` int(1) NOT NULL,
  `meningitis` int(1) NOT NULL,
  `encefalitis` int(1) NOT NULL,
  `otras` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entrevista`
--

CREATE TABLE `entrevista` (
  `id_ent` varchar(20) NOT NULL,
  `id_paciente` varchar(10) NOT NULL,
  `id_eni` varchar(10) NOT NULL,
  `id_magallanes` varchar(10) NOT NULL,
  `id_prueba` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE `escolaridad` (
  `id_escil` varchar(10) NOT NULL,
  `asiste` int(1) NOT NULL,
  `id_bilingue` varchar(10) NOT NULL,
  `prob_espec` varchar(60) NOT NULL,
  `id_guarderia` varchar(10) NOT NULL,
  `id_jardin` varchar(10) NOT NULL,
  `id_primaria` varchar(10) NOT NULL,
  `id_secundaria` varchar(10) NOT NULL,
  `id_prepa` varchar(10) NOT NULL,
  `id_apt_inter` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `expo_embarazo`
--

CREATE TABLE `expo_embarazo` (
  `id_exp_emb` varchar(10) NOT NULL,
  `rayos_x` varchar(30) NOT NULL,
  `rayos_x_mes` int(1) NOT NULL,
  `vacunas` varchar(30) NOT NULL,
  `vacunas_mes` int(1) NOT NULL,
  `medicamentos` varchar(30) NOT NULL,
  `medicamentos_mes` int(1) NOT NULL,
  `otros` varchar(30) NOT NULL,
  `otros_mes` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `familiar`
--

CREATE TABLE `familiar` (
  `id_fam` varchar(10) NOT NULL,
  `problema_lenguje` varchar(50) NOT NULL,
  `deficiencia_sensorial` varchar(50) NOT NULL,
  `paralisis_sensorial` varchar(50) NOT NULL,
  `epilsepsia` varchar(50) NOT NULL,
  `deficit_atencion` varchar(50) NOT NULL,
  `problemas_coordinacion` varchar(50) NOT NULL,
  `drogadiccion` varchar(50) NOT NULL,
  `alcoholismo` varchar(50) NOT NULL,
  `enfermedad_psiquiatrica` varchar(50) NOT NULL,
  `sindrome_down` varchar(50) NOT NULL,
  `retardo_mental` varchar(50) NOT NULL,
  `problema_aprendizaje` varchar(50) NOT NULL,
  `retraso_escolar` varchar(50) NOT NULL,
  `otros` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guarderia`
--

CREATE TABLE `guarderia` (
  `id_guarderia` varchar(10) NOT NULL,
  `guarderia` int(1) NOT NULL,
  `g_ingreso` int(2) NOT NULL,
  `g_duracion` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habit_alim`
--

CREATE TABLE `habit_alim` (
  `id_habit_alim` varchar(10) NOT NULL,
  `c_comidas` int(1) NOT NULL,
  `selectivo` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hospitalizaciones`
--

CREATE TABLE `hospitalizaciones` (
  `id_hosp` varchar(10) NOT NULL,
  `cirugias` int(1) NOT NULL,
  `motivo` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jardin`
--

CREATE TABLE `jardin` (
  `id_jardin` varchar(10) NOT NULL,
  `jardin` int(1) NOT NULL,
  `j_ingreso` int(1) NOT NULL,
  `j_duracion` int(1) NOT NULL,
  `j_rendimiento` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `labilidad_emo`
--

CREATE TABLE `labilidad_emo` (
  `id_lab_em` varchar(10) NOT NULL,
  `llora_facil` int(1) NOT NULL,
  `llanto_risa` int(1) NOT NULL,
  `emo_facil` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `magallanes`
--

CREATE TABLE `magallanes` (
  `id_magallanes` varchar(10) NOT NULL,
  `calla` int(1) NOT NULL,
  `mov` int(1) NOT NULL,
  `sent` int(1) NOT NULL,
  `rapid` int(1) NOT NULL,
  `ocup` int(1) NOT NULL,
  `distr` int(1) NOT NULL,
  `aban` int(1) NOT NULL,
  `tarea` int(1) NOT NULL,
  `aten` int(1) NOT NULL,
  `movEx` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metod_dis`
--

CREATE TABLE `metod_dis` (
  `id_metod_dis` varchar(10) NOT NULL,
  `reganio` int(1) NOT NULL,
  `castigo_fis` int(1) NOT NULL,
  `t_fuera` int(1) NOT NULL,
  `premio` int(1) NOT NULL,
  `convencimiento` int(1) NOT NULL,
  `metod_otros` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `motricidad`
--

CREATE TABLE `motricidad` (
  `id_motriz` varchar(10) NOT NULL,
  `correr` int(1) NOT NULL,
  `bicicleta` int(1) NOT NULL,
  `jugar` int(1) NOT NULL,
  `gusto_deport` int(1) NOT NULL,
  `escribir` int(1) NOT NULL,
  `dibujar` int(1) NOT NULL,
  `recortar` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `natal`
--

CREATE TABLE `natal` (
  `id_natal` varchar(10) NOT NULL,
  `tipo_parto` varchar(30) NOT NULL,
  `sem_gestacion` int(2) NOT NULL,
  `duracion_parto` int(2) NOT NULL,
  `necesidades` varchar(25) NOT NULL,
  `sufrimiento` int(1) NOT NULL,
  `id_datos_nac` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id_paciente` varchar(12) NOT NULL,
  `tratamiento` int(1) NOT NULL,
  `fecha_nac` varchar(10) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `contacto` varchar(60) NOT NULL,
  `lentes` int(1) NOT NULL,
  `lateralidad` varchar(3) NOT NULL,
  `sueno` int(2) NOT NULL,
  `ayuno` int(2) NOT NULL,
  `diagnosticoP` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pade_embarazo`
--

CREATE TABLE `pade_embarazo` (
  `id_pad_emb` varchar(10) NOT NULL,
  `rubeola` int(1) NOT NULL,
  `varicela` int(1) NOT NULL,
  `edema` int(1) NOT NULL,
  `traumatismo` int(1) NOT NULL,
  `amenaza_aborto` int(1) NOT NULL,
  `sifilis` int(1) NOT NULL,
  `toxoplasmosis` int(1) NOT NULL,
  `vih` int(1) NOT NULL,
  `hipertension` int(1) NOT NULL,
  `toxemia` int(1) NOT NULL,
  `otros` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `postnatal`
--

CREATE TABLE `postnatal` (
  `id_postnat` varchar(10) NOT NULL,
  `tipo_alim` varchar(50) NOT NULL,
  `vomito` int(1) NOT NULL,
  `succion_pobre` int(1) NOT NULL,
  `actividad` varchar(25) NOT NULL,
  `id_motor` varchar(10) NOT NULL,
  `id_leng` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prenatal`
--

CREATE TABLE `prenatal` (
  `id_pren` varchar(10) NOT NULL,
  `prod_gesta` int(2) NOT NULL,
  `embar_deseo` int(1) NOT NULL,
  `drogas_embar` varchar(5) NOT NULL,
  `alim_embar` int(1) NOT NULL,
  `id_pad_emb` varchar(10) NOT NULL,
  `id_exp_emb` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preparatoria`
--

CREATE TABLE `preparatoria` (
  `id_prepa` varchar(10) NOT NULL,
  `pre_ingreso` int(2) NOT NULL,
  `pre_rendimiento` int(1) NOT NULL,
  `pre_grad_repet` int(1) NOT NULL,
  `id_preterap_clases` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `primaria`
--

CREATE TABLE `primaria` (
  `id_primaria` varchar(10) NOT NULL,
  `p_ingreso` int(1) NOT NULL,
  `p_tiempo` int(1) NOT NULL,
  `p_rendimiento` int(1) NOT NULL,
  `p_grad_repet` int(1) NOT NULL,
  `id_pterap_clases` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pruebas`
--

CREATE TABLE `pruebas` (
  `id_prueba` varchar(50) NOT NULL,
  `id_usuario` varchar(25) NOT NULL,
  `id_paciente` varchar(10) NOT NULL,
  `pruebas` varchar(10) NOT NULL,
  `archivos_prueba` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rel_fam`
--

CREATE TABLE `rel_fam` (
  `id_rel_fam` varchar(10) NOT NULL,
  `dif_madre` int(1) NOT NULL,
  `dif_padre` int(1) NOT NULL,
  `dif_hermanos` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `secundaria`
--

CREATE TABLE `secundaria` (
  `id_secundaria` varchar(10) NOT NULL,
  `s_ingreso` int(2) NOT NULL,
  `s_rendimiento` int(1) NOT NULL,
  `s_grad_repet` varchar(15) NOT NULL,
  `id_sterap_clases` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socializacion`
--

CREATE TABLE `socializacion` (
  `id_social` varchar(10) NOT NULL,
  `retraido` int(1) NOT NULL,
  `abierto` int(1) NOT NULL,
  `aislado` int(1) NOT NULL,
  `facil_amigos` int(1) NOT NULL,
  `amigos_edad` int(1) NOT NULL,
  `amigos_grandes` int(1) NOT NULL,
  `amigos_pequenos` int(1) NOT NULL,
  `amigos_otros` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `suenio`
--

CREATE TABLE `suenio` (
  `id_suenio` varchar(10) NOT NULL,
  `prom_horas` int(2) NOT NULL,
  `sonam` int(1) NOT NULL,
  `siesta` int(1) NOT NULL,
  `pesadillas` int(1) NOT NULL,
  `dif_dormir` int(1) NOT NULL,
  `dif_despertar` int(1) NOT NULL,
  `suenio_cont` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiempo_libre`
--

CREATE TABLE `tiempo_libre` (
  `id_tilibre` varchar(10) NOT NULL,
  `tv` int(1) NOT NULL,
  `vjuegos` int(1) NOT NULL,
  `compu` int(1) NOT NULL,
  `j_aire` int(1) NOT NULL,
  `j_fantasia` int(1) NOT NULL,
  `t_lectura` int(1) NOT NULL,
  `j_colectivos` int(1) NOT NULL,
  `j_construccion` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trauma`
--

CREATE TABLE `trauma` (
  `id_trauma` varchar(10) NOT NULL,
  `fecha_tr` varchar(9) NOT NULL,
  `duracion_tr` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` varchar(25) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `correo` varchar(60) NOT NULL,
  `contrasena` varchar(64) NOT NULL,
  `id_paciente` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vision`
--

CREATE TABLE `vision` (
  `id_vision` varchar(10) NOT NULL,
  `normal` int(1) NOT NULL,
  `examen` int(1) NOT NULL,
  `fecha` varchar(9) NOT NULL,
  `resultados` varchar(25) NOT NULL,
  `lentes` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`id_act`);

--
-- Indices de la tabla `adaptacion`
--
ALTER TABLE `adaptacion`
  ADD PRIMARY KEY (`id_adapt`);
  
-- Indices de la tabla `alergias`
--
ALTER TABLE `alergias`
  ADD PRIMARY KEY (`id_alergias`);
  
-- Indices de la tabla `atencion`
--
ALTER TABLE `atencion`
  ADD PRIMARY KEY (`id_aten`);

  
-- Indices de la tabla `ante_patologico`
--
ALTER TABLE `ante_patologico`
  ADD PRIMARY KEY (`id_ant_pat`);
  
-- Indices de la tabla `audicion`
--
ALTER TABLE `audicion`
  ADD PRIMARY KEY (`id_audicion`);

--
-- Indices de la tabla `apt_inter`
--
ALTER TABLE `apt_inter`
  ADD PRIMARY KEY (`id_apt_inter`);
  
--
-- Indices de la tabla `bilingue`
--
ALTER TABLE `bilingue`
  ADD PRIMARY KEY (`id_bilingue`);

--
-- Indices de la tabla `clases_terap`
--
ALTER TABLE `clases_terap`
  ADD PRIMARY KEY (`id_pterap_clases`);

--
-- Indices de la tabla `clases_terap2`
--
ALTER TABLE `clases_terap2`
  ADD PRIMARY KEY (`id_sterap_clases`);

--
-- Indices de la tabla `clases_terap3`
--
ALTER TABLE `clases_terap3`
  ADD PRIMARY KEY (`id_preterap_clases`);

--
-- Indices de la tabla `comportamiento`
--
ALTER TABLE `comportamiento`
  ADD PRIMARY KEY (`id_comp`);


--
-- Indices de la tabla `comp_comer`
--
ALTER TABLE `comp_comer`
  ADD PRIMARY KEY (`id_comp_comer`);

--
-- Indices de la tabla `convulsiones`
--
ALTER TABLE `convulsiones`
  ADD PRIMARY KEY (`id_convul`);

--
-- Indices de la tabla `crisis`
--
ALTER TABLE `crisis`
  ADD PRIMARY KEY (`id_crisis_col`);

--
-- Indices de la tabla `datos_nacimiento`
--
ALTER TABLE `datos_nacimiento`
  ADD PRIMARY KEY (`id_datos_nac`);
  
--
-- Indices de la tabla `des_actual`
--
ALTER TABLE `des_actual`
  ADD PRIMARY KEY (`id_des_act`);
  
--
-- Indices de la tabla `desarrollo_leng`
--
ALTER TABLE `desarrollo_leng`
  ADD PRIMARY KEY (`id_leng`);
  
-- Indices de la tabla `desarrollo_leng2`
--
ALTER TABLE `desarrollo_leng2`
  ADD PRIMARY KEY (`id_leng2`);

--
-- Indices de la tabla `desarrollo_motor`
--
ALTER TABLE `desarrollo_motor`
  ADD PRIMARY KEY (`id_motor`);
  
--
-- Indices de la tabla `enfermedades_contag`
--
ALTER TABLE `enfermedades_contag`
  ADD PRIMARY KEY (`id_infecto_cont`);

--
-- Indices de la tabla `entrevista`
--
ALTER TABLE `entrevista`
  ADD PRIMARY KEY (`id_ent`);

--
-- Indices de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  ADD PRIMARY KEY (`id_escil`);



--
-- Indices de la tabla `expo_embarazo`
--
ALTER TABLE `expo_embarazo`
  ADD PRIMARY KEY (`id_exp_emb`);

--
-- Indices de la tabla `familiar`
--
ALTER TABLE `familiar`
  ADD PRIMARY KEY (`id_fam`);

--
-- Indices de la tabla `guarderia`
--
ALTER TABLE `guarderia`
  ADD PRIMARY KEY (`id_guarderia`);
  
--
-- Indices de la tabla `habit_alim`
--
ALTER TABLE `habit_alim`
  ADD PRIMARY KEY (`id_habit_alim`);

-- Indices de la tabla `hospitalizaciones`
--
ALTER TABLE `hospitalizaciones`
  ADD PRIMARY KEY (`id_hosp`);
  

--
-- Indices de la tabla `jardin`
--
ALTER TABLE `jardin`
  ADD PRIMARY KEY (`id_jardin`);
  

--
-- Indices de la tabla `labilidad_emo`
--
ALTER TABLE `labilidad_emo`
  ADD PRIMARY KEY (`id_lab_em`);


--
-- Indices de la tabla `magallanes`
--
ALTER TABLE `magallanes`
  ADD PRIMARY KEY (`id_magallanes`);


--
-- Indices de la tabla `metod_dis`
--
ALTER TABLE `metod_dis`
  ADD PRIMARY KEY (`id_metod_dis`);


-- Indices de la tabla `motricidad`
--
ALTER TABLE `motricidad`
  ADD PRIMARY KEY (`id_motriz`);


--
-- Indices de la tabla `natal`
--
ALTER TABLE `natal`
  ADD PRIMARY KEY (`id_natal`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id_paciente`);

--
-- Indices de la tabla `pade_embarazo`
--
ALTER TABLE `pade_embarazo`
  ADD PRIMARY KEY (`id_pad_emb`);

--
-- Indices de la tabla `postnatal`
--
ALTER TABLE `postnatal`
  ADD PRIMARY KEY (`id_postnat`);

--
-- Indices de la tabla `prenatal`
--
ALTER TABLE `prenatal`
  ADD PRIMARY KEY (`id_pren`);

--
-- Indices de la tabla `preparatoria`
--
ALTER TABLE `preparatoria`
  ADD PRIMARY KEY (`id_prepa`);

--
-- Indices de la tabla `primaria`
--
ALTER TABLE `primaria`
  ADD PRIMARY KEY (`id_primaria`);

--
-- Indices de la tabla `pruebas`
--
ALTER TABLE `pruebas`
  ADD PRIMARY KEY (`id_prueba`);

-- Indices de la tabla `trauma`
--
ALTER TABLE `trauma`
  ADD PRIMARY KEY (`id_trauma`);

--
-- Indices de la tabla `rel_fam`
--
ALTER TABLE `rel_fam`
  ADD PRIMARY KEY (`id_rel_fam`);


--
-- Indices de la tabla `secundaria`
--
ALTER TABLE `secundaria`
  ADD PRIMARY KEY (`id_secundaria`);

--
-- Indices de la tabla `socializacion`
--
ALTER TABLE `socializacion`
  ADD PRIMARY KEY (`id_social`);


--
-- Indices de la tabla `suenio`
--
ALTER TABLE `suenio`
  ADD PRIMARY KEY (`id_suenio`);


--
-- Indices de la tabla `tiempo_libre`
--
ALTER TABLE `tiempo_libre`
  ADD PRIMARY KEY (`id_tilibre`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);
  
-- Indices de la tabla `vision`
--
ALTER TABLE `vision`
  ADD PRIMARY KEY (`id_vision`);  

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
