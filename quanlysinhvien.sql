-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2023 at 03:36 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quanlysinhvien`
--

-- --------------------------------------------------------

--
-- Table structure for table `buoihoc`
--

CREATE TABLE `buoihoc` (
  `mabuoihoc` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `giobatdau` time NOT NULL,
  `gioketthuc` time NOT NULL,
  `ngay` date NOT NULL,
  `malop` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `magiangvien` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `diemdanh`
--

CREATE TABLE `diemdanh` (
  `madiemdanh` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `masv` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `giovao` time NOT NULL,
  `giora` time NOT NULL,
  `ngay` date NOT NULL,
  `mabuoihoc` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `trangthai` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `hinhanh` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `giangvien`
--

CREATE TABLE `giangvien` (
  `magiangvien` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `hoten` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sodienthoai` int(11) NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `matkhau` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `hinhanh_sinhvien`
--

CREATE TABLE `hinhanh_sinhvien` (
  `masinhvien` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `hinhanh` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `khoa`
--

CREATE TABLE `khoa` (
  `makhoa` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tenkhoa` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lop`
--

CREATE TABLE `lop` (
  `malop` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tenlop` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `makhoa` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sinhvien`
--

CREATE TABLE `sinhvien` (
  `masinhvien` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `hoten` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `malop` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `cmnd` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `gioitinh` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ngaysinh` date NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sodienthoai` int(11) NOT NULL,
  `khoahoc` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD PRIMARY KEY (`mabuoihoc`),
  ADD KEY `buoihoc_giangvien_FK` (`magiangvien`);

--
-- Indexes for table `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD PRIMARY KEY (`madiemdanh`),
  ADD KEY `diemdanh_buoihoc_FK` (`mabuoihoc`);

--
-- Indexes for table `giangvien`
--
ALTER TABLE `giangvien`
  ADD PRIMARY KEY (`magiangvien`);

--
-- Indexes for table `hinhanh_sinhvien`
--
ALTER TABLE `hinhanh_sinhvien`
  ADD PRIMARY KEY (`masinhvien`,`hinhanh`);

--
-- Indexes for table `khoa`
--
ALTER TABLE `khoa`
  ADD PRIMARY KEY (`makhoa`);

--
-- Indexes for table `lop`
--
ALTER TABLE `lop`
  ADD PRIMARY KEY (`malop`),
  ADD KEY `lop_khoa_FK` (`makhoa`);

--
-- Indexes for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD PRIMARY KEY (`masinhvien`),
  ADD KEY `sinhvien_lop_FK` (`malop`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD CONSTRAINT `buoihoc_giangvien_FK` FOREIGN KEY (`magiangvien`) REFERENCES `giangvien` (`magiangvien`);

--
-- Constraints for table `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD CONSTRAINT `diemdanh_buoihoc_FK` FOREIGN KEY (`mabuoihoc`) REFERENCES `buoihoc` (`mabuoihoc`);

--
-- Constraints for table `hinhanh_sinhvien`
--
ALTER TABLE `hinhanh_sinhvien`
  ADD CONSTRAINT `hinhanhsv_sinhvien_FK` FOREIGN KEY (`masinhvien`) REFERENCES `sinhvien` (`masinhvien`);

--
-- Constraints for table `lop`
--
ALTER TABLE `lop`
  ADD CONSTRAINT `lop_khoa_FK` FOREIGN KEY (`makhoa`) REFERENCES `khoa` (`makhoa`);

--
-- Constraints for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `sinhvien_lop_FK` FOREIGN KEY (`malop`) REFERENCES `lop` (`malop`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
