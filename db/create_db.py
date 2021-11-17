import sqlite3

conn = sqlite3.connect('database')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS cursos (
  nombre VARCHAR(6) PRIMARY KEY NOT NULL,
  aclaracion VARCHAR(45) NULL DEFAULT NULL
)
'''
)

c.execute('''CREATE TABLE IF NOT EXISTS alumnos (
  dni INT PRIMARY KEY NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  apellido VARCHAR(45) NOT NULL,
  session_id VARCHAR(45) NOT NULL,
  nombre_curso VARCHAR(6) NOT NULL,
  FOREIGN KEY (nombre_curso) REFERENCES cursos(nombre))

  ''')


c.execute('''CREATE TABLE IF NOT EXISTS docentes (
  dni INT PRIMARY KEY NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  apellido VARCHAR(45) NOT NULL,
  session_id VARCHAR(45) NOT NULL
)''')


c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    email VARCHAR(45) PRIMARY KEY NOT NULL,
    password VARCHAR(45) NOT NULL,
    admin INT NOT NULL
)
''')


c.execute('''CREATE TABLE IF NOT EXISTS modulos (
  id INT PRIMARY KEY NOT NULL,
  dia INT NOT NULL,
  hora_inicio TIME NOT NULL,
  hora_final TIME NOT NULL,
  fecha DATE NULL DEFAULT NULL,
  nombre_curso VARCHAR(6) NOT NULL,
  dni_docente INT NOT NULL,
  FOREIGN KEY (nombre_curso) REFERENCES cursos (nombre),
  FOREIGN KEY (dni_docente) REFERENCES docentes (dni))
  ''')


c.execute('''
CREATE TABLE IF NOT EXISTS presentismo (
  id_modulo INT NOT NULL,
  dni_alumno INT NOT NULL,
  fecha DATE NOT NULL,
  presente TINYINT NOT NULL,
  nota VARCHAR(45) NULL,
  FOREIGN KEY (dni_alumno) REFERENCES alumnos (dni),
  FOREIGN KEY (id_modulo) REFERENCES modulos (id))
''')

conn.commit()

