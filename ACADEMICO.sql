CREATE DATABASE IF NOT EXISTS ACADEMICO;
USE ACADEMICO;

DROP TABLE ESTUDIANTES;
CREATE TABLE IF NOT EXISTS ESTUDIANTES(
CEDULA INT (10) PRIMARY KEY,
NOMBRE VARCHAR (100) NOT NULL,
EDAD INT (100),
PROMEDIO FLOAT
);

DROP TABLE CURSOS;
CREATE TABLE IF NOT EXISTS CURSOS(
ID INT PRIMARY KEY,
NOMBRE_CURS VARCHAR(100),
CODIGO INT
);

DROP TABLE MATRICULAS;
CREATE TABLE IF NOT EXISTS MATRICULAS(
CEDULA INT (10) NOT NULL,
CURSO_ID INT NOT NULL,
ESTUDIANTE_CEDULA INT NOT NULL,
PRIMARY KEY (ESTUDIANTE_CEDULA, CURSO_ID),
foreign key (ESTUDIANTE_CEDULA) REFERENCES ESTUDIANTES(CEDULA),
FOREIGN KEY (CURSO_ID) REFERENCES CURSOS(ID)
);

SELECT * FROM ESTUDIANTES;
SELECT * FROM MATRICULAS;
SELECT * FROM CURSOS;