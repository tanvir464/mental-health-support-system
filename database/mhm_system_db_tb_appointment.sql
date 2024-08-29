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
-- Table structure for table `tb_appointment`
--

DROP TABLE IF EXISTS `tb_appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_appointment` (
  `aId` int NOT NULL AUTO_INCREMENT,
  `appId` int NOT NULL,
  `aspId` int NOT NULL,
  `adate` date NOT NULL,
  `atime` varchar(20) DEFAULT NULL,
  `aStatus` int DEFAULT '1',
  `aPayment` int DEFAULT '0',
  PRIMARY KEY (`aId`),
  KEY `appId` (`appId`),
  KEY `aspId` (`aspId`),
  CONSTRAINT `tb_appointment_ibfk_1` FOREIGN KEY (`appId`) REFERENCES `tb_person` (`pId`),
  CONSTRAINT `tb_appointment_ibfk_2` FOREIGN KEY (`aspId`) REFERENCES `tb_person` (`pId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_appointment`
--

LOCK TABLES `tb_appointment` WRITE;
/*!40000 ALTER TABLE `tb_appointment` DISABLE KEYS */;
INSERT INTO `tb_appointment` VALUES (1,7,9,'2024-07-27','Time 1',2,0),(2,7,9,'2024-07-31','Time 2',1,0),(3,7,10,'2024-08-03','Time 2',1,0);
/*!40000 ALTER TABLE `tb_appointment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-29 14:52:10
