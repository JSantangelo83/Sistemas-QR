from os import error
import sqlite3

conn = sqlite3.connect('../db/database',check_same_thread=False)
c = conn.cursor()

def getUser(email):
    
    c.execute('SELECT * FROM usuarios WHERE email = ?',(email,))
    rows = c.fetchall()

    #print(rows)

    if len(rows) > 0:
        return (rows[0])
    return False

