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
-- Table structure for table `addme`
--

DROP TABLE IF EXISTS `addme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `addme` (
  `stusab` varchar(2) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `county` varchar(3) DEFAULT NULL,
  `tract` varchar(6) DEFAULT NULL
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
  `stusab` varchar(2) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `county` varchar(3) DEFAULT NULL,
  `tract` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t` (`t`),
  KEY `host` (`host`(255)),
  KEY `file` (`file`),
  KEY `line` (`line`)
) ENGINE=InnoDB AUTO_INCREMENT=481 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geo`
--

DROP TABLE IF EXISTS `geo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `STUSAB` char(2) NOT NULL,
  `SUMLEV` varchar(3) NOT NULL,
  `LOGRECNO` varchar(7) NOT NULL,
  `STATE` varchar(2) NOT NULL,
  `COUNTY` varchar(3) NOT NULL,
  `TRACT` varchar(6) DEFAULT NULL,
  `BLOCK` varchar(4) DEFAULT NULL,
  `NAME` varchar(90) DEFAULT NULL,
  `POP100` int(9) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `STUSAB` (`STUSAB`,`COUNTY`,`TRACT`,`BLOCK`),
  KEY `STATE` (`STATE`),
  KEY `LOGRECNO` (`LOGRECNO`),
  KEY `COUNTY` (`COUNTY`),
  KEY `TRACT` (`TRACT`),
  KEY `BLOCK` (`BLOCK`),
  KEY `NAME` (`NAME`),
  KEY `POP100` (`POP100`),
  KEY `SUMLEV` (`SUMLEV`),
  KEY `STATE_2` (`STATE`,`COUNTY`,`TRACT`,`BLOCK`)
) ENGINE=InnoDB AUTO_INCREMENT=13151296 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `geo_blocks`
--

DROP TABLE IF EXISTS `geo_blocks`;
/*!50001 DROP VIEW IF EXISTS `geo_blocks`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `geo_blocks` AS SELECT 
 1 AS `geocode`,
 1 AS `state`,
 1 AS `county`,
 1 AS `tract`,
 1 AS `block`,
 1 AS `name`,
 1 AS `pop100`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `geo_counties`
--

DROP TABLE IF EXISTS `geo_counties`;
/*!50001 DROP VIEW IF EXISTS `geo_counties`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `geo_counties` AS SELECT 
 1 AS `geocode`,
 1 AS `state`,
 1 AS `county`,
 1 AS `name`,
 1 AS `pop100`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `geo_tracts`
--

DROP TABLE IF EXISTS `geo_tracts`;
/*!50001 DROP VIEW IF EXISTS `geo_tracts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `geo_tracts` AS SELECT 
 1 AS `geocode`,
 1 AS `state`,
 1 AS `county`,
 1 AS `tract`,
 1 AS `name`,
 1 AS `pop100`*/;
SET character_set_client = @saved_cs_client;

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
) ENGINE=InnoDB AUTO_INCREMENT=490435 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tracts`
--

DROP TABLE IF EXISTS `tracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stusab` varchar(2) NOT NULL,
  `state` char(2) NOT NULL,
  `county` char(3) NOT NULL,
  `tract` char(6) NOT NULL,
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
  `Nodes` int(11) DEFAULT NULL,
  `IterCount` float DEFAULT NULL,
  `BarIterCount` float DEFAULT NULL,
  `isMIP` int(11) DEFAULT NULL,
  `hostlock` varchar(64) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `modified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `csv_start` datetime DEFAULT NULL,
  `csv_end` datetime DEFAULT NULL,
  `csv_host` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `state` (`stusab`,`county`,`tract`),
  UNIQUE KEY `state_2` (`state`,`county`,`tract`),
  KEY `lp_start` (`lp_start`),
  KEY `lp_end` (`lp_end`),
  KEY `sol_start` (`sol_start`),
  KEY `sol_end` (`sol_end`),
  KEY `final_pop` (`final_pop`),
  KEY `hostlock` (`hostlock`),
  KEY `PID` (`pid`),
  KEY `csv_start` (`csv_start`),
  KEY `csv_end` (`csv_end`)
) ENGINE=InnoDB AUTO_INCREMENT=74081 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `tracts_geostatus`
--

DROP TABLE IF EXISTS `tracts_geostatus`;
/*!50001 DROP VIEW IF EXISTS `tracts_geostatus`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `tracts_geostatus` AS SELECT 
 1 AS `geocode`,
 1 AS `state`,
 1 AS `county`,
 1 AS `tract`,
 1 AS `lp_end`,
 1 AS `sol_end`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `geo_blocks`
--

/*!50001 DROP VIEW IF EXISTS `geo_blocks`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`recon_writer`@`%.biohpc.cornell.edu` SQL SECURITY DEFINER */
/*!50001 VIEW `geo_blocks` AS select concat(`geo`.`STATE`,`geo`.`COUNTY`,`geo`.`TRACT`,`geo`.`BLOCK`) AS `geocode`,`geo`.`STATE` AS `state`,`geo`.`COUNTY` AS `county`,`geo`.`TRACT` AS `tract`,`geo`.`BLOCK` AS `block`,`geo`.`NAME` AS `name`,`geo`.`POP100` AS `pop100` from `geo` where (`geo`.`SUMLEV` = '101') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `geo_counties`
--

/*!50001 DROP VIEW IF EXISTS `geo_counties`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`recon_writer`@`%.biohpc.cornell.edu` SQL SECURITY DEFINER */
/*!50001 VIEW `geo_counties` AS select concat(`geo`.`STATE`,`geo`.`COUNTY`) AS `geocode`,`geo`.`STATE` AS `state`,`geo`.`COUNTY` AS `county`,`geo`.`NAME` AS `name`,`geo`.`POP100` AS `pop100` from `geo` where (`geo`.`SUMLEV` = '050') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `geo_tracts`
--

/*!50001 DROP VIEW IF EXISTS `geo_tracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`recon_writer`@`%.biohpc.cornell.edu` SQL SECURITY DEFINER */
/*!50001 VIEW `geo_tracts` AS select concat(`geo`.`STATE`,`geo`.`COUNTY`,`geo`.`TRACT`) AS `geocode`,`geo`.`STATE` AS `state`,`geo`.`COUNTY` AS `county`,`geo`.`TRACT` AS `tract`,`geo`.`NAME` AS `name`,`geo`.`POP100` AS `pop100` from `geo` where (`geo`.`SUMLEV` = '140') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `tracts_geostatus`
--

/*!50001 DROP VIEW IF EXISTS `tracts_geostatus`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = latin1 */;
/*!50001 SET character_set_results     = latin1 */;
/*!50001 SET collation_connection      = latin1_swedish_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`recon_writer`@`%.biohpc.cornell.edu` SQL SECURITY DEFINER */
/*!50001 VIEW `tracts_geostatus` AS select concat(`tracts`.`state`,`tracts`.`county`,`tracts`.`tract`) AS `geocode`,`tracts`.`state` AS `state`,`tracts`.`county` AS `county`,`tracts`.`tract` AS `tract`,`tracts`.`lp_end` AS `lp_end`,`tracts`.`sol_end` AS `sol_end` from `tracts` */;
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

-- Dump completed on 2019-07-30 13:21:27
