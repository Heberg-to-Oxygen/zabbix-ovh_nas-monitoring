/*
SQLyog Ultimate v13.1.7 (64 bit)
MySQL - 10.6.12-MariaDB-1:10.6.12+maria~deb11 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `ovh-partition_info` (
	`id` int (10),
	`nas` varchar (96),
	`name` varchar (192),
	`size` smallint (6),
	`capacity` smallint (6)
	PRIMARY KEY (`id`),
	UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci; 
