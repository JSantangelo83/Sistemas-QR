from os import error
from flask import jsonify
import sqlite3
from pathlib import Path

import threading
lock = threading.Lock()

PATH_DB = Path(__file__).parent.parent / "db" / "database"

conn = sqlite3.connect(PATH_DB.resolve(),check_same_thread=False)
c = conn.cursor()

def insert(table_name, values):
    query = f"INSERT INTO {table_name} VALUES ({','.join(['?' for v in values])});"
    c.execute(query, values)
    conn.commit()

def get_user(email):
    c.execute('SELECT email, admin FROM usuarios WHERE email = ?;',(email,))
    rows = c.fetchall()
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(rows, columns) if len(rows) else None

def get_user_full(email):
    c.execute('SELECT * FROM usuarios WHERE email = ?;',(email,))
    rows = c.fetchall()
    return rows[0] if len(rows) else None

def get_users():
    #results = c.execute("SELECT email, admin FROM usuarios;").fetchall();
    results = c.execute("SELECT * FROM usuarios;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)

def delete_user(pk):
    query = f"DELETE FROM usuarios WHERE email IN ({','.join(['?' for v in pk])});"
    c.execute(query, pk)
    conn.commit()

def get_student(gid):
    query = f"SELECT * FROM alumnos WHERE dni = ?;";
    rows = c.execute(query, (gid,)).fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(rows, columns) if len(rows) else None

def get_students():
    results = c.execute("SELECT * FROM alumnos;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)

def get_class(gid):
    c.execute('SELECT * FROM modulos WHERE id = ?;',(gid,))
    rows = c.fetchall()
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(rows, columns) if len(rows) else None

def get_classes():
    results = c.execute("SELECT * FROM modulos;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)

def get_professor(gid):
    c.execute('SELECT * FROM docentes WHERE dni = ?;',(gid,))
    rows = c.fetchall()
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(rows, columns) if len(rows) else None

def get_professors():
    results = c.execute("SELECT * FROM docentes;").fetchall();
    columns = [d[0] for d in c.description]
    return format_result_with_field_names(results, columns)
    
def does_professor_exist(gid):
    result = c.execute('SELECT dni FROM docentes WHERE dni = ?;',(gid,)).fetchall()
    return len(result) > 0

def user_exists(email):
    result = c.execute('SELECT admin FROM usuarios WHERE email = ?;',(email,)).fetchall()
    return len(result) > 0

def is_admin(email):
    result = c.execute('SELECT admin FROM usuarios WHERE email = ?;',(email,)).fetchall()
    if not result: return False
    return result[0][0] == 1

def update_user(data):
    pk = data["pk"];
    del data["pk"]
    fields = list(data.keys())
    values = list(data.values());
    query = f"UPDATE usuarios SET {', '.join([f'{f}=?' for f in fields])} WHERE email = ?;"
    values.append(pk)
    c.execute(query, values)
    conn.commit()

def get_primary_key_field(table_name):
    result = c.execute(f"SELECT l.name FROM pragma_table_info('{table_name}') as l WHERE l.pk = 1;").fetchall()
    if not result: return None
    return format_field_to_frontend(result[0][0])

def format_result_with_field_names(result, columns):
    data = []
    for r in result:
        dic = {}
        for index in range(len(r)):
            field = columns[index]
            field = format_field_to_frontend(field)
            dic[field] = r[index]
        data.append(dic)
    return data        

def format_field_to_frontend(field):
    field = field[0].upper() + field[1:].lower()
    field = field.replace("_", " ")
    return field

# insert("usuarios", ["hola@jaja.com", "chau"])
# print(does_professor_exist(30111111))
# get_user("jrodil@gmail.com")
# print(is_admin('fdemartino@gmail.com'))
# print(get_primary_key_field("docentes"))
