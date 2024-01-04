use gymDB;

DROP TABLE usuario

select * from usuario	




#eliminacion FKs
ALTER TABLE medidas DROP FOREIGN KEY fk_medidas_usuario;
ALTER TABLE mensualidad DROP FOREIGN KEY fk_mensualidad_usuario;
ALTER TABLE casillero DROP FOREIGN KEY fk_casillero_usuario;
ALTER TABLE qr DROP FOREIGN KEY fk_qr_usuario;

ALTER TABLE usuario DROP PRIMARY KEY;

ALTER TABLE usuario ADD PRIMARY KEY AUTO_INCREMENT (idusuario);

SELECT *
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS;

drop table usuario

# Creacion de tabla usuario
CREATE TABLE IF NOT EXISTS usuario (
  `idusuario` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(60) NOT NULL,
  `numIdentificacion` VARCHAR(15) NOT NULL UNIQUE,
  `fechaNacimiento` DATE NOT NULL,
  `telefono` VARCHAR(45) NULL,
  `fechaRegistro` DATE NOT NULL,
  `qrAsociado` INT NOT NULL UNIQUE,
  `cGrupales` INT NULL,
  `enfermedades` VARCHAR(255) NULL,
  `objetivos` VARCHAR(512) NULL,
  `notasGenerales` VARCHAR(1024) NULL,
  `direccion` VARCHAR(100) NULL
  )
  
INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos) 
			VALUES('Cristian Penagos', 1053257, '1993-04-18', 3147748687, '2024-01-02', 2, 0, "Sin Enfermedades", "Aumento de masa muscular")
INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos) 
			VALUES('Cristian P', 10336532557, '1993-04-18', 314774864187, '2024-01-02', 1, 0, "Sin Enfermedades", "Aumento de masa muscular")

# Creacion de tabla QR
CREATE TABLE IF NOT EXISTS qr (
  `idqr` INT NOT NULL AUTO_INCREMENT,
  `consecutivo` INT NOT NULL,
  PRIMARY KEY (`idqr`),
  UNIQUE INDEX `consecutivo_UNIQUE` (`consecutivo` ASC) VISIBLE)
  
  #Creacion FK usuario QR
ALTER TABLE usuario ADD CONSTRAINT fk_usuario_qr FOREIGN KEY (qrAsociado) REFERENCES qr (idqr);


#Creacion tabla Casillero

CREATE TABLE IF NOT EXISTS casillero (
  `idcasillero` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `numCasillero` INT NOT NULL UNIQUE,
  `diasAlquiler` INT NULL,
  `usuario_idusuario` INT NULL
  )
  
INSERT INTO casillero (numCasillero, diasAlquiler, usuario_idusuario) VALUES (1, 30, 1)

# Creacion FK Casillero Usuario
ALTER TABLE casillero ADD CONSTRAINT fk_casillero_usuario FOREIGN KEY (usuario_idusuario) REFERENCES usuario(idusuario) ON DELETE CASCADE
mensualidadmensualidad

#Creacion de tabla mensualidad
CREATE TABLE IF NOT EXISTS mensualidad (
  `idmensualidad` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `valor` INT NOT NULL,
  `plan` INT NOT NULL,
  `usuario_idusuario` INT NOT NULL

  )

#Creacion de FK Mensualidad Usuario
ALTER TABLE mensualidad ADD CONSTRAINT fk_mensualidad_usuario FOREIGN KEY (usuario_idusuario) REFERENCES usuario(idusuario) ON DELETE CASCADE

INSERT INTO mensualidad (fecha, valor, plan, usuario_idusuario) VALUES ("2024-01-04", 55000, 5, 1)

SELECT * FROM mensualidad

#Creacion tabla Medidas
CREATE TABLE IF NOT EXISTS medidas (
  `idmedidas` INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
  `fecha` DATE NOT NULL,
  `cuelloM` FLOAT NOT NULL,
  `brazoM` FLOAT NOT NULL,
  `abdomenM` FLOAT NOT NULL,
  `caderaM` FLOAT NOT NULL,
  `piernaAltaM` FLOAT NOT NULL,
  `piernaBajaM` FLOAT NOT NULL,
  `pantorrillaM` FLOAT NOT NULL,
  `abdomenG` FLOAT NOT NULL,
  `bicepG` FLOAT NOT NULL,
  `tricepG` FLOAT NOT NULL,
  `escapulaG` FLOAT NOT NULL,
  `piernaG` FLOAT NOT NULL,
  `usuario_idusuario` INT NOT NULL
)

SELECT * FROM medidas

#Creacion de FK Medidas Usuario

ALTER TABLE medidas ADD CONSTRAINT fk_medidas_usuario FOREIGN KEY (usuario_idusuario) REFERENCES usuario(idusuario) ON DELETE CASCADE

INSERT INTO medidas (fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, usuario_idusuario )
			VALUES ("2024-01-04", 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 11.11, 12.12, 1 )

INSERT INTO medidas (fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, usuario_idusuario )
			VALUES ("2024-01-04", 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 11.11, 12.12, 1 )
            


#Creacion de la tabla otrosIngresos

CREATE TABLE otrosIngresos(
	`idingreso` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `elemento` varchar(100) NOT NULL,
    `valor` INT  
)



INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro, qrAsociado, cGrupales) 
			VALUES('Cristian Penagos', 1033653257, '1993-04-18', 3147748687, '2024-01-02', 1, 0)

INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro, qrAsociado, cGrupales) 
VALUES ('Juan', 123456789, '2023-01-01', 1234567890, '2023-01-02', 1, 0);

INSERT INTO qr (consecutivo) VALUES (100)

ALTER TABLE usuario MODIFY COLUMN qrAsociado INT;
ALTER TABLE usuario MODIFY COLUMN telefono BIGINT;

SELECT * FROM usuario
SELECT * FROM qr

# consulta con join
SELECT
  usuario.idusuario,
  usuario.nombre,
  usuario.numIdentificacion,
  usuario.fechaNacimiento,
  usuario.telefono,
  usuario.fechaRegistro,
  qr.*
FROM
  usuario
JOIN
  qr
ON
  usuario.qrAsociado = qr.idqr;