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
-- Table structure for table `tb_person`
--

DROP TABLE IF EXISTS `tb_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_person` (
  `pId` int NOT NULL AUTO_INCREMENT,
  `pFname` varchar(30) NOT NULL,
  `pLname` varchar(30) NOT NULL,
  `pGender` varchar(8) NOT NULL,
  `pContact` varchar(15) NOT NULL,
  `pEmail` varchar(50) NOT NULL,
  `pDOB` date NOT NULL,
  `pBlood` varchar(4) DEFAULT NULL,
  `pHouse` varchar(10) DEFAULT NULL,
  `pRoad` varchar(10) DEFAULT NULL,
  `pArea` varchar(20) DEFAULT NULL,
  `pDistrict` varchar(20) DEFAULT NULL,
  `pCountry` varchar(30) NOT NULL,
  `pPassword` varchar(40) NOT NULL,
  `pProfile` blob,
  `pAccType` int DEFAULT NULL,
  `pAccStatus` int DEFAULT '2',
  PRIMARY KEY (`pId`),
  UNIQUE KEY `pContact` (`pContact`),
  UNIQUE KEY `pEmail` (`pEmail`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_person`
--

LOCK TABLES `tb_person` WRITE;
/*!40000 ALTER TABLE `tb_person` DISABLE KEYS */;
INSERT INTO `tb_person` VALUES (7,'Rayhan','Hossain','Male','01312961737','rayhansciencepupil@gmail.com','2024-07-26','B+','18','32','Badda','Dhaka','Bangladesh','1234','',1,1),(9,'Rayhan','Hossain','Male','01478523690','mdrayhanhossainextra2022@gmail.com','2024-07-26','B+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',2,1),(10,'Rayhan','Hossain','Male','01234567890','phylosopherhossain2022@gmai.com','2024-07-27','B+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',3,1),(12,'Ismile','Sheikh','Male','015935764820','ismile@gmailcom','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(13,'Ismile','Sheikh','Male','01596357824','smilesheikh@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',3,1),(14,'Ismile','Sheikh','Male','01596357820','ismilesheikh@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',2,2),(16,'Ismile','Khan','Male','01596357829','smile@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',2,2),(18,'Riazul','Kazi','Male','01321697173','kazi@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(19,'Riazul','Kazi','Male','01321697177','riazul@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',2,2),(21,'Riazul','Kazi','Male','01321697179','kaziriazul@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',2,2),(22,'Riazul','Kazi','Male','01321697170','riazulkazi@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',3,1),(23,'Riazul','Kazi','Male','01321697171','riazul123@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(24,'Rakib','Kazi','Male','01321697175','rakib123@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(25,'Rakib','Kazi','Male','01321697176','rakib12@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(29,'Rakib','Kazi','Male','01321697189','rakib@gmail.com','2024-07-27','O+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(30,'Rakib','Kazi','Male','01346798250','rakibkhan@gmail.com','2024-07-27','B+',NULL,NULL,NULL,NULL,'Bangladesh','1234','',1,1),(32,'Admin','User','Male','11223344556','admin@admin.com','2024-08-06','A-',NULL,NULL,NULL,NULL,'Bangladesh','123456','',1,1),(33,'asdfsadf','asdf','Female','0171212121212','abc@doc.com','2024-08-08','B+',NULL,NULL,NULL,NULL,'Bangladesh','1234',_binary 'later',3,2),(35,'Saima','Sinthiya','Female','0171313131313','saima@doc.com','2002-08-06','O-',NULL,NULL,NULL,NULL,'Bangladesh','123456',_binary 'later',2,1),(36,'Tanvir','Ahmed','Male','017333222333','tanvir@doc.com','2001-08-19','A+',NULL,NULL,NULL,NULL,'Bangladesh','123456',_binary 'later',3,1);
/*!40000 ALTER TABLE `tb_person` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-29 14:52:06
