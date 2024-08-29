-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mhm_system_db
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `tb_eworkshop`
--

DROP TABLE IF EXISTS `tb_eworkshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_eworkshop` (
  `ewId` int NOT NULL AUTO_INCREMENT,
  `ewActivities` varchar(255) DEFAULT NULL,
  `ewMaterial` blob,
  `ewPrerequisite` varchar(100) DEFAULT NULL,
  `ewFollow` varchar(255) DEFAULT NULL,
  `ewFacilitatorId` int DEFAULT NULL,
  PRIMARY KEY (`ewId`),
  KEY `ewFacilitatorId` (`ewFacilitatorId`),
  CONSTRAINT `tb_eworkshop_ibfk_1` FOREIGN KEY (`ewId`) REFERENCES `tb_event` (`eId`),
  CONSTRAINT `tb_eworkshop_ibfk_2` FOREIGN KEY (`ewFacilitatorId`) REFERENCES `tb_person` (`pId`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_eworkshop`
--

LOCK TABLES `tb_eworkshop` WRITE;
/*!40000 ALTER TABLE `tb_eworkshop` DISABLE KEYS */;
INSERT INTO `tb_eworkshop` VALUES (14,'Activities1,Activities2',NULL,'Nothing','See you',13);
/*!40000 ALTER TABLE `tb_eworkshop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-29 14:52:11
