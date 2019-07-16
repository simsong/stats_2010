-- MySQL dump 10.13  Distrib 5.6.44, for Linux (x86_64)
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
-- Table structure for table `blocks`
--

DROP TABLE IF EXISTS `blocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blocks` (
  `STUSAB` varchar(2) NOT NULL,
  `STATE` varchar(2) NOT NULL,
  `LOGRECNO` varchar(7) NOT NULL,
  `COUNTY` varchar(3) NOT NULL,
  `TRACT` varchar(6) NOT NULL,
  `BLOCK` varchar(4) NOT NULL,
  PRIMARY KEY (`STUSAB`,`COUNTY`,`TRACT`,`BLOCK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `errors`
--

DROP TABLE IF EXISTS `errors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `errors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `t` datetime DEFAULT CURRENT_TIMESTAMP,
  `host` varchar(256) DEFAULT NULL,
  `error` mediumtext,
  `argv0` varchar(128) DEFAULT NULL,
  `file` varchar(64) DEFAULT NULL,
  `line` int(11) DEFAULT NULL,
  `stack` mediumtext,
  `last_value` mediumtext,
  PRIMARY KEY (`id`),
  KEY `t` (`t`),
  KEY `host` (`host`(255)),
  KEY `file` (`file`),
  KEY `line` (`line`)
) ENGINE=InnoDB AUTO_INCREMENT=359 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `glog`
--

DROP TABLE IF EXISTS `glog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `glog` (
  `gurobi_version` varchar(254) DEFAULT NULL,
  `rows` int(8) DEFAULT NULL,
  `columns` int(8) DEFAULT NULL,
  `nonzeros` int(8) DEFAULT NULL,
  `presolve_rows` int(8) DEFAULT NULL,
  `presolve_NZ` int(8) DEFAULT NULL,
  `integer_vars` int(8) DEFAULT NULL,
  `binary_vars` int(8) DEFAULT NULL,
  `simplex_iterations` int(8) DEFAULT NULL,
  `seconds` float DEFAULT NULL,
  `start` varchar(254) DEFAULT NULL,
  `state` varchar(254) DEFAULT NULL,
  `county` varchar(254) DEFAULT NULL,
  `tract` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sysload`
--

DROP TABLE IF EXISTS `sysload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sysload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `t` datetime NOT NULL,
  `host` varchar(64) NOT NULL,
  `min1` decimal(6,2) DEFAULT NULL,
  `min5` decimal(6,2) DEFAULT NULL,
  `min15` decimal(6,2) DEFAULT NULL,
  `freegb` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `t` (`t`,`host`),
  KEY `host` (`host`),
  KEY `min1` (`min1`),
  KEY `min5` (`min5`),
  KEY `min15` (`min15`),
  KEY `freegb` (`freegb`)
) ENGINE=InnoDB AUTO_INCREMENT=483868 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tracts`
--

DROP TABLE IF EXISTS `tracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracts` (
  `state` varchar(2) NOT NULL,
  `county` varchar(3) NOT NULL,
  `tract` varchar(6) NOT NULL,
  `lp_start` datetime DEFAULT NULL,
  `lp_end` datetime DEFAULT NULL,
  `lp_gb` int(6) DEFAULT NULL,
  `lp_host` varchar(64) DEFAULT NULL,
  `sol_start` datetime DEFAULT NULL,
  `sol_end` datetime DEFAULT NULL,
  `sol_gb` int(6) DEFAULT NULL,
  `sol_host` varchar(64) DEFAULT NULL,
  `sol_time` double DEFAULT NULL,
  `final_pop` int(11) DEFAULT NULL,
  `NumVars` int(11) DEFAULT NULL,
  `NumConstrs` int(11) DEFAULT NULL,
  `NumNZs` int(11) DEFAULT NULL,
  `NumIntVars` int(11) DEFAULT NULL,
  `MIPGap` float DEFAULT NULL,
  `Runtime` float DEFAULT NULL,
  `IterCount` float DEFAULT NULL,
  `BarIterCount` float DEFAULT NULL,
  `isMIP` int(11) DEFAULT NULL,
  `hostlock` varchar(64) DEFAULT NULL,
  `error` varchar(64) DEFAULT NULL,
  `modified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`state`,`county`,`tract`),
  KEY `lp_start` (`lp_start`),
  KEY `lp_end` (`lp_end`),
  KEY `sol_start` (`sol_start`),
  KEY `sol_end` (`sol_end`),
  KEY `final_pop` (`final_pop`),
  KEY `hostlock` (`hostlock`)
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

-- Dump completed on 2019-07-16  9:45:15
