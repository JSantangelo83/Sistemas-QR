from os import error
import sqlite3
from pathlib import Path

PATH_DB = Path(__file__).parent.parent / "db" / "database"

conn = sqlite3.connect(PATH_DB.resolve(),check_same_thread=False)
c = conn.cursor()

def get_user(email):
    c.execute('SELECT * FROM usuarios WHERE email = ?',(email,))
    rows = c.fetchall()
    if len(rows) > 0: return (rows[0])
    return False

def insert(table_name, values):
    query = f"INSERT INTO {table_name} VALUES ({','.join(['?' for v in values])});"
    c.execute(query, values)
    conn.commit()

def does_user_exist(id):
    result = c.execute('SELECT dni FROM docentes WHERE dni = ?',(id,)).fetchall()
    if not len(result): return False
    return True
    
# insert("usuarios", ["hola@jaja.com", "chau"])
# print(does_user_exist(30111111))
    
#get_user("jrodil@gmail.com")