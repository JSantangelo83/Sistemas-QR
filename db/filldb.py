import sqlite3

conn = sqlite3.connect('database')
c = conn.cursor()

#/* Cursos */
c.execute('''INSERT INTO cursos (nombre,aclaracion) VALUES ("4AO","Sexto Computadoras") ''')
c.execute('''INSERT INTO cursos (nombre,aclaracion) VALUES ("2AO","Cuarto Computadoras") ''')
c.execute('''INSERT INTO cursos (nombre,aclaracion) VALUES ("3AO","Quinto Computadoras") ''')



#/* Alumnos */
c.execute(''' INSERT INTO alumnos (dni,nombre,apellido,session_id,nombre_curso) VALUES (44111111,"Joaquin","Santangelo","528ed4b34e6e66790957c3bdf39877e8","4AO")''')
c.execute('''INSERT INTO alumnos (dni,nombre,apellido,session_id,nombre_curso) VALUES (44111112,"Joaquin","Trabucco","77f142ecd0e23e8a7666411e28785410","4AO") ''')
c.execute(''' INSERT INTO alumnos (dni,nombre,apellido,session_id,nombre_curso) VALUES (44111113,"Joaquin","Rodil","0b69d314b0c2b0c17d0de954413f3e5b","4AO")''')
c.execute(''' INSERT INTO alumnos (dni,nombre,apellido,session_id,nombre_curso) VALUES (44111114,"Theo","Sanchez Pintor","d484da16f12971bfc33ad5a56f6f0056","4AO")''')
c.execute('''INSERT INTO alumnos (dni,nombre,apellido,session_id,nombre_curso) VALUES (44111115,"Federico","Torrado","6d6881a36139a14dba7b64cc0ddb5adb","4AO") ''')





#/* Profesores */
c.execute(''' INSERT INTO docentes (dni,nombre,apellido,session_id) VALUES (30111111,"Francisco","Demartino", "61bc48c63b909eb7c9f2f93cd4964dee")''')
c.execute(''' INSERT INTO docentes (dni,nombre,apellido, session_id) VALUES (30111112,"Nicolas","Mastropascua", "9fbb51d013a3b0bebfc4be304cb57f09")''')
c.execute('''INSERT INTO docentes (dni,nombre,apellido, session_id) VALUES (30111113,"Andres","Visco Bonomo", "a56b809f4b564951711a4f188f91f7b1") ''')

# usuarios
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("jsantangelo@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("jtrabucco@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("jrodil@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("tspintor@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("ftorrado@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("fdemartino@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("nmastropascua@gmail.com","toor")''')
c.execute(''' INSERT INTO usuarios (email, password) VALUES ("avbonomo@gmail.com","toor")''')



#/* Modulos */
#/* Lunes */

c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("1","1","16:45","17:25","4AO","30111111") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("2","1","17:35","19:35","4AO","30111113") ''')
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("3","1","19:45","21:05","4AO","30111112")''')
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("4","1","21:15","21:55","4AO","30111112")''')



#/* Martes */
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("5","2","16:05","17:25","4AO","30111111") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("6","2","17:35","19:35","4AO","30111112") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("7","2","19:45","21:05","4AO","30111113") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("8","2","21:15","21:55","4AO","30111113") ''')



#/* Miercoles */
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("9","3","16:05","17:25","4AO","30111111") ''')
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("10","3","17:35","19:35","4AO","30111111")''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("11","3","19:45","21:05","4AO","30111112") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("12","3","21:15","21:55","4AO","30111113") ''')



#/* Jueves */
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("13","4","15:10","15:50","4AO","30111111")''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("14","4","16:05","17:25","4AO","30111111") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("15","4","17:35","19:35","4AO","30111113") ''')
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("16","4","19:45","21:05","4AO","30111113")''')
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("17","4","21:15","21:55","4AO","30111113")''')




#/* Viernes */
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,fecha,nombre_curso,dni_docente) VALUES ("18","5","14:30","16:30","2021-09-11","4AO","30111111")''')  #/* Modulo UNICO con campo fecha */
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("19","5","17:35","19:35","4AO","30111112") ''')
c.execute(''' INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("20","5","19:45","21:05","4AO","30111112")''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("21","5","21:15","21:55","4AO","30111112") ''')



#/* Sabado */
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("22","6","10:00","10:50","4AO","30111111") ''')
c.execute('''INSERT INTO modulos (id,dia,hora_inicio,hora_final,nombre_curso,dni_docente) VALUES ("23","6","11:00","12:00","4AO","30111111") ''')

conn.commit()



