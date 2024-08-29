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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7r8u1d8peoarlmr0xmcwf8kpr1w3flzf','.eJyrVkrOzytJTC5RslIyMDQ2NLI0MzQ3NlfSUSrwTFGyMgfSzkgKjIxNTM3MLSwNlGoB1e0PRA:1sXhf5:bqzWmzPkAhxVk7TsazuBoDeq7dYjV6Vun5KJ8t_Mg4E','2024-08-10 13:40:39.544787'),('f2uozib0oobqdofvkdgxsr3hcto0unjn','eyJwSWQiOjksImNvbnRhY3QiOiIwMTQ3ODUyMzY5MCJ9:1sY7Ky:msDmxI_XK9wBrquxo3jFK5N4Tb5czML1qwQqJAAnJ4Q','2024-08-11 17:05:36.385310'),('k0uuharkiq2f8kcvvqnxjiu1qi9n018t','eyJwSWQiOjcsImNvbnRhY3QiOiIwMTMxMjk2MTczNyJ9:1sabtL:XyzlPNIu_WO0EcypZrrigSlK10db7ctpRCVIt2PLRV0','2024-08-18 14:07:23.994484'),('le1lj10lku7kpr7v4p2mseyc50li1kty','.eJyrVkrOzytJTC5RslIyMDQ2NLI0MzQ3NlfSUSrwTAGKJabkZuYBeaXFqUUuiSWJcKFaAOfsESM:1sdBQz:cfpzJJBAwYsvTSmTbcMIyl_QE4GLS-4OpyCaOwtH_LI','2024-08-25 16:28:45.431798'),('myhwjtnl1atizhu6h3omzwafywxrqs08','eyJwSWQiOjM2LCJ1c2VyRGF0YSI6WzM2LDMsInBlcnNvbiJdLCJjb250YWN0IjoiMDE3MzMzMjIyMzMzIn0:1sjakp:aRZww7PKdYINLiYRx1t85s6OAay7AAlOQ4o8WvLtGyc','2024-09-12 08:43:43.580919'),('w71kpn3xkh4y5quo3g6t5y7vwqrbz6jw','eyJwSWQiOjEwLCJjb250YWN0IjoiMDEyMzQ1Njc4OTAifQ:1sYOu4:ba_wzKCbhSaEmNSH9DkuLlfuRtKqfw1-4V7K17Jbajk','2024-08-12 11:51:00.540623'),('xdzx61p0vgmge6bq7aaix2vt4b0oz082','.eJyrVirwTFGyUkpMyc3MU9JRKi1OLXJJLElEEkrOzytJTC4BihgYGhsaWZoZmhubK9UCABYJESM:1sitNz:Iu_51NQgErzdyPYychcc4TaldtRhEMgMMv4g5SY6104','2024-09-10 10:25:15.293257'),('zg2219kraeol4n7zajq8ty8aye7spafw','eyJwSWQiOiJhZG1pbiIsInVzZXJEYXRhIjoiYWRtaW4ifQ:1sizan:AU0vufuZXWd-VEzfo02PhfCJMO0rsWuiqw_StGgN2Ns','2024-09-10 17:02:53.112222'),('znk35p4f84d3njxvgduzznvok4nzxx73','eyJwSWQiOiJhZG1pbiIsInVzZXJEYXRhIjoiYWRtaW4ifQ:1sirCv:tusC6pOpBrAC8RDYDt-qZLuHLNbDDJKNzlx_kFSQvqI','2024-09-10 08:05:41.000703');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
