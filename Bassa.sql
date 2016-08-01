-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 29, 2016 at 10:21 PM
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
CREATE DATABASE IF NOT EXISTS `Bassa` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `Bassa`;

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
  `gid` varchar(256) DEFAULT NULL,
  `completed_time` bigint(20) NOT NULL DEFAULT '0',
  `path` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `download`
--

INSERT INTO `download` (`id`, `link`, `user_name`, `added_time`, `status`, `rating`, `gid`, `completed_time`, `path`) VALUES
(6, 'https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz#md5=b07a897511a3c585251fe2ea85a9d9d9', 'rand', 1438363998, 3, 0, '1a58327748885ead', 1438833950, '/home/rand/bassa/websocket_client-0.32.0.tar.gz.1'),
(7, 'https://pypi.python.org/packages/source/F/Flask-Cors/Flask-Cors-2.1.0.tar.gz#md5=dd8a83b98d86490e2b7d72ff4e07f970', 'rand', 1438364004, 3, 0, '0a06f3987abd4735', 1438833949, '/home/rand/bassa/Flask-Cors-2.1.0.tar.gz.1'),
(8, 'https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz#md5=b07a897511a3c585251fe2ea85a9d9d9', 'rand', 1438364005, 1, 3, 'b10f84e81763b611', 0, NULL),
(9, 'https://pypi.python.org/packages/source/F/Flask-Cors/Flask-Cors-2.1.0.tar.gz#md5=dd8a83b98d86490e2b7d72ff4e07f970', 'rand', 1438364006, 0, 0, '7896a9f895af2fd5', 0, NULL),
(10, 'https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz#md5=b07a897511a3c585251fe2ea85a9d9d9', 'rand', 1438763880, 0, 0, NULL, 0, NULL),
(11, 'dummy', 'rand', 1438833176, 0, 0, NULL, 0, NULL),
(12, 'dummy1', 'rand', 1438833890, 0, 0, NULL, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

CREATE TABLE IF NOT EXISTS `rate` (
  `user_name` varchar(256) NOT NULL,
  `id` bigint(20) NOT NULL,
  `rate` tinyint(1) NOT NULL,
  PRIMARY KEY (`user_name`,`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`user_name`, `id`, `rate`) VALUES
('rand', 8, 1),
('tom', 8, 5);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_name` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `auth` tinyint(11) NOT NULL,
  `email` varchar(256) NOT NULL,
  `blocked` tinyint(1) NOT NULL DEFAULT '0',
  `approved` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_name`),
  UNIQUE KEY `user_name` (`user_name`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_name`, `password`, `auth`, `email`, `blocked`, `approved`) VALUES
('rand', '1a1dc91c907325c69271ddf0c944bc72', 0, 'dilankachathurangi@gmail.com', 0, 1),
('rush', '1a1dc91c907325c69271ddf0c944bc72', 1, 'mgdmadusanka@gmail.com', 0, 0),
('tom', '1a1dc91c907325c69271ddf0c944bc72', 0, 'tom@mail.com', 0, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `download`
--
ALTER TABLE `download`
  ADD CONSTRAINT `download_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`);

--
-- Constraints for table `rate`
--
ALTER TABLE `rate`
  ADD CONSTRAINT `rate_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`),
  ADD CONSTRAINT `rate_ibfk_2` FOREIGN KEY (`id`) REFERENCES `download` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
