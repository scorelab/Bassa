-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 22, 2017 at 02:57 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Bassa`
--

-- --------------------------------------------------------

--
-- Table structure for table `compression`
--

CREATE TABLE IF NOT EXISTS `compression` (
  `id` varchar(255) NOT NULL,
  `progress` tinyint(4) DEFAULT NULL,
  `start_time` bigint(20) DEFAULT NULL,
  `completed_time` bigint(20) DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `download`
--

CREATE TABLE IF NOT EXISTS `download` (
  `id` bigint(20) NOT NULL,
  `link` text NOT NULL,
  `user_name` varchar(256) NOT NULL,
  `download_name` varchar(256) NOT NULL,
  `added_time` bigint(20) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  `rating` tinyint(4) NOT NULL DEFAULT '0',
  `gid` varchar(256) DEFAULT NULL,
  `completed_time` bigint(20) NOT NULL DEFAULT '0',
  `size` varchar(7) NOT NULL DEFAULT '0',
  `path` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

CREATE TABLE IF NOT EXISTS `rate` (
  `user_name` varchar(256) NOT NULL,
  `id` bigint(20) NOT NULL,
  `rate` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `approved` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_name`, `password`, `auth`, `email`, `blocked`, `approved`) VALUES
('rand', '1a1dc91c907325c69271ddf0c944bc72', 0, 'dilankachathurangi@gmail.com', 0, 1),
('rush', '1a1dc91c907325c69271ddf0c944bc72', 1, 'mgdmadusanka@gmail.com', 0, 0),
('tom', '1a1dc91c907325c69271ddf0c944bc72', 0, 'tom@mail.com', 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `download`
--
ALTER TABLE `download`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user_name` (`user_name`);

--
-- Indexes for table `rate`
--
ALTER TABLE `rate`
  ADD PRIMARY KEY (`user_name`,`id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_name`),
  ADD UNIQUE KEY `user_name` (`user_name`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `download`
--
ALTER TABLE `download`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;