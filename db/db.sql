CREATE DATABASE clinica_medica;
USE clinica_medica;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(45) NOT NULL,
    password VARCHAR(255) NOT NULL,
    tipo ENUM('Doctor', 'Empleado') NOT NULL
);

CREATE TABLE doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    especialidad VARCHAR(45),
    telefono VARCHAR(20),
    email VARCHAR(45),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(45),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    fecha_nacimiento DATE,
    genero ENUM('M', 'F'),
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(45)
);

CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha DATE,
    hora TIME,
    motivo VARCHAR(1000),
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

CREATE TABLE consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cita_id INT,
    motivo VARCHAR(500),
    precio DECIMAL(10, 2),
    fecha DATE,
    FOREIGN KEY (cita_id) REFERENCES citas(id)
);

CREATE TABLE historiales_medicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    descripcion TEXT,
    fecha DATE,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

CREATE TABLE casos_clinicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    descripcion VARCHAR(1000),
    fecha DATE,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

CREATE TABLE tratamientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

CREATE TABLE notificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    mensaje VARCHAR(255),
    fecha DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE reportes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    tipo VARCHAR(45),
    contenido TEXT,
    fecha_generacion DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
casos_clinicos