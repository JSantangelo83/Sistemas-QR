-- MySQL Script generated by MySQL Workbench
-- Wed Aug 25 18:55:10 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema qrdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema qrdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `qrdb` DEFAULT CHARACTER SET utf8 ;
USE `qrdb` ;

-- -----------------------------------------------------
-- Table `qrdb`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qrdb`.`cursos` (
  `nombre` VARCHAR(6) NOT NULL,
  `aclaracion` VARCHAR(45) NULL,
  PRIMARY KEY (`nombre`))
ENGINE = InnoDB
COMMENT = '	';


-- -----------------------------------------------------
-- Table `qrdb`.`alumnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qrdb`.`alumnos` (
  `dni` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `mac_address` VARCHAR(45) NULL,
  `nombre_curso` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`dni`),
  INDEX `fk_alumnos_cursos_idx` (`nombre_curso` ASC) VISIBLE,
  CONSTRAINT `fk_alumnos_cursos`
    FOREIGN KEY (`nombre_curso`)
    REFERENCES `qrdb`.`cursos` (`nombre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qrdb`.`docentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qrdb`.`docentes` (
  `dni` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`dni`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qrdb`.`modulos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qrdb`.`modulos` (
  `id` INT NOT NULL,
  `dia` INT NOT NULL,
  `hora_inicio` TIME NOT NULL,
  `hora_final` TIME NOT NULL,
  `fecha` DATE NULL,
  `nombre_curso` VARCHAR(6) NOT NULL,
  `dni_docente` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_modulos_cursos1_idx` (`nombre_curso` ASC) VISIBLE,
  INDEX `fk_modulos_docentes1_idx` (`dni_docente` ASC) VISIBLE,
  CONSTRAINT `fk_modulos_cursos1`
    FOREIGN KEY (`nombre_curso`)
    REFERENCES `qrdb`.`cursos` (`nombre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_modulos_docentes1`
    FOREIGN KEY (`dni_docente`)
    REFERENCES `qrdb`.`docentes` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
