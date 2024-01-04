use gymDB;

DROP TABLE usuario

select * from usuario	

# Creacion de tabla usuario
ALTER TABLE usuario MODIFY idusuario INT AUTO_INCREMENT PRIMARY KEY NOT NULL;
ALTER TABLE usuario DROP PRIMARY KEY;

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

SELECT COUNT(*) AS num_primary_keys
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'gymdb'
AND TABLE_NAME = 'usuario'
AND CONSTRAINT_TYPE = 'PRIMARY KEY';

CREATE TABLE IF NOT EXISTS usuario (
  `idusuario` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `numIdentificacion` VARCHAR(45) NULL,
  `fechaNacimiento` DATE NULL,
  `telefono` VARCHAR(45) NULL,
  `fechaRegistro` DATE NULL,
  `qrAsociado` INT NOT NULL,
  `cGrupales` INT NULL,
  `enfermedades` VARCHAR(255) NULL,
  `objetivos` VARCHAR(512) NULL,
  `notasGenerales` VARCHAR(1024) NULL,
  `direccion` VARCHAR(100) NULL
  )

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
  `idcasillero` INT NOT NULL AUTO_INCREMENT,
  `numCasillero` INT NOT NULL,
  `diasAlquiler` INT NULL,
  `usuario_idusuario` INT NULL,
  PRIMARY KEY (`idcasillero`)
  )
# Creacion FK Casillero Usuario
ALTER TABLE casillero ADD CONSTRAINT fk_casillero_usuario FOREIGN KEY (usuario_idusuario) REFERENCES usuario(idusuario)


#
CREATE TABLE IF NOT EXISTS mensualidad (
  `idmensualidad` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `valor` INT NOT NULL,
  `plan` VARCHAR(45) NULL,
  `usuario_idusuario` INT NOT NULL,
  `usuario_qrAsociado` INT NOT NULL,
  PRIMARY KEY (`idmensualidad`)
  )

#Creacion de FK Mensualidad Usuario

ALTER TABLE mensualidad ADD CONSTRAINT fk_mensualidad_usuario FOREIGN KEY (usuario_idusuario) REFERENCES usuario(idusuario)

#Creacion tabla Medidas
CREATE TABLE IF NOT EXISTS medidas (
  `idmedidas` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `cuelloM` FLOAT NOT NULL,
  `brazoM` FLOAT NOT NULL,
  `abdomenM` FLOAT NOT NULL,
  `caderaM` FLOAT NOT NULL,
  `piernaAltaM` FLOAT NOT NULL,
  `PiernaBajaM` FLOAT NOT NULL,
  `pantorrillaM` FLOAT NOT NULL,
  `AbdomenG` FLOAT NOT NULL,
  `bicepG` FLOAT NOT NULL,
  `tricepG` FLOAT NOT NULL,
  `escapulaG` FLOAT NOT NULL,
  `piernaG` FLOAT NOT NULL,
  `usuario_idusuario` INT NOT NULL,
  `usuario_qrAsociado` INT NOT NULL,
  PRIMARY KEY (`idmedidas`),
  UNIQUE INDEX `idmedidas_UNIQUE` (`idmedidas` ASC) VISIBLE
)

#Creacion de FK Medidas Usuario

ALTER TABLE medidas ADD CONSTRAINT fk_medidas_usuario FOREIGN KEY (usuario_idusuario) REFERENCES usuario(idusuario) ON DELETE CASCADE

#Creacion de la tabla otrosIngresos

usuarioCREATE TABLE otrosIngresos(
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