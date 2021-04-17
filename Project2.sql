-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 17, 2021 at 10:17 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project2`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_id` int(11) NOT NULL,
  `emp_fname` varchar(25) NOT NULL,
  `emp_lname` varchar(25) NOT NULL,
  `emp_role` varchar(15) NOT NULL,
  `emp_addr` varchar(255) NOT NULL,
  `emp_email` varchar(30) NOT NULL,
  `emp_hiredate` date NOT NULL,
  `emp_color` text NOT NULL,
  `emp_borncity` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_id`, `emp_fname`, `emp_lname`, `emp_role`, `emp_addr`, `emp_email`, `emp_hiredate`, `emp_color`, `emp_borncity`) VALUES
(1, 'Apoorva', 'Sambhav', 'Admin', 'Brampton, Ontario', 'asambhav@myseneca.ca', '2019-04-01', 'Blue', 'Toronto'),
(2, 'Ajay', 'Modgil', 'Admin', 'Brampton, Ontario', 'amodgil1@myseneca.ca', '2020-03-01', 'Red', 'Toronto'),
(3, 'Jon', 'Snow', 'Janitor', '22 Bong', 'Snow.Jon@myseneca.ca', '2021-04-16', 'Orange', 'Hanoi'),
(19, 'Matt', 'Modi', 'Janitor', 'New Palace, Toronto', 'Matt.Modi@myseneca.ca', '2021-04-16', 'Black', 'New Delhi'),
(20, 'Sal', 'All', 'Sales Rep', 'Not here', 'Sal.All@myseneca.ca', '2021-04-16', 'Pink', 'New York'),
(21, 'Killa', 'Shahdad', 'Accountant', 'Ajax, Ontario', 'Killa.Shahdad@myseneca.ca', '2021-04-15', 'Black', 'Wuhan'),
(22, 'Donkey', 'Kong', 'Sales Rep', 'Litty City', 'Donkey.kong@myseneca.ca', '2021-04-16', 'Red', 'Hamilton');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `emp_id` int(11) NOT NULL,
  `emp_passhash` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`emp_id`, `emp_passhash`) VALUES
(21, '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'),
(22, 'd22f115abd6b44f9985037cfb39d6e1ab2db87a470d3e1081196562d420b8e41');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`emp_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `fk_import` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
