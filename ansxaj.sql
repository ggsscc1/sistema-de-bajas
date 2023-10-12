-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: datosalumnosbajas
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos_infbasica`
--

DROP TABLE IF EXISTS `alumnos_infbasica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos_infbasica` (
  `clave_unica` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `ap_paterno` varchar(45) NOT NULL,
  `ap_materno` varchar(45) DEFAULT NULL,
  `carrera` varchar(40) NOT NULL,
  `generacion` int NOT NULL,
  PRIMARY KEY (`clave_unica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos_infbasica`
--

LOCK TABLES `alumnos_infbasica` WRITE;
/*!40000 ALTER TABLE `alumnos_infbasica` DISABLE KEYS */;
INSERT INTO `alumnos_infbasica` VALUES (257299,'Joel Alejandro','Rodríguez','Cruz','Sistemas Inteligentes',2017),(282468,'Giacinto Carmelo','Castagnetto ','Ibarra','Sistemas Inteligentes',2017),(284742,'Diana Ivonne','Arce ','Ochoa','Sistemas Inteligentes',2018),(284944,'Jordan','Rodríguez','Vargas','Computacion',2017);
/*!40000 ALTER TABLE `alumnos_infbasica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carreras`
--

DROP TABLE IF EXISTS `carreras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carreras` (
  `idCarrera` int NOT NULL,
  `Carrera` varchar(30) NOT NULL,
  PRIMARY KEY (`idCarrera`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carreras`
--

LOCK TABLES `carreras` WRITE;
/*!40000 ALTER TABLE `carreras` DISABLE KEYS */;
INSERT INTO `carreras` VALUES (0,'Sistemas Inteligentes'),(1,'Computacion'),(2,'Informatica');
/*!40000 ALTER TABLE `carreras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forma_titulacion`
--

DROP TABLE IF EXISTS `forma_titulacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forma_titulacion` (
  `id_formatit` int NOT NULL,
  `nombre_formatit` varchar(45) NOT NULL,
  PRIMARY KEY (`id_formatit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forma_titulacion`
--

LOCK TABLES `forma_titulacion` WRITE;
/*!40000 ALTER TABLE `forma_titulacion` DISABLE KEYS */;
INSERT INTO `forma_titulacion` VALUES (0,'PROMEDIO'),(1,'TESIS'),(2,'EGEL'),(3,'EXAMEN DE CONOCIMIENTOS'),(4,'TRABAJO RECEPCIONAL'),(5,'ESTUDIOS DE POSGRADO');
/*!40000 ALTER TABLE `forma_titulacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formulario`
--

DROP TABLE IF EXISTS `formulario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formulario` (
  `id_baja` int NOT NULL AUTO_INCREMENT,
  `clave_unica` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `ap_paterno` varchar(45) NOT NULL,
  `ap_materno` varchar(45) DEFAULT NULL,
  `email_alumno` varchar(60) NOT NULL,
  `fecha_solicitud` date NOT NULL,
  `carrera` varchar(45) NOT NULL,
  `generacion` int NOT NULL,
  `tipobaja` varchar(45) NOT NULL,
  `motbaja` varchar(45) NOT NULL,
  `prepa_origen` varchar(100) NOT NULL,
  `matdif1` varchar(45) NOT NULL,
  `matdif2` varchar(45) NOT NULL,
  `matdif3` varchar(45) NOT NULL,
  `formatit` varchar(45) DEFAULT NULL,
  `fecha_egel` varchar(20) DEFAULT NULL,
  `detalles_baja` varchar(200) DEFAULT NULL,
  `empresa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_baja`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formulario`
--

LOCK TABLES `formulario` WRITE;
/*!40000 ALTER TABLE `formulario` DISABLE KEYS */;
INSERT INTO `formulario` VALUES (11,260568,'Diego','Dávila','Puente','diego@gmail.com','2023-05-29','Sistemas Inteligentes',2017,'Definitiva','Titulación','Gabriela Mistral, A.C','DISEÑO DIGITAL','DISEÑO DE JUEGOS','CRIPTOGRAFIA','EGEL','2023-10-10','ninguno',''),(12,284944,'Jordan','Rodríguez','Vargas','jord@gmail.com','2023-05-30','Computacion',2017,'Temporal','Económico','Colegio De Bachilleres Num. 26','BASES DE DATOS','CRIPTOGRAFIA','DISEÑO DE INTERFACES','','','Problemas economicos',''),(13,209145,'Luis','Alvarado','Torres','luisa@gmail.com','2023-05-30','Sistemas Inteligentes',2020,'Temporal','Personal','Colegio De Bachilleres Num. 28','COMPUTO PARALELO','CRIPTOGRAFIA','DISEÑO DE INTERFACES','','','Problemas familiares',''),(14,279965,'Nallely','Hernández','Hernández','nell@gmail.com','2023-05-30','Sistemas Inteligentes',2017,'Definitiva','Titulación','Colegio Hispano Mexicano, A.C.','DISEÑO DIGITAL','ESTRUCTURAS DE DATOS I','ESTRUCTURAS DE DATOS II','EGEL','2023-08-30','ninguno',''),(15,257299,'Joel Alejandro','Rodríguez','Cruz','joel01@gmail.com','2023-05-30','Sistemas Inteligentes',2017,'Temporal','Trabajo','Preparatoria Foránea','ESTRUCTURAS DE DATOS II','FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL','INTERFACES GRAFICAS CON APLICACIONES','','','No puedo pagar la carrera','Honeywell');
/*!40000 ALTER TABLE `formulario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lista_de_espera`
--

DROP TABLE IF EXISTS `lista_de_espera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lista_de_espera` (
  `clave_unica` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `ap_paterno` varchar(45) NOT NULL,
  `ap_materno` varchar(45) DEFAULT NULL,
  `carrera` varchar(45) NOT NULL,
  `generacion` int NOT NULL,
  `email` varchar(60) DEFAULT NULL,
  `lista_de_esperacol` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `tipobaja` varchar(45) DEFAULT NULL,
  `motbaja` varchar(45) DEFAULT NULL,
  `prepa_origen` varchar(100) DEFAULT NULL,
  `matdif1` varchar(45) DEFAULT NULL,
  `matdif2` varchar(45) DEFAULT NULL,
  `matdif3` varchar(45) DEFAULT NULL,
  `formatit` varchar(45) DEFAULT NULL,
  `lista_de_esperacol1` varchar(45) DEFAULT NULL,
  `fecha_egel` varchar(20) DEFAULT NULL,
  `detalles_baja` varchar(200) DEFAULT NULL,
  `empresa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`clave_unica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista_de_espera`
--

LOCK TABLES `lista_de_espera` WRITE;
/*!40000 ALTER TABLE `lista_de_espera` DISABLE KEYS */;
INSERT INTO `lista_de_espera` VALUES (257304,'José Edilberto','Torres','Cruz','Sistemas Inteligentes',2018,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(261881,'Luis Fernando','Moreno','Vega','Informatica',2016,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(284742,'Diana Ivonne','Arce ','Ochoa','Sistemas Inteligentes',2018,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(284944,'Jordan','Rodríguez','Vargas','Computacion',2017,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(345149,'Sergio Andrés','Hernández','Guerrero','Computacion',2019,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `lista_de_espera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materias_dificiles`
--

DROP TABLE IF EXISTS `materias_dificiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materias_dificiles` (
  `id_matdif` int NOT NULL,
  `nombre_materia` varchar(50) NOT NULL,
  PRIMARY KEY (`id_matdif`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materias_dificiles`
--

LOCK TABLES `materias_dificiles` WRITE;
/*!40000 ALTER TABLE `materias_dificiles` DISABLE KEYS */;
INSERT INTO `materias_dificiles` VALUES (0,'ADMINISTRACION DE BASES DE DATOS'),(1,'ADMINISTRACION DE PROYECTOS I'),(2,'ADMINISTRACION DE PROYECTOS II'),(3,'ALGORITMOS Y COMPLEJIDAD'),(4,'ANALISIS NUMERICO'),(5,'APLICACIONES WEB ESCALABLES'),(6,'APLICACIONES WEB INTERACTIVAS'),(7,'APRENDIZAJE AUTOMATICO'),(8,'ARQUITECTURA DE COMPUTADORAS'),(9,'ARTE CONCEPTUAL PARA VIDEOJUEGOS'),(10,'BASES DE DATOS'),(11,'COMPUTACION UBICUA'),(12,'COMPUTACION Y SOCIEDAD'),(13,'COMPUTACION INTERACTIVA'),(14,'COMPUTO DE ALTO RENDIMIENTO'),(15,'COMPUTO MOVIL'),(16,'COMPUTO PARALELO'),(17,'COMUNICACIONES INALAMBRICAS'),(18,'COMUNICACIONES OPTICAS'),(19,'COMUNICACIONES POR SATÉLITE'),(20,'COMUNICACIONES POR VOZ'),(21,'COMUNICACIONES UNIFICADAS'),(22,'COMUNICACIONES Y REDES'),(23,'CRIPTOGRAFIA'),(24,'DISEÑO DE INTERFACES'),(25,'DISEÑO DE JUEGOS'),(26,'DISEÑO DE MICROCOMPUTADORAS'),(27,'DISEÑO DIGITAL'),(28,'DISEÑO E IMPLEMENTACIÓN DE REDES'),(29,'DISPOSITIVOS SEMICONDUCTORES'),(30,'ESTRUCTURAS DE DATOS AVANZADAS'),(31,'ESTRUCTURAS DE DATOS I'),(32,'ESTRUCTURAS DE DATOS II'),(33,'FUNDAMENTOS DE CIRCUITOS ELECTRICOS'),(34,'FUNDAMENTOS DE COMPILADORES'),(35,'FUNDAMENTOS DE DESARROLLO MOVIL'),(36,'FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL'),(37,'FUNDAMENTOS DE SOFTWARE DE SISTEMAS'),(38,'GRAFICACION POR COMPUTADORA'),(39,'HERRAMIENTAS DE SOFTWARE'),(40,'INGENIERIA DE SOFTWARE'),(41,'INTERFACES DE COMUNICACIONES'),(42,'INTERFACES GRAFICAS CON APLICACIONES'),(43,'LENGUAJES DE PROGRAMACION'),(44,'MATEMATICAS DISCRETAS I'),(45,'MATEMATICAS DISCRETAS II'),(46,'MICROCONTROLADORES'),(47,'MODELADO MATEMATICO'),(48,'PENSAMIENTO ALGORITMICO'),(49,'PROBABILIDAD Y ESTADISTICA'),(50,'PROYECTO INTEGRADOR'),(51,'PROYECTOS COMPUTACIONALES I'),(52,'PROYECTOS COMPUTACIONALES II'),(53,'PROYECTOS COMPUTACIONALES III'),(54,'REDES DE COMPUTADORAS Y SEGURIDAD'),(55,'REPRESENTACION DEL CONOCIMIENTO Y ONTOLOGIAS'),(56,'ROBOTICA'),(57,'ROBOTICA INTELIGENTE'),(58,'SEMINARIO I.C.'),(59,'SEMINARIO I.I.'),(60,'SISTEMAS DE INFORMACION A'),(61,'SISTEMAS INTERACTIVOS'),(62,'SISTEMAS OPERATIVOS'),(63,'SISTEMAS OPERATIVOS AVANZADOS'),(64,'SOFTWARE DE SISTEMAS'),(65,'SUPERCOMPUTO'),(66,'TECNOLOGIA INFORMATICA'),(67,'TECNOLOGIA ORIENTADA A OBJETOS'),(68,'TELEMATICA A'),(69,'TEMAS SELECTOS DE MATEMATICAS'),(70,'TEMAS SELECTOS DE VIDEOJUEGOS'),(71,'VISION COMPUTACIONAL');
/*!40000 ALTER TABLE `materias_dificiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motivo_baja`
--

DROP TABLE IF EXISTS `motivo_baja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motivo_baja` (
  `id_motbaja` int NOT NULL,
  `nombre_motbaja` varchar(45) NOT NULL,
  PRIMARY KEY (`id_motbaja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motivo_baja`
--

LOCK TABLES `motivo_baja` WRITE;
/*!40000 ALTER TABLE `motivo_baja` DISABLE KEYS */;
INSERT INTO `motivo_baja` VALUES (0,'Personal'),(1,'Trabajo'),(2,'Económico'),(3,'Académico'),(4,'Cambio de Carrera'),(5,'Titulación');
/*!40000 ALTER TABLE `motivo_baja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prepa_procedencia`
--

DROP TABLE IF EXISTS `prepa_procedencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prepa_procedencia` (
  `id_prepa` int NOT NULL,
  `nombre_prepa` varchar(100) NOT NULL,
  PRIMARY KEY (`id_prepa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prepa_procedencia`
--

LOCK TABLES `prepa_procedencia` WRITE;
/*!40000 ALTER TABLE `prepa_procedencia` DISABLE KEYS */;
INSERT INTO `prepa_procedencia` VALUES (0,'Atenea'),(1,'Bachillerato Universidad Cuauhtemoc'),(2,'Centro De Bachillerato Tecnológico Agropecuario Num. 196'),(3,'Centro De Bachillerato Tecnológico Industrial Y De Servicios Num. 125'),(4,'Centro De Bachillerato Tecnológico Industrial Y De Servicios Num. 131'),(5,'Centro De Estudios Superiores Pedro Moreno'),(6,'Centro De Estudios Tecnológicos Industrial Y De Servicios Num. 125'),(7,'Centro Educativo Montessori'),(8,'Colegio Chapultepec De San Luis'),(9,'Colegio De Bachilleres Num. 01'),(10,'Colegio De Bachilleres Num. 19'),(11,'Colegio De Bachilleres Num. 25'),(12,'Colegio De Bachilleres Num. 26'),(13,'Colegio De Bachilleres Num. 28'),(14,'Colegio Hispano Mexicano'),(15,'Colegio Hispano Mexicano, A.C.'),(16,'Colegio San Luis Rey De Francia'),(17,'Colegio Vallarta'),(18,'Gabriela Mistral, A.C'),(19,'Instituto Benemerito De Las Americas'),(20,'Instituto Carlos Gómez'),(21,'Instituto De Estudios Superiores De Instituto De Estudios Superiores De San Luis, A.C.Luis, A.C.'),(22,'Instituto Harvard'),(23,'Instituto Lomas Del Real'),(24,'Instituto Oxford'),(25,'Instituto Ponciano Arriaga'),(26,'Instituto Santa Rita'),(27,'Instituto Tecnológico Julio Verne, A.C.'),(28,'Instituto Tecnológico Proyección Educativa'),(29,'Plantel Conalep 043'),(30,'Preparatoria San Pablo'),(31,'Prof. Antonio Tristan Alvarez'),(32,'Prof. José Juárez Barbosa'),(33,'Profa. Margarita Cardenas De Renteria'),(34,'Universidad Del Centro De México'),(35,'Preparatoria Foránea'),(36,'Otra');
/*!40000 ALTER TABLE `prepa_procedencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_de_baja`
--

DROP TABLE IF EXISTS `tipo_de_baja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_de_baja` (
  `id_tipobaja` int NOT NULL,
  `nombre_tipobaja` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipobaja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_de_baja`
--

LOCK TABLES `tipo_de_baja` WRITE;
/*!40000 ALTER TABLE `tipo_de_baja` DISABLE KEYS */;
INSERT INTO `tipo_de_baja` VALUES (0,'Temporal'),(1,'Definitiva');
/*!40000 ALTER TABLE `tipo_de_baja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `nom_usuario` varchar(35) NOT NULL,
  `password` varchar(30) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `ap_paterno` varchar(30) NOT NULL,
  `ap_materno` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `tipo_usuario` tinyint NOT NULL,
  PRIMARY KEY (`nom_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES ('DianaTorres','asdfg123','Diana','Torres','Castro','dianatc@uaslp.mx',1),('FcoMartinez','qwerty123','Francisco','Martínez','Pérez','fcomart@uaslp.mx',0),('Joel01','hola1','Joel Alejandro','Rodriguez','Cruz','joelale_18@outlook.com',1),('Manu01','asdfg123','Manuel','Torres','Castro','manu01@gmail.com',1),('SandraNava','zxcvb123','Sandra','Nava','Martinez','sandnav@uaslp.mx',1),('smps','qwerty123','homero','simpson','hola','hola@correo',1),('u1','u2','hola','hola','hola','hola@gmail.com',0);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_anio`
--

DROP TABLE IF EXISTS `view_anio`;
/*!50001 DROP VIEW IF EXISTS `view_anio`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_anio` AS SELECT 
 1 AS `year(fecha_solicitud)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_carreras`
--

DROP TABLE IF EXISTS `view_carreras`;
/*!50001 DROP VIEW IF EXISTS `view_carreras`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_carreras` AS SELECT 
 1 AS `carrera`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_generaciones`
--

DROP TABLE IF EXISTS `view_generaciones`;
/*!50001 DROP VIEW IF EXISTS `view_generaciones`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_generaciones` AS SELECT 
 1 AS `generacion`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_anio`
--

/*!50001 DROP VIEW IF EXISTS `view_anio`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_anio` AS select distinct year(`formulario`.`fecha_solicitud`) AS `year(fecha_solicitud)` from `formulario` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_carreras`
--

/*!50001 DROP VIEW IF EXISTS `view_carreras`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_carreras` AS select distinct `formulario`.`carrera` AS `carrera` from `formulario` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_generaciones`
--

/*!50001 DROP VIEW IF EXISTS `view_generaciones`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_generaciones` AS select distinct `formulario`.`generacion` AS `generacion` from `formulario` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-10 18:37:42
