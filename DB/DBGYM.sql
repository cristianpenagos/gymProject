-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: gymdb
-- ------------------------------------------------------
-- Server version	8.0.32

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
  KEY `fk_casillero_usuario` (`usuario_idusuario`),
  CONSTRAINT `fk_casillero_usuario` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casillero`
--

LOCK TABLES `casillero` WRITE;
/*!40000 ALTER TABLE `casillero` DISABLE KEYS */;
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
  `PiernaBajaM` float NOT NULL,
  `pantorrillaM` float NOT NULL,
  `AbdomenG` float NOT NULL,
  `bicepG` float NOT NULL,
  `tricepG` float NOT NULL,
  `escapulaG` float NOT NULL,
  `piernaG` float NOT NULL,
  `usuario_idusuario` int NOT NULL,
  `usuario_qrAsociado` int NOT NULL,
  PRIMARY KEY (`idmedidas`),
  UNIQUE KEY `idmedidas_UNIQUE` (`idmedidas`),
  KEY `fk_medidas_usuario` (`usuario_idusuario`),
  CONSTRAINT `fk_medidas_usuario` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medidas`
--

LOCK TABLES `medidas` WRITE;
/*!40000 ALTER TABLE `medidas` DISABLE KEYS */;
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
  `plan` varchar(45) DEFAULT NULL,
  `usuario_idusuario` int NOT NULL,
  `usuario_qrAsociado` int NOT NULL,
  PRIMARY KEY (`idmensualidad`),
  KEY `fk_mensualidad_usuario` (`usuario_idusuario`),
  CONSTRAINT `fk_mensualidad_usuario` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensualidad`
--

LOCK TABLES `mensualidad` WRITE;
/*!40000 ALTER TABLE `mensualidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensualidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qr`
--

DROP TABLE IF EXISTS `qr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qr` (
  `idqr` int NOT NULL AUTO_INCREMENT,
  `consecutivo` int NOT NULL,
  PRIMARY KEY (`idqr`),
  UNIQUE KEY `consecutivo_UNIQUE` (`consecutivo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qr`
--

LOCK TABLES `qr` WRITE;
/*!40000 ALTER TABLE `qr` DISABLE KEYS */;
/*!40000 ALTER TABLE `qr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `numIdentificacion` varchar(45) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `fechaRegistro` date DEFAULT NULL,
  `qrAsociado` int NOT NULL,
  `cGrupales` int DEFAULT NULL,
  `casillero_idcasillero` int NOT NULL,
  `enfermedades` varchar(255) DEFAULT NULL,
  `objetivos` varchar(512) DEFAULT NULL,
  `notasGenerales` varchar(1024) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idusuario`,`qrAsociado`),
  KEY `fk_usuario_qr` (`qrAsociado`),
  CONSTRAINT `fk_usuario_qr` FOREIGN KEY (`qrAsociado`) REFERENCES `qr` (`idqr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
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

-- Dump completed on 2024-01-03 18:11:33
