from os import error
from flask import jsonify
import sqlite3
from pathlib import Path

PATH_DB = Path(__file__).parent.parent / "db" / "database"

conn = sqlite3.connect(PATH_DB.resolve(),check_same_thread=False)
c = conn.cursor()

def get_user(email):
    c.execute('SELECT * FROM usuarios WHERE email = ?;',(email,))
    rows = c.fetchall()
    return rows[0] if len(rows) else None

def insert(table_name, values):
    query = f"INSERT INTO {table_name} VALUES ({','.join(['?' for v in values])});"
    c.execute(query, values)
    conn.commit()
    
def get_student(gid):
    query = f"SELECT * FROM alumnos WHERE WHERE DNI = ?;";
    rows = c.execute(query, gid).fetchall();
    return rows[0] if len(rows) else None

def get_users():
    results = c.execute("SELECT email, admin FROM usuarios;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)

def get_students():
    results = c.execute("SELECT * FROM alumnos;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)

def get_classes():
    results = c.execute("SELECT * FROM modulos;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)    
    
def does_professor_exist(gid):
    result = c.execute('SELECT dni FROM docentes WHERE dni = ?;',(gid,)).fetchall()
    return len(result) > 0

def is_admin(email):
    return c.execute('SELECT admin FROM usuarios WHERE email = ?;',(email,)).fetchall()[0][0] == "TRUE"

def format_result_with_field_names(result, columns):
    data = []
    for r in result:
        dic = {}
        for index in range(len(r)):
            dic[columns[index]] = r[index]
        data.append(dic)
    return data        

# insert("usuarios", ["hola@jaja.com", "chau"])
# print(does_professor_exist(30111111))
# get_user("jrodil@gmail.com")
# print(is_admin('fdemartino@gmail.com'))
