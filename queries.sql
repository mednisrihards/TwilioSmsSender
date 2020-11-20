-- Queries to create a clients table into database

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE ClientsDB;

USE ClientsDB;

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `Clients` (
    `id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `phone_number` char(50) NOT NULL,
    `first_name` text NOT NULL,
    `last_name` text NOT NULL,
    `appointment_date` DATETIME DEFAULT NULL,
    `message_sent` DATETIME DEFAULT NULL
) AUTO_INCREMENT = 1 ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fake data insertion
--

INSERT INTO Clients (phone_number, first_name, last_name, appointment_date)
VALUES ('+37120401160', 'Anatolijs', 'Mednis', '2020-12-10 10:10:10');

INSERT INTO Clients (phone_number, first_name, last_name, appointment_date)
VALUES ('+37126443405', 'Olafs', 'Mednis', '2020-09-20 11:10:10');

INSERT INTO Clients (phone_number, first_name, last_name, appointment_date)
VALUES ('+37126443405', 'Akasna', 'Medne', '2020-09-03 10:13:10');

INSERT INTO Clients (phone_number, first_name, last_name, appointment_date)
VALUES ('+37123201160', 'Andris', 'Mednis', '2020-09-21 20:10:10');

INSERT INTO Clients (phone_number, first_name, last_name, appointment_date)
VALUES ('+37120401160', 'Rihards', 'Mednis', '2020-11-20 20:10:10');