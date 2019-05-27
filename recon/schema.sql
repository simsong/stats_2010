
-- MySQL dump 10.13  Distrib 5.5.58, for debian-linux-gnu (x86_64)
--
-- Host: mysql.simson.net    Database: recon
-- ------------------------------------------------------
-- Server version	5.6.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sysload`
--

DROP TABLE IF EXISTS `sysload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sysload` (
  `t` datetime NOT NULL,
  `min1` decimal(6,2) DEFAULT NULL,
  `min5` decimal(6,2) DEFAULT NULL,
  `min15` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tracts`
--

DROP TABLE IF EXISTS `blocks`;
CREATE TABLE `blocks` (
  STUSAB varchar(2) NOT NULL,
  STATE varchar(2) NOT NULL,
  LOGRECNO varchar(7) NOT NULL,
  COUNTY varchar(3) NOT NULL,
  TRACT varchar(6) NOT NULL,
  BLOCK varchar(4) NOT NULL,
  PRIMARY KEY (stusab,county,tract,block)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracts` (
  `state` varchar(2) NOT NULL,
  `county` varchar(3) NOT NULL,
  `tract` varchar(6) NOT NULL,
  `lp_start` datetime DEFAULT NULL,
  `lp_end` datetime DEFAULT NULL,
  `sol_start` datetime DEFAULT NULL,
  `sol_end` datetime DEFAULT NULL,
  `final_pop` int(11) DEFAULT NULL,
  `sol_time` double DEFAULT NULL,
  `modified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`state`,`county`,`tract`),
  KEY `lp_start` (`lp_start`),
  KEY `lp_end` (`lp_end`),
  KEY `sol_start` (`sol_start`),
  KEY `sol_end` (`sol_end`),
  KEY `final_pop` (`final_pop`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-23 23:02:26
