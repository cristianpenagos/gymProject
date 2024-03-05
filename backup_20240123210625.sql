-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: gymdb
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `casillero`
--

DROP TABLE IF EXISTS `casillero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `casillero` (
  `idcasillero` int NOT NULL AUTO_INCREMENT,
  `numCasillero` int NOT NULL,
  `diasAlquiler` int DEFAULT NULL,
  `usuario_idusuario` int DEFAULT NULL,
  PRIMARY KEY (`idcasillero`),
  UNIQUE KEY `numCasillero` (`numCasillero`),
  KEY `fk_casillero_usuario` (`usuario_idusuario`),
  CONSTRAINT `fk_casillero_usuario` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casillero`
--

LOCK TABLES `casillero` WRITE;
/*!40000 ALTER TABLE `casillero` DISABLE KEYS */;
INSERT INTO `casillero` VALUES (1,1,30,1);
/*!40000 ALTER TABLE `casillero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medidas`
--

DROP TABLE IF EXISTS `medidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medidas` (
  `idmedidas` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `cuelloM` float NOT NULL,
  `brazoM` float NOT NULL,
  `abdomenM` float NOT NULL,
  `caderaM` float NOT NULL,
  `piernaAltaM` float NOT NULL,
  `piernaBajaM` float NOT NULL,
  `pantorrillaM` float NOT NULL,
  `abdomenG` float NOT NULL,
  `bicepG` float NOT NULL,
  `tricepG` float NOT NULL,
  `escapulaG` float NOT NULL,
  `piernaG` float NOT NULL,
  `usuario_idusuario` int NOT NULL,
  PRIMARY KEY (`idmedidas`),
  UNIQUE KEY `idmedidas` (`idmedidas`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medidas`
--

LOCK TABLES `medidas` WRITE;
/*!40000 ALTER TABLE `medidas` DISABLE KEYS */;
INSERT INTO `medidas` VALUES (1,'2024-01-04',1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1,11.11,12.12,1),(2,'2024-01-01',1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1,11.11,12.12,2);
/*!40000 ALTER TABLE `medidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensualidad`
--

DROP TABLE IF EXISTS `mensualidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensualidad` (
  `idmensualidad` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `valor` int NOT NULL,
  `plan` int NOT NULL,
  `usuario_idusuario` int NOT NULL,
  PRIMARY KEY (`idmensualidad`),
  KEY `fk_mensualidad_usuario` (`usuario_idusuario`),
  CONSTRAINT `fk_mensualidad_usuario` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensualidad`
--

LOCK TABLES `mensualidad` WRITE;
/*!40000 ALTER TABLE `mensualidad` DISABLE KEYS */;
INSERT INTO `mensualidad` VALUES (1,'2024-01-04',55000,5,1),(4,'2024-01-17',55000,5,1),(5,'2024-01-18',10000,5,1),(6,'2020-01-01',10,3,20),(7,'2024-01-23',50000,5,20);
/*!40000 ALTER TABLE `mensualidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `otrosingresos`
--

DROP TABLE IF EXISTS `otrosingresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `otrosingresos` (
  `idingreso` int NOT NULL AUTO_INCREMENT,
  `elemento` varchar(100) NOT NULL,
  `valor` int DEFAULT NULL,
  `fecha` date NOT NULL DEFAULT '2024-01-05',
  PRIMARY KEY (`idingreso`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `otrosingresos`
--

LOCK TABLES `otrosingresos` WRITE;
/*!40000 ALTER TABLE `otrosingresos` DISABLE KEYS */;
INSERT INTO `otrosingresos` VALUES (3,'Creatina',42000,'2024-01-06'),(4,'ensayo',45000,'2022-01-01');
/*!40000 ALTER TABLE `otrosingresos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) NOT NULL,
  `numIdentificacion` varchar(15) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `fechaRegistro` date NOT NULL,
  `qrAsociado` int NOT NULL,
  `cGrupales` int DEFAULT NULL,
  `enfermedades` varchar(255) DEFAULT NULL,
  `objetivos` varchar(512) DEFAULT NULL,
  `notasGenerales` varchar(1024) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE KEY `numIdentificacion` (`numIdentificacion`),
  UNIQUE KEY `qrAsociado` (`qrAsociado`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Cristian Penagos','1033653257','1993-04-18','3147748687','2018-01-01',1,7,'No','No','No','No'),(17,'Ariana','06789','2022-04-19','3147748687','2023-01-03',7,0,'Sin Enfermedades','Aumento de masa muscular','Sin notas generales','Medellin'),(18,'Cristian Penagos','1053257','1993-04-18','3147748687','2024-01-02',2,0,'Sin Enfermedades','Aumento de masa muscular',NULL,NULL),(20,'Ariana','089','2022-04-19','3147748687','2023-01-03',3,0,'Sin Enfermedades','Aumento de masa muscular','Sin notas generales','Medellin'),(21,'Ariana','9089','2022-04-19','3147748687','2023-01-03',4,0,'Sin Enfermedades','Aumento de masa muscular','Sin notas generales','Medellin'),(22,'Fulanito','123','2022-01-01','123','2022-01-01',8,0,'no','no','no','no');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-23 21:06:25
