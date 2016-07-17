
from base import conn, cursor

def create(username, password, fullName):
    sql = "INSERT INTO users (username, password, full_name) VALUES ('{}', '{}', '{}')".format(username, password, fullName)
    cursor.execute(sql)
    conn.commit()
    return cursor.lastrowid



def find(username):
    sql = "SELECT * FROM users WHERE username = '{}' LIMIT 1".format(username)
    cursor.execute(sql)
    return cursor.fetchone()
