/* Cursos */
INSERT INTO cursos (nombre,aclaracion) VALUES ("4AO","Sexto Computadoras");
INSERT INTO cursos (nombre,aclaracion) VALUES ("2AO","Cuarto Computadoras");
INSERT INTO cursos (nombre,aclaracion) VALUES ("3AO","Quinto Computadoras");


/* Alumnos */
INSERT INTO alumnos (dni,nombre,apellido,mac_address,nombre_curso) VALUES (44111111,"Joaquin","Santangelo","83:DB:84:C1:CC:F3","4AO");
INSERT INTO alumnos (dni,nombre,apellido,mac_address,nombre_curso) VALUES (44111112,"Joaquin","Trabucco","70:26:80:D0:E0:4C","4AO");
INSERT INTO alumnos (dni,nombre,apellido,mac_address,nombre_curso) VALUES (44111113,"Joaquin","Rodil","BC:60:C8:07:D7:80","4AO");
INSERT INTO alumnos (dni,nombre,apellido,mac_address,nombre_curso) VALUES (44111114,"Theo","Sanchez Pintor","1F:7D:0E:8B:96:76","4AO");
INSERT INTO alumnos (dni,nombre,apellido,mac_address,nombre_curso) VALUES (44111115,"Federico","Torrado","05:55:90:74:C7:DE","4AO");



/* Profesores */
INSERT INTO docentes (dni,nombre,apellido) VALUES (30111111,"Francisco","Demartino");
INSERT INTO docentes (dni,nombre,apellido) VALUES (30111112,"Nicolas","Mastropascua");
INSERT INTO docentes (dni,nombre,apellido) VALUES (30111113,"Andres","Visco Bonomo");



/* Modulos */

/* Lunes */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("1","1","16:45","17:25","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("2","1","17:35","19:35","4AO","30111113");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("3","1","19:45","21:05","4AO","30111112");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("4","1","21:15","21:55","4AO","30111112");

/* Martes */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("5","2","16:05","17:25","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("6","2","17:35","19:35","4AO","30111112");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("7","2","19:45","21:05","4AO","30111113");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("8","2","21:15","21:55","4AO","30111113");

/* Miercoles */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("9","3","16:05","17:25","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("10","3","17:35","19:35","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("11","3","19:45","21:05","4AO","30111112");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("12","3","21:15","21:55","4AO","30111113");

/* Jueves */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("13","4","15:10","15:50","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("14","4","16:05","17:25","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("15","4","17:35","19:35","4AO","30111113");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("16","4","19:45","21:05","4AO","30111113");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("17","4","21:15","21:55","4AO","30111113");

/* Viernes */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,fecha,nombre_curso,dni_docente) VALUES ("18","5","14:30","16:30","2021-09-11","4AO","30111111"); /* Modulo UNICO con campo fecha */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("19","5","17:35","19:35","4AO","30111112");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("20","5","19:45","21:05","4AO","30111112");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("21","5","21:15","21:55","4AO","30111112");


/* Sabado */
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("22","6","10:00","10:50","4AO","30111111");
INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("23","6","11:00","12:00","4AO","30111111");





