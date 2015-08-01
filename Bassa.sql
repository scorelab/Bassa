-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 01, 2015 at 02:55 AM
-- Server version: 5.5.44-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Bassa`
--

-- --------------------------------------------------------

--
-- Table structure for table `download`
--

CREATE TABLE IF NOT EXISTS `download` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `link` text NOT NULL,
  `user_name` varchar(256) NOT NULL,
  `added_time` bigint(20) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  `rating` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `download`
--

INSERT INTO `download` (`id`, `link`, `user_name`, `added_time`, `status`, `rating`) VALUES
(6, 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQzODM0NjU4NywiaWF0IjoxNDM4MzQ1OTg3fQ.eyJ1c2VyTmFtZSI6InJhbmQifQ.OzkhGRHBQX8u3xuqZ2lI9rvMWv_vqQ7T3-lnSsAGNJk', 'rand', 1438363998, 3, 0),
(7, 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQzODM0NjU4NywiaWF0IjoxNDM4MzQ1OTg3fQ.eyJ1c2VyTmFtZSI6InJhbmQifQ.OzkhGRHBQX8u3xuqZ2lI9rvMWv_vqQ7T3-lnSsAGNJk', 'rand', 1438364004, 0, 0),
(8, 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQzODM0NjU4NywiaWF0IjoxNDM4MzQ1OTg3fQ.eyJ1c2VyTmFtZSI6InJhbmQifQ.OzkhGRHBQX8u3xuqZ2lI9rvMWv_vqQ7T3-lnSsAGNJk', 'rand', 1438364005, 3, 3),
(9, 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQzODM0NjU4NywiaWF0IjoxNDM4MzQ1OTg3fQ.eyJ1c2VyTmFtZSI6InJhbmQifQ.OzkhGRHBQX8u3xuqZ2lI9rvMWv_vqQ7T3-lnSsAGNJk', 'rand', 1438364006, 0, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `download`
--
ALTER TABLE `download`
  ADD CONSTRAINT `download_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
